# Introduction to Queue & Implementation Using Arrays

**Duration** 50 min total — 43 min instruction + 5 min Classroom Quiz + 2 min buffer · **Topic** Queue — Introduction and Array Implementation · **Prerequisite** Largest Rectangle in Histogram
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

## Concept Walkthrough (10–29 min)

**Core idea:** a fixed-size array queue tracks two pointers — `front` (where you remove) and `back` (where you add), both starting at `-1` to mean empty. When `back` reaches the end of the array but slots have been freed at the front (from prior pops), it **wraps around** via `back = (back + 1) % capacity` instead of reporting full.

**Worked example** — capacity-5 array: `push(1), push(2), push(3), push(4)` fills to `front=0, back=3`. Two pops move `front` to `2`, freeing indices `0` and `1`. `push(5)` uses index `4` (still in bounds); `push(6)` needs a slot — the only free ones are behind `front` positionally, so `back` wraps `4 → 0`.

**Checkpoint:**
> *"Why does a queue need two pointers when a stack only needed one?"*
> **Answer:** A queue adds at one end and removes from the other; a stack does both at the same end.

---

## ⚡ Active Learning Strategy 1 — Predict the Output: Trace the Circular Wraparound (29–36 min)

**Format:** Predict-the-Output / Live Trace · **Exposes:** whether students can track `front`, `back`, and `size` through a full wraparound cycle themselves — the single trickiest mechanical detail in this session.

**Setup line (say this):**
> *"Capacity-4 array, starts empty. Sequence: `push(A), push(B), push(C), pop(), pop(), push(D), push(E)`. After each operation, tell me `front`, `back`, and what's actually stored, before I confirm."*

Run **one operation at a time**:

```
push(A) → front=0, back=0.                arr: [A, _, _, _]
push(B) → back=1.                         arr: [A, B, _, _]
push(C) → back=2.                         arr: [A, B, C, _]
pop()   → front=1 (A removed logically).  arr: [A, B, C, _]  (A still physically there, just unreachable)
pop()   → front=2 (B removed logically).  arr: [A, B, C, _]
push(D) → back=3.                         arr: [A, B, C, D]
push(E) → back=(3+1)%4=0 → wraps!         arr: [E, B, C, D]  (E overwrites A's old slot)
```

**How it surfaces:** At `push(E)`, ask before revealing: *"Is the array full at this point? `back` is about to go past index 3 — what happens?"* Correct: it's *not* full — `front` is sitting at index 2, meaning slots 0 and 1 are free — so `back` wraps to `0` and reuses that freed slot, rather than reporting overflow.

**Debrief line:**
> *"The values at indices 0 and 1 never got erased — `pop()` just moved `front` past them. `push(E)` is the operation that actually overwrites what's there. Physical array position and logical queue position are two different things, and that gap is exactly what the modulo arithmetic bridges."*

**Cut rule:** If running short, do only the `push(D)` and `push(E)` steps — the wraparound is the entire point; the earlier pushes and pops are just setup.

---

## ⚡ Active Learning Strategy 2 — Spot the Bug: Full or Empty? (36–43 min)

**Format:** Spot the Bug · **Exposes:** the classic array-queue ambiguity — `front == back` can mean either "completely empty" or "exactly one element," and conflating the two is the most common real bug in this implementation.

**Setup line (say this):**
> *"Three queue states, each showing `front` and `back` at the same index. For each: is the queue empty, or does it have exactly one element? How would code even tell the difference?"*

```
1.  front = -1, back = -1
2.  front = 2,  back = 2   (after a fresh push(x) as the very first element)
3.  front = 2,  back = 2   (after several push/pop cycles have looped back around)
```

**What students do:** 45 seconds silent, then hands up.

**Answers**

| # | State | How to tell |
|---|---|---|
| 1 | Empty | `-1, -1` is the dedicated sentinel — this is the *only* unambiguous empty signal in this design |
| 2 | One element | `front == back` at a real index, with a `size` counter confirming `size = 1` |
| 3 | One element | Same as #2 — `front == back` alone can't distinguish "just started" from "wrapped back around"; only an explicit `size` variable (or capacity check) resolves it |

**How it surfaces:** Push students to say explicitly *why* `front == back` is ambiguous on its own — it's true both when there's exactly one element and, in some naive implementations, when the queue is completely empty. This deck's design sidesteps the ambiguity with the dedicated `-1, -1` sentinel plus an explicit `size` counter — flag that as a deliberate design choice, not an accident.

**Debrief line:**
> *"`front == back` alone never tells you the whole story. This implementation solves it two ways at once: a `-1, -1` sentinel for genuinely empty, and a `size` counter for everything else. Skip either one and you'll misreport empty as full, or vice versa."*

**Cut rule:** If running short, do state 1 vs. state 2 only — that pairing alone establishes the sentinel-vs-real-index distinction; state 3 is a reinforcement.

---

## Classroom Quiz (43–48 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session.

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. If you land here with time on the clock, let the session end early — don't stretch content to fill it.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| `pop()` physically removes/clears the array slot | Mental model of arrays as "boxes that empty out" | ALS 1 — showing earlier elements still physically present after their pops, simply unreachable |
| `front == back` always means the queue is empty | Natural first guess, carried over from single-pointer emptiness checks | ALS 2 — distinguishing the `-1, -1` sentinel (truly empty) from `front == back` at a real index (exactly one element) |
| Once `back` reaches the last index, the queue is full, permanently | Feels like running off the end of an array is a hard stop | ALS 1's wraparound step — `back` reuses freed slots via modulo |
| A circular array queue can grow without limit | Confusing this session's fixed-capacity array with next session's linked-list version | This implementation has a **fixed** capacity — say so explicitly |

---
