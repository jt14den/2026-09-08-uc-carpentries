# Tidy Data - full instructor script

Every slide's speaker notes, in order - the same text reveal shows in presenter view (press **S** in the deck). Open the deck alongside this.

Transition slides run **SHOW** (what's on the slide) then **DO** (drive the Sheet / learners work) then **THEN** (debrief, what to reiterate, advance).

- Deck: <https://www.tim-dennis.com/2026-09-08-uc-carpentries/slides/tidy-data/>
- One-page run card: `RUN-CARD.md`

Legend: **DEMO** = you drive the Sheet  ·  **EXERCISE** = learners work in their copy  ·  **DISCUSS** = chat / pad prompt

---

## 1. Tidy Data

**Holding slide - learners arriving (0:00)**

- Greet people by name
- Ask them to: (1) add their name to the Etherpad; (2) click the practice-sheet link; (3) File ▸ Make a copy; (4) rename it `tidy-data-yourname`
- Helpers watch the chat

**Etherpad - pin at the top:** practice-sheet copy link 

 docs.google.com/spreadsheets/d/1NuHEr-1xDKpZHq77e5XDBdRAdROWbwEG/copy

**Zoom model, all session:**

- You screen-share the practice sheet during demos
- Learners work in their own copy the whole time
- Done / stuck = a reaction icon, or a line in the chat
- Pair / group work happens in the chat and the Etherpad; no breakout rooms

---

## 2. Everyone: make your copy
<sub>Before we start  ·  **DEMO**</sub>

**0:00–0:04 · make your copy · DEMO**

**SHOW**: this slide, the 3 steps

**DO**

1. Share the Sheet; do the 3 steps live in your own copy
2. Say: "the sheet I was given is evidence: I never type in it, I work in a copy"
3. Point at the tabs along the bottom (2016_messy, 2017_messy, dates, checkpoint_*, ai_input, Notes)
4. Don't tour the messy data yet

**THEN**

- Wait for the chat to fill with "copied"
- Reiterate: you edit your copy, I edit mine on screen
- → slide 3

> *slide footnote:* the original is left immutable; your copy is a working copy

---

## 3. Two questions
<sub>To start  ·  **DISCUSS**</sub>

**0:04–0:07 · opening poll · DISCUSS · LC Episode 1**

**SHOW**: this slide, the two questions stay up

**DO**

- "Drop answers in the chat"
- Read 4–5 aloud
- Common frustrations: autocorrect changing values; dates mangled; a sort that shuffled rows; "it looked right but the formula was wrong"

**THEN**

- Reiterate: spreadsheets are great for entering and eyeballing data; today is about entering it so the next tool can use it
- → slide 4

> *slide footnote:* spreadsheets are strong for data entry and quick views; weaker for reproducible analysis and version control

---

## 4. Habits for data you're creating
<sub>Before we start</sub>

**0:07–0:09 · six habits**

- The whole lesson on one slide, and it is the lesson's keypoints list
- Don't over-explain; it's a preview
- → slide 5: everyone's first real edit

> *slide footnote:* these are the lesson's keypoints; consistent names and codes are a controlled vocabulary, which librarians already keep

---

## 5. Work in a copy: your first edit
<sub>Concept 2  ·  **DEMO** **EXERCISE**</sub>

**0:09–0:14 · your first edit · DEMO + EXERCISE · LC Episode 1**

Completes the warm-up: one real edit before minute 10.

**SHOW**: this slide, the "Everyone, now" box. Leave it up; drop the 3 steps in the Etherpad.

**DO**

1. Switch your share to the Sheet; demo the 3 steps slowly in your copy
2. Switch back so they can see the box
3. Wait while everyone does it in their own copy
4. Watch the chat for check / x; helpers DM the stuck

**THEN**

- Reiterate: from here on every edit happens in `2016_clean`; `2016_messy` is never touched. That's the habit.
- → slide 6

> *slide footnote:* raw data as a single source of truth, kept immutable; the lesson's first rule

---

## 6. The one rule
<sub>Concept 1</sub>

**0:14–0:18 · the one rule**

- Back on slides
- Name the two things they just did: worked in a copy, and made the sheet more of a rectangular table
- That's the rule. Keep it to the rule.
- → slide 7

> *slide footnote:* tidy data (Wickham). The grid is rows & columns in a database, cases & variables in stats, observations & variables here

---

## 7. What would a program choke on?
<sub>Concept 1  ·  **DISCUSS**</sub>

**0:18–0:24 · what would a program choke on · DISCUSS**

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

> *slide footnote:* you're reading a schema - the column structure a tool expects. When it changes between files that's schema drift

---

## 8. One value per cell
<sub>Concept 1 · in practice</sub>

**0:24–0:28 · one value per cell**

- Show the split visually: `GQ & DF` into two columns; `45|0|0` into three
- You'll do it live in the next segment
- → slide 9, leave it up

> *slide footnote:* atomic values / first normal form (1NF). The Sheets tool is Data ▸ Split text to columns (splitting on a delimiter)

---

## 9. Clean the messy training data
<sub>The core exercise  ·  **DEMO** **EXERCISE**</sub>

**0:28–0:53 · core exercise (25 min) · DEMO + EXERCISE · LC Episode 2**

**SHOW**: keep this slide up the whole segment (task + "how we'll run it"). Put the task in the Etherpad.

**DO - (a) demo the RDM table, ~8 min:**

1. Unmerge the title (Format ▸ Merge cells ▸ Unmerge)
2. Delete title / spacer rows if any remain
3. Select PGR|PDRA|other ▸ Data ▸ Split text to columns ▸ separator "|"
4. Rename the three new columns
5. Add a `cancelled` column; fill yes/no from the grey rows
6. Make blank / na consistent
7. Narrate every click. Flag the 1900 date out loud; do NOT fix it

**DO - (b) learners, ~12 min:**

- Clean the Open access table (units in Len, name drift), then the 2017 tab (text dates, GQ & DF, legend row)
- Check against `checkpoint_clean`
- Post row counts in the chat; watch for check / x; helpers DM the stuck

**THEN - reconvene:**

- Show `checkpoint_combined` (both years cleaned the same way, plus a year column)
- Row-count check aloud: 2016 + 2017 = combined minus one header
- Ask whose count differed and why (a cancelled row, or a stray blank)
- Reiterate the four moves: split packed columns; value not colour; one null; combine
- → slide 10

> *slide footnote:* the moves: decomposition (split packed columns), a cancelled flag not colour, consistent nulls; combining years then checking counts is basic reconciliation

---

## 10. Formatting is not data
<sub>Concept 3</sub>

**after the break (1:01) · formatting is not data**

- Names what they just did with the grey rows
- From LC "Common mistakes": merged cells; formatting-as-info; units / comments in cells; metadata in the data table
- Ask: how would a script know those rows were cancelled? It wouldn't
- → slide 11

> *slide footnote:* separation of data from presentation - the same idea as content vs. style on the web. Colour-as-data is a known anti-pattern

---

## 11. Zeros and nulls
<sub>Practice 1</sub>

**~1:03 · zeros and nulls**

- From LC "Common mistakes": fill in zeroes; use one null value for missing
- Tie forward: in the dates tab, cancelled rows carry `num_attended` 0. Real zero, or a stand-in for missing?
- A data-dictionary question. Flag it for the QC exercise
- → slide 12

> *slide footnote:* -999 and 0-for-missing are sentinel values / magic numbers. Missing ≠ not-applicable ≠ zero ≠ unknown is null semantics

---

## 12. A date has three states
<sub>Concept 4  ·  **DISCUSS**</sub>

**1:05–1:15 · a date has three states · DISCUSS · LC Episode 3**

**SHOW**: this slide (three identical-looking cells + the question). Leave it up.

**DO**

1. Take a couple of chat answers to "what could differ / be ambiguous"
2. Walk the three states on the slide
3. Switch to the Sheet briefly: a real date, Format ▸ Number shows the serial number; a text date left-aligns with none

**THEN**

- Reiterate: `ISNUMBER` TRUE means it's a real date, not that the date is correct
- → slide 13 (locale)

> *slide footnote:* a stored value vs. how it looks is data type vs. lexical representation; Sheets guessing on entry is type inference. Dates are stored as serial numbers

---

## 13. Locale, and the safe move
<sub>Concept 4</sub>

**1:15–1:20 · locale**

- Replaces the lesson's 1900 / 1904 date-system material (not a thing in Sheets)
- Say your sheet's locale out loud
- → slide 14 (dates exercise)

> *slide footnote:* date-text ambiguity is a locale / internationalisation (i18n) problem; yyyy-mm-dd is the ISO 8601 standard

---

## 14. Dates as data
<sub>Concept 4  ·  **DEMO** **EXERCISE**</sub>

**1:20–1:32 · dates as data · DEMO + EXERCISE · LC Episode 3, Challenges 1 & 2**

**SHOW**: this slide, both exercise boxes. Leave it up; put both in the Etherpad.

**DO - Part 1:**

1. Switch to the Sheet; demo `=MONTH` / `=DAY` / `=YEAR` on the first 2–3 rows of `dates`, format as number
2. Learners fill down (~4 min), post the wrong-year rows in chat

**DO - Part 2:**

1. Demo File ▸ Download ▸ CSV on the dates tab
2. Open the file in a text editor: dates show as month / day, no year
3. Re-import to Sheets: dates come back with the current year, not 2015

**THEN - reconvene:**

- The two rows read 2017 (data-entry year) not 2015 (workshop year); an error that passes every format check
- The same YEAR trick catches the 1900 date in 2016_messy
- Reiterate: store dates as `yyyy-mm-dd` or y / m / d columns; full year before export; check dates after any export
- → slide 15

> *slide footnote:* the wrong-year rows are a data-entry error (entry year vs. event year) that passes every format check; the CSV round-trip is lossy and not reversible

---

## 15. QA blocks · QC finds
<sub>Concept 5</sub>

**1:32–1:40 · QA blocks / QC finds · one demo**

**SHOW**: this slide: QA (the gate) vs QC (the flashlight)

**DO**

1. Switch to the Sheet: select `num_registered` ▸ Data ▸ Data validation ▸ Whole number ▸ min 1 max 100 ▸ "Reject the input"
2. Try a bad value; show it blocked
3. Mention you could add a dropdown for the session type

**THEN**

- Reiterate: QA stops bad data at entry; QC finds bad data already there
- Next we do the QC side
- → slide 16, leave it up

> *slide footnote:* QA = prevention (process), QC = detection (product). "Reject the input" is a constraint / input validation

---

## 16. Sort, then colour-scale
<sub>Concept 5  ·  **EXERCISE**</sub>

**1:40–1:52 · sort, then colour-scale · EXERCISE · LC Episode 4**

**SHOW**: this slide (Sort box + Colour scale box). Leave it up; learners follow the steps straight from it. Put them in the Etherpad.

**DO**: no demo; learners work in their own copies (~6 min)

- Sort: "90 min" / "1 hour" text values sort to the top; the numeric 90 / 60 / 15 also stand out
- Colour scale on `num_attended`: two cells at 0 pop

**THEN - reconvene:**

- Those two 0s are the cancelled classes
- Reiterate: is a 0 a real zero or a stand-in for missing? Tie back to slide 11 (zeros and nulls)
- The two pre-sort moves: select the whole table; tick "Data has header row"
- → slide 17

> *slide footnote:* scanning sorted extremes is range checking / basic outlier detection. Sorting a partial selection corrupts a dataset - always select the whole table

---

## 17. Export to CSV
<sub>Practice 2</sub>

**2:03–2:15 · export to CSV**

- You already showed the CSV round-trip in the dates exercise
- Here: name why CSV anyway: portable, open, one table, machine-readable
- LC Episodes "Exporting data" and "Data format caveats"
- → slide 18

> *slide footnote:* a CSV is a flat file, machine-readable and non-proprietary; the export is lossy and doesn't round-trip. Library of Congress lists it as a preferred format

---

## 18. Write down what you changed
<sub>Practice 3</sub>

**~2 min · write down what you changed**

- LC "Formatting data": keep your clean-up steps in a plain text file in the same folder as the data
- Show your own changelog file or tab as an example
- → slide 19

> *slide footnote:* where data came from is provenance; what happened to it is lineage; the goal is reproducible cleaning

---

## 19. Everything downstream reads your structure
<sub>Framing idea</sub>

**2:15–2:20 · everything downstream reads your structure**

- This slide and the next are beyond the LC lesson; your run sheet's AI segment
- **Data caution first:** today's data is fictional
- No real patron / student / personnel / health / licensed / unpublished research data into an AI service unless it's institutionally approved
- → slide 20

> *slide footnote:* reshape-then-hand-off is the "T" in ETL (extract, transform, load); the whole chain is a data pipeline. Fluent-but-wrong output is hallucination

---

## 20. Check the AI's work by counting
<sub>Framing idea · verify  ·  **EXERCISE**</sub>

**2:25–2:38 · check the AI by counting · EXERCISE**

**SHOW**: this slide (12 in, 11 out; the missing source_row_id). Leave it up.

**DO**

1. Switch to the Sheet; show the pre-built AI-output tab next to `ai_input`
2. Learners compare the source_row_id columns, post the missing id in chat (~4 min)

**THEN**

- Ask: "how would you catch this without the id column?" (row counts before and after; compare to the raw)
- Optional: live re-run to show the output varies
- Reiterate: AI shifts the work to specifying and verifying; it still doesn't count reliably
- → slide 21

> *slide footnote:* the source_row_id is a surrogate key; matching input to output on it is a join and the check is reconciliation. Without a key you'd need fuzzy matching / record linkage

---

## 21. What the field calls this
<sub>You now have the words</sub>

**2:38–2:40 · what the field calls this**

- Don't read the whole slide
- Point at 3–4 they'll hit soonest: ISO 8601; wide vs long; data validation
- It's also on the notes page
- → slide 22

---

## 22. Recap

**2:40–2:50 · recap**

- The left column is the lesson's keypoints, verbatim
- Then the feedback link (in the Etherpad)
- 10-minute buffer after this: questions, or an early finish

---
