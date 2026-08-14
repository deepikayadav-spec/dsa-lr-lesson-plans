# Session 60 — Queue Implementation Using Linked List

**Duration** 34 min total — 29 min instruction + 5 min Classroom Quiz (cap: 45 + 5, not more) · **Topic** Queue — Implementation Using Linked List · **Prerequisite** Session 59 — Introduction to Queue & Implementation Using Arrays
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. Explain why a linked-list-based queue has no fixed capacity, directly resolving last session's array limitation. *(REMEMBERING)*
2. Describe how `front` and `back` become node pointers rather than array indices, and why both still need explicit tracking. *(UNDERSTANDING)*
3. Trace `push` and `pop` operations on a linked-list queue, including the single-node special case where both `front` and `back` must be updated together. *(APPLYING)*
4. Compare the linked-list implementation against the array implementation — what's gained, what's identical. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Session 59 (Queue: Array Implementation) (0–5 min)

Say: *"Five quick ones on the array-based queue before we swap the array out entirely."*

**Q1.** A queue follows which principle?
`A` LIFO · `B` FIFO · `C` Random access · `D` Priority order
→ **B.**

**Q2.** In the array-based queue, `front == back` at a real index (not `-1, -1`) means:
`A` The queue is always empty · `B` The queue has exactly one element · `C` The queue is always full · `D` This state is impossible
→ **B.**

**Q3.** The modulo wraparound (`back = (back + 1) % capacity`) exists to:
`A` Sort the elements · `B` Reuse freed slots at the front once the array's physical end is reached · `C` Double the array's size · `D` Detect errors
→ **B.**

**Q4.** What is the biggest limitation of the array-based queue?
`A` It's slower than a linked list for `push` · `B` It has a fixed maximum capacity · `C` It can't track a `front` pointer · `D` It doesn't support `pop`
→ **B.**

**Q5 (MSQ — pick all correct).** Which are true of the array-based queue from last session?
`A` It uses two pointers, `front` and `back` · `B` It needs a `-1, -1` sentinel for the empty state · `C` It can grow without any upper bound · `D` `pop()` only moves `front`, it doesn't physically clear the slot
→ **A, B, D.**

---

## Hook (5–8 min)

Ask: *"A shared office printer has a print queue. Someone can send a 200-page print job at 2 AM, and someone else can send one job every minute all day. Should that queue ever say 'sorry, full, try again later'?"*

Let students answer (no). Then:

> *"Last session's array-based queue had exactly that flaw — a fixed capacity that could genuinely run out even with plenty of memory left. Today's fix is almost embarrassingly simple: swap the array for a linked list. Same FIFO behaviour, same O(1) operations, no capacity ceiling at all."*

---

## Slide Block A (8–15 min) — DELIVER SLIDES AS-IS

Covers: Node structure (`data` + `next` pointer) → `front` and `back` become **node pointers**, not array indices, both initialised to `null` for an empty queue.

**Beats to emphasise**

- Say the direct mapping explicitly: everything from last session still applies — you still need a `front` for removal and a `back` for insertion. The only thing that changed is *what kind of thing* they point to: a node, not a slot number.
- No capacity, no modulo, no wraparound — say this as a relief: the entire reason last session needed circular index arithmetic simply doesn't exist here.
- `front = null, back = null` is this session's version of last session's `-1, -1` sentinel.

**Checkpoint (at 15 min)** — cold-call:
> *"What replaces the array index arithmetic from last session's `push` and `pop`?"*
> **Answer:** Nothing needs arithmetic at all — `push` links a new node after `back` and moves `back` to it; `pop` moves `front` to `front->next`.

---

## Slide Block B (15–21 min) — DELIVER SLIDES AS-IS

Covers: Full dry run — `push(1), push(2), push(3), push(4)`, then `pop()`, `front()`, several more `pop()`s down to empty — using node links throughout → pseudocode → complexity (all O(1)).

**Beats to emphasise**

- Narrate `push(1)` as the special case: queue was empty, so the new node becomes *both* `front` and `back` at once. Every push after that just does `back->next = newNode; back = newNode`.
- Narrate popping the **last** element as the other special case: when `pop()` empties the queue entirely, *both* `front` and `back` must be reset to `null` — updating only `front` would leave `back` dangling.

**Checkpoint (at 21 min)** — cold-call:
> *"When the very last element is popped, why set *both* `front` and `back` to null, instead of just `front`?"*
> **Answer:** If only `front` is reset, `back` still points at the deleted node — a dangling pointer.

---

## ⚡ Active Learning Strategy 1 — Live Trace: Push and Pop by Pointer (21–25 min)

A short push/pop sequence traced node by node, students stating what `front` and `back` point to before each reveal. Exposes whether students can track pointers moving between actual nodes, rather than array indices.

---

## ⚡ Active Learning Strategy 2 — Spot the Bug: The Missing Reset (25–29 min)

A buggy `pop()` implementation that never resets `back` when the last node is removed; students find the bug. Exposes the single most common real bug in this implementation — a dangling `back` pointer.

---

## Classroom Quiz (29–34 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Only `front` needs updating when popping the last element | Pop is mentally centred on `front`, since that's the end being removed | ALS 2 — showing `back` left dangling if it isn't explicitly reset alongside `front` |
| `front == back` always means the queue is empty | Direct carryover from arrays | ALS 1's second pop — `front == back` here means exactly one node remains |
| The linked-list queue is a fundamentally different algorithm from the array queue | New pointer-based syntax looks unfamiliar | Slide Block A's direct mapping — same FIFO behaviour, same two-pointer design, only the storage mechanism changed |
| A linked-list queue can never run out of space | Technically bounded only by system memory | Brief, honest caveat: not capacity-*checked*, but not infinite either |

---

## Instructor Notes

- **34-min format: 29 min instruction + 5 min Classroom Quiz, capped at 45 + 5.** Active learning strategies are referenced by name and format only.
- **The Classroom Quiz runs last**, as the sole closing activity — no separate exit ticket or homework block.
- **This is a fast, mechanically simple session once the array-based mental model has been set aside** — lean on the direct one-to-one mapping from last session.
- **ALS 2 is the load-bearing activity** — the dangling-`back` bug is the single most common real-world bug in a hand-rolled linked-list queue.
- **This closes out the Queue pair.** If time allows, state explicitly which one an instructor would actually reach for in practice: the linked-list version, almost always.
