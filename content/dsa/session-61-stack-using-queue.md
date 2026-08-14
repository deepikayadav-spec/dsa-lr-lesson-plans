# Session 61 — Stack Using Queue

**Duration** 38 min total — 33 min instruction + 5 min Classroom Quiz (cap: 45 + 5, not more) · **Topic** Stack & Queue — Implementation: Stack Using Queue · **Prerequisite** Session 60 — Queue Implementation Using Linked List
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

**Platform units**

| Resource | Unit ID |
|---|---|
| Video + deck — Implementation Stack Using Queue | https://docs.google.com/presentation/d/1dbh5JIZD5r6Rw__F5MxnwIBMkkLmeZI-ExoISq4M6mQ/edit |

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the constraint of this problem: build a stack's `push`/`pop`/`top` behaviour using only a queue's `enqueue`/`dequeue` operations. *(REMEMBERING)*
2. Explain the rotation trick — after enqueueing a new element, rotate the entire rest of the queue behind it so the newest element sits at the front. *(UNDERSTANDING)*
3. Trace `push`, `pop`, and `top` on a single-queue stack simulation across a full sequence of operations. *(APPLYING)*
4. Analyse the resulting time complexity trade-off: `push` becomes O(n), while `pop` and `top` stay O(1) — and explain *why* the cost had to move somewhere. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Session 60 (Queue: Linked List Implementation) (0–5 min)

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

**Q5 (MSQ — pick all correct).** Which are true of the linked-list queue?
`A` Nodes are allocated on demand · `B` It has no fixed capacity · `C` `push` and `pop` involve pointer reassignment, not array arithmetic · `D` It requires a modulo operation somewhere
→ **A, B, C.**

---

## Hook (5–8 min)

Ask: *"You have a queue — enqueue at the back, dequeue from the front. That's the only tool you're allowed to use. Can you make it behave like a stack — last in, first out?"*

Let students think for a moment; most will assume this needs a completely different structure. Then:

> *"You can — with a single queue, and one clever trick played at push time. It costs you something, though, and figuring out *what* it costs, and *why*, is the real lesson today."*

---

## Slide Block A (8–16 min) — DELIVER SLIDES AS-IS

Covers: Introduction (simulate a stack's behaviour using a queue's `enqueue`/`dequeue`) → Basic Operations (`push`, `pop`, `top`, `empty`, `size`) → Approach: use a single queue; on `push`, insert the new element, then rotate the queue so the newest element moves to the front.

**Beats to emphasise**

- State the goal precisely: the *interface* looks like a stack, but the *only* primitive operations available underneath are `enqueue` and `dequeue`.
- **Say the rotation idea as one sentence:** every time you push, rotate everything already in the queue around to behind the new element — so whatever you just pushed ends up at the very front.
- Preview the cost trade-off without resolving it yet: `pop` and `top` become trivially O(1) — but that rotation on every `push` isn't free.

**Checkpoint (at 16 min)** — cold-call:
> *"After every `push`, where does the newly pushed element end up sitting in the queue?"*
> **Answer:** At the front — so `pop()` and `top()` can just read the queue's front directly.

---

## Slide Block B (16–24 min) — DELIVER SLIDES AS-IS

Covers: Full dry run of `push(10), push(20), push(30), push(40), pop(), top(), pop(), top()` → pseudocode (`push` enqueues then rotates `n` times) → complexity (`push`: O(N); `pop`, `top`, `empty`, `size`: O(1)) → code.

**Beats to emphasise**

- Narrate the rotation count exactly as the deck does: `push(20)` on a 1-element queue rotates once; `push(30)` on a 2-element queue rotates twice.
- **Say explicitly: rotation count equals the queue's size *before* the new element was added** — the detail students most often get off-by-one on.
- Walk `pop()` and `top()` as trivial reads — no rotation involved in either.

**Checkpoint (at 24 min)** — cold-call:
> *"When we called `push(40)` with three elements already in the queue, how many times did we rotate — and why that many?"*
> **Answer:** Three times — once per pre-existing element, each rotation moving one "older" element from front to back.

---

## ⚡ Active Learning Strategy 1 — Live Trace: Rotate It Yourself (24–29 min)

A fresh push sequence (`push(5), push(15), push(25)`), students stating rotation count and resulting queue order before each reveal. Exposes whether students can execute the rotation mechanics themselves, not just watch the deck's example.

---

## ⚡ Active Learning Strategy 2 — Predict & Discuss: Where Did the Cost Go? (29–33 min)

Class discussion: a native stack has all three operations at O(1); this version matches on `pop`/`top` — so where did the cost go? Exposes whether students understand the complexity trade-off as a *conservation* of work, not a free win. Answer: the cost moved entirely into `push`, now O(N).

---

## Classroom Quiz (33–38 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session. <!-- placement: inferred — question bank not available in source material; instructor to pull from platform before class. -->

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| The rotation count is based on the queue's size *after* the new element is added | Off-by-one instinct | ALS 1's `push(25)` step — explicitly counting rotations for *pre-existing* elements only |
| `pop()` and `top()` also need some kind of rotation | Feels symmetric with `push` | Slide Block B — `pop` and `top` are direct reads/removals of the front, no rotation at all |
| This trade-off is a "trick" with no real cost, since the interface still looks like O(1) stack operations | The O(1) `pop`/`top` result is what's usually highlighted | ALS 2 — explicitly locating the O(N) cost inside `push` |
| A native stack is strictly worse than this approach, since this one also achieves O(1) pop/top | Surface-level comparison stops at matching complexities on two operations | State plainly: a native stack has *all three* operations at O(1); this is strictly worse overall — a constraint-following exercise, not an optimisation |

---

## Instructor Notes

- **38-min format: 33 min instruction + 5 min Classroom Quiz, capped at 45 + 5.** Active learning strategies are referenced by name and format only.
- **The Classroom Quiz runs last**, as the sole closing activity — no separate exit ticket or homework block.
- **This session's payoff is ALS 2, not the mechanical trace.** Students can often execute the rotation dry run correctly while still missing *why* it's interesting. Protect time for the discussion.
- **Say "Stack Using Queue" out loud, distinctly.** It's easily confused with the mirror-image "Queue Using Stack" problem — flag this explicitly if that session is covered elsewhere in the course.
