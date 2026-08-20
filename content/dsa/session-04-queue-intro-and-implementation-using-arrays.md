# Introduction to Queue & Implementation Using Arrays

**Duration** 50 min total — 43 min instruction + 5 min Classroom Quiz + 2 min buffer (buffer is inside the 50, not extra) · **Topic** Queue — Introduction and Array Implementation · **Prerequisite** Largest Rectangle in Histogram
**Session type** Concept lecture · **Format** Class Delivery Framework — Safe Points, dry run → observations → pseudocode → code, engagement activity reuses the session's own example

---

## Learning Objectives

By the end of this session, students will be able to:

1. Define a queue as a First-In-First-Out (FIFO) data structure, contrasting it explicitly with a stack's LIFO behaviour. *(REMEMBERING)*
2. Explain why an array-based queue needs both a `front` and a `back` pointer, rather than just one, and why naive shifting on every `pop` would be wasteful. *(UNDERSTANDING)*
3. Trace `push` and `pop` operations on a fixed-size circular array, including the modulo wraparound that reuses freed slots. *(APPLYING)*
4. Identify the queue's fixed-capacity limitation and explain why that motivates a linked-list-based implementation, covered next session. *(ANALYZING)*

---

## Warm-Up Poll — Recap of Previous Session (0–5 min)

Live poll (Mentimeter or similar) on **Largest Rectangle in Histogram**. **Don't summarize LRH yourself first** — run the poll cold, then read the aggregate result out loud as the recap. The numbers *are* the recap; you're not re-teaching it.

**Q1.** A rectangle anchored at a given bar's height can extend as far as:
`A` The edges of the array, always · `B` The nearest shorter bar on each side · `C` The nearest taller bar on each side · `D` Exactly one bar in each direction
→ **B.**

**Q2.** In the one-pass optimal approach, a bar's area is computed:
`A` At the very start · `B` At the very end, for all bars at once · `C` The moment it's popped from the stack · `D` Only if it's the tallest bar
→ **C.**

**Q3.** If the stack empties during a pop in the one-pass approach, the rectangle's width is:
`A` Zero · `B` Undefined · `C` The current index · `D` Always 1
→ **C.**

**Q4.** Overall time complexity of the one-pass approach:
`A` O(1) · `B` O(N) · `C` O(N²) · `D` O(N log N)
→ **B.**

Say: *"Alright — [X]% got two or more of these. Let's leave stacks behind for a session and meet an entirely new structure."*

---

## Hook (5–8 min)

State the topic explicitly, then motivate it: *"Today we're learning Queue — a new linear data structure. Everything you've built this block — Balanced Parenthesis, Asteroid Collision, Largest Rectangle — used a stack. Today that changes."*

Ask: *"You're standing in a line at a ticket counter. Who gets served first — the person who joined the line first, or the person standing closest to the counter right now?"*

Let students answer (first joined). Then name the advantage explicitly:

> *"That's a queue. Whoever arrived first leaves first — First In, First Out, FIFO. It's the exact opposite discipline from every stack you've built so far. The advantage: anything that has to be processed fairly, in arrival order — a print queue, a support ticket queue, a task scheduler — needs exactly this. Today we build it from scratch, starting with the simplest possible version: a plain array."*

---

## Problem Statement (8–12 min)

*(Deck: Slides 4–6 — problem definition + example diagram)*

Design a queue backed by a fixed-size array, supporting FIFO insertion and removal.

**Input:** a fixed capacity, then a sequence of operations — `enqueue(x)`, `dequeue()`, `front()`.
**Output:** for each `dequeue()`/`front()` call, the value returned (or an explicit error if the queue is empty/full).

**Example 1**
Input: capacity 3 → `enqueue(1)`, `enqueue(2)`, `front()`, `dequeue()`, `front()`
Output: `front() = 1`, `dequeue() = 1`, `front() = 2`
Why: whatever was added first (`1`) is always the one at the front until it's removed.

**Example 2**
Input: capacity 2 → `enqueue(1)`, `enqueue(2)`, `enqueue(3)`
Output: `enqueue(3)` fails — `"Queue is full"`
Why: a fixed-capacity array queue has a hard ceiling — no room for a third element until one is dequeued.

**Safe Point 1 — Problem Statement Clarity.** *Technique: Predict-the-Output, on a new input.* Write a third sequence on the board — one they haven't seen: capacity `3` → `enqueue(4)`, `enqueue(5)`, `dequeue()`, `enqueue(6)`, `front()`. Ask: *"What does `front()` return here, and why?"*

**What to listen for:** the correct answer is `5` — `4` was removed first, so `5` is next in line; `6` just joined the back. The common wrong answer is `6` — the *most recently added* element, which is LIFO thinking left over from every stack session this block. If the room lands on `6`, don't correct it yet — just note it out loud: *"Hold that thought — that's stack thinking, and today is the one day it doesn't apply."*

---

## Concept Walkthrough (12–38 min)

*(Deck: Setup Slides 7–8 · Dry Run Slides 9–29 · Pseudocode Slides 30–35 · Complexity Slide 38 · C++ Code Slides 39–45 · Key Takeaways Slides 52–53)*

