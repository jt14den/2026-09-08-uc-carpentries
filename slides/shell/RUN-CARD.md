# The Unix Shell - instructor run card

One page. Keep this where you can see it while you drive the terminal. Full per-slide script: **`script.html`** (`/slides/shell/script.html`) - open it on a second screen; the deck's built-in presenter view (press `S`) is unreliable from a CDN.

**Lesson:** Software Carpentry, [The Unix Shell](https://swcarpentry.github.io/shell-novice/). **Today: Episodes 1-6.** Episode 7 (Finding Things / `grep` / `find`) dropped - the standard cut.

**Zoom:** share **one window** (the terminal), not the whole screen. Font size way up. Say what you're about to type *before* you type it.

---

## The split — two instructors

| Part | Slides | Episodes | Clock (PT) | Instructor |
|---|---|---|---|---|
| **Part 1** | 1-16 | 1-3: intro, navigating, creating/moving/deleting files | 9:00 - 10:38 | Instructor 1 *(suggested: Tim)* |
| **Part 2** | 17-28 | 4-6: pipes & filters, loops, shell scripts | 10:38 - 12:00 | Instructor 2 *(suggested: Frew)* |

- **Pace is brisk.** Official time for Ep 1-6 is ~225 min vs ~160 min of teaching time. Each part carries one break.
- **Handoff is at slide 17** (start of Ep 4 / pipes), right after the wildcards exercise. Instructor 2 re-anchors the room (`pwd` check) and takes over.
- **If Part 2 is behind at the second break:** cut the loop-trace exercise (slide 24), skip the `$1`/`$2` aside on slide 26 and demo `"$@"` only. Trim exercises before demos.
- Whoever is not driving: watch chat + pad, read questions aloud, keep time, DM stuck learners with the helpers.

---

## Pre-flight - both instructors, before you teach

- [ ] Your own terminal open in `~/Desktop/shell-lesson-data`, large font
- [ ] Terminal set up for teaching (Tim's usual): shell is **bash** (`bash` if your default is zsh), **prompt shortened** to `$` (`PS1='$ '`), **color output off** so `ls` looks like learners' plain output
- [ ] `shell-lesson-data` folder on your Desktop with `exercise-data/` (alkanes, animal-counts, creatures, writing, numbers.txt) and `north-pacific-gyre/`
- [ ] **Run your half of the script once** on the machine you'll teach from - especially the Part 2 loop and script demos (slides 22-26)
- [ ] Agree the handoff: who takes Part 1 / Part 2
- [ ] `man` works on your machine? If not (some Git Bash), plan to use `ls --help` on slide 6
- [ ] Editor for slide 11 + 25: `nano` (Mac/Linux/Git Bash) or `notepad` (Windows). Practice the save-and-exit once - you use it three times today
- [ ] A scratch copy of `shell-lesson-data` you can delete and re-unzip between runs (you create/rename/delete files, and write `sorted.sh`)
- [ ] Etherpad populated (paste `files/shell-etherpad.txt`), setup + data-download link pinned at the top

---

## Part 1 segments — Instructor 1 (Episodes 1-3)

| Clock | Slides | On screen | Move |
|---|---|---|---|
| 9:00 | 1-2 | **terminal** | Greet by name. Live: `whoami` ▸ `ls` ▸ `cd ~/Desktop/shell-lesson-data` ▸ `ls`. Never type the `$`; blank line = success. REPL: read-evaluate-print. |
| 9:08 | 3 | slides | Why the shell (Ep 1). Your own example. Nelle: 1520 files, ~12h clicking. Chat poll. **~5 min.** |
| 9:14 | 4-6 | **terminal** | `pwd`, `ls`, `ls exercise-data`. Options `-F` `-l` `-lh` `-a` / `-Fa`. Help: `man ls` (**press q!**) / `ls --help`; `ls -j` error. Capitalisation matters. |
| 9:32 | 7-8 | **terminal** | `cd` in / `cd ..` up / `cd` home / `cd -` back. Deliberate error: `cd shell-lesson-data` from inside `exercise-data`. `pwd` after every move. Absolute vs relative, `~`. |
| **9:44** | **9** | terminal | **Nav exercise (~7 min):** `ls nor` + Tab; the `cd` reading question; alkanes round-trip (relative in, absolute back). Chat answers. |
| 9:51 | — | — | Reconvene. **Break, 8 min.** |
| 10:00 | 10 | slides | Command shape recap (command / option / argument). `pwd` re-anchor. |
| 10:03 | 11 | **terminal** | `cd exercise-data/writing`. `nano draft.txt` - type 2 lines, **Ctrl-O, Enter, Ctrl-X** (slowly, point at the `^O ^X` bar). `ls`. |
| 10:09 | 12-14 | **terminal** | `mkdir thesis`, `mkdir -p ../project/data ../project/results`. `mv` rename + `mv ... .` back. `cp` + the `-r not specified` error, then `cp -r`. |
| 10:26 | 15 | **terminal** | `rm quotes.txt`; `rm thesis` (error); `rm -r`. **No-undo danger, twice.** Tidy up. |
| **10:31** | **16** | **terminal** | Wildcards in `alkanes`: `ls *.pdb`, `p*.pdb`, `???ane.pdb`, `*.pdf` (error). **Exercise (~5 min):** which pattern = ethane + methane only? (`*t??ne.pdb`) |
| 10:38 | — | — | Reconvene in `alkanes`. **Hand to Instructor 2.** |

---

## Part 2 segments — Instructor 2 (Episodes 4-6)

| Clock | Slides | On screen | Move |
|---|---|---|---|
| 10:38 | 17 | **terminal** | Take over. Re-anchor: "run `pwd`, you're in `alkanes`." `wc cubane.pdb`, `wc -l *.pdb`, `> lengths.txt`, `cat`. Warn: `>` overwrites silently. |
| 10:46 | 18 | **terminal** | `sort` vs `sort -n` on `../numbers.txt`. `sort -n lengths.txt > sorted`, `head -n 1`. `>` vs `>>` (run `echo ... >>` twice, `cat`). |
| 10:53 | 19 | **terminal** | Build the pipe: `sort -n lengths.txt \| head -n 1` ▸ `wc -l *.pdb \| sort -n` ▸ `wc -l *.pdb \| sort -n \| head -n 1`. Read right-to-left. |
| **11:00** | **20** | terminal | **Pipeline exercise (~8 min):** 3 shortest files; `cut -d , -f 2 animals.csv \| sort \| uniq` (+ `\| wc -l`). Nelle story (~1 min). |
| 11:08 | — | — | Reconvene. **Break, 8 min.** |
| 11:16 | 21-22 | slides → **terminal** | Loops. The `for / do / done` form (read aloud). `cd ../creatures`. Demo the `basilisk minotaur unicorn` loop with `echo $filename` + `head -n 2 $filename \| tail -n 1` - narrate one iteration, watch the `>` prompt. |
| 11:30 | 23 | **terminal** | Dry run: `for f in *.dat; do echo cp $f original-$f; done` - read the previewed commands, then drop the `echo` and run for real. `ls`. |
| **11:37** | **24** | terminal | **Loop-trace exercise (~6 min):** `ls *.pdb` vs `ls $f` inside a `for f in *.pdb` loop - why different? *(cut this if behind)* |
| 11:43 | 25-26 | **terminal** | Scripts. `cd ../alkanes`. `nano sorted.sh` = `wc -l *.pdb \| sort -n` + a `#` comment; `bash sorted.sh`. Then change `*.pdb` to `"$@"`; `bash sorted.sh *.pdb` and `bash sorted.sh ../creatures/*.dat`. |
| 11:55 | 27-28 | slides | Vocab - point at 3-4, don't read. Recap = keypoints. Feedback link in the Etherpad. |
| ~12:00 | — | — | If you finish early, that's fine - don't add Episode 7. |

---

## If a demo goes sideways

"Delete your `shell-lesson-data` folder, unzip a fresh copy, and pick up from here." In Part 2, learners renaming/deleting files will have diverged - that's expected. Don't debug one terminal live; a helper takes it in a DM.

## The things that actually trip people

1. **`man` with no exit** - people get stuck in the pager. Say "press q" loudly on slide 6, and again if anyone goes quiet.
2. **`nano` save/exit** - Ctrl-O *then Enter* to confirm the name, *then* Ctrl-X. You do this on slides 11, 25, and 26. Have the vim escape ready (`Esc` `:q!` `Enter`).
3. **The loop prompt `>`** - when learners hit Enter mid-loop and see `>`, they think it's broken. Tell them: the shell is waiting for `done`. If they're lost, Ctrl-C and start the loop over.
4. **A long shell prompt** eating the shared screen - `PS1='$ '` before you share.
5. **`cd` to a sibling** - `cd` only sees directories inside the current one. The error on slide 7 is deliberate.
6. **`>` overwriting silently** - flag it every time.

## Keeping the room with you

- Never more than ~15 min without learners typing. The pace is tight, so make exercises count - don't pad demos.
- Make a mistake on purpose (typo, `cd` to a sibling, `cp` a directory without `-r`), read the error aloud, recover.
- Formative checks beat "any questions?": "what does `ls -lh` add", "which `cd` options reach home", "paste the pipeline that finds the 3 shortest files", "why did the two loops differ". (If you want to run Socrative the way Tim does in-person, set the room code beforehand and pin it in the pad - the deck's exercise questions map straight to Socrative items.)
- <kbd>Ctrl</kbd>+<kbd>C</kbd> is the safety net - mention it early for anything that hangs (`man`, a half-typed loop, `wc` with no filename).
