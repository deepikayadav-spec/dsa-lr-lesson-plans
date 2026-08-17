# Stack Using Queue

**Duration** 50 min total — 43 min instruction + 5 min Classroom Quiz + 2 min buffer · **Topic** Stack & Queue — Implementation: Stack Using Queue · **Prerequisite** Queue Implementation Using Linked List
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the constraint of this problem: build a stack's `push`/`pop`/`top` behaviour using only a queue's `enqueue`/`dequeue` operations. *(REMEMBERING)*
2. Explain the rotation trick — after enqueueing a new element, rotate the entire rest of the queue behind it so the newest element sits at the front. *(UNDERSTANDING)*
3. Trace `push`, `pop`, and `top` on a single-queue stack simulation across a full sequence of operations. *(APPLYING)*
4. Analyse the resulting time complexity trade-off: `push` becomes O(n), while `pop` and `top` stay O(1) — and explain *why* the cost had to move somewhere. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Queue: Linked List Implementation (0–6 min)

Say: *"Five on the linked-list queue, then we do something a little backwards — build a stack out of a queue."*

**Q1.** In the linked-list queue, `front` and `back` are:
`A` Array indices · `B` Node pointers · `C` Both required to be integers · `D` Not needed at all
→ **B.**

**Q2.** When the last remaining node is popped from a linked-list queue, which pointers must be reset?
`A` Just `front` · `B` Just `back` · `C` Both `front` and `back` · `D` Neither
→ **C.**

**Q3.** The main advantage of a linked-list queue over an array-based one is:
`A` Faster `push` · `B` No fixed capacity limit · `C` Supports random access · `D` Uses less memory always
→ **B.**

**Q4.** All core operations on a linked-list queue (`push`, `pop`, `front`) run in:
`A` O(1) · `B` O(n) · `C` O(log n) · `D` O(n²)
→ **A.**

---

## Hook (6–10 min)

Ask: *"You have a queue — enqueue at the back, dequeue from the front. That's the only tool you're allowed to use. Can you make it behave like a stack — last in, first out?"*

Let students think for a moment; most will assume this needs a completely different structure. Then:

> *"You can — with a single queue, and one clever trick played at push time. It costs you something, though, and figuring out *what* it costs, and *why*, is the real lesson today."*

---

## Concept Walkthrough (10–29 min)

**Core idea:** simulate a stack using only a queue's `enqueue`/`dequeue`. On every `push`, enqueue the new element, then rotate the rest of the queue behind it — exactly `size-before-the-push` rotations — so the newest element ends up at the front, where `pop()` and `top()` can read it directly.

**Worked example:** `push(10)` — 0 rotations. `push(20)` — 1 element already there, rotate once: `[20, 10]`. `push(30)` — 2 elements, rotate twice: `[30, 20, 10]`. `pop()` and `top()` are then trivial front reads — no rotation involved.

**Checkpoint:**
> *"`push(40)` on a 3-element queue rotates how many times, and why?"*
> **Answer:** Three — once per pre-existing element, until `40` reaches the front.

---

## ⚡ Active Learning Strategy 1 — Live Trace: Rotate It Yourself (29–36 min)

**Format:** Live Coding / Dry-Run Relay · **Exposes:** whether students can execute the rotation count and mechanics themselves on a fresh sequence, rather than having only watched the deck's example.

**Setup line (say this):**
> *"Fresh queue. Sequence: `push(5), push(15), push(25)`. After each push, tell me the rotation count and the resulting queue order, front to back, before I confirm."*

Run **one push at a time**:

```
push(5)  → queue empty → 0 rotations → enqueue 5.                     Queue: [5]
push(15) → 1 element already there → rotate once:
           enqueue 15 → [5, 15]; move 5 to back → [15, 5].            Queue: [15, 5]
push(25) → 2 elements already there → rotate twice:
           enqueue 25 → [15, 5, 25];
           move 15 to back → [5, 25, 15];
           move 5 to back → [25, 15, 5].                              Queue: [25, 15, 5]
```

**How it surfaces:** At `push(25)`, ask before revealing: *"How many rotations, and what's the very first one?"* Correct: two rotations, and the first one moves `15` (not `5`) to the back — rotation always operates on whatever is currently at the *front*, in order, one at a time.

**Debrief line:**
> *"Front to back, always: `[25, 15, 5]` — most recently pushed at the front, oldest at the back. That's a stack's order, LIFO, built entirely from a FIFO structure plus one rotation step per push."*

**Cut rule:** If running short, do just `push(15)` — a single rotation is enough to demonstrate the mechanism; `push(25)`'s two-rotation step is confirmation, not new information.

---

## ⚡ Active Learning Strategy 2 — Predict & Discuss: Where Did the Cost Go? (36–43 min)

**Format:** Predict-the-Output / Discussion · **Exposes:** whether students understand the complexity trade-off as a *conservation* of work, not a free win — the actual insight behind this whole session.

**Setup line (say this):**
> *"A native stack — the kind you built earlier in this block — has `push`, `pop`, and `top` all at O(1). This queue-based version has `pop` and `top` at O(1) too. So where did the cost go? It has to be somewhere — nothing here is actually free."*

**What students do:** Discuss for a minute, then share out.

**Answer:** The cost moved entirely into `push`, which is now O(N) — every single push rotates however many elements were already there. A native stack's `push` is O(1); this version trades that away specifically so that `pop` and `top` can stay O(1), matching a native stack's behaviour on those two operations.

**How it surfaces:** Ask a follow-up: *"If your program does mostly pushes and very few pops, is this a good trade?"* Push toward: no — you'd be paying the O(N) cost repeatedly for little benefit. *"If your program does one big burst of pushes, then mostly pops and tops?"* Better trade — the expensive part happens once, then everything else is cheap.

**Debrief line:**
> *"Every 'simulate X using Y' trick you'll ever see works this way — something gets cheaper, and something else absorbs that cost. The real skill isn't memorising the trick, it's being able to say exactly where the bill went."*

**Cut rule:** If running short, skip the "mostly pushes vs. mostly pops" follow-up discussion and just state the O(N) push / O(1) pop-and-top trade-off directly.

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
| The rotation count is based on the queue's size *after* the new element is added | Off-by-one instinct | ALS 1's `push(25)` step — explicitly counting rotations for *pre-existing* elements only |
| `pop()` and `top()` also need some kind of rotation | Feels symmetric with `push` | `pop` and `top` are direct reads/removals of the front — no rotation at all |
| This trade-off is a "trick" with no real cost, since the interface still looks like O(1) stack operations | The O(1) `pop`/`top` result is what's usually highlighted | ALS 2 — explicitly locating the O(N) cost inside `push` |
| A native stack is strictly worse than this approach, since this one also achieves O(1) pop/top | Surface-level comparison stops at matching complexities on two operations | State plainly: a native stack has *all three* operations at O(1); this is strictly worse overall — a constraint-following exercise, not an optimisation |

---
