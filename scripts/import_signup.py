#!/usr/bin/env python3
"""
Round-trip importer: turns the UC Carpentries instructor sign-up CSV into
this site's schedule table and the people lists in workshop-facts.yaml.

Re-run this any time the sign-up sheet changes (export it as CSV again and
overwrite data/instructor-signup.csv, or point --csv at the new file):

    python3 scripts/import_signup.py
    python3 scripts/import_signup.py --csv ~/Downloads/latest-export.csv

What it updates:
    _includes/swc/schedule.html           — one row per session, from the CSV
                                             (site.carpentry is "swc", not "lc" —
                                             see the carpentry/curriculum note in
                                             CONTEXT.md before changing this path)
    ../../tools/workshop-website-agent/workshop-facts.yaml
                                           — people.instructors / people.helpers
                                             (deduplicated, order of first appearance)

What it does NOT touch:
    _config.yml / index.md — re-run render-config.py in the kit after this
    if the instructor/helper lists changed, to push the new lists into
    index.md's front matter.

Never invents names: blank sign-up cells become "TBD" in the schedule table
and are simply omitted from the deduplicated people lists.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_DIR / "data" / "instructor-signup.csv"
DEFAULT_SCHEDULE = REPO_DIR / "_includes" / "swc" / "schedule.html"
DEFAULT_FACTS = REPO_DIR / ".." / ".." / "tools" / "workshop-website-agent" / "workshop-facts.yaml"

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\s*(.*)$")


EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+")


def clean_names_multi(cell, email_to_name=None):
    """Like clean_name, but splits on '|' first so a cell listing several
    people (e.g. "Tim Dennis/tdennis@... | Leigh Phan | Laura Langdon")
    yields one (name, note) pair per person instead of mangling them into one."""
    return [clean_name(part, email_to_name) for part in cell.split("|") if part.strip()]


def split_name_email(cell):
    """'James Frew / frew@ucsb.edu' -> ('James Frew', 'frew@ucsb.edu')."""
    parts = re.split(r"[/]", cell, maxsplit=1)
    name = parts[0].strip()
    email = parts[1].strip() if len(parts) > 1 else None
    if email is None and EMAIL_RE.fullmatch(name):
        # cell was just an email with no name, e.g. "frew@ucsb.edu"
        email, name = name, None
    return (name or None), email


def display_with_note(name, note):
    """Append a parenthetical note for display, unless the note is just an
    email address (e.g. someone wrote "Name (name@example.edu)" instead of
    "Name / name@example.edu") — that's contact info, not context, and
    shouldn't leak onto the public schedule table."""
    if not note or EMAIL_RE.fullmatch(note):
        return name
    return f"{name} ({note})"


def clean_name(cell, email_to_name=None):
    """'James Frew / frew@ucsb.edu' -> 'James Frew'. Preserves parenthetical notes.
    Falls back to email_to_name to resolve cells that give only an email
    (seen elsewhere in the sheet with a name attached)."""
    cell = cell.strip()
    if not cell:
        return None, None
    note = None
    m = re.search(r"\(([^)]*)\)", cell)
    if m:
        note = m.group(1).strip()
        cell = cell[: m.start()].strip()
    name, email = split_name_email(cell)
    if not name and email and email_to_name:
        name = email_to_name.get(email.lower())
    return (name or None), note


def build_email_to_name(csv_path):
    """First pass over the sheet: map every email seen with a name to that name."""
    mapping = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            for cell in row[2:9]:
                for part in cell.split("|"):
                    part = re.sub(r"\([^)]*\)", "", part).strip()
                    name, email = split_name_email(part)
                    if name and email:
                        mapping[email.lower()] = name
    return mapping


