# Session 59 — Introduction to Queue & Implementation Using Arrays

**Duration** 38 min total — 33 min instruction + 5 min Classroom Quiz (cap: 45 + 5, not more) · **Topic** Queue — Introduction and Array Implementation · **Prerequisite** Session 58 — Largest Rectangle in Histogram
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. Define a queue as a First-In-First-Out (FIFO) data structure, contrasting it explicitly with a stack's LIFO behaviour. *(REMEMBERING)*
2. Explain why an array-based queue needs both a `front` and a `back` pointer, rather than just one, and why naive shifting on every `pop` would be wasteful. *(UNDERSTANDING)*
3. Trace `push` and `pop` operations on a fixed-size circular array, including the modulo wraparound that reuses freed slots. *(APPLYING)*
4. Identify the queue's fixed-capacity limitation and explain why that motivates a linked-list-based implementation, covered next session. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Session 58 (Largest Rectangle in Histogram) (0–5 min)

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

**Q5 (MSQ — pick all correct).** Which are true of the Largest Rectangle problem?
`A` Both approaches give the same final answer · `B` The two-pass approach uses two separate stack scans · `C` It requires sorting the bars first · `D` Every bar's rectangle width depends on its neighbours' heights
→ **A, B, D.**

---

## Hook (5–8 min)

Ask: *"You're standing in a line at a ticket counter. Who gets served first — the person who joined the line first, or the person standing closest to the counter right now?"*

Let students answer (first joined). Then:

> *"That's a queue. Whoever arrived first leaves first — First In, First Out, FIFO. It's the exact opposite discipline from every stack you've built so far, where the *most recently* added thing came out first. Today we build this from scratch, starting with the simplest possible version: a plain array."*

---

## Slide Block A (8–15 min) — DELIVER SLIDES AS-IS

Covers: Queue definition (FIFO, linear data structure) → array-based setup: a fixed-size array, with `front` and `back` pointers both initialised to `-1` to signal "empty."

**Beats to emphasise**

- Say the FIFO/LIFO contrast out loud, explicitly, once: "A stack's `top` is both where you add and where you remove. A queue splits that into two roles — `back` is where you add, `front` is where you remove."
- `front = -1, back = -1` is a sentinel meaning "nothing here yet" — flag this now; it resurfaces at every empty/single-element edge case.
- This session uses a **fixed-size** array on purpose — name the tension up front: what happens when the array is full but there's still room at the *front*, because things have already been popped from there?

**Checkpoint (at 15 min)** — cold-call:
> *"Why does a queue need two pointers, `front` and `back`, when a stack only ever needed one, `top`?"*
> **Answer:** A queue adds at one end and removes from the *other* end. A stack adds and removes from the *same* end, so one pointer covers both.

---

## Slide Block B (15–23 min) — DELIVER SLIDES AS-IS

Covers: Full dry run — `push(1), push(2), push(3), push(4)`, `front()`, `pop(), pop()`, `push(5), push(6)`, more pops — on a capacity-5 array, including the moment `back` wraps around from index 4 back to index 0 using modulo.

**Beats to emphasise**

- Narrate the ordinary pushes first, then the two pops that free up indices 0 and 1 at the front even though `back` is sitting further along. **Slow down here:** `push(5)` uses index 4, but `push(6)` needs a slot — the only free ones are behind `front` positionally, but logically still "next." That's what `back = (back + 1) % capacity` buys.
- State plainly: without the modulo wraparound, this array would report "full" after just one round of pushes and pops, even with free slots sitting right there. That's why it's called a **circular** array.

**Checkpoint (at 23 min)** — show hands:
> *"After popping enough that `front` has moved past index 0 and 1, and `back` is about to overflow past the last index — who says `back` just stays stuck? Who says it wraps around?"*
> **Answer:** It wraps around, via `back = (back + 1) % capacity`.

---

## ⚡ Active Learning Strategy 1 — Predict the Output: Trace the Circular Wraparound (23–28 min)

A capacity-4 array traced operation by operation through a full wraparound cycle, students predicting `front`, `back`, and array contents before each reveal. Exposes whether students can track a wraparound themselves — the single trickiest mechanical detail in this session.

---

## ⚡ Active Learning Strategy 2 — Spot the Bug: Full or Empty? (28–33 min)

Three queue states, all with `front == back` at the same index; students decide whether each is empty or has exactly one element, and how code would tell. Exposes the classic array-queue ambiguity — `front == back` alone can't distinguish "empty" from "one element."

---

## Classroom Quiz (33–38 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| `pop()` physically removes/clears the array slot | Mental model of arrays as "boxes that empty out" | ALS 1 — showing earlier elements still physically present after their pops, simply unreachable |
| `front == back` always means the queue is empty | Natural first guess, carried over from single-pointer emptiness checks | ALS 2 — distinguishing the `-1, -1` sentinel (truly empty) from `front == back` at a real index (exactly one element) |
| Once `back` reaches the last index, the queue is full, permanently | Feels like running off the end of an array is a hard stop | ALS 1's wraparound step — `back` reuses freed slots via modulo |
| A circular array queue can grow without limit | Confusing this session's fixed-capacity array with next session's linked-list version | Explicit callout in Slide Block A: this implementation has a **fixed** capacity |

---

## Instructor Notes

- **38-min format: 33 min instruction + 5 min Classroom Quiz, capped at 45 + 5.** Active learning strategies are referenced by name and format only.
- **The Classroom Quiz runs last**, as the sole closing activity — no separate exit ticket or homework block.
- **ALS 2 is the load-bearing activity** — the empty-vs-one-element ambiguity is the single most common real bug when students implement this later.
- **Bridge to the next session explicitly at the close:** "Every problem today came from one root cause — a *fixed-size* array. Next session removes that constraint entirely by switching to a linked list."
