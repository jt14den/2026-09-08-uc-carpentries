# Tidy Data - full instructor script

**Rendered (pre-flight + bullets): [script.html](script.html)**

Times are clock time (PT); session runs 9:00 am - 12:00 pm.

---

## 1. Tidy Data

**Open `script.html` (link, bottom-right of this slide) on a second screen for the full per-slide script. Reveal's own presenter view (S) is unreliable from a CDN.**

**Holding slide - learners arriving (9:00)**

- Greet people by name
- Ask them to: (1) add their name to the Etherpad; (2) click the practice-sheet link; (3) File ▸ Make a copy; (4) rename it `tidy-data-yourname`
- Helpers watch the chat

**Etherpad - pin at the top:** practice-sheet copy link docs.google.com/spreadsheets/d/1NuHEr-1xDKpZHq77e5XDBdRAdROWbwEG/copy

**Zoom model, all session:**

- You screen-share the practice sheet during demos
- Learners work in their own copy the whole time
- Done / stuck = a reaction icon, or a line in the chat
- Pair / group work happens in the chat and the Etherpad; no breakout rooms

---

## 2. Everyone: make your copy
<sub>Before we start  ·  **DEMO**</sub>

**9:00–9:04 · make your copy · DEMO**

**SHOW**: this slide, the 3 steps

**DO** - share the Sheet and do this live in your own copy:

