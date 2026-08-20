# CONTEXT.md — UC Library Carpentry Workshop, Fall 2026

> For workflow rules and non-negotiables, load: `projctx bundle carpentries_program`
> Built with the `~/projects/lessons/tools/workshop-website-agent` kit — see its
> `instructions/core.md` for the general workflow this repo follows.

## Status: DRAFT — not yet a live GitHub repo

This directory is a **local clone of `carpentries/workshop-template`**, not yet
published. No `gh repo create` has been run and there is no `origin` remote.
The roster (see below) locks around 2026-08-08; create the real repo once it's
settled, or sooner if Tim says go.

To go live:
```bash
cd ~/projects/lessons/tools/workshop-website-agent
bash scripts/bootstrap-repo.sh --dry-run   # preview
bash scripts/bootstrap-repo.sh             # creates jt14den/2026-09-08-uc-lc via gh,
                                            # clones fresh, enables Pages
# then copy this draft's customized _config.yml, index.md, _includes/lc/schedule.html,
# and _includes/syllabus.html over the fresh clone before pushing
```

## Event Facts

| Field | Value |
|---|---|
| Workshop title | UC Library Carpentry Workshop (Fall 2026) |
| Carpentry type | lc (Library Carpentry) |
| Curriculum / flavor | lc / r |
| Start date | 2026-09-08 |
| End date | 2026-09-17 (core run; see note below on the 8th session) |
| Mode | online |
| Location | UC Carpentries (Online) |
| Host institution | UCLA Library |
| Daily times + timezone | 9:00 AM – 12:00 PM PT — **ASSUMED**, carried over from the Spring workshop; not yet confirmed for Fall |
| Contact email | tdennis@library.ucla.edu |
| Registration link | TBD |
| Etherpad / notes link | TBD |
| GitHub repo (planned) | jt14den/2026-09-08-uc-lc |
| GitHub Pages URL (planned) | https://jt14den.github.io/2026-09-08-uc-lc |

## Format difference from the Spring workshop

Spring (`2026-05-11-uc-lc`) had one fixed instructor team for the whole 2-week
run. Fall is **7 discrete single-day sessions with a different instructor/helper
pairing each day**, pulled from a live sign-up sheet that's still filling in.
Because of that, the schedule table (not just the page-level instructor list)
carries the per-session instructor/helper attribution — see
`_includes/lc/schedule.html`.

## Roster round-trip (the CSV import workflow)

