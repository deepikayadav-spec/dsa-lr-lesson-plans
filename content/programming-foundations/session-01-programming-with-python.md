# Programming with Python

**Duration** 47 min total — 40 min instruction + 7 min Classroom Quiz · **Topic** Introduction to Python — software, code, syntax, `print()` · **Prerequisite** None — day one
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. Define software as a set of instructions to the hardware, and explain what a programming language is for. *(REMEMBERING)*
2. Write and run a `print()` statement that displays a text message. *(APPLYING)*
3. Predict the output of `print()` with and without quotes, and perform arithmetic inside `print()`. *(APPLYING)*
4. Identify the four common `print()` errors — misspelling, capital `P`, missing quotes, missing parenthesis — and correct them. *(ANALYZING)*

---

## Warm-Up Poll — Diagnostic (0–6 min) · ALS: Polling

There's no previous session to recall, so this poll is diagnostic, not retrieval practice — no wrong answers. Purpose is to calibrate pace on day one.

Say: *"Five quick questions. Nobody is graded, nobody is named. I need to know who I'm teaching."*

**Q1.** Have you written a computer program before — any language?
`A` Never · `B` Tried once or twice · `C` A few small programs · `D` Yes, comfortably

**Q2.** Have you used Python specifically?
`A` No · `B` Heard of it, never used it · `C` Some · `D` Regularly

**Q3.** Do you have Python installed on the laptop you'll use for this course?
`A` No · `B` Not sure · `C` Yes · `D` Yes, plus VS Code

**Q4.** When you hear "software", what comes to mind first?
`A` Apps on my phone · `B` Windows / operating system · `C` Instructions a computer follows · `D` Not sure

**Q5.** In your own guess — what does `print("Hello")` do?
`A` Prints on paper · `B` Shows `Hello` on screen · `C` Shows `"Hello"` with quotes · `D` No idea

**Running it** — poll tool, ~40 s per question, project the distribution after each. Never name individuals.

---

## Hook (6–11 min)

Stand at the board with a marker. Ask for one volunteer to stay seated and give you instructions.

> *"I am now a computer. I will do **exactly** what you tell me — nothing more, nothing less. Your job: get me to write your name on that board."*

Follow every instruction with deliberate literalism. *"Pick up the marker"* — pick it up and stop. *"Write my name"* — write the words "my name". Keep going until the room is laughing and the volunteer is exasperated.

> *"You knew exactly what you wanted. You just couldn't say it precisely enough. A computer is fast, obedient, and completely stupid — it does what you said, not what you meant. Today you start learning how to say things precisely."*

---

## Concept Walkthrough (11–26 min)

**Core idea:** software is a set of instructions to the hardware; code is what you write; syntax is the set of rules that code must follow to be understood. `print()` displays exactly what's between its quotes; without quotes, Python evaluates it as an expression instead.

**Worked example:** `print("Hello World!")` → `Hello World!`. `print(2 + 5)` → `7` (no quotes, so Python computes it). `print("2 + 5")` → `2 + 5` (quotes mean "print these exact characters"). Four common breaks: `prnt("Hi")` → `NameError` (misspelled). `Print("Hi")` → `NameError` (Python is case-sensitive). `print(Hi)` → `SyntaxError` (missing quotes). `print("Hi"` → `SyntaxError` (missing closing parenthesis).

**Checkpoint:**
> *"`print(6 / 3)` — who says `2`? Who says `2.0`?"*
> **Answer:** `2.0` — Python's `/` always gives a decimal result.

---

## ⚡ Active Learning Strategy 1 — Error-Spotting Pairs (26–33 min)

Four broken `print()` lines on screen; students guess the error alone, then compare with a partner, then share out — instructor runs each broken line live so the real error message appears. Exposes whether students can read an error message instead of freezing at it.

---

## ⚡ Active Learning Strategy 2 — Predict & Verify (33–40 min)

A short sequence of `print()` lines typed live, one at a time; students commit to a predicted output before each run, ending with a deliberately broken `Print("...")` line the class has to fix. Exposes the quotes-vs-no-quotes misconception before it becomes a habit.

---

## Classroom Quiz (40–47 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block, covering software/syntax definitions, `print()` output prediction, and the four common errors.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| `print("2 + 5")` outputs `7` | They read for meaning; quotes look decorative | Running both quoted and unquoted lines back-to-back |
| `Print` and `print` are the same | Every other written language they know is case-forgiving | Showing the raw `NameError`, then stating "Python is case-sensitive" |
| `print(6 / 3)` outputs `2` | Whole-number division from school maths | Running it live — `/` always returns a decimal |
| Error messages mean "you failed" | School conditioning | Deliberately breaking code in ALS 2 and reading the message aloud calmly |
| Software = the apps on my phone | Only consumer-facing software is visible | The hook's precision exercise, reinforced by the software definition |
