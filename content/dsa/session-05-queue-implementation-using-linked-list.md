# Queue Implementation Using Linked List

**Duration** 50 min total — 43 min instruction + 5 min Classroom Quiz + 2 min buffer (buffer is inside the 50, not extra) · **Topic** Queue — Implementation Using Linked List · **Prerequisite** Introduction to Queue & Implementation Using Arrays
**Session type** Concept lecture · **Format** Class Delivery Framework — Safe Points, dry run → observations → pseudocode → code, engagement activity reuses the session's own example

---

## Learning Objectives

By the end of this session, students will be able to:

1. Explain why a linked-list-based queue has no fixed capacity, directly resolving last session's array limitation. *(REMEMBERING)*
2. Describe how `front` and `back` become node pointers rather than array indices, and why both still need explicit tracking. *(UNDERSTANDING)*
3. Trace `push` and `pop` operations on a linked-list queue, including the single-node special case where both `front` and `back` must be updated together. *(APPLYING)*
4. Compare the linked-list implementation against the array implementation — what's gained, what's identical. *(ANALYZING)*

---

## Warm-Up Poll — Recap of Previous Session (0–5 min)

Live poll (Mentimeter or similar) on **Queue: Array Implementation**. **Don't summarize it yourself first** — run the poll cold, then read the aggregate result out loud as the recap.

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

Say: *"[X]% caught the fixed-capacity limitation — good, because that's exactly what today fixes."*

---

## Hook (5–8 min)

State the topic explicitly: *"Today we're staying with queues, but swapping out the array for a linked list — fixing the one real weakness from last session."*

Ask: *"A shared office printer has a print queue. Someone can send a 200-page print job at 2 AM, and someone else can send one job every minute all day. Should that queue ever say 'sorry, full, try again later'?"*

Let students answer (no). Then name the advantage explicitly:

> *"Last session's array-based queue had exactly that flaw — a fixed capacity that could genuinely run out even with plenty of memory left. Today's fix is almost embarrassingly simple: swap the array for a linked list. Same FIFO behaviour, same O(1) operations, no capacity ceiling at all — that's the advantage, concretely."*

---

## Problem Statement (8–12 min)

*(Deck: Slides 4–6 — introduction, node structure, front/back pointers)*

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

**Safe Point 1 — Problem Statement Clarity.** *Technique: Paraphrase-Back.* Pick a different student than last session's Safe Point 1. Ask them to restate, in their own words: "what's the same as last session's queue, and what's explicitly different?" Don't proceed until both halves of that answer are clean.

---

## Concept Walkthrough (12–38 min)

*(Deck: Dry Run Slides 7–21 · Pseudocode Slides 22–27 · Complexity Slide 28 · C++ Code Slides 29–36 · Key Takeaways Slide 45)*

**Approach Exploration (~2 min).** Before revealing anything, ask: *"If we're not using an array at all, what do `front` and `back` even mean anymore? What could they point to instead?"* Let students land on "a node" themselves if possible — it's a small leap from Linked List sessions earlier in the block. Then give the brief version: *"`front` and `back` become node pointers, not indices. No capacity, no modulo — we're trading array indices for pointers."*

**Dry Run (~6 min).** Empty queue to start. Track `front` and `back` explicitly at every step, and choose the sequence so it hits the single-node special case — both the creation and the removal side of it:

```
front = back = null (empty)

enqueue(A) → queue was empty → front = back = new node(A).         front→A←back
enqueue(B) → back->next = node(B); back moves to node(B).          front→A→B←back
enqueue(C) → back->next = node(C); back moves to node(C).          front→A→B→C←back
dequeue()  → returns A. front moves to front->next = node(B).      front→B→C←back
dequeue()  → returns B. front moves to node(C). Now front==back.   front→C←back
dequeue()  → returns C. front->next is null, so front = null.
             front is now null — reset back to null too.           front=back=null (empty again)
```

**Observations — write these on the board, in plain English, before touching pseudocode:**
1. `front` and `back` are node pointers, both `null` when the queue is empty.
2. On `enqueue`: if the queue was empty, the new node becomes *both* `front` and `back`. Otherwise, link it after the current `back` and move `back` to it.
3. On `dequeue`: read `front`'s data, then move `front` to `front->next`.
4. If that move leaves `front` as `null` (the queue just emptied), reset `back` to `null` too — don't leave it dangling.

**Safe Point 2 — Approach Understanding.** *Technique: Hand-Signal Check.* "Thumbs up if you can tell me what happens to `back` on the very last `dequeue()`, when only one node was left. Thumbs down if not." Address any thumbs-down before moving on.

**Deriving the Code (~9 min)** — pseudocode, then the C++ it becomes. Derive step by step, not all at once.

**Pseudocode.** First the node and the empty case:

```
class Node: data, next

class LinkedQueue:
    front = null
    back = null
```

Then `enqueue`, referring back to Observation 2:

```
    function enqueue(x):
        node = new Node(x)
        if back == null:                # queue was empty
            front = back = node
        else:
            back.next = node
            back = node
```

Then `dequeue`, referring back to Observations 3 and 4:

```
    function dequeue():
        if front == null: error "Queue is empty"
        x = front.data
        front = front.next
        if front == null: back = null   # just removed the last node
        return x
```