**Approach Exploration (~2 min).** Before revealing the design, ask: *"We need FIFO behaviour out of a plain array — no built-in queue type. What would you try first?"* Let 2–3 guesses land. The common one: "keep everything at the front, shift left on every pop." Don't shoot it down yet — bank it, and come back to it during Deriving the Code's complexity discussion. Then give the brief, one-line version of the actual approach, not the full mechanism: *"We're going to track two positions instead of shifting anything — where the next removal happens, and where the next addition happens."*

**Dry Run (~6 min).** Before running anything, name the variables on the board:
- **`front`** — index of the next slot to remove from.
- **`back`** — index of the last slot filled.
- **The array** — fixed size (`capacity`), slots reused via wraparound rather than grown.

Capacity-5 array, empty to start. Track `front` and `back` explicitly at every step, and choose the example so it actually triggers the wraparound edge case — don't stop before that:

```
front = back = -1 (empty)

enqueue(1) → front was -1, so front becomes 0. back = 0.        arr: [1, _, _, _, _]  front=0 back=0
enqueue(2) → back = 1.                                          arr: [1, 2, _, _, _]  front=0 back=1
enqueue(3) → back = 2.                                          arr: [1, 2, 3, _, _]  front=0 back=2
enqueue(4) → back = 3.                                          arr: [1, 2, 3, 4, _]  front=0 back=3
dequeue()  → returns 1. front = 1.                               arr: [1, 2, 3, 4, _]  front=1 back=3
dequeue()  → returns 2. front = 2.                               arr: [1, 2, 3, 4, _]  front=2 back=3
enqueue(5) → back = 4 (still in bounds).                         arr: [1, 2, 3, 4, 5]  front=2 back=4
enqueue(6) → back would be 5 — off the end. But front=2, so
             slots 0 and 1 are free. back wraps: (4+1)%5 = 0.    arr: [6, 2, 3, 4, 5]  front=2 back=0
```

**Observations — write these on the board, in plain English, before touching pseudocode:**
1. Two pointers: `front` (next slot to remove from) and `back` (last slot filled).
2. On `enqueue`: move `back` forward one slot — wrapping to `0` if it runs past the end — and write the value there.
3. On `dequeue`: read the value at `front`, then move `front` forward one slot — wrapping the same way.
4. If `back` would run past the array's end but `front` has moved forward (freeing slots behind it), wrap instead of reporting full.

**Safe Point 2 — Approach Understanding.** *Technique: Hand-Signal Check.* "Thumbs up if you can tell me what `back` becomes when it's at the last index and slot 0 is free. Thumbs down if not." Address any thumbs-down before moving on — don't take silence as agreement.

**Deriving the Code (~9 min)** — pseudocode, then the C++ it becomes. Derive step by step, not all at once.

**Pseudocode.** First just the state and the empty/full checks:

```
class ArrayQueue:
    array[capacity]
    front = -1
    back = -1

    function isEmpty(): return front == -1
    function isFull():  return (back + 1) % capacity == front
```

Then `enqueue`, referring back to Observation 2:

```
    function enqueue(x):
        if isFull(): error "Queue is full"
        if isEmpty(): front = 0
        back = (back + 1) % capacity
        array[back] = x
```

Then `dequeue`, referring back to Observation 3:

```
    function dequeue():
        if isEmpty(): error "Queue is empty"
        x = array[front]
        if front == back: front = back = -1     # queue just emptied
        else: front = (front + 1) % capacity
        return x
```

**Safe Point 3 — Pseudocode Understanding.** *Technique: Deliberate Bug.* Show `enqueue` with the `if isEmpty(): front = 0` line removed, and ask: *"Is this still correct?"* Students tracking the logic will catch that a fresh queue would leave `front` stuck at `-1` forever, even after elements are pushed. Students who accept it uncritically are the ones to check in with individually.

**Hands-On Coding** — build this live, in the coding playground, straight from the pseudocode above. Do not read out a finished block. If anyone hasn't seen a `vector<int>` constructed with a fixed size before, address that syntax gap now, before it surfaces mid-derivation. Relate every line back to the pseudocode line it came from as you type it:

```cpp
class ArrayQueue {
    vector<int> arr;
    int capacity, front, back;
public:
    ArrayQueue(int cap) : arr(cap), capacity(cap), front(-1), back(-1) {}

    bool isEmpty() { return front == -1; }
    bool isFull()  { return (back + 1) % capacity == front; }

    void enqueue(int x) {
        if (isFull()) throw runtime_error("Queue is full");
        if (isEmpty()) front = 0;
        back = (back + 1) % capacity;
        arr[back] = x;
    }

    int dequeue() {
        if (isEmpty()) throw runtime_error("Queue is empty");
        int x = arr[front];
        if (front == back) front = back = -1;    // queue just emptied
        else front = (front + 1) % capacity;
        return x;
    }
};
```

