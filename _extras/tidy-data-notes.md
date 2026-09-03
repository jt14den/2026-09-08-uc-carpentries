---
layout: page
title: "Tidy Data (Sep 8) — Session Notes"
permalink: /tidy-data-notes/index.html
---

Notes for the **Tidy Data** session, Tuesday September 8, 2026, 9:00 am to 12:00 pm
Pacific, online. Based on Library Carpentry's
[Spreadsheets / Tidy Data for Librarians](https://librarycarpentry.github.io/lc-spreadsheets/)
lesson, taught in **Google Sheets**.

The first part of this page is a reference you can use during and after the session. The
[run sheet](#run-sheet) and [instructor guide](#instructor-guide) further down are open
for anyone who wants to see how the session is put together or teach it themselves.

- Full self-paced lesson: <https://librarycarpentry.github.io/lc-spreadsheets/aio.html>
- Collaborative notes (Etherpad): <https://pad.carpentries.org/2026-fall-uc-carpentries-tidydate>
- Practice data (xlsx): [training_attendance_practice.xlsx]({{ relative_root_path }}/files/training_attendance_practice.xlsx)

---

## The practice data

`training_attendance_practice.xlsx` is a teaching build derived from the Library
Carpentry `training_attendance.xlsx` (fictional records of library training sessions,
2015&ndash;2017). Your instructor will share it as a Google Sheet with a "make a copy"
link. Tabs:

- **`2016_messy`** &mdash; two side-by-side tables, merged titles, a `PGR|PDRA|other`
  column that packs three numbers into one cell, durations written as text
  (`1.5 hours`), two dates that landed in 1900, cancelled sessions shown only by grey
  row shading.
- **`2017_messy`** &mdash; schema drifts from 2016; some dates typed as text
  (`7/8 Feb`); one date in 1970; two trainers in one cell (`GQ & DF`); a legend row
  inside the data.
- **`dates`** &mdash; already close to tidy. `len_hours` mixes hours, minutes, and
  text; two rows dated 2017 should be 2015; cancelled rows carry `num_attended` 0.
- **`checkpoint_clean` / `checkpoint_combined` / `checkpoint_dates`** &mdash; answer
  keys.
- **`ai_input`** &mdash; a tidy table with a `source_row_id` column, for the AI exercise.
- **`Notes`** &mdash; kept from the original, an example of metadata living inside the
  workbook.

---

## The one rule

A rectangular table processes the same way on every row:

- every **column** is one variable
- every **row** is one observation
- each **cell** holds one value *for that column* (`GQ & DF` in one cell is two people;
  `45|0|0` in one cell is three counts)
- treat the source file as **read-only**; work in a named copy

Everything in this session is a version of this rule. Some layouts are built to be read
at a glance (titles, colour, spacing). A rectangular table is built to be processed. You
can always build a nice view from the table; you cannot reliably process the pretty
layout.

---

## Google Sheets: where things live

| Task | Path |
|---|---|
| Duplicate a tab | right-click the tab &rarr; **Duplicate** |
| Delete rows | select the row numbers &rarr; right-click &rarr; **Delete rows** |
| Unmerge cells | **Format &rarr; Merge cells &rarr; Unmerge** |
| Number / date format | **Format &rarr; Number** |
| Data validation | **Data &rarr; Data validation &rarr; Add rule**; Advanced options &rarr; *If the data is invalid* &rarr; **Reject the input** |
| Sort a table | **Data &rarr; Sort range &rarr; Advanced range sorting options**; tick **Data has header row**, then sort |
| Conditional formatting | **Format &rarr; Conditional formatting &rarr; Color scale** tab |
| Version history | **File &rarr; Version history &rarr; See version history** |
| Download as CSV | **File &rarr; Download &rarr; Comma-separated values (.csv)** (current sheet only; one download per tab) |
| Locale | **File &rarr; Settings &rarr; Locale** |

---

## Functions we use

| Function | What it does |
|---|---|
| `=ISNUMBER(A2)` | TRUE if the cell holds a real date **value**, FALSE if it is text |
| `=ISTEXT(A2)` | the mirror check: TRUE if the cell is text |
| `=YEAR(A2)` | pulls the year out of a real date |
| `=MONTH(A2)` | pulls the month (1&ndash;12) |
| `=DAY(A2)` | pulls the day of the month |

`ISNUMBER` returning TRUE means the cell holds a real date, **not** that the date is
correct.

---

## Missing values

- Pick one representation per column and use it everywhere.
- For this session: a blank cell for a genuinely missing value; `0` only for a measured
  zero.
- Never use `0` for missing. Never use `-999`.
- In real work: decide what "missing" means here, pick one representation, write it
  down, then check how the next tool reads it.

---

## Dates

A date in a spreadsheet is in one of three states, and all three can look identical in
the cell:

1. a **recognised date value** &mdash; stored as a number, shown through a display format
2. **text** that happens to look like a date
3. a **recognised date with the wrong value** in it

Locale (`File &rarr; Settings &rarr; Locale`) sets the default date format and how Sheets
reads ambiguous date *text* (`03/04/2016` as March 4 or April 3). Once Sheets has stored
a real date, changing locale changes how it is written on screen, not which day it is.

### The defensive move

- store dates as separate `year` / `month` / `day` columns, or as a recognised date
  displayed `yyyy-mm-dd`
- set the locale on purpose and record it
- format dates with the full year **before** you export &mdash; a CSV keeps only what is
  shown
- after any export, open the file and check the dates

---

## Export to CSV

- A Google Sheet or an `.xlsx` keeps formulas, formatting, tabs, and validation.
  Standardised but complex, and software-dependent.
- A CSV is a plain text table: one table, no colour, no formulas, no tabs. Simpler and
  more portable for a single table, which is why the Library of Congress treats CSV as a
  preferred format for datasets.
- `File &rarr; Download &rarr; CSV` exports the **current sheet only**. Five tabs means
  five downloads.
- A value containing a comma (`GQ, DF`) is written wrapped in quotes (`"GQ, DF"`) so the
  comma is not read as a new column. Sheets does this for you. The deeper problem is two
  values in one cell at all.
- CSV does not carry types, formulas, tabs, validation, or your change log. Keep the
  working Google Sheet alongside the CSV, or export the change log as its own file.

---

## AI tools and your data

- **This session's dataset is fictional.** Do not paste real patron, student, personnel,
  health, licensed, or unpublished research data into an AI service unless that service
  and that use are approved by your institution.
- Everything that reads your sheet next consumes the structure you built: R, Python, a
  colleague, a preservation system, Gemini, ChatGPT.
- Tidy data makes all of them work better. Merged cells and colour-as-data break all of
  them.
- AI does not fix messy data. It produces a fluent, plausible answer even when its
  assumptions are wrong. Fluent is not correct.
- Check its output the same way every time: compare row count and values against the raw
  data you kept.

---

## Self-check questions

1. Look at `2016_messy`. Name one thing a program would choke on.
2. In a tidy table, the months of the year should be: (a) twelve columns Jan&ndash;Dec,
   (b) one column called `month`, (c) colour-coded rows. *(Answer: b)*
3. Turn the RDM table in `2016_messy` into a tidy table: one table, header in row 1, one
   value per cell (split `PGR|PDRA|other`), a real `cancelled` column, consistent nulls.
   Write down your data row count.
4. In `2017_messy`, run `=ISNUMBER()` down the RDM Date column. Which rows come back
   FALSE (stored as text)? Then in `dates`, add `year` with `=YEAR()`. Which two rows
   have the wrong year? *(the events were in 2015)*
5. True or false: if a cell shows `2016-03-04`, the file definitely stores March 4 2016.
   *(Answer: false &mdash; it could be text, or a real date with a wrong value)*
6. Sort the whole `dates` table by `len_hours`, largest to smallest. What junk shows up
   at each end?
7. You sort a table to find outliers. What two things do you do first? *(Answer: select
   the whole table; tick **Data has header row**)*
8. An AI hands you a clean-looking table. First thing you do before you use it?
   *(Answer: compare row count and values against the raw data)*

---

## Resources

- Library Carpentry Spreadsheets lesson: <https://librarycarpentry.github.io/lc-spreadsheets/>
- All-in-one page: <https://librarycarpentry.github.io/lc-spreadsheets/aio.html>
- Hadley Wickham, "Tidy Data": <https://www.jstatsoft.org/article/view/v059i10>
- Cornell, "Guide to writing README files": <https://data.research.cornell.edu/data-management/sharing/readme/>

---

## Run sheet

180 minutes. First keyboard action at minute 8; a curated slice of the data rather than a
full year; a real 10-minute buffer at the end.

| Time | Min | Segment | What happens |
|---|---|---|---|
| 0:00 | 12 | **Welcome + first hands-on** | Norms. Everyone makes their copy, duplicates the `2016_messy` tab to `2016_clean`, deletes the title/spacer rows. One real edit before minute 10. |
| 0:12 | 16 | **Why + tidy data** | Name the two things they just did: work in a copy; a rectangular table processes consistently. The rule. One value *per column*. Think-pair-share on `2016_messy`. |
| 0:28 | 25 | **Formatting problems** *(the core)* | Demo on the RDM table: unmerge the title, split the packed `PGR\|PDRA\|other` cell into three columns, recode grey-shaded cancelled rows into a `cancelled` column. Learners take the Open-access table (units in `Len`, name drift) against `checkpoint_clean`. Flag the two 1900 dates. |
| 0:53 | 8 | Break | |
| 1:01 | 4 | **Combine** | Show `checkpoint_combined`: 2017 rows cleaned the same way, plus a `year` column. Row-count check: 2016 + 2017 = combined &minus; 1 header. `7/8 Feb` is a judgement call, not a cleanup. |
| 1:05 | 25 | **Dates as data** | Three states: real value / text / real-but-wrong. `Format &rarr; Number` to show value vs display. Locale = display and text parsing, not the stored day. `=ISNUMBER` on `2017_messy` catches the text dates. `=YEAR` on `dates` catches the 2017&rarr;2015 bug (and the 1900s in `2016_messy`). |
| 1:30 | 25 | **Quality control** | QA: `Data &rarr; Data validation`, a number range and a dropdown, "Reject the input". QC: sort the whole table with **Data has header row** ticked; `Format &rarr; Conditional formatting &rarr; Color scale`. Zeros are a question for the data dictionary, not an auto-blank. |
| 1:55 | 8 | Break | |
| 2:03 | 22 | **Export** | Why CSV. `File &rarr; Download &rarr; CSV` = current sheet only. Date gotcha: CSV keeps the *displayed* string, so format with the full year first. Comma quoting. CSV drops your change log. |
| 2:25 | 15 | **AI as a downstream consumer** | Data caution. A saved genuine flawed AI output plus a `source_row_id` audit. Optional live rerun. AI shifts work to specifying and verifying; it still does not count reliably. |
| 2:40 | 10 | **Wrap** | Recap the five concepts. Change-log habit. Resources. Feedback. |
| 2:50 | 10 | Buffer | Catch-up, questions, or an early break. |

---

## Instructor guide

### Should you teach the lesson as-is?

Teach it, but reframe it. The lesson was written around Excel in 2016 and it shows in
places (1900 vs 1904 date systems, CR/LF line endings, "which application should I
install"). Little of that matters to a general library audience. What the lesson gets
right has only become more important: **data structure literacy**. Columns are variables,
rows are observations, one value per cell, raw data left untouched, dates are dangerous,
export to open formats.

Since 2016, fewer people need to hand-clean a spreadsheet. Google Sheets autoformats, has
version history, and now has Gemini in the sidebar. Excel has Copilot. ChatGPT and Claude
will reshape a table on request. So the mechanical skills in the lesson are increasingly
things a tool does for you. That makes the lesson a **supervision** skill: to get usable
output from an AI tool or a research assistant, you have to know what tidy data looks
like and be able to check whether what came back is correct.

### What is timeless

- columns are variables, rows are observations, one value per column per cell
- treat the source file as read-only; work in a named copy
- formatting (colour, position, merged cells) is not data and is absent from a CSV
- a date cell can hold a real date, text that looks like a date, or a real date with a
  wrong value
- be explicit and consistent about missing values, and decide what missing means
- export to CSV or another open, text-based format
- write down what you changed, somewhere the CSV does not drop it

### Adapting the Excel lesson for Google Sheets

| Lesson content (Excel) | Google Sheets |
|---|---|
| "Install LibreOffice or Excel" | Skip. Everyone has a browser. |
| 1900 / 1904 date systems | Not a thing in Sheets. Sheets is locale-sensitive instead: `File &rarr; Settings &rarr; Locale` sets the default date format and how ambiguous date *text* is read. It does not change which day an already-recognised date is. |
| "Save As CSV loses my dates" | In Sheets, CSV export writes the *displayed* date string. `4 Mar` exports with no year; `2016-03-04` keeps it. Fix: format with the full year before export. |
| `ISDATE()` to test date-vs-text | Do not use it: `ISDATE("July 20 1969")` returns TRUE, so parseable text passes. Use `=ISNUMBER()` / `=ISTEXT()`. |
| CR/LF line endings | Cut it. Not actionable for this audience. |
| Raw-data preservation | Version history helps, but teach the discipline: source file read-only, work in a named copy. Duplicating a *tab* keeps both in the same file, so it is a working copy, not a backup. |

### Pedagogical approach

- Live demo, learners follow in their own copy. No slides for the hands-on parts.
- Never talk more than ~15 minutes without learners doing something.
- Make deliberate mistakes and recover them on screen.
- Formative checks with a committed answer before the reveal, not "any questions?".
- Done / stuck signal (reactions or sticky notes); helpers move toward "stuck".
- Shared collaborative notes with the schedule, the practice Sheet link, and every
  function and link at the top, so latecomers self-onboard.
- Pair a confident spreadsheet user with a new one, on purpose.
- For a mixed / drop-in group: plan the demo for the middle, give helpers the bottom and
  an extension task the top, and provide `checkpoint_*` tabs so anyone can rejoin.

### Concept budget

Five core concepts, three practices, one framing idea. Do not add a sixth core concept
mid-session.

- **C1** a rectangular table processes consistently: columns = variables, rows =
  observations, one value per column per cell
- **C2** treat the source file as read-only; work in a named copy
- **C3** formatting is not data
- **C4** a recognised date is a value plus a display format; text that looks like a date
  may still be text
- **C5** QA blocks known-invalid entries; QC finds bad values already present
- **P1** represent missing values consistently, and decide what missing means
- **P2** export to CSV for a portable single table; keep documentation alongside
- **P3** write down what you changed, somewhere the CSV does not drop
- **F1** downstream tools including AI consume your structure; verify AI output against
  the raw data

### Prep

- `training_attendance_practice.xlsx` (linked at the top of this page) already has the
  nine tabs and the planted problems. Upload it to Drive, open as a Google Sheet, and
  make a force-copy link (share link, replace `/edit...` with `/copy`).
- The planted problems: `2016_messy` has two side-by-side tables, merged titles, the
  packed `PGR|PDRA|other` column, `1 hour` / `1.5 hours` text durations, two dates in
  1900, cancelled shown by grey row shading plus one stray `cancelled` note.
  `2017_messy` has text dates, a 1970 date, `GQ & DF`, a legend row, missing values.
  `dates` has the two 2017&rarr;2015 values, a mixed `len_hours` column, a `1.5` in
  `num_registered`, and `0` attendance on cancelled rows.
- Set the Sheet locale on purpose and record it.
- Confirm the current Data Validation wording in your own Google account.
- Run the AI prompt on `ai_input`; save one genuine flawed output; record model, date,
  prompt, and input / output row counts. Decide which AI tool you drive; do not assume
  learners have Gemini in Sheets.

### The AI segment

Do not rely on a live model failing in an instructive way. Run "Clean this up and make it
tidy" on the `ai_input` tab before class (12 rows, `source_row_id` 1&ndash;12; rows 5, 7,
11 have a blank `num_attended`), save an output that dropped a row or mangled a value,
and use that as the audit exercise. In class: show the saved output next to `ai_input`,
state the row counts, and have learners find the missing row by comparing `source_row_id`
values. Then ask how they would catch it without the row IDs (row counts before and
after; compare to the raw data). Optional live rerun to show output varies.

Takeaway: AI may shift work toward specifying and verifying transformations. It does not
remove the need to inspect and clean, and it does not count reliably.

---

*This page and the practice materials are shared under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The underlying lesson is
Library Carpentry's, also CC BY 4.0.*