def parse_rows(csv_path):
    """Yield session dicts, skipping header/footer/blank rows in the sheet."""
    email_to_name = build_email_to_name(csv_path)
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if not row or not any(c.strip() for c in row):
                continue
            date_raw, lesson = row[0].strip(), row[1].strip()
            if not lesson or lesson.lower().startswith("etherpad") or lesson.lower().startswith("helper stars"):
                continue
            cols = row + [""] * (11 - len(row))
            leads = clean_names_multi(cols[2], email_to_name)
            inst2s = clean_names_multi(cols[3], email_to_name)
            helpers = []
            helper_names = []
            for raw in cols[4:9]:
                name, note = clean_name(raw, email_to_name)
                if name:
                    helpers.append(display_with_note(name, note))
                    helper_names.append(name)
            instructor_pairs = leads + inst2s
            instructors = [display_with_note(n, note) for n, note in instructor_pairs if n]

            m = DATE_RE.match(date_raw)
            is_confirmed_date = bool(m)
            date_note = m.group(2) if m else None
            yield {
                "date_raw": m.group(1) if m else date_raw,
                "date_note": date_note,
                "date_confirmed": is_confirmed_date,
                "lesson": lesson,
                "instructors": instructors,
                "helpers": helpers,
                "instructor_names": [n for n, _ in instructor_pairs if n],
                "helper_names": helper_names,
            }


def format_date(date_raw, confirmed, note=None):
    if not confirmed:
        return f"TBD ({date_raw})" if date_raw else "TBD"
    from datetime import date as _date

    y, m, d = (int(x) for x in date_raw.split("-"))
    disp = _date(y, m, d).strftime("%a, %b %-d")
    return f"{disp} ({note})" if note else disp


# Maps CSV "Workshop Type" text to the official lesson URL.
# Per Tim (2026-08-06): Tidy Data, Unix Shell, and Version Control with Git
# run as Software/Data Carpentry lessons for this workshop, not Library
# Carpentry's own lc-* equivalents; OpenRefine and SQL stay Library Carpentry.
# - Tidy Data -> Data Carpentry's spreadsheets lesson (ecology flavor, per Tim),
#   verified against https://datacarpentry.org/spreadsheet-ecology-lesson/ (2026-08-06).
# - Unix Shell / Git -> Software Carpentry's own lessons, verified against
#   https://swcarpentry.github.io/shell-novice/ and
#   https://swcarpentry.github.io/git-novice/ (2026-08-06).
# - OpenRefine / SQL -> Library Carpentry, verified against
#   https://librarycarpentry.org/lessons/ (2026-08-05).
# R days teach Software Carpentry's R content (not Library Carpentry's own lc-r),
# verified against https://github.com/swcarpentry/r-novice-gapminder (2026-08-05).
# Python days pair with the same SWC gapminder track, verified against
# https://swcarpentry.github.io/python-novice-gapminder/ (2026-08-06).
# "Sharing Research Software" is the UC-OSPO-Network Carpentries Incubator
# lesson (not LC/SWC curriculum), verified against
# https://ucospo.net/research-software-citable-discoverable/ (2026-08-06),
# date confirmed 2026-09-23.
# Sessions not in this map render as plain text — add an entry here if the
# CSV starts using a name that should link out.
LESSON_URLS = {
    "Tidy Data": "https://datacarpentry.org/spreadsheet-ecology-lesson/",
    "Unix Shell": "https://swcarpentry.github.io/shell-novice/",
    "Version Control with Git": "https://swcarpentry.github.io/git-novice/",
    "OpenRefine": "https://librarycarpentry.org/lc-open-refine/",
    "R, day one": "https://swcarpentry.github.io/r-novice-gapminder/",
    "R, day two": "https://swcarpentry.github.io/r-novice-gapminder/",
    "Python, day one": "https://swcarpentry.github.io/python-novice-gapminder/",
    "Python, day two": "https://swcarpentry.github.io/python-novice-gapminder/",
    "SQL": "https://librarycarpentry.org/lc-sql/",
    "Sharing Research Software": "https://ucospo.net/research-software-citable-discoverable/",
}

# Freeform annotations shown under a session's name, keyed by the exact CSV
# "Workshop Type" text. Not sourced from the CSV's own Notes column (that
# column tracks Zoom/Etherpad logistics, gets overwritten wholesale on every
# re-export) — this is for durable provenance/context that should survive
# re-imports regardless of what the sign-up sheet says that week.
SESSION_NOTES = {
    "Sharing Research Software": "via UC OSPO Net collaboration",
}


