# Queue Implementation Using Linked List

**Duration** 50 min total — 43 min instruction + 5 min Classroom Quiz + 2 min buffer · **Topic** Queue — Implementation Using Linked List · **Prerequisite** Introduction to Queue & Implementation Using Arrays
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

## Hook (6–9 min)

Ask: *"A shared office printer has a print queue. Someone can send a 200-page print job at 2 AM, and someone else can send one job every minute all day. Should that queue ever say 'sorry, full, try again later'?"*

Let students answer (no). Then:

> *"Last session's array-based queue had exactly that flaw — a fixed capacity that could genuinely run out even with plenty of memory left. Today's fix is almost embarrassingly simple: swap the array for a linked list. Same FIFO behaviour, same O(1) operations, no capacity ceiling at all."*

---

## Problem Statement (9–13 min)

Design a queue backed by a singly linked list, supporting FIFO insertion and removal with no fixed capacity.

**Input:** a sequence of operations — `enqueue(x)`, `dequeue()`, `front()`.
**Output:** for each `dequeue()`/`front()` call, the value returned (or an explicit error if the queue is empty).

**Example 1**
Input: `enqueue(10)`, `enqueue(20)`, `dequeue()`, `front()`
Output: `dequeue() = 10`, `front() = 20`
Why: `10` was added first, so it's the first one out; `20` is now the only element left, so it's also the front.

**Example 2**
Input: `dequeue()` on an empty queue
Output: fails — `"Queue is empty"`
Why: there's no node to remove; unlike the array version, there's no capacity ceiling, but emptiness still has to be checked.

---

## Concept Walkthrough (13–29 min)

**Core idea:** swap the fixed array for a linked list — `front` and `back` become **node pointers**, not indices, both `null` when empty. No capacity, no modulo. `push` links a new node after `back` and moves `back` to it; `pop` moves `front` to `front->next`.

**Worked example:** on the very first `push`, the queue was empty, so the new node becomes *both* `front` and `back`. When `pop()` removes the **last** remaining node, *both* `front` and `back` must be reset to `null` — resetting only `front` leaves `back` dangling, pointing at a deleted node.

**Pseudocode** — derived from the core idea:

```
class Node: data, next

class LinkedQueue:
    front = null
    back = null

    function enqueue(x):
        node = new Node(x)
        if back == null:                # queue was empty
            front = back = node
        else:
            back.next = node
            back = node

    function dequeue():
        if front == null: error "Queue is empty"
        x = front.data
        front = front.next
        if front == null: back = null   # just removed the last node
        return x
```

**C++ implementation:**

```cpp
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedQueue {
    Node* front = nullptr;
    Node* back  = nullptr;
public:
    void enqueue(int x) {
        Node* node = new Node(x);
        if (!back) front = back = node;       // queue was empty
        else { back->next = node; back = node; }
    }

    int dequeue() {
        if (!front) throw runtime_error("Queue is empty");
        int x = front->data;
        Node* temp = front;
        front = front->next;
        if (!front) back = nullptr;           // just removed the last node
        delete temp;
        return x;
    }
};
```

`enqueue` and `dequeue` are both O(1) — no traversal, no capacity ceiling.

**Checkpoint:**
> *"When the last element is popped, why reset both pointers, not just `front`?"*
> **Answer:** If only `front` is reset, `back` still points at the deleted node — a dangling pointer that corrupts the next `push`.

---

## ⚡ Active Learning Strategy 1 — Live Trace: Push and Pop by Pointer (29–36 min)

**Format:** Live Coding / Dry-Run Relay · **Exposes:** whether students can track `front` and `back` as they move between actual nodes, rather than array indices — the one genuinely new mental model this session introduces.

**Setup line (say this):**
> *"Empty queue. Sequence: `push(A)`, `push(B)`, `push(C)`, `pop()`, `pop()`. After each step, tell me what `front` and `back` point to — before I confirm."*

Run **one operation at a time**:

```
push(A) → queue was empty → front = back = node(A).             front→A←back
push(B) → back->next = node(B); back = node(B).                 front→A→B←back
push(C) → back->next = node(C); back = node(C).                 front→A→B→C←back
pop()   → front = front->next = node(B).                        front→B→C←back
pop()   → front = front->next = node(C). Now front == back == node(C).   front→C←back
```

**How it surfaces:** After the second `pop()`, ask before revealing: *"`front` and `back` now point at the same node — does that mean the queue is empty?"* Correct: no — it means exactly one element remains (`C`), the same "front equals back, one element" case from last session's Activity 2, just expressed as pointers instead of indices.

**Debrief line:**
> *"Same underlying situations as last session — 'one element left' and 'completely empty' are still two different states that happen to look similar. The representation changed from indices to pointers; the logic you have to get right didn't."*

**Cut rule:** If running short, do just `push(A)` and the second `pop()` — one shows the empty-queue special case, the other shows the one-element state.

---

## ⚡ Active Learning Strategy 2 — Spot the Bug: The Missing Reset (36–43 min)

**Format:** Spot the Bug · **Exposes:** the single most common real bug in this implementation — forgetting to reset `back` to `null` when the last element is popped, leaving it dangling.

**Setup line (say this):**
> *"Here's a `pop()` implementation with a bug. Find it."*

```
pop() {
    if (size == 0) { print("Queue is empty"); return }
    Node* temp = front
    front = front->next
    delete temp
    size--
}
```

**What students do:** 45 seconds silent, then hands up.

**Answer:** This version *always* just does `front = front->next`, even when popping the very last element. When `front` was the only node, `front->next` is `null`, so `front` correctly becomes `null` — but `back` was never touched, and still points at the now-deleted node. `back` is left dangling.

**How it surfaces:** Ask: *"If I call `push(x)` right after this buggy `pop()` empties the queue, what happens?"* Walk through it: `push` checks `if (size == 0)` to decide whether to set `front = back = newNode` — but `size` was correctly decremented to `0`, so this particular bug is masked *this time*. Then ask: *"What if `push`'s empty-check used `back == null` instead of `size == 0`?"* Now it breaks — `back` isn't null, so `push` thinks the queue isn't empty and tries to do `back->next = newNode` on a dangling pointer.

**Debrief line:**
> *"The fix: when `size` reaches `0` after a pop, explicitly set both `front = null` and `back = null`. Don't rely on one pointer's state to imply the other's — say it directly, every time."*

**Cut rule:** If running short, state the bug and its fix directly rather than running the "what if push used `back == null`" extension — the core lesson (reset both pointers together) still lands.

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
| Only `front` needs updating when popping the last element | Pop is mentally centred on `front`, since that's the end being removed | ALS 2 — showing `back` left dangling if it isn't explicitly reset alongside `front` |
| `front == back` always means the queue is empty | Direct carryover from arrays | ALS 1's second pop — `front == back` here means exactly one node remains |
| The linked-list queue is a fundamentally different algorithm from the array queue | New pointer-based syntax looks unfamiliar | Same FIFO behaviour, same two-pointer design as last session — only the storage mechanism changed |
| A linked-list queue can never run out of space | Technically bounded only by system memory | Brief, honest caveat: not capacity-*checked*, but not infinite either |

---