**Safe Point 3 — Pseudocode Understanding.** *Technique: Deliberate Bug.* Show `dequeue` with the `if front == null: back = null` line removed, and ask: *"Is this still correct?"* Students tracking the logic should catch that `back` is left pointing at a now-conceptually-removed node — a dangling reference that will corrupt the very next `enqueue`. (This is exactly what the Engagement Activity below drills into further.)

**Hands-On Coding** — build this live, in the coding playground, straight from the pseudocode above. Do not read out a finished block. If anyone hasn't seen a `struct` with a constructor before, address that syntax gap now. Relate every line back to the pseudocode line it came from:

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

**Complexity — derive it, don't state it (~2 min).** Take a concrete case: a queue holding 4 nodes, `dequeue()` called once. There's no shifting, no scanning — reading `front->data`, moving one pointer, and (conditionally) resetting `back` is the same fixed handful of operations whether the queue holds 4 nodes or 4,000. Compare directly against last session's array version on the board: same O(1) result, but derived from *pointer reassignment* here instead of *modulo arithmetic* there — same cost, different mechanism.

**Key Takeaways** *(mandatory — matches the deck's own Key Takeaways slide, state these explicitly):*
- Nodes contain data and a pointer to the next node; the queue uses `front` and `back` pointers.
- `enqueue`: add a new node at the back, update the back pointer and link it to the new node.
- `dequeue`: remove the node at the front, update the front pointer — set both `front` and `back` to null if the queue becomes empty.
- `front`/`back` access the first and last elements directly via the pointers, no traversal needed.
- Advantage over the array version: dynamic size, no element shifting, no fixed capacity.

**Safe Point 4 — Final Check.** *Technique: Quiet-Bench Check-In.* Walk toward a less-interactive part of the room and ask, low-stakes: *"When the last element is popped, why reset both pointers, not just `front`?"* **Answer:** if only `front` is reset, `back` still points at the deleted node — a dangling pointer that corrupts the next `enqueue`.

---

## ⚡ Engagement Activity (38–43 min)

*Reuses the exact scenario from Concept Walkthrough's Safe Point 3 — no new content, so no extra time added to the session.*

**Format:** What-If / Deliberate Bug, live · **Exposes:** whether students can trace the *consequence* of a bug forward through subsequent operations, not just spot that a line is missing.

**Prompt 1 — say this, and write this exact buggy `pop()` on the board:**

```
pop() {
    if (size == 0) { print("Queue is empty"); return }
    Node* temp = front
    front = front->next
    delete temp
    size--
}
```

> *"What if I only reset `front` here, and never touch `back`? Walk me through what happens if this `pop()` empties the queue completely."*

**Expected walk-through:** `front` correctly becomes `null` (since `front->next` was `null` on the last node). But `back` is never touched — it still points at the now-deleted node. `back` is left dangling.

**Prompt 2 — the consequence, say this:**
> *"OK, the bug is there, but nothing crashed yet. What if I now call `push(x)` right after this? Does it break immediately, or does it look fine for a while?"*

**Anticipated response A (common, incomplete):** *"It would break immediately."* — Not quite. Walk through it: if `push`'s empty-check uses `size == 0` (which was correctly decremented), it takes the `front = back = newNode` branch and silently *overwrites* the dangling `back` — the bug is masked, this time.

**Anticipated response B (the real trap, ask directly if nobody raises it):** *"What if `push`'s empty-check used `back == null` instead of `size == 0`?"* Now it genuinely breaks — `back` isn't `null` (it's dangling, not null), so `push` thinks the queue isn't empty and tries `back->next = newNode` on a deleted node.

**Debrief line:**
> *"That's the trap with dangling-pointer bugs specifically — they don't always fail where they're created. This one can sit silent for an entire `push` call and only surface later, depending on which check the next function happens to use. That's exactly why we reset both pointers explicitly, every time, rather than relying on one to imply the other."*

**Cut rule:** If running short, do Prompt 1 only — spotting the missing reset is the core lesson; Prompt 2's masking behaviour is a deeper reinforcement, not new insight.

---

## Classroom Quiz (43–48 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session.

---

## Buffer (48–50 min) · Flex — not instructional, inside the 50-minute block

Unscheduled on purpose. If you land here with time on the clock, let the session end early — don't stretch content to fill it. If students have open questions, this is where they get handled.

---

## Optional Activity — Live Trace: Push and Pop by Pointer

*Not part of the core timed flow — pointer movement is already covered in Concept Walkthrough's Dry Run. Run this only if the room finishes early, or as a follow-up warm-up next session.*

**Format:** Dry-Run Relay · **Exposes:** whether students can track `front` and `back` as they move between actual nodes, on a sequence they haven't seen.

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

**Cut rule:** If running short, do just `push(A)` and the second `pop()` — one shows the empty-queue special case, the other shows the one-element state.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Only `front` needs updating when popping the last element | Pop is mentally centred on `front`, since that's the end being removed | Engagement Activity — showing `back` left dangling, and the delayed way it surfaces |
| `front == back` always means the queue is empty | Direct carryover from arrays | Dry Run's second-to-last pop — `front == back` here means exactly one node remains |
| The linked-list queue is a fundamentally different algorithm from the array queue | New pointer-based syntax looks unfamiliar | Complexity derivation — same FIFO behaviour, same O(1) result, only the mechanism changed |
| A linked-list queue can never run out of space | Technically bounded only by system memory | Brief, honest caveat: not capacity-*checked*, but not infinite either |

---
