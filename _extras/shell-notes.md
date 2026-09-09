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
- Collaborative notes (Etherpad): <https://pad.carpentries.org/2026-fall-uc-shell-novice>
- Practice data: **[shell-lesson-data.zip](https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip)** — download to your Desktop and unzip it there; you should end up with a folder called `shell-lesson-data`
- Setup (a Unix-like shell): <https://swcarpentry.github.io/shell-novice/#setup>
- Slides: [{{ '/slides/shell/' | relative_url }}]({{ '/slides/shell/' | relative_url }}) — 8 slides (title, get-to-the-prompt, why the shell, and the four diagrams: filesystem tree, command shape, the pipe, the loop). Everything else is live at the prompt.
- **[Live-coding spine](#live-coding-spine)** below — the command-by-command sequence, in order, by segment, with what to say and where to cut. This is what you teach from.
- Older per-slide script ([script.html]({{ '/slides/shell/script.html' | relative_url }}) / [SCRIPT.md]({{ '/slides/shell/SCRIPT.md' | relative_url }})) is kept for reference but was written against the previous 29-slide deck; the spine supersedes it.
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

## Live-coding spine

The whole session, command by command, in order. **You teach from this, not the slides.**
The deck has 8 slides: the title, the get-to-the-prompt slide, the "why", and four
diagrams (filesystem tree, command shape, the pipe, the loop). Show a diagram when you
reach it; the rest of the time you are in the terminal and learners are typing along.

Times are clock time (PT). Learners have `shell-lesson-data` on their **Desktop**, so paths
below use `~/Desktop/shell-lesson-data`. Adapt if someone unzipped to Downloads. Commands
follow Software Carpentry [The Unix Shell](https://swcarpentry.github.io/shell-novice/),
Episodes 1–6.

Legend: **DEMO** you drive · **EXERCISE** learners work · **DISCUSS** chat/pad.

---

### 1. Get everyone to the prompt · 9:00–9:10 · slide 2 · DEMO

The riskiest ten minutes. Do not rush it.

**Say:** the `$` is the **prompt** — the shell saying "ready". Yours may have a username
and machine name in front; ignore that, focus on the `$`. We never type the `$`. Press
Enter to run. Blank line back = it worked. `command not found` = typo or not installed.
`No such file or directory` = wrong path or you're not where you think.

**Type** (slowly, name each one):

```bash
whoami
pwd
cd ~/Desktop/shell-lesson-data
ls
```

Everyone should see `exercise-data/` and `north-pacific-gyre/`.

**Check:** learners post a green check in chat when they see those two folders, a red x
if not. **Do not move on until the chat is mostly green.** Helpers DM the setup + data
links to anyone stuck, or take them to a breakout.

---

### 2. Why the shell · 9:10–9:16 · slide 3 · DISCUSS

**Say:** a GUI is fine for one file, bad for hundreds. The commands you type *are* a
record you can re-run — a methods section a GUI never writes. Containers, HPC schedulers,
CI, and AI coding agents all run on shell commands. Give **your own** recent example.

**Then:** Nelle — 1520 files, one analysis program, ~12 hours of clicking by hand.
Today's six episodes automate that. Chat prompt: "one repetitive file task that ate an
afternoon." Read 3–4 answers aloud. Keep to ~5 min.

---

### 3. Navigating: `pwd` / `ls` / options / help · 9:16–9:35 · Episode 2 · DEMO

**Start:** `~/Desktop/shell-lesson-data`. Show **slide 4 (the tree)** here — root `/`,
`~` home, where you are, `.` and `..`.

**Say:** you are always *somewhere*; `pwd` answers "where". `ls` lists "here". `ls
somewhere` lists there without moving you. Options change what a command does; capital
vs lowercase matters (`-s` ≠ `-S`); miss the space (`ls-F`) and the shell looks for a
command called `ls-F`. Nobody memorises options — you look them up.

**Type:**

```bash
pwd
ls
ls -F
ls -F exercise-data
cd exercise-data
pwd
ls -F
ls -F -a
ls -s exercise-data      # (back in shell-lesson-data) sizes
ls -S exercise-data      # sort by size — capital S is different
ls --help                # Linux / Git Bash
man ls                   # macOS / Linux — SAY "press q to quit" LOUDLY
ls -j                    # deliberate: "invalid option" — a clear error, not a crash
```

**Trip hazard:** `man` with no exit. Say "press `q`" loudly, and again if anyone goes
quiet.

---

### 4. Navigating: `cd` and paths · 9:35–9:44 · Episode 2 · DEMO

**Say:** no output after `cd` = success; the shell only speaks when something is wrong.
`cd` only sees directories *inside* where you are — it can't jump to a sibling. `cd ..`
goes up, `cd` alone goes home (your escape hatch), `cd -` goes back. Relative paths are
short but depend on where you are; absolute paths start at `/` and mean the same
anywhere; `~` is home.

**Type:**

```bash
cd ~/Desktop/shell-lesson-data/exercise-data
cd creatures
pwd
cd ..
cd shell-lesson-data       # deliberate error: cd only sees children — read it aloud
cd ../..
pwd
cd                          # home
cd ~/Desktop/shell-lesson-data
cd exercise-data/creatures
cd ~/Desktop/shell-lesson-data
cd -                        # back to creatures
cd -                        # back again
```

Run `pwd` after moves. End with everyone in `shell-lesson-data`.

---

### 5. Navigation exercise · 9:44–9:51 · Episode 2 · EXERCISE → BREAK

```bash
ls nor                      # then press Tab — shell finishes north-pacific-gyre/
ls north-pacific-gyre/goo   # Tab Tab — see goodiff.sh / goostats.sh
```

- From `/Users/you/data`, which reach home? `cd .` / `cd ~` / `cd ../..` / `cd` / `cd ..`
  — **answer:** `cd ~`, `cd`, and `cd ..` reach `/Users/you`; `cd .` stays; `cd ../..`
  goes to `/Users`.
- Reach `exercise-data/alkanes` with one **relative** path, then leave and come back
  with one **absolute** path. **answer:** `cd exercise-data/alkanes` /
  `cd ~/Desktop/shell-lesson-data/exercise-data/alkanes`.

Post answers in chat; green check on the alkanes round-trip. Reconvene in
`shell-lesson-data`, then **BREAK 8 min** (back ~10:00).

---

### 6. The shape of a command · 10:00–10:03 · slide 5 · recap

Coming back from the break. Show **slide 5**. Name the parts once: `ls` command, `-F`
option, `/` argument — separated by spaces. This is the only "lecture" beat in the
navigating block. Re-anchor: "run `pwd`, you should be in `shell-lesson-data`."

---

### 7. Creating files: `nano` and `mkdir` · 10:03–10:15 · Episode 3 · DEMO

**Start:** `cd exercise-data/writing` (has `haiku.txt`, `LittleWomen.txt`).

**Say:** `mkdir` makes a directory here (relative path). `-p` builds intermediate
directories. `nano` is a plain-text editor inside the shell; the bottom bar shows the
keys, `^` means Ctrl. Save = `Ctrl-O` **then Enter** to confirm the name, **then**
`Ctrl-X` to exit. Do this slowly.

**Type:**

```bash
cd ~/Desktop/shell-lesson-data/exercise-data/writing
ls -F
mkdir thesis
ls -F
mkdir -p ../project/data ../project/results
ls -F ../project
cd thesis
nano draft.txt            # type two lines; Ctrl-O, Enter, Ctrl-X
ls
```

**Trip hazard:** the `nano` save/exit sequence. Have the vim escape ready for anyone in
the wrong editor: `Esc` then `:q!` then Enter. On Windows, `notepad draft.txt` works the
same way.

**Names:** try `mkdir north pacific gyre` then `ls` — you get *three* directories.
Spaces separate arguments. Good names: no spaces, don't start with `-`, stick to letters
/ numbers / `. - _`.

---

### 8. `mv` / `cp` / `rm` · 10:15–10:32 · Episode 3 · DEMO

**Start:** `cd ~/Desktop/shell-lesson-data/exercise-data/writing`.

**Say:** `mv` is one command for rename *and* move — first argument is what to move,
second is where it goes or what to call it. `.` as a target means "here". `cp` is the
same but leaves the original; `-r` for a directory. `rm` **has no Trash, no undo** — say
this twice. `rm` won't touch a directory; `rm -r` deletes a directory and everything in
it, no prompt.

**Type:**

```bash
mv thesis/draft.txt thesis/quotes.txt
ls thesis
mv thesis/quotes.txt .
ls thesis
ls quotes.txt
cp quotes.txt thesis/quotations.txt
ls quotes.txt thesis/quotations.txt
cp thesis thesis_backup        # deliberate error: omitting directory
cp -r thesis thesis_backup
ls thesis thesis_backup
rm quotes.txt
ls quotes.txt                  # error: no such file
rm thesis                      # error: is a directory
rm -r thesis thesis_backup ../project
```

**Trip hazard:** `mv` and `cp` silently overwrite an existing target — mention `-i`.

---

### 9. Wildcards (+ exercise) · 10:32–10:38 · Episode 3 · DEMO + EXERCISE → HANDOFF

**Start:** `cd ../alkanes` — six `.pdb` files.

**Say:** the **shell** expands the pattern to a list of names *before* the command runs;
`ls` never sees the `*`. `*` = zero or more characters, `?` = exactly one. A pattern
matching nothing is passed through unchanged, so `ls *.pdf` here errors.

**Type:**

```bash
cd ~/Desktop/shell-lesson-data/exercise-data/alkanes
ls *.pdb
ls p*.pdb
ls *ane.pdb
ls ???ane.pdb
ls *.pdf          # error — nothing to expand to
```

**Exercise (~4 min):** which pattern lists **only** `ethane.pdb` and `methane.pdb`?
`*t*ane.pdb` / `*t?ne.*` / `*t??ne.pdb` / `ethane.*` — **answer:** `*t??ne.pdb` (two
characters between `t` and `ne`).

**HANDOFF to Instructor 2** (~10:38), everyone in `alkanes`.

---

### 10. `wc` and redirect · 10:38–10:48 · Episode 4 · DEMO — Instructor 2 starts

**Re-anchor:** "run `pwd`, you should be in `exercise-data/alkanes`."

**Say:** `wc` = word count: lines, words, characters. `wc -l` just lines. `>` sends
output to a **file** instead of the screen — **overwrites with no prompt**. `cat` prints
a file. `wc -l` with no filename just sits waiting for typed input — `Ctrl-C` to escape.

**Type:**

```bash
wc cubane.pdb
wc *.pdb
wc -l *.pdb
wc -l *.pdb > lengths.txt
ls lengths.txt
cat lengths.txt
```

---

### 11. `sort` / `head` / `tail` / `>>` · 10:48–10:55 · Episode 4 · DEMO

**Say:** plain `sort` is alphabetical (text): "10" comes before "2". `sort -n` reads
numbers. None of these change the input file — they read it and write output. `>`
replaces, `>>` appends.

**Type:**

```bash
sort -n ../numbers.txt
sort ../numbers.txt           # text sort — "10" before "2"
sort -n lengths.txt
sort -n lengths.txt > sorted-lengths.txt
head -n 1 sorted-lengths.txt  # the shortest file
echo appended >> sorted-lengths.txt
cat sorted-lengths.txt
```

---

### 12. The pipe `|` · 10:55–11:02 · slide 6 · Episode 4 · DEMO

Show **slide 6 (the pipe diagram)**. Build the pipeline one stage at a time.

**Say:** `|` sends the output of the left command straight into the right one. No temp
files. Read it left to right: `wc` then `sort` then `head`.

**Type:**

```bash
sort -n lengths.txt | head -n 1
wc -l *.pdb | sort -n
wc -l *.pdb | sort -n | head -n 1
```

---

### 13. Pipeline exercise + Nelle · 11:02–11:10 · Episode 4 · EXERCISE → BREAK

**Start (for the `cut` part):** `cd ../animal-counts`.

```bash
cut -d , -f 2 animals.csv
cut -d , -f 2 animals.csv | sort | uniq
cut -d , -f 2 animals.csv | sort | uniq | wc -l
```

- 3 shortest files: `wc -l * | sort -n | head -n 3`. `head` before `sort` grabs the
  wrong 3.
- `cut -d , -f 2` = animal column; `sort` groups identical names; `uniq` collapses
  *adjacent* runs (so `sort` must come first). `| wc -l` = count of distinct animals
  (**5**: deer, rabbit, raccoon, fox, bear).

**Nelle (tell fast, ~1 min):** she ran `wc -l *.txt | sort -n | head -n 5` on 17 output
files — one was 240 lines, not 300 (machine left off over a weekend). `tail -n 5` and
`ls *Z.txt` caught a `Z` in a filename (her lab's "missing info" code).

Reconvene, then **BREAK 8 min** (back ~11:18).

---

### 14. Loops: the idea, then a real one · 11:18–11:32 · slide 7 · Episode 5 · DEMO

Show **slide 7 (the loop form)**. Read it aloud slowly: "for each thing in this list: do
the following, using that thing."

**Say:** `for` runs the block once per item. The **loop variable** holds the current
item; `$filename` reads its value (same `$` idea as the prompt, different job). The
prompt changes to `>` while the shell waits for `done` — not broken, just waiting.
Indentation is for humans.

**Type** (line by line — point at the prompt flipping to `>`):

```bash
cd ~/Desktop/shell-lesson-data/exercise-data/creatures
head -n 5 basilisk.dat minotaur.dat unicorn.dat
for filename in basilisk.dat minotaur.dat unicorn.dat
do
    echo $filename
    head -n 2 $filename | tail -n 1
done
```

**Narrate one full iteration:** "Pass one: filename is basilisk.dat. echo prints it.
`head -n 2` gives the first two lines, `tail -n 1` keeps the second — the
classification." Then walk minotaur, unicorn fast.

---

### 15. Dry run + backup loop · 11:32–11:40 · Episode 5 · DEMO

**Say:** `cp *.dat original-*.dat` does **not** work — the shell expands both sides and
`cp` gets confused. A loop is the fix. Put `echo` in front to **preview** the commands
without running them; check them; then drop the `echo` and run for real. A dry run is a
habit worth keeping for anything destructive.

**Type:**

```bash
cp *.dat original-*.dat        # deliberate: show it fail
for filename in *.dat
do
    echo cp $filename original-$filename
done
for filename in *.dat
do
    cp $filename original-$filename
done
ls
```

**Trip hazard:** learners press Enter mid-loop, see `>`, think it's broken. It's the
shell waiting for `done`. If they're lost: `Ctrl-C` and restart the loop.

---

### 16. Loop-trace exercise · 11:40–11:45 · Episode 5 · EXERCISE — **cut if behind**

**Start:** `cd ../alkanes`.

```bash
for datafile in *.pdb
do
    ls *.pdb
done

for datafile in *.pdb
do
    ls $datafile
done
```

**Answer:** the first prints the full `.pdb` list six times (it re-globs `*.pdb` every
pass, ignoring the variable); the second prints one filename per pass (it uses
`$datafile`). The loop variable is what carries the current item into the body. Also
mention: `↑` recalls the whole loop on one line, `history` + `!123` re-runs a past
command.

---

### 17. Shell scripts · 11:45–11:57 · Episode 6 · DEMO

**Start:** `cd ~/Desktop/shell-lesson-data/exercise-data/alkanes`.

**Say:** a script is commands saved in a plain-text file, run with `bash`. A line
starting with `#` is a comment — for the human, ignored by the shell. Inside a script,
`"$1"` / `"$2"` are the first, second argument the caller typed; `"$@"` is *all* of them
— which lets the caller pick the files, the way built-in commands work. Saving the
pipeline saves the method: it runs again, on new data, the same way.

**Type:**

```bash
nano middle.sh
#   file contents:
#   head -n 15 octane.pdb | tail -n 5
bash middle.sh

nano middle.sh
#   change to:  head -n 15 "$1" | tail -n 5
bash middle.sh octane.pdb
bash middle.sh pentane.pdb

nano middle.sh
#   change to:  head -n "$2" "$1" | tail -n "$3"
bash middle.sh pentane.pdb 20 5
```

**Then, if time — save the pipeline from Episode 4:**

```bash
nano sorted.sh
#   file contents:
#   # Sort filenames by their length.
#   # Usage: bash sorted.sh one_or_more_filenames
#   wc -l "$@" | sort -n
bash sorted.sh *.pdb
bash sorted.sh *.pdb ../creatures/*.dat
```

**Cut if behind:** skip the `"$2"`/`"$3"` step, do `middle.sh` with `"$1"` only, or go
straight to `sorted.sh` with `"$@"`.

---

### 18. Recap · 11:57–12:00 · slide 8

Show **slide 8**. Point at the two columns (keypoints from Episodes 2–6), don't read
them. The vocabulary table is on this page. Feedback link is in the Etherpad. Episode 7
(Finding Things — `grep`, `find`) is at the bottom of this page for anyone who wants it,
and could be a later session. **Finishing early is fine — don't add Episode 7.**

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
behind: the loop-trace exercise, and the `$1`/`$2` aside in the scripts block
(do `"$@"` only).

### The two-instructor split

| Part | Episodes | Clock | Diagrams | Instructor |
|---|---|---|---|---|
| **1** | 1–3 (intro, navigating, creating/moving/deleting files) | ~9:00–10:38 | slides 4–5 | suggested: Tim |
| **2** | 4–6 (pipes & filters, loops, shell scripts) | ~10:38–12:00 | slides 6–7 | suggested: Frew |

- Each part carries one break (after the navigation exercise in Part 1, after the pipeline
  exercise in Part 2).
- The handoff is at the **start of Episode 4 / pipes**, right after the wildcards
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

### Pre-flight (both instructors, before you teach)

- [ ] Your own terminal open in `~/Desktop/shell-lesson-data`, large font
- [ ] Terminal set for teaching: shell is **bash** (run `bash` if your default is zsh),
  prompt shortened with `PS1='$ '`, colour output off so `ls` looks like a learner's
- [ ] `shell-lesson-data` on your Desktop with `exercise-data/` (alkanes, animal-counts,
  creatures, writing, `numbers.txt`) and `north-pacific-gyre/`
- [ ] Run **your half** of the script once on the machine you'll teach from — especially
  the Part 2 loop and script demos
- [ ] Agree the handoff: who takes Part 1, who takes Part 2
- [ ] Does `man` work on your machine? If not (some Git Bash), use `ls --help` in the navigating segment
- [ ] `nano` (or `notepad` on Windows) for the file-creation and scripts segments — do the save-and-exit once
- [ ] A scratch copy of `shell-lesson-data` you can delete and re-unzip between runs
- [ ] Etherpad populated (paste `files/shell-etherpad.txt`); setup and data-download links
  pinned at the top

### Prep — the things that trip people

1. **`man` with no exit** — people get stuck in the pager. Say "press `q`" loudly when
   you open `man ls`, and again if anyone goes quiet.
2. **`nano` save/exit** — `Ctrl-O` *then Enter* to confirm the name, *then* `Ctrl-X`.
   Practice it. Have the vim escape ready (`Esc` `:q!` `Enter`) for anyone in the wrong
   editor. On Windows, `notepad` is fine.
3. **A long shell prompt** eating the shared screen — set `PS1='$ '` before you share.
4. **`cd` to a sibling** — `cd` only sees directories inside the current one. The
   deliberate `cd shell-lesson-data` error from inside `exercise-data` is worth showing;
   don't skip it.
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