def render_schedule_html(sessions):
    rows = []
    for s in sessions:
        date_disp = format_date(s["date_raw"], s["date_confirmed"], s.get("date_note"))
        instr = ", ".join(s["instructors"]) if s["instructors"] else "TBD"
        help_ = ", ".join(s["helpers"]) if s["helpers"] else "&mdash;"
        url = LESSON_URLS.get(s["lesson"])
        lesson_cell = f'<a href="{url}">{s["lesson"]}</a>' if url else s["lesson"]
        note = SESSION_NOTES.get(s["lesson"])
        if note:
            lesson_cell += f'<br><small class="text-muted">{note}</small>'
        rows.append(
            f"      <tr>\n"
            f"        <td>{date_disp}</td>\n"
            f"        <td>{lesson_cell}</td>\n"
            f"        <td>{instr}</td>\n"
            f"        <td>{help_}</td>\n"
            f"      </tr>"
        )
    rows_html = "\n".join(rows)
    return f"""<!-- AUTO-GENERATED by scripts/import_signup.py from data/instructor-signup.csv.
     Do not hand-edit these rows — edit the CSV and re-run the script instead. -->
<table class="table table-striped">
  <thead>
    <tr>
      <th>Date</th>
      <th>Session</th>
      <th>Instructor(s)</th>
      <th>Helper(s)</th>
    </tr>
  </thead>
  <tbody>
{rows_html}
  </tbody>
</table>
<p><em>Gap Sep 12&ndash;14: no sessions (weekend + Monday off).</em></p>
"""


def dedupe_preserve_order(items):
    seen = set()
    out = []
    for i in items:
        if i and i not in seen:
            seen.add(i)
            out.append(i)
    return out


def render_people_block(key, names, indent="  "):
    lines = [f"{indent}{key}:"]
    for n in names:
        lines.append(f'{indent}  - "{n}"')
    return "\n".join(lines)


def update_facts_people(facts_path, instructors, helpers):
    text = facts_path.read_text()

    def find_block(text, key):
        pattern = re.compile(
            rf"(^  {re.escape(key)}:\n)((?:^    -.*\n)*)", re.MULTILINE
        )
        return pattern.search(text)

    for key, names in (("instructors", instructors), ("helpers", helpers)):
        m = find_block(text, key)
        if not m:
            print(f"  WARN    people.{key} block not found in {facts_path} — skipping")
            continue
        new_block = "".join(f'    - "{n}"\n' for n in names)
        text = text[: m.start()] + m.group(1) + new_block + text[m.end():]

    facts_path.write_text(text)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    ap.add_argument("--schedule", type=Path, default=DEFAULT_SCHEDULE)
    ap.add_argument("--facts", type=Path, default=DEFAULT_FACTS)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    if not args.csv.exists():
        print(f"ERROR: CSV not found at {args.csv}")
        return 2

    sessions = list(parse_rows(args.csv))
    if not sessions:
        print("ERROR: no session rows parsed from CSV — check the format")
        return 1

    print(f"Parsed {len(sessions)} session(s) from {args.csv}")
    for s in sessions:
        print(f"  {s['date_raw']:<18} {s['lesson']:<28} instr={s['instructors'] or 'TBD'}  helpers={s['helpers'] or '-'}")

    all_instructors = dedupe_preserve_order(n for s in sessions for n in s["instructor_names"])
    all_helpers = dedupe_preserve_order(n for s in sessions for n in s["helper_names"])
    # A helper-column name flagged "avail as instructor if needed" still counts as a helper here;
    # promote/demote by hand in workshop-facts.yaml if that changes.

    print(f"\nUnique instructors ({len(all_instructors)}): {all_instructors}")
    print(f"Unique helpers ({len(all_helpers)}): {all_helpers}")

    schedule_html = render_schedule_html(sessions)

    if args.dry_run:
        print(f"\n[dry-run] Would write {args.schedule}")
        print(f"[dry-run] Would update people.instructors/helpers in {args.facts}")
        return 0

    args.schedule.write_text(schedule_html)
    print(f"\nOK      wrote {args.schedule}")

    if args.facts.exists():
        update_facts_people(args.facts, all_instructors, all_helpers)
        print(f"OK      updated people.instructors/helpers in {args.facts}")
        print("        Re-run render-config.py in the kit to push these into index.md.")
    else:
        print(f"WARN    facts file not found at {args.facts} — skipped people-list update")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
