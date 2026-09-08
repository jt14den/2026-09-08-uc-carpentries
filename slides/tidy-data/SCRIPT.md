# Tidy Data — full instructor script

Every slide's speaker notes, in order — the same text reveal shows in presenter view (press **S** in the deck). Open the deck alongside this.

- Deck: <https://www.tim-dennis.com/2026-09-08-uc-carpentries/slides/tidy-data/>
- One-page run card: `RUN-CARD.md`
- Reference (menu paths, functions): the notes page

Legend: **DEMO** = you drive the Sheet · **EXERCISE** = learners work in their copy · **DISCUSS** = chat/pad prompt

---

## 1. Tidy Data

HOLDING SLIDE (learners arriving, 0:00). Greet people by name. Ask them to (1) add their name to the Etherpad, (2) click the practice-sheet link, (3) File Make a copy, (4) rename it "tidy-data-YOURNAME". Helpers watch the chat.

Practice-sheet copy link (pin at the top of the Etherpad): https://docs.google.com/spreadsheets/d/1NuHEr-1xDKpZHq77e5XDBdRAdROWbwEG/copy

Zoom model all session: your screen shares the practice sheet during demos; learners work in their own copy throughout; "done/stuck" via reaction icons or a chat line; pair/group work happens in the chat and the Etherpad, not breakout rooms.

---

## 2. Everyone: make your copy
<sub>Before we start  ·  **DEMO**</sub>

0:00–0:04. Share your own copy of the practice sheet. Do the three steps live so they mirror them. Say: "the sheet I was given is evidence; I never type in it, I work in a copy." Point out the tabs along the bottom (2016_messy, 2017_messy, dates, checkpoint_*, ai_input, Notes) so they know the shape of what's here. Don't tour the messy data yet. Wait for the chat to show most people have a renamed copy.

> *slide footnote:* the original is left immutable; your copy is a working copy

---

## 3. Two questions
<sub>To start  ·  **DISCUSS**</sub>

LC Episode 1 opening. Keep it to ~3 min. Read 4–5 chat answers. Common frustrations: autocorrect changing values, dates mangled, sort that shuffled rows, "it looked right but the formula was wrong". Land on: spreadsheets are great for entering and eyeballing data, and today is about entering it so the next tool can use it.

> *slide footnote:* spreadsheets are strong for data entry and quick views; weaker for reproducible analysis and version control

---

## 4. Habits for data you're creating
<sub>Before we start</sub>

0:07–0:09. This is the whole lesson on one slide, and it is the lesson's keypoints list. Don't over-explain, it's a preview. Next slide: everyone's first real edit.

> *slide footnote:* these are the lesson's keypoints; consistent names and codes are a controlled vocabulary, which librarians already keep

---

## 5. Work in a copy: your first edit
<sub>Concept 2  ·  **DEMO** **EXERCISE**</sub>

0:09–0:14. This completes the warm-up: one real edit before minute 10 (LC Episode 1). SWITCH TO SHEET. Demo the three steps slowly in your copy - right-click 2016_messy, Duplicate, rename 2016_clean, delete the title and spacer rows. Then wait while everyone does the same in their copy; watch the chat for check / x. From here on every edit happens in 2016_clean and 2016_messy is never touched. SWITCH BACK TO SLIDES.

> *slide footnote:* raw data as a single source of truth, kept immutable; the lesson's first rule

---

## 6. The one rule
<sub>Concept 1</sub>

0:14–0:18. Back on slides. Name the two things they just did: worked in a copy, and made the sheet a bit more of a rectangular table. That's the rule. Keep it to the rule.

> *slide footnote:* tidy data (Wickham). The grid is rows & columns in a database, cases & variables in stats, observations & variables here

---

## 7. What would a program choke on?
<sub>Concept 1  ·  **DISCUSS**</sub>

0:18–0:24. Share 2016_messy on screen while they look at their own. A real 60 seconds of quiet, then "type one thing in the chat." Read 4–5 aloud and group them: two side-by-side tables / packed PGR|PDRA|other column / colour-only cancelled rows / "1.5 hours" text in the Len column / the 1900 date. Land on: a person reads this fine, a program can't. In the lesson this is the group debrief after the cleaning exercise; we do it first to set up the exercise.

