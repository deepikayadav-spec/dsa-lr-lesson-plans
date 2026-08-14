# Queue Implementation Using Linked List

**Duration** 44 min total — 37 min instruction + 7 min Classroom Quiz · **Topic** Queue — Implementation Using Linked List · **Prerequisite** Introduction to Queue & Implementation Using Arrays
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. Explain why a linked-list-based queue has no fixed capacity, directly resolving last session's array limitation. *(REMEMBERING)*
2. Describe how `front` and `back` become node pointers rather than array indices, and why both still need explicit tracking. *(UNDERSTANDING)*
3. Trace `push` and `pop` operations on a linked-list queue, including the single-node special case where both `front` and `back` must be updated together. *(APPLYING)*
4. Compare the linked-list implementation against the array implementation — what's gained, what's identical. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Queue: Array Implementation (0–6 min)

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

---

## Hook (6–10 min)

Ask: *"A shared office printer has a print queue. Someone can send a 200-page print job at 2 AM, and someone else can send one job every minute all day. Should that queue ever say 'sorry, full, try again later'?"*

Let students answer (no). Then:

> *"Last session's array-based queue had exactly that flaw — a fixed capacity that could genuinely run out even with plenty of memory left. Today's fix is almost embarrassingly simple: swap the array for a linked list. Same FIFO behaviour, same O(1) operations, no capacity ceiling at all."*

---

## Concept Walkthrough (10–23 min)

**Core idea:** swap the fixed array for a linked list — `front` and `back` become **node pointers**, not indices, both `null` when empty. No capacity, no modulo. `push` links a new node after `back` and moves `back` to it; `pop` moves `front` to `front->next`.

**Worked example:** on the very first `push`, the queue was empty, so the new node becomes *both* `front` and `back`. When `pop()` removes the **last** remaining node, *both* `front` and `back` must be reset to `null` — resetting only `front` leaves `back` dangling, pointing at a deleted node.

**Checkpoint:**
> *"When the last element is popped, why reset both pointers, not just `front`?"*
> **Answer:** If only `front` is reset, `back` still points at the deleted node — a dangling pointer that corrupts the next `push`.

---

## ⚡ Active Learning Strategy 1 — Live Trace: Push and Pop by Pointer (23–30 min)

A short push/pop sequence traced node by node, students stating what `front` and `back` point to before each reveal. Exposes whether students can track pointers moving between actual nodes, rather than array indices.

---

## ⚡ Active Learning Strategy 2 — Spot the Bug: The Missing Reset (30–37 min)

A buggy `pop()` implementation that never resets `back` when the last node is removed; students find the bug. Exposes the single most common real bug in this implementation — a dangling `back` pointer.

---

## Classroom Quiz (37–44 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Only `front` needs updating when popping the last element | Pop is mentally centred on `front`, since that's the end being removed | ALS 2 — showing `back` left dangling if it isn't explicitly reset alongside `front` |
| `front == back` always means the queue is empty | Direct carryover from arrays | ALS 1's second pop — `front == back` here means exactly one node remains |
| The linked-list queue is a fundamentally different algorithm from the array queue | New pointer-based syntax looks unfamiliar | Same FIFO behaviour, same two-pointer design as last session — only the storage mechanism changed |
| A linked-list queue can never run out of space | Technically bounded only by system memory | Brief, honest caveat: not capacity-*checked*, but not infinite either |

---