1. Open the practice-sheet link (it's the `/copy` URL, pinned in the Etherpad)
2. `File ▸ Make a copy`
3. Rename the copy `tidy-data-yourname`
4. Say: "the sheet I was given is evidence: I never type in it, I work in a copy"
5. Point at the tabs along the bottom (2016_messy, 2017_messy, dates, checkpoint_*, ai_input, Notes) - don't tour the messy data yet

**THEN**

- Wait for the chat to fill with "copied"
- Reiterate: you edit your copy, I edit mine on screen
- → slide 3

> *slide footnote:* the original is left **immutable**; your copy is a **working copy**

---

## 3. Two questions
<sub>To start  ·  **DISCUSS**</sub>

**9:04–9:07 · opening poll · DISCUSS · LC Episode 1**

**SHOW**: this slide, the two questions stay up

**DO**

- "Drop answers in the chat"
- Read 4–5 aloud
- Common frustrations: autocorrect changing values; dates mangled; a sort that shuffled rows; "it looked right but the formula was wrong"

**THEN**

- Reiterate: spreadsheets are great for entering and eyeballing data; today is about entering it so the next tool can use it
- → slide 4

> *slide footnote:* spreadsheets are strong for **data entry** and **quick views**; weaker for **reproducible analysis** and **version control**

---

## 4. Habits for data you're creating
<sub>Before we start</sub>

**9:07–9:09 · six habits**

- The whole lesson on one slide, and it is the lesson's keypoints list
- Don't over-explain; it's a preview
- → slide 5: everyone's first real edit

> *slide footnote:* these are the lesson's **keypoints**; consistent names and codes are a **controlled vocabulary**, which librarians already keep

---

## 5. Work in a copy: your first edit
<sub>Concept 2  ·  **DEMO** **EXERCISE**</sub>

**9:09-9:14 · your first edit · DEMO + EXERCISE · LC Episode 1**

Completes the warm-up: one real edit before minute 10.

**SHOW**: this slide, the "Everyone, now" box. Drop these steps in the Etherpad.

**DO** - share the Sheet, demo slowly, narrate each click:

1. Right-click the `2016_messy` tab ▸ **Duplicate**
2. Double-click the new tab, type `2016_clean`
3. The top of `2016_clean` has a blank row and a merged "RDM training" / "Open access" title row. Select those row numbers ▸ right-click ▸ **Delete rows**, so the real header (Date, Length (hours), ...) becomes row 1
4. Switch back to this slide; wait while everyone does the same in their own copy
5. Watch the chat for check / x; helpers DM the stuck

**THEN**

- Reiterate: from here on every edit happens in `2016_clean`; `2016_messy` is never touched. That's the habit.
- → slide 6

> *slide footnote:* raw data as a **single source of truth**, kept **immutable**; the lesson's first rule

---

## 6. The one rule
<sub>Concept 1</sub>

**9:14–9:18 · the one rule**

- Back on slides
- Name the two things they just did: worked in a copy, and made the sheet more of a rectangular table
- That's the rule. Keep it to the rule.
- → slide 7

> *slide footnote:* **tidy data** (Wickham). The grid is **rows & columns** in a database, **cases & variables** in stats, **observations & variables** here

---

## 7. What would a program choke on?
<sub>Concept 1  ·  **DISCUSS**</sub>

**9:18–9:24 · what would a program choke on · DISCUSS**

In the lesson this is the debrief after the cleaning exercise; we do it first to set up the exercise.

**SHOW**: this slide stays up; share `2016_messy` alongside, or flip between the two

**DO**

- A real 60 seconds of quiet
- "Type one thing in the chat"
- Read 4–5 aloud and group them: two side-by-side tables; packed PGR|PDRA|other column; colour-only cancelled rows; "1.5 hours" text in the Len column; the 1900 date

**THEN**

- Reiterate: a person reads this fine, a program can't
- Every item on your list is something we fix next
- → slide 8

> *slide footnote:* you're reading a **schema** - the column structure a tool expects. When it changes between files that's **schema drift**

---

## 8. One value per cell
<sub>Concept 1 · in practice</sub>

**9:24–9:28 · one value per cell**

- Show the split visually: `GQ & DF` into two columns; `45|0|0` into three
- You'll do it live in the next segment
- → slide 9, leave it up

> *slide footnote:* **atomic values** / **first normal form (1NF)**. The Sheets tool is **Data ▸ Split text to columns** (splitting on a **delimiter**)

---

## 9. Clean the messy training data
<sub>The core exercise  ·  **DEMO** **EXERCISE**</sub>

**9:28-9:53 · core exercise (25 min) · DEMO + EXERCISE · LC Episode 2**

**SHOW**: keep this slide up all segment. Put the task and the checkpoint tab names in the Etherpad.

**Layout:** `2016_messy` and `2017_messy` each hold **two tables side by side** - RDM training on the left, Open access on the right. You demo the left table; learners take the right table, then the 2017 tab.

**DO - (a) demo the RDM (left) table in 2016_clean, ~8 min:**

1. Title / blank rows already gone from slide 5. If not: select them ▸ right-click ▸ Delete rows
2. The `PGR|PDRA|other` column packs three counts in one cell (e.g. `45|0|0` = 45 postgrads, 0 postdocs, 0 other). Select that column ▸ **Data ▸ Split text to columns** ▸ separator: **Custom** ▸ type `|`
3. Rename the three new columns `pgr`, `pdra`, `other`
4. Nulls: replace any stray `na` / `n/a` / `-` in the count columns with an empty cell (this session's null is a blank)
5. You'll pass a row with a **1900 date** - say "that's a date bug, we fix dates after the break", leave it
6. Narrate every click

**DO - (b) learners, ~12 min:**

- **Open access (right) table** in 2016_clean: the `Len` column mixes "1.5 hours", "1 hour", "1 hours" - make each a plain number of hours. Watch for name drift in `Delivered by`. One row is grey-shaded / has a stray "cancelled" note - add a `cancelled` column (yes/no), then clear the shading and the note
- **2017 tab** (same side-by-side layout): text dates like "7/8 Feb" and "2 June?"; a 1970 date; `GQ & DF` in one Delivered-by cell (split into two columns); packed counts with leading zeros like `15|03|00`; blank / legend rows at the bottom to delete
- Check the result against `checkpoint_clean`
- Post your **data row count** (rows, not counting the header) in the chat

**THEN - reconvene:**

- Show `checkpoint_combined` - 2016 and 2017 cleaned the same way, stacked into one table, with a `year` column added
- Row-count check aloud: 2016 rows + 2017 rows = combined table minus one header
- Ask whose count differed and why (a cancelled row kept vs dropped, or a stray blank row)
- Reiterate the four moves: split packed columns; meaning as a value not colour; one consistent null; then stack the years
- → slide 10

> *slide footnote:* the moves: **decomposition** (split packed columns), a **cancelled** flag not colour, consistent **nulls**; combining years then checking counts is basic **reconciliation**

---

## 10. Formatting is not data
<sub>Concept 3</sub>

**after the break (10:01) · formatting is not data**

- Names what they just did with the grey rows
- From LC "Common mistakes": merged cells; formatting-as-info; units / comments in cells; metadata in the data table
- Ask: how would a script know those rows were cancelled? It wouldn't
- → slide 11

> *slide footnote:* **separation of data from presentation** - the same idea as content vs. style on the web. Colour-as-data is a known **anti-pattern**

---

## 11. Zeros and nulls
<sub>Practice 1</sub>

**~10:03 · zeros and nulls**

- From LC "Common mistakes": fill in zeroes; use one null value for missing
- Tie forward: in the dates tab, cancelled rows carry `num_attended` 0. Real zero, or a stand-in for missing?
- A data-dictionary question. Flag it for the QC exercise
- → slide 12

> *slide footnote:* `-999` and `0`-for-missing are **sentinel values** / **magic numbers**. Missing ≠ not-applicable ≠ zero ≠ unknown is **null semantics**

---

## 12. A date has three states
<sub>Concept 4  ·  **DISCUSS**</sub>

**10:05-10:15 · a date has three states · DISCUSS · LC Episode 3**

**SHOW**: this slide (three identical-looking cells + the question). Leave it up.

**DO**

1. Ask: "these all show 2016-03-04 - what could be different underneath? what's ambiguous?" Take 2-3 chat answers
2. Walk the three states on the slide: a real date value / text that looks like a date / a real date with the wrong day
3. Switch to the Sheet (`dates` tab): click a real date, **Format ▸ Number ▸ Number** - it shows the underlying serial number (e.g. 42433). Click a text date - Format ▸ Number shows nothing numeric, and it's left-aligned
4. Type `=ISNUMBER(A2)` next to one of each: TRUE vs FALSE

**THEN**

- Reiterate: `ISNUMBER` TRUE means it's a real date value - **not** that the date is correct
- → slide 13 (locale)

> *slide footnote:* a stored value vs. how it looks is **data type** vs. **lexical representation**; Sheets guessing on entry is **type inference**. Dates are stored as **serial numbers**

---

## 13. Locale, and the safe move
<sub>Concept 4</sub>

**10:15–10:20 · locale**

- Replaces the lesson's 1900 / 1904 date-system material (not a thing in Sheets)
- Say your sheet's locale out loud
- → slide 14 (dates exercise)

> *slide footnote:* date-text ambiguity is a **locale** / **internationalisation (i18n)** problem; `yyyy-mm-dd` is the **ISO 8601** standard

---

## 14. Dates as data
<sub>Concept 4  ·  **DEMO** **EXERCISE**</sub>

**10:20-10:32 · dates as data · DEMO + EXERCISE · LC Episode 3, Challenges 1 & 2**

**SHOW**: this slide, both boxes. Put both in the Etherpad.

**DO - Part 1 (~6 min), in the `dates` tab:**

1. In three empty columns to the right of the data, first data row (row 2): `=MONTH(A2)`, `=DAY(A2)`, `=YEAR(A2)` (A2 is the date cell)
2. Format those cells as plain number: **Format ▸ Number ▸ Number**, so the year doesn't display as a date
3. Select the three cells, drag the fill handle down to the last data row
4. Learners do the same; ask for the row numbers where `YEAR` shows **2017** (should be 2015) in the chat

**DO - Part 2 (~4 min):**

1. **File ▸ Download ▸ Comma-separated values (.csv)** - downloads the `dates` tab only
2. Open the downloaded file in **TextEdit** (Mac) or **Notepad** (Windows): the dates show as month/day, **no year** - the CSV kept only the displayed string
3. Bring it back: **File ▸ Import ▸ Upload** ▸ pick the CSV ▸ "Insert new sheet(s)". The dates now show with the **current year**, not 2015
4. Ask in the chat: what changed, and why

**THEN - reconvene:**

- The two wrong-year rows read 2017 - the year someone typed the data - not 2015, the year of the event. A real date value, wrong day; every format check passes
- The same `=YEAR` trick catches the 1900 date back in 2016_clean
- Reiterate: store dates as `yyyy-mm-dd` or as year/month/day columns; format the full year before you export; open the file and check dates after any export
- → slide 15

> *slide footnote:* the wrong-year rows are a **data-entry error** (entry year vs. event year) that passes every format check; the CSV round-trip is **lossy** and not **reversible**

---

## 15. QA blocks · QC finds
<sub>Concept 5</sub>

**10:32-10:40 · QA blocks / QC finds · one demo**

**SHOW**: this slide - QA (the gate) vs QC (the flashlight)

**DO** - switch to the Sheet (`dates` tab):

1. Select the `num_registered` column
2. **Data ▸ Data validation ▸ Add rule**
3. Criteria: **Value is a number between** 1 and 100 (or Advanced ▸ Whole number, min 1, max 100)
4. Set "If the data is invalid" to **Reject the input**
5. Click a cell in that column, type something invalid (500, or "abc") - Sheets refuses it
6. Say: you could do the same with a dropdown list on the session-type column, so no one free-types a new spelling

**THEN**

- Reiterate: QA stops bad data at the point of entry; QC finds bad data already in the sheet
- Next slide is the QC side
- → slide 16, leave it up

> *slide footnote:* **QA** = prevention (process), **QC** = detection (product). "Reject the input" is a **constraint** / **input validation**

---

## 16. Sort, then colour-scale
<sub>Concept 5  ·  **EXERCISE**</sub>

**10:40-10:52 · sort, then colour-scale · EXERCISE · LC Episode 4**

**SHOW**: this slide (Sort box + Colour scale box). Put both in the Etherpad.

**DO** - no demo; learners work in their own copy of the `dates` tab (~6 min):

- **Sort:** select the **whole** dates table (all columns, all rows incl. header) ▸ **Data ▸ Sort range ▸ Advanced range sorting options** ▸ tick **"Data has header row"** ▸ sort by `len_hours`, Z → A
- What's odd: "90 min" / "1 hour" / "15 min" as text sort to the top; the big raw numbers 90 / 60 / 15 stand out too
- **Colour scale:** select the `num_attended` column ▸ **Format ▸ Conditional formatting ▸ Colour scale** ▸ scan for outliers - two cells sit at 0

**THEN - reconvene:**

- Those two 0s are the cancelled classes - is a 0 a real zero, or a stand-in for "didn't happen"? A data-dictionary call; tie back to slide 11 (zeros and nulls)
- Why select the whole table first: sorting a partial selection shears rows away from their keys and corrupts the data
- → slide 17

> *slide footnote:* scanning sorted extremes is **range checking** / basic **outlier detection**. Sorting a partial selection **corrupts** a dataset - always select the whole table

---

## 17. Export to CSV
<sub>Practice 2</sub>

**11:03–11:15 · export to CSV**

- You already showed the CSV round-trip in the dates exercise
- Here: name why CSV anyway: portable, open, one table, machine-readable
- LC Episodes "Exporting data" and "Data format caveats"
- → slide 18

> *slide footnote:* a CSV is a **flat file**, **machine-readable** and **non-proprietary**; the export is **lossy** and doesn't **round-trip**. Library of Congress lists it as a **preferred format**

---

## 18. Write down what you changed
<sub>Practice 3</sub>

**~2 min · write down what you changed**

- LC "Formatting data": keep your clean-up steps in a plain text file in the same folder as the data
- Show your own changelog file or tab as an example
- → slide 19

> *slide footnote:* where data came from is **provenance**; what happened to it is **lineage**; the goal is **reproducible** cleaning

---

## 19. Everything downstream reads your structure
<sub>Framing idea</sub>

**11:15–11:20 · everything downstream reads your structure**

- This slide is beyond the core LC lesson - a short note on AI as a downstream consumer
- **Data caution first:** today's data is fictional
- No real patron / student / personnel / health / licensed / unpublished research data into an AI service unless it's institutionally approved
- → slide 20 (vocab)

> *slide footnote:* reshape-then-hand-off is the **"T" in ETL** (extract, transform, load); the whole chain is a **data pipeline**. Fluent-but-wrong output is **hallucination**

---

## 20. What the field calls this
<sub>You now have the words</sub>

**11:20–11:25 · what the field calls this**

- Don't read the whole slide
- Point at 3–4 they'll hit soonest: ISO 8601; wide vs long; data validation
- It's also on the notes page
- → slide 21

---

## 21. Recap

**11:25–11:35 · recap**

- The left column is the lesson's keypoints, verbatim
- Then the feedback link (in the Etherpad)
- Buffer 11:35–12:00: questions, or an early finish

---
