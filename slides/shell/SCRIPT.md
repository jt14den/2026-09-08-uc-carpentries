# The Unix Shell - full instructor script

> **Superseded.** This script was written against the earlier 29-slide deck. The deck is
> now 8 slides (title, get-to-the-prompt, why, and four diagrams), and the command-by-command
> teaching flow lives in the **[Live-coding spine](../../shell-notes/#live-coding-spine)**
> on the session notes page. Teach from the spine. This file is kept for reference only —
> its SAY / TYPE notes per command are still accurate, but the slide numbers are not.

**Rendered version (bullets, badges, nav): [script.html](script.html)** - `/slides/shell/script.html`. This `.md` is the plain-text source.

**Pre-flight checklist** (both instructors, before you teach): see the instructor guide on the [session notes page](../../shell-notes/#instructor-guide).

Times are clock time (PT); session runs 9:00 am - 12:00 pm. Open the deck alongside this on a second screen.

**Lesson:** Software Carpentry, [The Unix Shell](https://swcarpentry.github.io/shell-novice/). **Today: Episodes 1-6** (Introducing the Shell, Navigating, Working With Files, Pipes and Filters, Loops, Shell Scripts). Episode 7 (Finding Things / `grep` / `find`) is dropped - the standard cut for a single session.

Legend: **DEMO** = you drive the terminal  ·  **EXERCISE** = learners work  ·  **DISCUSS** = chat / pad prompt. Each slide reads **SAY** then **TYPE** then **THEN**.

## The split

Two instructors (Tim + James Frew), two parts, handoff after the wildcards block.

| Part | Slides | Episodes | Clock | Instructor |
|---|---|---|---|---|
| **1** | 1-17 | 1-3 (intro, navigating, creating/moving/deleting files) | ~9:00-10:38 | Instructor 1 (suggested: Tim) |
| **2** | 18-29 | 4-6 (pipes & filters, loops, shell scripts) | ~10:38-12:00 | Instructor 2 (suggested: Frew) |

**Pace is brisk.** Official time for Ep 1-6 is ~225 min against ~160 min of teaching time. The compressible end is loops + scripts (Ep 5-6): if Part 2 is behind at the second break, cut the loop exercise (slide 25) and the `$1`/`$2` aside (slide 27), and demo `"$@"` only. Trim exercises before demos.

Breaks: after slide 10 (~9:51, 8 min) and after slide 21 (~11:08, 8 min).

---

# PART 1 — Instructor 1 — Episodes 1-3

## 1. The Unix Shell

**Open `script.html` on a second screen. Reveal's own presenter view (S) is unreliable from a CDN.**

**Holding slide - learners arriving (9:00)**

- Greet people by name
- Ask them to: (1) add their name to the Etherpad; (2) open their shell - Terminal on Mac, Git Bash on Windows; (3) confirm there is a `shell-lesson-data` folder on their Desktop

**Zoom model, all session:** instructor screen-shares one window (terminal, ~150%, large font, short prompt, colour off); learners work in their own terminal; done/stuck = a Zoom reaction or a chat line; questions go in the pad.

---

## 2. Open your shell
<sub>Before we start  ·  **DEMO**</sub>

**9:00-9:08 · open your shell · DEMO**

**SAY**

- The `$` is the prompt. Yours might have your username and machine name in front - fine, ignore it, focus on the `$`.
- We never type the `$`. Press Enter to run a command.
- The loop: you type a command, the shell reads it, evaluates (runs) it, prints the result, waits. Read-evaluate-print loop.
- Blank line back = it worked. `command not found` = typo or not installed.

**TYPE**

```
whoami
ls
cd ~/Desktop/shell-lesson-data
ls
```

**THEN** - wait for "I see exercise-data" in chat; helpers DM the stuck. -> slide 3

> *slide footnote:* the shell runs a **read-evaluate-print loop (REPL)**; the `$` is the **prompt** - "ready for input"

---

## 3. Why the command line?
<sub>Why the shell</sub>

**9:08-9:11 · why the command line · SWC Episode 1**

**SAY**

- Short slide, framing not depth. The shell went from a power-user tool to the layer almost everything else runs on - containers are Linux underneath, HPC schedulers want Bash, and CI is mostly shell scripts.
- The newer reason: AI coding agents act by running shell commands. To check what Claude Code did in your repo, or what a cluster job actually ran, you're reading the same commands we cover today.
- Optional: your own example of driving an agent or a cluster job from the terminal.

**THEN** - keep it to ~3 min. -> slide 4

> *slide footnote:* the shell is the layer HPC schedulers and AI agents both sit on top of

---

## 4. Why type when you can click?
<sub>Concept 1  ·  **DISCUSS**</sub>

**9:11-9:14 · why type when you can click · DISCUSS · SWC Episode 1**

**SAY**

- Give your own recent example - a real thing you did last week or month with the shell.
- Nelle Nemo, marine biologist, is the story that runs through this lesson. 1520 files, one program, by end of month. We meet her again in every episode - navigate, create, check length, chain commands, loop, script.

**DO** - read 3-4 chat answers aloud. Common: batch renaming, find-and-replace across many docs, "which of these 200 files mentions X".

**THEN** - keep it tight, ~3 min. -> slide 5

> *slide footnote:* Unix's design rule: **small pieces, loosely joined** - many tiny tools that each do one job well and combine

---

## 5. Where am I? What's here?
<sub>Navigating  ·  **DEMO**</sub>

**9:14-9:20 · pwd / ls · DEMO · SWC Episode 2**

**SAY**

- You are always *somewhere*. `pwd` answers "where". Use it any time you're unsure.
- Draw the tree if it helps: `/` at the top, `/Users` inside it, `/Users/you` inside that.
- `ls` with a name after it lists *that* place without moving you.

**TYPE**

```
pwd
ls
ls exercise-data
ls exercise-data/alkanes
```

**THEN** -> slide 6

> *slide footnote:* the filesystem is a **tree**: the **root** `/` at the top; your **home directory** is where a new shell starts

---

## 6. Options change what a command does
<sub>Navigating  ·  **DEMO**</sub>

**9:20-9:27 · ls options · DEMO · SWC Episode 2**

**SAY**

- Options modify the command. Capital vs lowercase matters: `ls -s` (show sizes) is not `ls -S` (sort by size).
- Miss the space - `ls-F` - and the shell looks for a command called `ls-F` and fails.
- `-a` reveals `.` (here) and `..` (one level up).

**TYPE**

```
ls -F
ls -l
ls -lh
ls -F -a
ls -Fa
```

**Quick check (~1 min):** chat - "what does `ls -lh` add over `ls -l`?" (human-readable sizes)

**THEN** -> slide 7

> *slide footnote:* an `-F` is an **option** (also **flag** / **switch**); a name to act on is an **argument**

---

## 7. How do I find the options?
<sub>Navigating  ·  **DEMO**</sub>

**9:27-9:32 · getting help · DEMO · SWC Episode 2**

**SAY**

- Nobody memorises these. You look them up.
- Get into `man ls`, scroll a little, then **press q** - say "q gets you out" clearly.
- Git Bash / Windows: `man` often missing, use `ls --help`. For built-ins like `cd`: `help cd`.

**TYPE**

```
ls --help          # or: man ls   (q to quit)
ls -j              # error for an unknown option
```

**THEN** -> slide 8

> *slide footnote:* a **manual page** (man page) is the reference doc shipped with the tool

---

## 8. Moving around: `cd`
<sub>Navigating  ·  **DEMO**</sub>

**9:32-9:38 · cd · DEMO · SWC Episode 2**

**SAY**

- No output after `cd` = success. The shell only speaks when something's wrong.
- Try `cd shell-lesson-data` from inside `exercise-data` - it errors, because `cd` only sees children. Read the error aloud.
- `cd ..` goes up. `cd` with nothing goes home - your escape hatch.
- Run `pwd` after each move.

**TYPE**

```
cd exercise-data
pwd
cd creatures
cd ..
cd ../..
pwd
cd
cd Desktop/shell-lesson-data
```

**THEN** - everyone back in `shell-lesson-data`. -> slide 9

> *slide footnote:* `.` = the current directory, `..` = its parent

---

## 9. Two ways to name a place
<sub>Navigating  ·  **DEMO**</sub>

**9:38-9:44 · paths · DEMO · SWC Episode 2**

**SAY**

- Relative paths are shorter but depend on where you are. Absolute paths are longer but unambiguous.
- `pwd` gives you an absolute path you can copy.
- `~` saves typing your home path. `cd -` is the "undo" for `cd`.

**TYPE**

```
cd exercise-data/creatures
pwd
cd ~/Desktop/shell-lesson-data
cd -
cd -
```

**THEN** -> slide 10

> *slide footnote:* a path is an address; **absolute** from `/`, **relative** from where you stand

---

## 10. Tab completion, and a walk around
<sub>Navigating  ·  **EXERCISE**</sub>

**9:44-9:51 · navigation exercise · EXERCISE · SWC Episode 2**

**Task (~7 min):**

- Type `ls nor` then press Tab - the shell finishes `north-pacific-gyre/`
- Type `ls north-pacific-gyre/g` + Tab Tab - see the choices
- From `/Users/you/data`, which reach home? `cd .` / `cd ~` / `cd ../..` / `cd` / `cd ..`
- Reach `exercise-data/alkanes` with one **relative** path, then leave and come back with one **absolute** path

**Answers:** `cd ~`, `cd`, and `cd ..` reach `/Users/you`. `cd .` stays put, `cd ../..` goes to `/Users`. Relative: `cd exercise-data/alkanes`. Absolute back: `cd ~/Desktop/shell-lesson-data/exercise-data/alkanes`.

**THEN** - reconvene, everyone in `shell-lesson-data`, then **BREAK, 8 min** (back ~10:00). -> slide 11

> *slide footnote:* if Tab does nothing, the name isn't there or you're not where you think

---

## 11. The shape of a command
<sub>Navigating · recap</sub>

**10:00-10:03 · command syntax · SWC Episode 2 close**

**SAY**

- Quick recap coming back from the break. Name the parts (command / option / argument) once.
- Re-anchor: "run `pwd`, you should be in `shell-lesson-data`."
- Then straight into creating files.

**THEN** -> slide 12

> *slide footnote:* options and arguments together are **parameters**; options that take no value are **flags** or **switches**

---

## 12. Create a file with `nano`
<sub>Concept 2 · files  ·  **DEMO**</sub>

**10:03-10:09 · nano · DEMO · SWC Episode 3**

**SAY**

- Go to `exercise-data/writing` first.
- Type a sentence or two. Then **slowly**: "Ctrl and O, the letter O, then Enter to confirm the name. Then Ctrl and X to leave."
- Point at the bottom bar - `^O WriteOut`, `^X Exit`. `^` is Ctrl.
- Trapped in vim: Esc then `:q!` then Enter. Or close the tab and reopen.
- Windows: `notepad draft.txt` works the same way here.

**TYPE**

```
cd ~/Desktop/shell-lesson-data/exercise-data/writing
nano draft.txt
# type two lines, Ctrl-O, Enter, Ctrl-X
ls
```

**THEN** -> slide 13

> *slide footnote:* a **plain-text** file is just characters - that's what shell tools expect

---

## 13. Make directories: `mkdir`
<sub>Files  ·  **DEMO**</sub>

**10:09-10:15 · mkdir · DEMO · SWC Episode 3**

**SAY**

- Relative path = made here. Leading slash would put it somewhere absolute.
- `-p` builds intermediate directories - without it, `mkdir a/b/c` fails if `a/b` doesn't exist.
- Names: try `mkdir north pacific gyre` then `ls` - you get *three* directories.

**TYPE**

```
mkdir thesis
ls -F
mkdir -p ../project/data ../project/results
ls -F ../project
```

**THEN** -> slide 14

> *slide footnote:* consistent, predictable names are what make wildcards and loops work later

---

## 14. Rename and move: `mv`
<sub>Files  ·  **DEMO**</sub>

**10:15-10:21 · mv · DEMO · SWC Episode 3**

**SAY**

- First argument = what to move, second = where it goes (or what to call it).
- Move into `thesis/` with a new name, then move back with `mv thesis/quotes.txt .` - the `.` means current directory.
- Check with `ls thesis` (empty) and `ls quotes.txt` (here).
- Overwrite risk is real - `-i` for a prompt.

**TYPE**

```
mv draft.txt thesis/quotes.txt
ls thesis
mv thesis/quotes.txt .
ls thesis
ls quotes.txt
```

**THEN** -> slide 15

> *slide footnote:* `.` as a target means "here"; `mv` is one command for both renaming and relocating

---

## 15. Copy: `cp`
<sub>Files  ·  **DEMO**</sub>

**10:21-10:26 · cp · DEMO · SWC Episode 3**

**SAY**

- `cp` is `mv` that leaves the original in place.
- Without `-r`, copying a directory fails: `cp: -r not specified; omitting directory`. Show that error, then add `-r`.
- `ls` with two arguments lists both.

**TYPE**

```
cp quotes.txt thesis/quotations.txt
ls quotes.txt thesis/quotations.txt
cp thesis thesis_backup          # show the error
cp -r thesis thesis_backup
ls thesis thesis_backup
```

**THEN** -> slide 16

> *slide footnote:* a copy is a working duplicate, not a snapshot in time - versioning is Git, day two

---

## 16. Delete: `rm` (carefully)
<sub>Files  ·  **DEMO**</sub>

**10:26-10:31 · rm · DEMO · SWC Episode 3**

**SAY** - say the danger twice.

- There is no recycle bin. `rm` means gone.
- `rm -r` on the wrong directory is the classic way people lose a project. `ls` first, then delete.
- Some people alias `rm` to `rm -i` permanently.

**TYPE**

```
rm quotes.txt
ls quotes.txt
rm thesis                # error: is a directory
rm -r thesis thesis_backup ../project
```

**THEN** - tidy up the practice files. -> slide 17

> *slide footnote:* the shell **unlinks** the file - the disk space is reusable immediately

---

## 17. Wildcards: act on many files at once
<sub>Files  ·  **DEMO** **EXERCISE**</sub>

**10:31-10:38 · wildcards · DEMO + EXERCISE · SWC Episode 3**

**SAY**

- Move to `alkanes` - six `.pdb` files.
- The command never sees the `*`. The shell turns `*.pdb` into the file list, then runs `ls` on that list.
- `ls *.pdf` (no PDFs) errors - nothing to expand to.

**TYPE**

```
cd ~/Desktop/shell-lesson-data/exercise-data/alkanes
ls *.pdb
ls p*.pdb
ls ???ane.pdb
ls *.pdf          # error
```

**Exercise (~5 min):** In `alkanes`, which pattern lists **only** `ethane.pdb` and `methane.pdb`? `ls *t*ane.pdb` / `ls *t?ne.*` / `ls *t??ne.pdb` / `ls ethane.*`

**Answer:** `ls *t??ne.pdb` - two characters between `t` and `ne`.

**END OF PART 1.** Reconvene, everyone in `alkanes`. Hand to Instructor 2 (~10:38). -> slide 18

> *slide footnote:* wildcard expansion is **globbing**; a pattern that matches nothing is passed through unchanged

---

# PART 2 — Instructor 2 — Episodes 4-6

## 18. Count with `wc`, save with `>`
<sub>Concept 3 · pipes & filters  ·  **DEMO**</sub>

**10:38-10:46 · wc + redirect · START OF PART 2 · DEMO · SWC Episode 4**

**Instructor 2: take over here.** Re-anchor: "run `pwd`, you should be in `exercise-data/alkanes`."

**SAY**

- `wc` = word count: three numbers, lines / words / characters.
- `wc -l *.pdb` - the shell expands `*.pdb`, `wc` counts each, adds a total line.
- `>` redirects: the screen shows nothing because it went into `lengths.txt`. `cat` to see it.
- Warn: `>` overwrites with no prompt.
- `wc -l` with no filename just sits waiting for typed input - Ctrl-C to escape.

**TYPE**

```
wc cubane.pdb
wc *.pdb
wc -l *.pdb
wc -l *.pdb > lengths.txt
cat lengths.txt
```

**THEN** -> slide 19

> *slide footnote:* redirecting to a file a command is also reading corrupts it - never `sort x > x`

---

## 19. `sort`, `head`, `tail`, `>>`
<sub>Pipes & filters  ·  **DEMO**</sub>

**10:46-10:53 · sort/head/tail · DEMO · SWC Episode 4**

**SAY**

- Detour: `sort ../numbers.txt` vs `sort -n ../numbers.txt` - text sort puts "10" before "2".
- `sort -n` prints to the screen; the file is unchanged. Redirect to keep it.
- `head -n 1 sorted.txt` = the shortest file, because we sorted ascending.
- `>` replaces, `>>` adds. Run an `echo ... >>` twice, `cat` to show it accumulating.

**TYPE**

```
sort -n ../numbers.txt
sort ../numbers.txt
sort -n lengths.txt > sorted-lengths.txt
head -n 1 sorted-lengths.txt
echo appended >> sorted-lengths.txt
cat sorted-lengths.txt
```

**THEN** -> slide 20

> *slide footnote:* `sort -n` reads it as numbers, plain `sort` reads it as text

---

## 20. The pipe: `|`
<sub>Pipes & filters  ·  **DEMO**</sub>

**10:53-11:00 · the pipe · DEMO · SWC Episode 4**

**SAY - build it up one stage at a time**

- We just used two temp files to answer "which file is shortest". The pipe removes them.
- `sort -n lengths.txt | head -n 1` - "sort's output goes straight into head".
- `wc -l *.pdb | sort -n` - no temp files. Add `| head -n 1` - the answer in one line.
- Read it right to left: "head of sort of wc".

**TYPE**

```
sort -n lengths.txt | head -n 1
wc -l *.pdb | sort -n
wc -l *.pdb | sort -n | head -n 1
```

**THEN** -> slide 21

> *slide footnote:* tools that read **standard input** and write **standard output** snap together - **pipes and filters**

---

## 21. Build a pipeline
<sub>Pipes & filters  ·  **EXERCISE**</sub>

**11:00-11:08 · pipeline exercise · EXERCISE · SWC Episode 4**

**Task (~8 min):**

- Which finds the **3** files with the fewest lines? `wc -l * | sort -n | head -n 3` / `wc -l * | head -n 3 | sort -n`
- In `animal-counts`: `cut -d , -f 2 animals.csv | sort | uniq` - what does each stage do? Then add `| wc -l`.

**Answers:**

- Fewest 3: `wc -l * | sort -n | head -n 3`. `head` before `sort` grabs the wrong 3.
- `cut -d , -f 2` = animal column; `sort` groups identical names; `uniq` collapses runs. One line per distinct animal.
- `| wc -l` = count of distinct animals (5: deer, rabbit, raccoon, fox, bear).

**Nelle (tell fast, ~1 min):** she ran `wc -l *.txt | sort -n | head -n 5` on 17 output files, one was 240 lines not 300 - machine left on over the weekend. `tail -n 5` caught a `Z` in a filename (her lab's "missing info" code).

**THEN** - reconvene, then **BREAK, 8 min** (back ~11:16). -> slide 22

> *slide footnote:* `cut -d , -f 2` pulls column 2; `uniq` collapses *adjacent* duplicates, so `sort` comes first

---

## 22. Loops: do it to the whole list
<sub>Concept 4 · automation</sub>

**11:16-11:22 · the loop idea · SWC Episode 5**

**SAY**

- Read the form aloud slowly: "for each thing in this list: do the following, using that thing."
- The `$` in front of the variable means "give me its value" - same `$` idea as the prompt, different job.
- Indentation is for humans; the shell doesn't need it.

The general form:

```
for thing in list_of_things
do
    operation_using $thing
done
```

**THEN** -> slide 23, a real one

> *slide footnote:* this is a **for loop**; a variable walking a list is the same shape in every programming language

---

## 23. A real loop
<sub>Automation  ·  **DEMO**</sub>

**11:22-11:30 · a real loop · DEMO · SWC Episode 5**

**SAY - narrate one full iteration**

- Type it line by line. Point at the prompt flipping to `>`.
- "Pass one: filename is basilisk.dat. Echo prints it. head -n 2 gives the first two lines, tail -n 1 keeps the second - the classification." Then walk minotaur, unicorn fast.
- Could also use `*.dat` instead of listing the three names - show that if time.

**TYPE**

```
cd ~/Desktop/shell-lesson-data/exercise-data/creatures
for filename in basilisk.dat minotaur.dat unicorn.dat
do
    echo $filename
    head -n 2 $filename | tail -n 1
done
```

**THEN** -> slide 24

> *slide footnote:* each pass is an **iteration**; the classification is line 2 of every file, so `head -n 2 | tail -n 1` pulls it out

---

## 24. Check before you run
<sub>Automation  ·  **DEMO**</sub>

**11:30-11:37 · dry run + backup loop · DEMO · SWC Episode 5**

**SAY**

- `cp *.dat original-*.dat` does NOT work - the shell expands both sides and `cp` gets confused. A loop is the fix.
- Prefix with `echo`: the loop prints the three `cp` commands it *would* run. Read them, check they're right.
- Drop the `echo`, run it, `ls` - the three `original-` files are there.
- `f` vs `filename`: the shell doesn't care, but a human reader does - name it for what it holds.

**TYPE**

```
for f in *.dat
do
    echo cp $f original-$f
done
for f in *.dat
do
    cp $f original-$f
done
ls
```

**THEN** -> slide 25

> *slide footnote:* a **dry run** - print what would happen before doing it - is a habit worth keeping for anything destructive

---

## 25. Trace the loop
<sub>Automation  ·  **EXERCISE**</sub>

**11:37-11:43 · loop exercise · EXERCISE · SWC Episode 5**

*(If Part 2 is behind: skip this, go straight to slide 26.)*

**Task (~6 min):** In `alkanes`, what does each print, and why are they different?

```
for f in *.pdb
do ls *.pdb
done

for f in *.pdb
do ls $f
done
```

**Answer:** the first prints the full `.pdb` list six times (it re-runs `ls *.pdb` every pass, ignoring `$f`). The second prints one filename per pass (it uses `$f`). The point: the loop variable is what carries the current item into the body.

**Also mention:** up-arrow to recall the loop, `history` to see recent commands, `!123` to re-run line 123.

**THEN** -> slide 26

> *slide footnote:* `$f` is the loop variable; `*.pdb` is expanded by the shell every time it's seen

---

## 26. Save commands as a script
<sub>Concept 5 · scripts  ·  **DEMO**</sub>

**11:43-11:49 · scripts: save a pipeline · DEMO · SWC Episode 6**

**SAY**

- We keep retyping `wc -l *.pdb | sort -n`. Put it in a file once.
- `nano sorted.sh`, type the comment line and the pipeline, save (`^O` Enter `^X`).
- `bash sorted.sh` - same output as typing the pipeline.
- The `#` comment says what it does - your future self will thank you.

**TYPE**

```
cd ~/Desktop/shell-lesson-data/exercise-data/alkanes
nano sorted.sh
# file contents:
#   # Sort files by their length.
#   wc -l *.pdb | sort -n
bash sorted.sh
```

**THEN** -> slide 27

> *slide footnote:* a script is a small program; saving your pipeline makes the work **reproducible**

---

## 27. Make the script take input
<sub>Scripts  ·  **DEMO**</sub>

**11:49-11:55 · scripts with arguments · DEMO · SWC Episode 6**

**SAY**

- Re-open `sorted.sh`, change `*.pdb` to `"$@"`, add a usage comment.
- Now `bash sorted.sh *.pdb` - the shell expands `*.pdb` and hands the list to the script; `"$@"` passes it to `wc`.
- Run it on `../creatures/*.dat` too - same script, different files. That's the payoff.
- If short on time: skip the `$1`/`$2` aside, just do `"$@"`.

**TYPE**

```
nano sorted.sh
# change the last line to:  wc -l "$@" | sort -n
bash sorted.sh *.pdb
bash sorted.sh ../creatures/*.dat
```

**THEN** -> slide 28

> *slide footnote:* `"$@"` / `"$1"` are **positional parameters**; letting the caller choose the files is how every built-in command already works

---

## 28. What the field calls this
<sub>You now have the words</sub>

**11:55-11:57 · vocab**

- Don't read the slide. Point at 3-4: options vs arguments, paths, pipes, the for loop.
- It's on the notes page.
- -> slide 29

---

## 29. Recap

**11:57-12:00 · recap**

- The two columns are the keypoints from Episodes 2-6, condensed.
- Then the feedback link (in the Etherpad).
- Episode 7 (Finding Things - `grep`, `find`) is on the notes page for anyone who wants it, and could be a later session.

---