The sign-up sheet (`data/instructor-signup.csv`, a snapshot of the "Fall 2026 -
Instructor Spreadsheet - UC Carpentries" Google Sheet) drives the schedule table
and the people lists. As of 2026-08-05 most instructor/helper cells are still
blank — the sheet is expected to keep changing until the roster locks around
2026-08-08.

**To refresh the site after the sheet changes:**
```bash
# 1. Re-export the Google Sheet as CSV, overwrite data/instructor-signup.csv
#    (or point --csv at wherever the new export landed)
cd ~/projects/lessons/delivery/2026-09-08-uc-lc
python3 scripts/import_signup.py --dry-run   # preview first
python3 scripts/import_signup.py             # writes schedule.html,
                                              # updates people.instructors/helpers
                                              # in the kit's workshop-facts.yaml

# 2. Push the updated people lists into index.md
cd ~/projects/lessons/tools/workshop-website-agent
python3 scripts/validate.py workshop-facts.yaml
python3 scripts/render-config.py workshop-facts.yaml --repo-dir ~/projects/lessons/delivery/2026-09-08-uc-lc
```

Blank sign-up cells always render as "TBD" in the schedule table and are simply
omitted from the deduplicated instructor/helper lists — the script never invents
a name. See the docstring in `scripts/import_signup.py` for details (email
resolution across rows, name/email cell parsing, etc).

## Lessons Being Taught

Per Tim (2026-08-06): Tidy Data, Unix Shell, and Version Control with Git run as
Software/Data Carpentry lessons for this workshop, not Library Carpentry's own
lc-* equivalents; OpenRefine and SQL stay Library Carpentry.

| Date | Lesson | URL | Instructor(s) | Helper(s) |
|---|---|---|---|---|
| 2026-09-08 | Tidy Data (Data Carpentry, ecology flavor) | https://datacarpentry.org/spreadsheet-ecology-lesson/ | TBD | — |
| 2026-09-09 | Unix Shell (Software Carpentry) | https://swcarpentry.github.io/shell-novice/ | James Frew | Geoffrey Boushey, Jose Niño Muriel |
| 2026-09-10 | Version Control with Git (Software Carpentry) | https://swcarpentry.github.io/git-novice/ | TBD | — |
| 2026-09-11 | OpenRefine (Library Carpentry) | https://librarycarpentry.org/lc-open-refine/ | TBD | — |
| 2026-09-15 | R, day one (Software Carpentry content, not LC's own lc-r) | https://swcarpentry.github.io/r-novice-gapminder/ | Jose Niño Muriel, Rachel Torres | Geno Sanchez, Anindya Ganguly |
| 2026-09-15 | Python, day one (parallel track to R day one) | https://swcarpentry.github.io/python-novice-gapminder/ | Geoffrey Boushey, Celeste Allaband | — |
| 2026-09-16 | R, day two (same) | https://swcarpentry.github.io/r-novice-gapminder/ | Jose Niño Muriel, Rachel Torres | Anindya Ganguly |
| 2026-09-16 | Python, day two (parallel track to R day two) | https://swcarpentry.github.io/python-novice-gapminder/ | Geoffrey Boushey, Celeste Allaband | — |
| 2026-09-17 | SQL (Library Carpentry) | https://librarycarpentry.org/lc-sql/ | Geoffrey Boushey, David Moles | Geno Sanchez, Kristi Liu |
| 2026-09-23 | Making Research Software Citable & Discoverable — date CONFIRMED | https://ucospo.net/research-software-citable-discoverable/ | Tim Dennis, Leigh Phan, Laura Langdon, Reid Otsuji, Karla Padilla | Derek Devnich, Jamie Jamison, Kelsey Brown |

Gap Sep 12–14: no sessions (weekend + Monday off). "Making Research Software Citable & Discoverable" (renamed from "Sharing Research Software" 2026-08-20 — clearer about what the session covers) is
a Carpentries Incubator lesson (UC-OSPO-Network org), not LC/SWC curriculum, taught
as a follow-on session via UC OSPO Net collaboration. Its confirmed Sep 23 date
pushed the page-level workshop date range to Sep 8–23 (see `index.md` front matter).

## Status

- [x] Local draft cloned from `carpentries/workshop-template`
- [x] `workshop-facts.yaml` filled in and validated (in the kit repo)
- [x] `_config.yml` rendered
- [x] `index.md` front matter rendered
- [x] Schedule table built from the CSV via `scripts/import_signup.py`
- [x] `_includes/syllabus.html` placeholder created (prevents known build error)
- [ ] Roster locked (target ~2026-08-08)
- [ ] Confirm daily start/end times for Fall (currently assumed 9am–12pm PT)
- [ ] Real GitHub repo created (`gh repo create` via `bootstrap-repo.sh`)
- [ ] GitHub Pages enabled and building
- [ ] Registration link and collaborative notes (Etherpad) link filled in — Jamie is building the Etherpad/minutes form separately
- [ ] Carpentries notified (`team@carpentries.org`)
- [ ] Self-organized workshop form submitted
- [ ] Repo description + URL metadata set on GitHub
- [x] "Making Research Software Citable & Discoverable" (renamed 2026-08-20 from "Sharing Research Software") date confirmed (2026-09-23) and lesson link added; stays on this site, page-level date range extended to Sep 8–23

## Template drift since the Spring workshop (assessed 2026-08-05)

`carpentries/workshop-template` moved on between the Spring build (Feb 2026 base,
commit `8eec921`) and this clone (July 2026, commit `1d50c4e`, PR #903
"hpc-correction"). Diffed both trees; findings:

- **New "hpcc" (High-Performance Computing Carpentry) program added** as a 4th
  official curriculum alongside swc/dc/lc, with new `site.hpcc_*` vars and a new
  `site.official_curricula: [swc, dc, lc, hpcc]` list. Not relevant to this `lc`
  workshop, but the kit's `schema/workshop-facts.schema.yaml` and
  `scripts/validate.py` don't know about `hpcc` yet — a future UCLA HPC Carpentry
  workshop would need that added to the kit first.
- **Front-end redesign**: Bootstrap bundle upgraded (old `bootstrap.css` +
  `bootstrap-theme.css` → single `bootstrap.min.css`/`bootstrap.bundle.min.js`),
  and `index.md` restructured from plain `<h2>`-header sections into Bootstrap
  card components (`<div class="card mb-2"><h5 class="card-header">...`).
  Cosmetic only — our `table table-striped` markup in `schedule.html` still
  renders correctly inside the new card wrapper (verified in browser).
- **Per-carpentry includes now computed, not hardcoded**: `index.md` used to have
  an explicit `{% if carpentry == "swc" %}...{% elsif == "dc" %}...{% elsif ==
  "lc" %}...{% endif %}` chain for intro/who/schedule/setup. Now it's
  `{% assign schedule_file = site.carpentry | append: '/schedule.html' %}` gated
  by `{% if isOfficial %}` (true whenever `carpentry` is in `official_curricula`).
  For `carpentry: lc` this still resolves to `_includes/lc/schedule.html` —
  same path, same file, no changes needed here.
- **Old lesson/episode boilerplate removed** from the template (`_episodes/`,
  episode-related `_layouts/`, old lesson-authoring `bin/` scripts, `.travis.yml`)
  — dead weight for a workshop site regardless, no impact.
- `_includes/syllabus.html` still isn't shipped by default — the manual
  `touch _includes/syllabus.html` fix (documented in the kit's
  `instructions/core.md`) is still required.

**Net effect on this repo: none.** `render-config.py`'s field-level substitutions
(`_config.yml`, `index.md` front matter) target the same key names in the new
template, and the live preview confirmed the schedule table, instructor/helper
lists, and dates all render correctly. Confirmed via direct diff against
`2026-05-11-uc-lc`'s original template commit (`8eec921`) and a live `make serve`
check in Chrome. No fixes needed in the kit for *this* workshop; the `hpcc`
validator gap is worth a follow-up PR to the kit only if a UCLA HPC Carpentry
workshop comes up.

## Open Issues / Notes

- Repo is at canonical location: `~/projects/lessons/delivery/2026-09-08-uc-lc/`
- Source sign-up sheet: `/Users/timdennis/Downloads/Fall 2026 - Instructor Spreadsheet - UC Carpentries - Sheet1.csv` (snapshot copied to `data/instructor-signup.csv`)
- `workshop-facts.yaml` (authoritative facts) lives in the kit repo, not here: `~/projects/lessons/tools/workshop-website-agent/workshop-facts.yaml`