**Complexity — derive it, don't state it (~2 min).** Go back to the shifting idea from Approach Exploration. Take a concrete case: a queue holding 4 elements, `dequeue()` called once.
- **Shifting approach:** remove index 0, then move every remaining element one slot left — 3 moves for 4 elements. With `n` elements, that's `n − 1` moves, every single time. That's O(N) per operation.
- **This approach:** one comparison (`isEmpty`), one pointer read, one pointer update — **3 operations**, regardless of whether the queue holds 4 elements or 4,000. That's what O(1) means: work that doesn't grow with `n`. Compare the two side by side on the board — the shifting approach's cost was the thing this design was built to avoid.

**Key Takeaways** *(mandatory — matches the deck's own Key Takeaways slides, state these explicitly):*
- Queue: a data structure following the First-In-First-Out (FIFO) principle.
- `enqueue()` adds an element to the rear; `dequeue()` removes an element from the front.
- `front()` retrieves the front element without removing it; `back()` retrieves the rear element without removing it.
- `empty()` checks if the queue is empty; `full()` checks if the queue is full.

**Safe Point 4 — Final Check.** *Technique: Quiet-Bench Check-In.* Walk toward a less-interactive part of the room and ask, low-stakes: *"Why does a queue need two pointers when a stack only needed one?"* **Answer:** a queue adds at one end and removes from the other; a stack does both at the same end.

---

## ⚡ Engagement Activity — What-If Discussion (38–43 min)

*Reuses the exact example from the Dry Run above — no new content, so no extra time added to the session.*

**Format:** What-If Discussion · **Exposes:** whether students actually understood *why* two pointers + wraparound beats the shifting approach they proposed earlier, not just whether they can recite the mechanism.

**Prompt 1 — say this:**
> *"Back in Approach Exploration, someone suggested shifting every element left on every pop instead of using `back` and wraparound. What if we'd actually built it that way — would it still be a correct queue?"*

**Anticipated response A (common, partially right):** *"Yes, it would still work."* — **Correct.** Push back: *"Right, it's correct. Now — this queue has 10,000 elements and I call `dequeue()` once. What did that single call just cost us?"* Steer toward: 9,999 shifts, every time, regardless of how the wraparound version would've handled it in 3 operations.

**Anticipated response B (common, off-target):** *"No, because you need `back` to know where to add."* — Validate the true part, then redirect: *"You're right that you need to know where to add — but you could always add right after the last used slot, no `back` pointer required for that. That's not the real problem with shifting. What actually costs you?"* Steer back toward Response A's cost analysis.

**Prompt 2 — say this:**
> *"What if a student builds this queue with capacity 1? Walk me through it: `enqueue(x)` — full or not? Then `dequeue()` — what do `front` and `back` become?"*

**Expected walk-through:** `enqueue(x)` — queue was empty, `front = 0`, `back = (−1+1)%1 = 0`. `isFull()` is now true (`(back+1)%capacity == front` → `(0+1)%1=0==front`). `dequeue()` — reads `arr[0]`, then since `front == back`, both reset to `-1`. This is the smallest possible case that still exercises every branch of the design — if students can walk it cleanly, the mechanism has landed.

**Debrief line:**
> *"Both what-ifs point at the same thing: the two-pointer design isn't just 'a way' to build a queue — every piece of it (the wraparound, the `front == back` reset) exists specifically to avoid the cost of shifting. Next session, we drop the array entirely and see what a linked-list version buys us instead."*

**Cut rule:** If running short, do Prompt 1 only — it's the one that directly tests the session's central trade-off; Prompt 2 is a reinforcement of the mechanism, not new insight.

---

## Classroom Quiz (43–48 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session.

---

## Buffer (48–50 min) · Flex — not instructional, inside the 50-minute block

Unscheduled on purpose. If you land here with time on the clock, let the session end early — don't stretch content to fill it. If students have open questions, this is where they get handled.

---

## Optional Activity — Predict the Output: Trace the Circular Wraparound

*Not part of the core timed flow — the wraparound mechanic is already covered in Concept Walkthrough's Dry Run. Run this only if the room finishes early, or as a follow-up warm-up next session.*

**Format:** Predict-the-Output / Live Trace · **Exposes:** whether students can track `front`, `back`, and `size` through a full wraparound cycle themselves, on a sequence they haven't seen.

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

**Cut rule:** If running short, do only the `push(D)` and `push(E)` steps — the wraparound is the entire point.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| `pop()` physically removes/clears the array slot | Mental model of arrays as "boxes that empty out" | Dry Run — showing earlier elements still physically present after their pops, simply unreachable |
| `front == back` always means the queue is empty | Natural first guess, carried over from single-pointer emptiness checks | Deriving the Code's `isEmpty`/reset logic — distinguishing the `-1, -1` sentinel from `front == back` at a real index |
| Once `back` reaches the last index, the queue is full, permanently | Feels like running off the end of an array is a hard stop | The Dry Run's wraparound step — `back` reuses freed slots via modulo |
| Shifting elements left on every pop is a reasonable way to build this | It's the first thing that comes to mind, and it *is* correct | Engagement Activity Prompt 1 — same correctness, but O(N) vs O(1) per operation |
| A circular array queue can grow without limit | Confusing this session's fixed-capacity array with next session's linked-list version | This implementation has a **fixed** capacity — say so explicitly |

---
