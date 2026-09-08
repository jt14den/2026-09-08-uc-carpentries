---
layout: page
title: "The Unix Shell (Sep 9) — Session Notes"
permalink: /shell-notes/index.html
---

Notes for the **Unix Shell** session, Wednesday September 9, 2026, 9:00 am to 12:00 pm
Pacific, online. Based on Software Carpentry's
[The Unix Shell](https://swcarpentry.github.io/shell-novice/) lesson.

**This session covers Episodes 1–6** (Introducing the Shell, Navigating, Working With
Files, Pipes and Filters, Loops, Shell Scripts). Episode 7 (Finding Things — `grep`,
`find`) is not covered today; it's summarised at the bottom of this page for anyone who
wants it.

The first part of this page is a reference you can use during and after the session. The
[run sheet](#run-sheet) and [instructor guide](#instructor-guide) further down are open
for anyone who wants to see how the session is put together or teach it themselves.

- Full self-paced lesson: <https://swcarpentry.github.io/shell-novice/>
- Collaborative notes (Etherpad): <https://pad.carpentries.org/2026-fall-uc-carpentries-shell>
- Practice data: **[shell-lesson-data.zip](https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip)** — download to your Desktop and unzip it there; you should end up with a folder called `shell-lesson-data`
- Setup (a Unix-like shell): <https://swcarpentry.github.io/shell-novice/#setup>
- Slides: <{{ '/slides/shell/' | relative_url }}> (instructor script: `script.html`)
- Instructor run card, one page: [RUN-CARD.md]({{ '/slides/shell/RUN-CARD.md' | relative_url }})
- Full slide-by-slide script, rendered: [script.html]({{ '/slides/shell/script.html' | relative_url }}) (plain-markdown source: [SCRIPT.md]({{ '/slides/shell/SCRIPT.md' | relative_url }}))
- Etherpad starter to paste into the live pad: [shell-etherpad.txt]({{ '/files/shell-etherpad.txt' | relative_url }})

---

## Before the session

1. Get a Unix-like shell working: **Terminal** (already on macOS), **Git Bash**
   (Windows — <https://gitforwindows.org>), or your normal shell on Linux.
2. Download **[shell-lesson-data.zip](https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip)**
   to your **Desktop** and unzip it there. You should have a folder called
   `shell-lesson-data`.
3. Open your shell and check:

   ```bash
   cd ~/Desktop/shell-lesson-data
   ls
   ```

   You should see `exercise-data` and `north-pacific-gyre`.

---

## How the shell works

You type a command, the shell **reads** it, **evaluates** (runs) it, **prints** the
result, and loops back to wait for the next one — a read-evaluate-print loop. The `$`
is the **prompt**: the shell saying it is ready. Don't type the `$`; type what comes
after it, then press Enter.

---

## The practice data

Inside `shell-lesson-data`:

| Path | What it is |
|---|---|
| `exercise-data/alkanes/` | Six `.pdb` files (molecule structures) — used for wildcards, `wc`, pipes |
| `exercise-data/animal-counts/animals.csv` | Comma-separated wildlife counts — used for `cut` / `sort` / `uniq` |
| `exercise-data/creatures/` | Three `.dat` files |
| `exercise-data/writing/` | `haiku.txt`, `LittleWomen.txt` — where we make files with `nano` |
| `exercise-data/numbers.txt` | `10 2 19 22 6` — shows why `sort -n` differs from `sort` |
| `north-pacific-gyre/` | Nelle's 17 sample files (`NENE*.txt`) plus her scripts — the story data |

The lesson follows **Nelle Nemo**, a marine biologist with 1520 sample files to process.
Each episode is one step toward automating that.

---

## The commands, by job

### Where am I / what's here (Episode 2)

| Command | Does |
|---|---|
| `whoami` | print the username the computer thinks you are |
| `pwd` | print working directory — where you are now |
| `ls` | list the contents of where you are |
| `ls [path]` | list somewhere else without moving there |
| `ls -F` | mark types: `/` directory, `*` executable, plain = file |
| `ls -l` | long listing: permissions, size, date, name |
| `ls -lh` | `-h` makes sizes human-readable (`5.3K`) |
| `ls -a` | show all, including hidden `.` names (and `.` / `..`) |
| `man [cmd]` / `[cmd] --help` | how to use a command; in `man`, `q` quits |
| `cd [path]` | change directory |
| `cd ..` | up one level (`..` = parent, `.` = current) |
| `cd` | back to your home directory |
| `cd -` | back to the previous directory you were in |

### Paths

| Form | Meaning |
|---|---|
| `/Users/you/Desktop` | **absolute** — from the root `/`, means the same anywhere |
| `exercise-data/alkanes` | **relative** — from where you are now |
| `~` | your home directory |
| `.` | here |
| `..` | one level up |

### Creating, moving, deleting (Episode 3)

| Command | Does |
|---|---|
| `nano [file]` | open a plain-text editor; `Ctrl-O` then Enter saves, `Ctrl-X` exits |
| `mkdir [name]` | make a directory |
| `mkdir -p a/b/c` | make nested directories in one step |
| `touch [file]` | make an empty file (or update its timestamp) |
| `mv [old] [new]` | rename, or (if `[new]` is a directory) move into it |
| `mv -i` | ask before overwriting |
| `cp [old] [new]` | copy a file |
| `cp -r [dir] [newdir]` | copy a directory and its contents |
| `rm [file]` | **delete — no Trash, no undo.** `rm -i` prompts first |
| `rm -r [dir]` | delete a directory and everything in it (no prompt) |

### Wildcards (globbing)

The shell expands these to a list of matching names **before** the command runs.

| Pattern | Matches |
|---|---|
| `*` | zero or more characters — `*.pdb`, `p*.pdb` |
| `?` | exactly one character — `?ethane.pdb` = `methane.pdb` |
| `???ane.pdb` | three characters then `ane.pdb` — `cubane`, `ethane`, `octane` |

A pattern that matches nothing is passed through unchanged, so `ls *.pdf` in a folder
with no PDFs is an error.

### Counting and combining (Episode 4)

| Command | Does |
|---|---|
| `wc [file]` | count lines, words, characters |
| `wc -l` / `-w` / `-m` | just lines / words / characters |
| `cat [file]` | print a file's contents (`less` for big ones; `q` quits) |
| `sort` | alphabetical order |
| `sort -n` | numerical order (`10` after `9`, not before) |
| `head -n N [file]` | first N lines |
| `tail -n N [file]` | last N lines |
| `cut -d , -f 2 [file]` | pull out column 2, using `,` as the delimiter |
| `uniq` | collapse **adjacent** duplicate lines (`sort` first); `uniq -c` counts them |

### Redirection and pipes

| Symbol | Does |
|---|---|
| `>` | send output to a file — **overwrites without asking** |
| `>>` | append output to a file |
| <code>&#124;</code> | send output straight into the next command |

Build a pipeline one stage at a time:

```bash
wc -l *.pdb                       # count lines in each file
wc -l *.pdb | sort -n             # ...then sort numerically
wc -l *.pdb | sort -n | head -n 1 # ...then take the shortest
```

### Loops (Episode 5)

Repeat a command over a list of things.

```bash
for filename in basilisk.dat minotaur.dat unicorn.dat
do
    echo $filename
    head -n 2 $filename | tail -n 1
done
```

- `for` runs the block once per item in the list
- the **loop variable** (`filename`) holds the current item; `$filename` reads its value
- the prompt shows `>` while the shell waits for `done`
- put `echo` in front of the commands to **preview** (dry run) what a loop would do before running it for real
- `for f in *.dat` uses a wildcard for the list; `${f}` is the same as `$f` with clearer boundaries
- up-arrow recalls the whole loop on one line (parts joined with `;`); `history` + `!123` re-runs a past command

### Shell scripts (Episode 6)

Commands saved in a plain-text file, run with `bash`.

```bash
# sorted.sh — Sort files by their length.
# Usage: bash sorted.sh file...
wc -l "$@" | sort -n
```

```bash
bash sorted.sh *.pdb
bash sorted.sh ../creatures/*.dat
```

- a line starting with `#` is a **comment** — ignored by the shell, there for the reader
- `"$1"`, `"$2"` = the first, second argument the caller typed
- `"$@"` = *all* the arguments — lets the caller choose the files, the way built-in commands work
- `history | tail -n 10 > steps.sh` captures what you just did as the start of a script

---

## The one idea

The shell is many small tools that each do one job — count, sort, cut, list — and
read plain text in and write plain text out. Because they all speak the same "lines
of text" interface, you can chain them with `|` into a pipeline that does something
none of them does alone. Save the pipeline and you've saved the method: it runs again,
on new data, the same way. That reproducibility is the reason the shell is the on-ramp
to Git, Python, and working on a server.

---

## Vocabulary

| You saw | The field calls it |
|---|---|
| the `$` the shell prints | the **prompt** |
| a `-l` after a command | an **option** / **flag** / **switch** |
| a name the command acts on | an **argument** (options + arguments = **parameters**) |
| the trail of names to a file | a **path** — **absolute** from `/`, **relative** from here |
| `.` and `..` | **current** and **parent** directory |
| `*` and `?` expanding to filenames | **globbing** |
| `>` / `>>` | **redirection** (overwrite / append) |
| `\|` chaining commands | a **pipe** |
| `wc`, `sort`, `cut` reading input, writing output | **filters** |
| where a command reads/writes by default | **standard input / output** (stdin/stdout) |
| `for … in … do … done` | a **for loop**; each pass is an **iteration** |
| `$name` / `${name}` | a **variable** (get its value) |
| `echo` in front of a loop before running it | a **dry run** |
| commands saved in a file, run with `bash` | a **shell script**; `#` starts a **comment** |
| `"$1"`, `"$@"` inside a script | **positional parameters** (the caller's arguments) |
| save the commands, re-run them | a **reproducible** workflow |

---

## Self-check questions

1. You open a shell and don't know where you are. What do you type?
2. What's the difference between `ls -s` and `ls -S`?
3. You're in `exercise-data` and type `cd shell-lesson-data`. Why does it fail? What works instead?
4. Write an absolute path and a relative path that both point to `exercise-data/alkanes`.
5. `ls *t??ne.pdb` in the `alkanes` folder — which files does it list, and who does the expansion, the shell or `ls`?
6. Why is `rm` more dangerous than dragging a file to the Trash?
7. `wc -l *.pdb > counts.txt` then `wc -l *.pdb >> counts.txt` — what's in the file now, and why?
8. Write a pipeline that prints the single `.pdb` file with the *most* lines. *(`wc -l *.pdb | sort -n | tail -n 2 | head -n 1`, to skip the total line — or `sort -n | tail -n 1` if you don't mind the total)*
9. `cut -d , -f 2 animals.csv | sort | uniq` — why does `sort` have to come before `uniq`?
10. In a `for f in *.pdb` loop, what's the difference between a body of `ls *.pdb` and a body of `ls $f`? *(the first re-globs and prints the whole list every pass; the second uses the loop variable and prints one file per pass)*
11. You want to preview what a loop of `cp` commands would do before running it. How? *(put `echo` in front of the command inside the loop)*
12. Your `sorted.sh` script has `wc -l *.pdb | sort -n` in it. Why does changing `*.pdb` to `"$@"` make it more useful? *(the caller chooses the files: `bash sorted.sh ../creatures/*.dat`)*
13. You built a pipeline that works. What do you do so you can run it again next month? *(save it as a script, or at least in your notes)*

---

## Resources

- Software Carpentry, The Unix Shell: <https://swcarpentry.github.io/shell-novice/>
- Library Carpentry, The Unix Shell (library-flavoured): <https://librarycarpentry.github.io/lc-shell/>
- The Unix shell reference (cheat sheet): <https://swcarpentry.github.io/shell-novice/reference.html>
- *The Linux Command Line* (free book): <https://linuxcommand.org/tlcl.php>

---

## Run sheet

180 minutes. **Two instructors**, split in two parts; handoff after the wildcards
exercise. Episodes 1–6. Official lesson time for those six episodes is ~225 min against
~160 min of teaching time, so **the pace is brisk** — trim exercises before demos, and
loops/scripts are the compressible end.

| Time | Min | Part | Segment | What happens |
|---|---|---|---|---|
| 0:00 | 8 | **1** | Open your shell | `whoami`, `ls`, `cd ~/Desktop/shell-lesson-data`, `ls`. First keystrokes. REPL. |
| 0:08 | 6 | 1 | Why the shell | Ep 1. Instructor's own example. Nelle: 1520 files, ~12h of clicking. Chat poll. ~5 min. |
| 0:14 | 18 | 1 | Navigating: `pwd` / `ls` / options / help | Ep 2. `pwd`, `ls` + `-F` `-l` `-lh` `-a`, `man` (press q!) / `--help`, unknown-option error. |
| 0:32 | 12 | 1 | Navigating: `cd` and paths | `cd` in / `..` up / home / `cd -`. The deliberate sibling error. Absolute vs relative, `~`. |
| 0:44 | 7 | 1 | **Exercise** | `ls nor` + Tab; the `cd` reading question; alkanes round-trip. |
| 0:51 | 8 | — | Break | |
| 0:59 | 3 | 1 | Command shape (recap) | Ep 2 close. Command / option / argument. `pwd` re-anchor. |
| 1:02 | 6 | 1 | `nano` | Ep 3. Make `draft.txt` in `writing/`. Ctrl-O, Enter, Ctrl-X — slowly. |
| 1:08 | 17 | 1 | `mkdir` / `mv` / `cp` | `mkdir` + `-p`; `mv` rename + move; `cp` + the `-r` error + `cp -r`. |
| 1:25 | 5 | 1 | `rm` | The no-undo danger, twice. `rm`, `rm` on a directory (error), `rm -r`. |
| 1:30 | 7 | 1 | Wildcards *(+ exercise)* | `alkanes`: `*.pdb`, `p*.pdb`, `???ane.pdb`, `*.pdf` error. Which pattern = ethane + methane only? |
| 1:38 | — | — | **Handoff to Instructor 2** | Reconvene in `alkanes`. |
| 1:38 | 8 | **2** | `wc` + redirect | Ep 4. `wc`, `wc -l *.pdb`, `> lengths.txt`, `cat`. Overwrite warning. |
| 1:46 | 7 | 2 | `sort` / `head` / `tail` / `>>` | `sort` vs `sort -n` on `numbers.txt`. `> sorted`, `head -n 1`. `>` vs `>>`. |
| 1:53 | 7 | 2 | The pipe `\|` | Build `wc -l *.pdb \| sort -n \| head -n 1` one stage at a time. Pipes and filters. |
| 2:00 | 8 | 2 | **Exercise** + Nelle | 3 shortest files; `cut \| sort \| uniq` (+ `\| wc -l`). Nelle-checks-her-files story. |
| 2:08 | 8 | — | Break | |
| 2:16 | 14 | 2 | Loops: idea + a real one | Ep 5. `for / do / done` form. `creatures` loop: `echo $filename` + `head -n 2 $filename \| tail -n 1`. Narrate one iteration. |
| 2:30 | 7 | 2 | Dry run + backup loop | `for f in *.dat; do echo cp $f original-$f; done`, then without `echo`. |
| 2:37 | 6 | 2 | **Loop-trace exercise** | `ls *.pdb` vs `ls $f` inside a loop. *(cut if behind)* |
| 2:43 | 12 | 2 | Shell scripts | Ep 6. `nano sorted.sh` = `wc -l *.pdb \| sort -n` + comment; `bash sorted.sh`. Then `*.pdb` → `"$@"`; run on `.pdb` and `../creatures/*.dat`. |
| 2:55 | 5 | 2 | Wrap | Vocabulary (point at 3-4). Recap = keypoints. Feedback link. |
| 3:00 | — | — | End | Finishing early is fine — don't add Episode 7. |

---

## Instructor guide

### Scope: Episodes 1–6, and why

The full lesson is seven episodes and ~4.5 hours of teaching plus exercises. A single
3-hour session can't do all of it, so **dropping the last episode is the standard cut** —
Episode 7 (Finding Things, `grep`/`find`) is self-contained and a follow-on session can
pick it up. Episodes 1–6 are the core arc: orient yourself, manipulate files, combine
commands, automate with loops, then save the automation as a script. That last step is
the payoff of the Nelle narrative.

The tradeoff: Ep 1–6 official time (~225 min) is well over the ~160 min of teaching time
in a 3-hour slot with two breaks. So the pace is brisk. Where to spend the time: the
navigating and pipes exercises (they're where novices actually get it). Where to cut if
behind: the loop-trace exercise (slide 24), and the `$1`/`$2` aside in the scripts block
(do `"$@"` only).

### The two-instructor split

| Part | Slides | Episodes | Clock | Instructor |
|---|---|---|---|---|
| **1** | 1–16 | 1–3 (intro, navigating, creating/moving/deleting files) | ~9:00–10:38 | suggested: Tim |
| **2** | 17–28 | 4–6 (pipes & filters, loops, shell scripts) | ~10:38–12:00 | suggested: Frew |

- Each part carries one break (after slide 9 in Part 1, after slide 20 in Part 2).
- The handoff is at **slide 17** (start of Episode 4 / pipes), right after the wildcards
  exercise. Instructor 2 re-anchors the room (`pwd` check in `alkanes`) and takes over.
- Roughly 85 minutes of teaching each. Part 1 is conceptually heavier (paths, the
  filesystem tree); Part 2 is more mechanical but has more to cover, so it moves faster.
- Whoever isn't driving: watch the chat and the pad, read questions aloud, keep time,
  and pair with the helpers to DM stuck learners.

### What's timeless

- **Knowing where you are** (`pwd`, `cd`, `ls`) is the whole foundation — a learner lost
  in the filesystem can't do anything else. Spend time here.
- The shell's advantage is **scale**: one file is a GUI job, 400 files is a shell job.
- **Wildcards and tab completion** are what make it fast — teach them as habits.
- **`>` writes to a file, `|` feeds the next command** — small filters chain into
  pipelines.
- **A loop repeats a command over a list** — and `echo` in front lets you check it
  before it runs.
- **Save the commands and you've saved the method** — a script is the reproducibility
  on-ramp; `"$@"` makes it reusable.

### Pedagogical approach (same as the Tidy Data session)

- Live coding, learners follow in their own terminal. No slides during the hands-on
  parts — the deck carries the framing and the exercise prompts.
- Never talk more than ~15 minutes without learners typing. The pace is tight today, so
  make the exercises count — don't pad demos.
- Make deliberate mistakes (a typo, `cd` to a sibling, `cp` a directory without `-r`),
  read the error aloud, recover on screen.
- Formative checks with a committed answer, not "any questions?": "what does `ls -lh`
  add", "which `cd` options reach home", "paste the pipeline that finds the 3 shortest
  files".
- Teach <kbd>Ctrl</kbd>+<kbd>C</kbd> and "press `q` to exit `man`" early — people get
  stuck in the pager and in editors.

### Concept budget

Five concepts.

- **C1** the shell is a CLI: type a command, get text; know where "here" is; options
  and arguments change what a command does
- **C2** create, move, copy, delete files and directories — and `rm` has no undo;
  wildcards act on many files at once
- **C3** `>` and `|` move output around; small filters (`wc`, `sort`, `cut`, `uniq`)
  chain into pipelines
- **C4** a `for` loop repeats a command over a list; `echo` in front is a safe dry run
- **C5** commands saved in a file are a script; `"$@"` lets the caller pick the files

### Prep — the things that trip people

1. **`man` with no exit** — people get stuck in the pager. Say "press `q`" loudly on
   slide 6, and again if anyone goes quiet.
2. **`nano` save/exit** — `Ctrl-O` *then Enter* to confirm the name, *then* `Ctrl-X`.
   Practice it. Have the vim escape ready (`Esc` `:q!` `Enter`) for anyone in the wrong
   editor. On Windows, `notepad` is fine.
3. **A long shell prompt** eating the shared screen — set `PS1='$ '` before you share.
4. **`cd` to a sibling** — `cd` only sees directories inside the current one. The error
   on slide 7 is deliberate; don't skip it.
5. **`>` overwriting silently** — flag it every time.
6. **The loop `>` prompt** — when learners press Enter mid-loop and see `>`, they think
   it's broken. It's the shell waiting for `done`. If they're lost, `Ctrl-C` and restart
   the loop.

Keep a scratch copy of `shell-lesson-data` you can delete and re-unzip between runs —
you create, rename, and delete files, and write `sorted.sh`, during the session.

### If a demo goes sideways

"Delete your `shell-lesson-data` folder, unzip a fresh copy, and pick up from here."
Learners who have been renaming and deleting files will have diverged — that's expected.
Don't debug one terminal live; a helper takes it in a DM.

---

## Not covered today: Finding Things (Episode 7)

The lesson's last episode is about searching. If you want to go further:

| Command | Does |
|---|---|
| `grep pattern file` | print lines in `file` that match `pattern` |
| `grep -w` / `-n` / `-i` / `-v` | whole word / line numbers / ignore case / invert (non-matching lines) |
| `grep -r pattern .` | search recursively through a directory |
| `grep -E "pattern"` | treat `pattern` as an extended regular expression |
| `find . -type f` | list every file below here; `-type d` for directories |
| `find . -name "*.txt"` | match filenames (quote the pattern so the shell doesn't expand it first) |
| `wc -l $(find . -name "*.txt")` | use one command's output as another's arguments |

Full episode: <https://swcarpentry.github.io/shell-novice/07-find.html>

---

*This page is shared under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The underlying lesson is
Software Carpentry's, also CC BY 4.0.*
