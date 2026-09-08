# Tidy Data — instructor run card

One page. Keep this where you can see it while you drive the Sheet. The full per-slide script is at **`script.html`** (`/slides/tidy-data/script.html`) — open it on a second screen or tablet; the deck's built-in presenter view (press `S`) is unreliable from a CDN, so use `script.html` instead.

**Zoom:** share **one window** (the Sheet), not the whole screen. Zoom the Sheet to ~150%. Lead helper drives the chat so you can watch the Sheet. Say what you are about to click *before* you click it.

---

## Pre-flight — do these before you teach

- [ ] Practice sheet sharing = **Anyone with the link → Viewer**
- [ ] Tabs present: `2016_messy` `2017_messy` `dates` `checkpoint_clean` `checkpoint_combined` `ai_input` `Notes`
- [ ] `checkpoint_combined` really is 2016 + 2017 cleaned the same way **plus a `year` column** — it has to match the row-count check you do out loud
- [ ] **AI-output tab built**: run "clean this and make it tidy" on `ai_input`, paste a version that dropped or mangled a row into its own tab, write down input vs output row counts
- [ ] **Run the slide-14 CSV round-trip once yourself** — Google Sheets may not behave exactly like the Excel lesson text; adjust your patter to what you actually see
- [ ] Etherpad populated (paste `files/tidy-data-etherpad.txt`), practice-sheet link pinned at the top
- [ ] Your Sheet's **Locale** set on purpose (`File ▸ Settings ▸ Locale`) — know what it is
- [ ] Have `checkpoint_clean` open in a second browser tab as your safety net

---

## Segments

| Clock | Slides | Screen | Your move |
|---|---|---|---|
| 0:00 | 1–2 | **Sheet** | Greet by name. Live: open practice link ▸ `File ▸ Make a copy` ▸ rename `tidy-data-yourname`. Point at the tabs along the bottom. Wait for the chat to fill with "copied" before moving on. |
| 0:04 | 3–4 | slides | Poll into chat: what do you use spreadsheets for / what has bitten you. Read 4–5 aloud. Then the six habits — **preview only, do not lecture**. |
| **0:09** | **5** | **Sheet** | **First edit, everyone does it.** Demo slowly, then wait: right-click `2016_messy` ▸ Duplicate ▸ rename `2016_clean` ▸ delete the merged title row + blank spacer rows. Watch the chat for ✓/✗. From here, all edits happen in `2016_clean`. **→ back to slide 6** |
| 0:14 | 6 | slides | The one rule. Name what they just did: worked in a copy, made it more of a rectangular table. |
| 0:18 | 7 | slides → **Sheet** | Show `2016_messy`: 60 seconds of quiet, "one thing a program can't read" into the chat. Read a handful, group them (two side-by-side tables / packed column / colour-only cancelled / text durations / 1900 date). **→ back to slide 8** |
| 0:24 | 8 | slides | One value per cell. Show the split visually; you'll do it live in the next segment. |
| **0:28** | **9** | **Sheet — 25 min** | **THE CORE EXERCISE.** Demo RDM (~8 min): unmerge title, `Data ▸ Split text to columns` on `\|`, rename `pgr/pdra/other`, add a `cancelled` column from the grey rows, make nulls consistent. Narrate every click. Flag the 1900 date, **do not fix it**. Learners then do the Open access table + the `2017` tab (~12 min) against `checkpoint_clean`. Reconvene: show `checkpoint_combined`, do the row-count check (2016 + 2017 = combined − 1 header), ask whose count differed and why. **→ back to slide 10** |
| 0:53 | — | — | **Break, 8 min** |
| 1:01 | 10–11 | slides | Formatting is not data. Zeros & nulls. |
| 1:05 | 12 | slides → **Sheet** | Three states of a date: ask "what could differ underneath / be ambiguous", take 2 chat answers, reveal. In the Sheet: `Format ▸ Number` on a real date shows the serial number; a text date left-aligns with none. |
| 1:15 | 13 | slides | Locale. Say your Sheet's locale out loud. |
| **1:20** | **14** | **Sheet — 12 min** | Part 1: demo `=MONTH` `=DAY` `=YEAR` on 2–3 rows of `dates`, format as number; learners fill down, post the wrong-year rows in chat (they read 2017, the events were 2015). Part 2: `File ▸ Download ▸ CSV` the `dates` tab, open in a text editor (dates lose the year), re-import to Sheets (dates come back with the current year). **→ back to slide 15** |
| 1:32 | 15 | slides → **Sheet** | QA/QC. Demo `Data ▸ Data validation` on `num_registered`: whole number, min 1 max 100, **Reject the input**. Try a bad value, show it blocked. |
| 1:40 | 16 | slides (learners in Sheet, ~6 min) | Sort `len_hours` largest→smallest with **"Data has header row"** ticked — text values ("90 min", "1 hour") sort to the top. Colour scale on `num_attended` — two `0` cells pop, those classes were cancelled. Tie back to zeros vs nulls. **→ back to slide 17** |
| 1:55 | — | — | **Break, 8 min** |
| 2:03 | 17–18 | slides | Why CSV anyway. Write down what you changed — show your own changelog. |
| 2:15 | 19 | slides | Downstream / AI. **Data caution first: today's data is fictional; no real patron/student/health/licensed data into an AI service.** |
| 2:25 | 20 | **Sheet — ~4 min** | Show the pre-built AI-output tab next to `ai_input`. Learners find the missing `source_row_id`. Ask: "how would you catch this without the id column?" (row counts; compare to the raw). **→ back to slide 21** |
| 2:38 | 21–22 | slides | Vocab — point at 3–4, don't read the slide. Recap = the lesson's keypoints. Feedback link in the Etherpad. |
| 2:50 | — | — | Buffer: questions, or an early finish. |

---

## If a demo goes sideways

Say: **"Grab `checkpoint_clean` and follow along from there,"** and move on. The checkpoint tabs exist for exactly this. Don't try to debug live — you have a 10-minute buffer, not 30.

## You are teaching this while under the weather

- The lead helper runs the chat. You watch the Sheet and talk. That's it.
- It's fine to say "let me take 10 seconds" for water. Silence while people work is normal, not dead air.
- Don't ad-lib new material. The deck is the scope. If you're fading, cut the AI segment (slide 20) — it's the one part beyond the core lesson.
- Formative checks beat "any questions?": "type the row count", "put the wrong-year rows in chat", "one thing a program can't read". Every one of those tells you where the room is without you having to read faces.