> *slide footnote:* you're reading a schema - the column structure a tool expects. When it changes between files that's schema drift

---

## 8. One value per cell
<sub>Concept 1 · in practice</sub>

0:24–0:28, slides, then into the exercise. Show the split visually here; do it on screen in the next slide's demo.

> *slide footnote:* atomic values / first normal form (1NF). The Sheets tool is Data ▸ Split text to columns (splitting on a delimiter)

---

## 9. Clean the messy training data
<sub>The core exercise  ·  **DEMO** **EXERCISE**</sub>

0:28–0:53, the core segment (25 min). This is LC Episode 2's exercise. SWITCH TO SHEET.

Demo on the RDM table (~8 min): unmerge the title (Format ▸ Merge cells ▸ Unmerge), delete title/spacer rows, select PGR|PDRA|other ▸ Data ▸ Split text to columns ▸ separator "|", rename the three columns, add a cancelled column and fill yes/no from the grey rows, make blank/na consistent. Narrate every click. Flag the 1900 date out loud but do NOT fix it - "dates get their own segment".

Learners take the Open access table (units in Len, name drift) then the 2017 tab (text dates, GQ & DF, legend row), ~12 min, checking checkpoint_clean. Watch the chat: row counts should converge. Reconvene, show checkpoint_combined (2016 + 2017 cleaned the same way, plus a year column). Row-count check: 2016 rows + 2017 rows = combined minus one header. Ask whose count differed and why (usually a cancelled row or a stray blank). SWITCH BACK TO SLIDES.

> *slide footnote:* the moves: decomposition (split packed columns), a cancelled flag not colour, consistent nulls; combining years then checking counts is basic reconciliation

---

## 10. Formatting is not data
<sub>Concept 3</sub>

Slides, ~3 min. Names what they just did with the grey rows. From LC Episode "Common mistakes": merged cells, formatting-as-info, units/comments in cells, metadata in the data table. Ask: how would a script know those rows were cancelled? It wouldn't.

> *slide footnote:* separation of data from presentation - the same idea as content vs. style on the web. Colour-as-data is a known anti-pattern

---

## 11. Zeros and nulls
<sub>Practice 1</sub>

~3 min, slides. From LC "Common mistakes": fill in zeroes; use an appropriate null. Tie forward: in the dates tab, cancelled rows carry num_attended 0. Real zero, or a stand-in for missing? A data-dictionary question. Flag it for the QC exercise.

> *slide footnote:* -999 and 0-for-missing are sentinel values / magic numbers. Missing ≠ not-applicable ≠ zero ≠ unknown is null semantics

---

## 12. A date has three states
<sub>Concept 4  ·  **DISCUSS**</sub>

1:05–1:15. This is LC Episode 3's discussion ("How can these features create data ambiguity? What changes between columns? What lacks specificity?"). Take a couple of chat answers, then reveal the three states. SWITCH TO SHEET briefly: click a real date, Format ▸ Number shows the serial number; click a text date, it left-aligns with no serial. Note: ISNUMBER TRUE means it's a real date, not that the date is correct. Back to slides for locale.

> *slide footnote:* a stored value vs. how it looks is data type vs. lexical representation; Sheets guessing on entry is type inference. Dates are stored as serial numbers

---

## 13. Locale, and the safe move
<sub>Concept 4</sub>

1:15–1:20, slides. This replaces the lesson's 1900/1904 date-system material (not a thing in Sheets). Say your sheet's locale out loud. Then the dates exercise.

> *slide footnote:* date-text ambiguity is a locale / internationalisation (i18n) problem; yyyy-mm-dd is the ISO 8601 standard

---

## 14. Dates as data
<sub>Concept 4  ·  **DEMO** **EXERCISE**</sub>

1:20–1:32. LC Episode 3, Challenge 1 and Challenge 2, verbatim.

