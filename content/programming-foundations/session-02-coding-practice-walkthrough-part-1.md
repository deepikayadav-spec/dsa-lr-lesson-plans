# Coding Practice Walkthrough — Part 1

**Duration** 44 min total — 39 min instruction + 5 min Classroom Quiz · **Topic** Introduction to Python — attacking a coding problem: Read, Restate, Write, Run · **Prerequisite** Programming with Python
**Session type** Walkthrough, no slide deck · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the four steps of attacking any coding problem — read, restate, write, run. *(REMEMBERING)*
2. Restate a problem statement in their own words before writing any code. *(UNDERSTANDING)*
3. Write and submit a solution on the platform without assistance. *(APPLYING)*
4. Read a Python error message and identify which line to fix. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Programming with Python (0–6 min) · ALS: Polling

4 questions on **Programming with Python** — the ones that matter for today's walkthrough.

**Q1.** What does `print(2 + 5)` output?
`A` `2 + 5` · `B` `7` · `C` `"7"` · `D` Error
→ **B.**

**Q2.** What does `print("2 + 5")` output?
`A` `7` · `B` `2 + 5` · `C` `"2 + 5"` · `D` Error
→ **B.**

**Q3.** `Print("Hello")` produces which error?
`A` SyntaxError · `B` NameError · `C` No error · `D` IndentationError
→ **B.**

**Q4.** You get an error you don't understand. First move?
`A` Delete the line and retry · `B` Read the error message and find the line number · `C` Ask a friend · `D` Restart the laptop
→ **B.**

---

## Hook (6–10 min)

Ask for a show of hands, honestly:

> *"Who attempted the coding problems last night?"*

Whatever the number, don't react to it. Then:

> *"Here's what I know happens. You open the problem, you read it, and your brain says 'I don't know how to start.' That feeling is not a sign you can't code. It's a sign nobody has shown you the first move. That's the entire hour."*

Write the four steps on the board and leave them there all session: **Read → Restate → Write → Run.**

---

## Concept Walkthrough (10–25 min)

**Core idea:** attack every coding problem the same way — read the whole statement out loud, restate it in your own words, write the simplest thing that could work, then run it and read the output or the error. Getting it wrong the first time is the normal path, not a failure.

**Worked example — *Hello World*:** read the statement → restate ("show these two words on screen, nothing else") → write `print("Hello World")` → run, see the output, submit on the platform. Then break it on purpose: `print("Hello World)` — missing quote — submit, let the error appear, read it aloud calmly, fix it.

**Checkpoint:**
> *"What's step 2, and why does it exist?"*
> **Answer:** Restate it in your own words — if you can't say what the program should do, you can't write it.

---

## ⚡ Active Learning Strategy 1 — Guided Construction: Fill the Blank Live (25–32 min)

**ALS format:** Cold-Call Construction — the instructor is a literal typist, students supply every token out loud one at a time. Chosen over a pair activity because the entire point is the gap between recognising code and producing it, which only shows up when one voice has to commit to an exact answer with nobody to lean on.

**Setup line:**
> *"I'm typing exactly what you say. Not what you mean — what you say. Character for character."*

Put this on screen:

```python
_____("Three Hashes")
```

Take the answer. Type **literally** what the student says. If they say "print", type `print`. If someone says "Print", type `Print` and run it — let the `NameError` land.

Then escalate, one blank at a time:

```python
print(_____)          →  "###"
_____(_____)          →  print("###")
```

**Debrief line:**
> *"Notice what happened when I typed exactly what was said. The computer is doing the same thing to you. It has no idea what you meant."*

**Cut rule:** Do the first blank only. The literal-typing moment is the lesson; the escalation is a bonus.

---

## ⚡ Active Learning Strategy 2 — Round-Robin Trace: Human Compiler (32–39 min)

**ALS format:** Round-Robin Structured Cold-Call — a different student takes each line, in order, no pairing or discussion. Chosen instead of a repeat of Activity 1's format because the skill here is different: reading code top-to-bottom as a sequence, not constructing it token by token.

**Setup line:**
> *"You are Python now. I point at a line, you tell me exactly what the machine does. Not what the program means — what that one line does."*

Put this on screen and point at each line in turn, taking a different student each time:

```python
print("Hello")
print(2 + 5)
print("2 + 5")
Print("Bye")
print(10 / 5)
```

| Line | Expected answer |
|---|---|
| 1 | Shows `Hello` |
| 2 | Works out 7, shows `7` |
| 3 | Shows the characters `2 + 5` |
| 4 | **Stops with a NameError** — `Print` doesn't exist |
| 5 | Shows `2.0` |

**The trap is line 4.** Most rooms will read past it. When someone catches it, press: *"So what happens to line 5?"*
**Answer:** it never runs. Python stops at the error.

**Debrief line:**
> *"Python reads top to bottom and stops at the first thing it can't do. That's why the error message gives you a line number — it's telling you exactly where it gave up."*

**Cut rule:** Use lines 1, 3 and 4 only. Line 4 is non-negotiable.

---

## Classroom Quiz (39–44 min)

**Classroom Quiz** *Reserved — not yet available.* No question bank exists for this walkthrough/support session (mirrors the source: no slide deck, no quiz pool). Use this slot for an instructor-led recap instead — re-run the `#`-is-a-comment mix-up or the `Print(...)` NameError trap one more time, cold-calling a different student to narrate it.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| "I should know how to start without thinking" | Nobody has shown them a method, so they assume competent people just *know* | Naming the four steps and running them visibly, twice |
| Errors mean you failed | School conditioning | Deliberately breaking code in the walkthrough and fixing it calmly |
| Python reads the whole program at once | Reading habits from prose | ALS 2 — a `Print(...)` typo on one line stops the next line from ever running |
| `#` is just a symbol | No reason to know otherwise yet | Running `print(###)` live and asking why nothing printed |
| Recognising correct code = being able to write it | Recognition feels like knowledge | ALS 1 — typing literally what's said exposes the gap |
