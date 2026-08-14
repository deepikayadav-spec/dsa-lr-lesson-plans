# Introduction to Queue & Implementation Using Arrays

**Duration** 46 min total — 39 min instruction + 7 min Classroom Quiz · **Topic** Queue — Introduction and Array Implementation · **Prerequisite** Largest Rectangle in Histogram
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. Define a queue as a First-In-First-Out (FIFO) data structure, contrasting it explicitly with a stack's LIFO behaviour. *(REMEMBERING)*
2. Explain why an array-based queue needs both a `front` and a `back` pointer, rather than just one, and why naive shifting on every `pop` would be wasteful. *(UNDERSTANDING)*
3. Trace `push` and `pop` operations on a fixed-size circular array, including the modulo wraparound that reuses freed slots. *(APPLYING)*
4. Identify the queue's fixed-capacity limitation and explain why that motivates a linked-list-based implementation, covered next session. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Largest Rectangle in Histogram (0–6 min)

Say: *"Five quick ones on histograms, then we leave stacks behind for one session and meet an entirely new structure."*

**Q1.** A rectangle anchored at a given bar's height can extend as far as:
`A` The edges of the array, always · `B` The nearest shorter bar on each side · `C` The nearest taller bar on each side · `D` Exactly one bar in each direction
→ **B.**

**Q2.** NSE (Next Smaller Element) for a bar is computed by scanning:
`A` Left to right · `B` Right to left · `C` From the tallest bar outward · `D` In sorted order
→ **B.**

**Q3.** In the one-pass optimal approach, a bar's area is computed:
`A` At the very start · `B` At the very end, for all bars at once · `C` The moment it's popped from the stack · `D` Only if it's the tallest bar
→ **C.**

**Q4.** If the stack empties during a pop in the one-pass approach, the rectangle's width is:
`A` Zero · `B` Undefined · `C` The current index · `D` Always 1
→ **C.**

---

## Hook (6–10 min)

Ask: *"You're standing in a line at a ticket counter. Who gets served first — the person who joined the line first, or the person standing closest to the counter right now?"*

Let students answer (first joined). Then:

> *"That's a queue. Whoever arrived first leaves first — First In, First Out, FIFO. It's the exact opposite discipline from every stack you've built so far, where the *most recently* added thing came out first. Today we build this from scratch, starting with the simplest possible version: a plain array."*

---

## Concept Walkthrough (10–25 min)

**Core idea:** a fixed-size array queue tracks two pointers — `front` (where you remove) and `back` (where you add), both starting at `-1` to mean empty. When `back` reaches the end of the array but slots have been freed at the front (from prior pops), it **wraps around** via `back = (back + 1) % capacity` instead of reporting full.

**Worked example** — capacity-5 array: `push(1), push(2), push(3), push(4)` fills to `front=0, back=3`. Two pops move `front` to `2`, freeing indices `0` and `1`. `push(5)` uses index `4` (still in bounds); `push(6)` needs a slot — the only free ones are behind `front` positionally, so `back` wraps `4 → 0`.

**Checkpoint:**
> *"Why does a queue need two pointers when a stack only needed one?"*
> **Answer:** A queue adds at one end and removes from the other; a stack does both at the same end.

---

## ⚡ Active Learning Strategy 1 — Predict the Output: Trace the Circular Wraparound (25–32 min)

A capacity-4 array traced operation by operation through a full wraparound cycle, students predicting `front`, `back`, and array contents before each reveal. Exposes whether students can track a wraparound themselves — the single trickiest mechanical detail in this session.

---

## ⚡ Active Learning Strategy 2 — Spot the Bug: Full or Empty? (32–39 min)

Three queue states, all with `front == back` at the same index; students decide whether each is empty or has exactly one element, and how code would tell. Exposes the classic array-queue ambiguity — `front == back` alone can't distinguish "empty" from "one element."

---

## Classroom Quiz (39–46 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| `pop()` physically removes/clears the array slot | Mental model of arrays as "boxes that empty out" | ALS 1 — showing earlier elements still physically present after their pops, simply unreachable |
| `front == back` always means the queue is empty | Natural first guess, carried over from single-pointer emptiness checks | ALS 2 — distinguishing the `-1, -1` sentinel (truly empty) from `front == back` at a real index (exactly one element) |
| Once `back` reaches the last index, the queue is full, permanently | Feels like running off the end of an array is a hard stop | ALS 1's wraparound step — `back` reuses freed slots via modulo |
| A circular array queue can grow without limit | Confusing this session's fixed-capacity array with next session's linked-list version | This implementation has a **fixed** capacity — say so explicitly |

---