Part 1: SWITCH TO SHEET, demo MONTH/DAY/YEAR on the first 2–3 rows, format as number. Learners fill down, ~4 min. The two rows show 2017 (the year the data was entered) not 2015 (the workshop year). Same trick with YEAR catches the 1900 date in 2016_messy.

Part 2: demo File ▸ Download ▸ CSV on the dates tab, open the file in a text editor - the dates show as month/day with no year. Re-open in Sheets - they come back with the current year, not 2015. Point: exporting and re-importing changed the data again. SWITCH BACK TO SLIDES.

> *slide footnote:* the wrong-year rows are a data-entry error (entry year vs. event year) that passes every format check; the CSV round-trip is lossy and not reversible

---

## 15. QA blocks · QC finds
<sub>Concept 5</sub>

1:32–1:40, slides + a QA demo. SWITCH TO SHEET: select num_registered ▸ Data ▸ Data validation ▸ Whole number ▸ min 1 max 100 ▸ "Reject the input". Try a bad value, show it blocked. Mention you can add a dropdown for the session type too. Then set up the sort for the QC exercise.

> *slide footnote:* QA = prevention (process), QC = detection (product). "Reject the input" is a constraint / input validation

---

## 16. Sort, then colour-scale
<sub>Concept 5  ·  **EXERCISE**</sub>

1:40–1:52. LC Episode 4, both QC challenges. Sort: "90 min", "1 hour", "15 min" as text sort to the top; the numeric 90/60/15 also stand out. Colour scale on num_attended: two cells at 0 pop - those two classes were cancelled. Connect back to the missing-values slide: is that 0 real, or missing? A data-dictionary call. SWITCH BACK TO SLIDES.

> *slide footnote:* scanning sorted extremes is range checking / basic outlier detection. Sorting a partial selection corrupts a dataset - always select the whole table

---

## 17. Export to CSV
<sub>Practice 2</sub>

2:03–2:15. You already showed the CSV round-trip in the dates exercise. Here, name why CSV anyway: portable, open, one table, machine-readable. LC Episodes "Exporting data" and "Data format caveats".

> *slide footnote:* a CSV is a flat file, machine-readable and non-proprietary; the export is lossy and doesn't round-trip. Library of Congress lists it as a preferred format

---

## 18. Write down what you changed
<sub>Practice 3</sub>

~2 min, slides. LC Episode "Formatting data": keep track of your analyses in a plain text file in the same folder. Show your own changelog file or tab as an example.

> *slide footnote:* where data came from is provenance; what happened to it is lineage; the goal is reproducible cleaning

---

## 19. Everything downstream reads your structure
<sub>Framing idea</sub>

2:15–2:20, slides. This and the next slide are beyond the LC lesson - your run sheet's AI segment. Data caution first: today's data is fictional. Do not paste real patron, student, personnel, health, licensed, or unpublished research data into an AI service unless it's institutionally approved.

> *slide footnote:* reshape-then-hand-off is the "T" in ETL (extract, transform, load); the whole chain is a data pipeline. Fluent-but-wrong output is hallucination

---

## 20. Check the AI's work by counting
<sub>Framing idea · verify  ·  **EXERCISE**</sub>

2:25–2:38. SWITCH TO SHEET. Show the pre-run AI output tab next to ai_input. Learners compare source_row_id columns and post the missing id, ~4 min. Then: "how would you catch this without the id column?" (row counts; compare to raw). Optional live re-run to show the output varies. Takeaway: AI shifts the work to specifying and verifying; it still doesn't count reliably. SWITCH BACK TO SLIDES.

> *slide footnote:* the source_row_id is a surrogate key; matching input to output on it is a join and the check is reconciliation. Without a key you'd need fuzzy matching / record linkage

---

## 21. What the field calls this
<sub>You now have the words</sub>

2:38–2:40. Don't read the whole slide. Point at 3 or 4 they'll hit soonest (ISO 8601, wide vs long, data validation). It's also on the notes page.

---

## 22. Recap

2:40–2:50. The left column is the lesson's keypoints, verbatim. Then the feedback form. 10-minute buffer after this.

---
