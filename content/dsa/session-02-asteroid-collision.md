# Asteroid Collision

**Duration** 50 min total — 36 min instruction + 5 min Classroom Quiz + 9 min buffer · **Topic** Stack — Asteroid Collision Simulation · **Prerequisite** Balanced Parenthesis
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the collision rules: smaller asteroid destroyed, equal-size asteroids both destroyed, same-direction asteroids never collide. *(REMEMBERING)*
2. Explain why a stack models this problem naturally — the most recently surviving asteroid is exactly what a new left-moving asteroid must be compared against first. *(UNDERSTANDING)*
3. Distinguish the three "no collision" cases (same direction, moving apart, one already destroyed) from the two collision-resolution cases. *(ANALYZING)*
4. Trace the stack-based simulation on a given array, including a case where one incoming asteroid destroys more than one stack element in a row. *(APPLYING)*

---

## Warm-Up Poll — Retrieval Practice on Balanced Parenthesis (0–6 min) · ALS: Polling

5 questions on **Balanced Parenthesis**. ~45 s each, project the distribution, never name individuals.

**Q1.** A closing bracket arrives and the stack is empty. The string is:
`A` Automatically valid · `B` Invalid · `C` Valid if it's the last character · `D` Undetermined
→ **B.**

**Q2.** After scanning the entire string, if the stack is *not* empty, the string is:
`A` Valid · `B` Invalid · `C` Depends on how many are left · `D` Undetermined
→ **B.**

**Q3.** Why isn't counting brackets of each type enough to check validity?
`A` It is enough · `B` Equal counts don't guarantee correct order or matching types · `C` Counting is too slow · `D` Some brackets don't have pairs
→ **B.**

**Q4.** What's the time and space complexity of the balanced-parenthesis check?
`A` O(N) time, O(N) space · `B` O(N²) time, O(1) space · `C` O(1) time, O(N) space · `D` O(N log N) time, O(N) space
→ **A.**

---

## Hook (6–9 min)

Write this on the board: `[5, 10, -10, -5]` (positive = moving right, negative = moving left).

Ask: *"Picture these as literally asteroids in a straight line in space, each moving at the same speed in the direction its sign shows. Which two are ever going to meet?"*

Let students reason: `10` (moving right) and `-10` (moving left) are heading toward each other.

> *"When they meet, one of two things happens: the bigger one survives and the smaller one is destroyed, or if they're exactly equal, both are destroyed. Same-direction asteroids never catch each other. Today we simulate an entire line of these collisions, and a stack is exactly the right tool: the only asteroid a new left-mover can hit is whichever one most recently survived and is still in front of it."*

---

## Problem Statement (9–13 min)

*(Deck: Slides 4–7 — problem definition; Slides 8–29 carry the deck's own animated examples, which overlap with the Dry Run below)*

Given an array of integers `asteroids`, each entry's absolute value is its size and its sign is its direction — positive moves right, negative moves left, all at the same speed. Simulate every collision and return the asteroids that remain.

**Input:** an array of non-zero integers `asteroids`.
**Output:** an array of integers — the surviving asteroids, left to right, after all collisions resolve.

Two asteroids collide only if a right-mover is followed by a left-mover converging on it. The smaller one explodes; if they're exactly equal, both explode. Same-direction asteroids never meet.

**Example 1**
Input: `asteroids = [5, 10, -5]`
Output: `[5, 10]`
Why: `5` and `10` both move right, no collision between them. `-5` then collides with `10` — `10` survives, `-5` explodes.

**Example 2**
Input: `asteroids = [8, -8]`
Output: `[]`
Why: equal magnitude, opposite directions — both explode, nothing survives.

---

## Concept Walkthrough (13–29 min)

*(Deck: Approach Slides 30–31 · Dry Run Slides 32–61 (also Slides 8–29 for the two dry-run examples) · Pseudocode Slides 62–63 · Complexity Slides 64–66 · C++ Code Slides 67–68 · Key Takeaways Slides 69–70 — deck continues to Slide 106 with bonus/alternate practice examples, not needed for this script)*

**Core idea:** keep a stack of surviving asteroids. Push positives (moving right) directly. For a negative (moving left) asteroid, keep colliding it against the stack's top — in a `while`, not an `if` — popping any smaller positive, until it either meets something bigger/equal or the stack empties.

**Dry Run** — `[7, 5, 4, -5, -6, -8, -9, 12]`. Show the status of the stack after every update:

```
7   → moving right → push                              Stack: 7
5   → moving right, same direction → push               Stack: 7, 5
4   → moving right, same direction → push               Stack: 7, 5, 4
-5  → top 4: |4|<|-5| → 4 explodes
      new top 5: |5|=|-5| → both explode                Stack: 7
-6  → top 7: |7|>|-6| → 7 survives, -6 explodes          Stack: 7
-8  → top 7: |7|<|-8| → 7 explodes, stack empty → push   Stack: -8
-9  → moving left, same direction as top → push          Stack: -8, -9
12  → moving right, top -9 moving left → moving apart → push   Stack: -8, -9, 12
```

Final: `-8, -9, 12`.

**Pseudocode** — derived from the core idea:

```
function collide(asteroids):
    stack = empty stack
    for each a in asteroids:
        alive = true
        while alive and a < 0 and stack not empty and top(stack) > 0:
            if top(stack) < -a:
                pop stack                  # top explodes, a keeps moving
            else if top(stack) == -a:
                pop stack                  # both explode
                alive = false
            else:
                alive = false              # a explodes, top survives
        if alive:
            push a onto stack
    return stack, bottom to top
```

**Deriving the code** — build this live in the coding playground, straight from the pseudocode above; don't just read out a finished block:

```cpp
vector<int> asteroidCollision(vector<int>& asteroids) {
    vector<int> st;   // used as a stack
    for (int a : asteroids) {
        bool alive = true;
        while (alive && a < 0 && !st.empty() && st.back() > 0) {
            if (st.back() < -a) {
                st.pop_back();            // top explodes, a survives, keeps checking
            } else if (st.back() == -a) {
                st.pop_back();            // both explode
                alive = false;
            } else {
                alive = false;            // a explodes, top survives
            }
        }
        if (alive) st.push_back(a);
    }
    return st;
}
```

Each asteroid is pushed once and popped at most once — O(N) time, O(N) space.

**Key Takeaways** *(mandatory — matches the deck's own Key Takeaways slides, state these explicitly before moving on):*
- Use a stack to handle collisions as asteroids move in opposite directions.
- Positive asteroids (moving right) are pushed to the stack; negative ones may cause collisions.
- When a collision occurs, the smaller asteroid explodes — or both explode if they're equal.
- Continue processing until all collisions are resolved; the stack's remaining elements are the final state.
- Overall complexity: O(N) time, O(N) space.

**Checkpoint:**
> *"When `-9` arrives and the stack top is `-8`, why is there no collision?"*
> **Answer:** Both are moving left — same-direction asteroids never collide, regardless of size.

---

## ⚡ Active Learning Strategy — Spot the Bug: Collide or Not? (29–36 min)

**ALS format:** Spot the Bug / Predict-the-Output — exposes whether students can correctly classify each pairwise interaction into "collide" vs. "no collision," and if colliding, resolve the outcome — the single skill the whole algorithm depends on.

**Setup line:**
> *"Four pairs of asteroids about to meet or not meet. For each: do they collide? If yes, what survives?"*

```
1.  Stack top = 6,  incoming = -6
2.  Stack top = -3, incoming = -9
3.  Stack top = 4,  incoming = 9    (incoming is positive)
4.  Stack top = -2, incoming = 8
```

45 seconds silent, then hands up. Take one pair per student.

**Answers**

| # | Collide? | Outcome |
|---|---|---|
| 1 | Yes | Equal magnitude, opposite directions → both explode |
| 2 | No | Both negative (same direction, moving left) → no collision, both survive, `-9` pushed on top |
| 3 | No | Incoming is positive (moving right) → same direction as everything already on the stack moving right → no collision, `9` just pushed |
| 4 | No | Top is negative (already moving left), incoming is positive (moving right) — they're moving *apart*, not toward each other |

**How it surfaces:** Pair 4 is the trap — students will often assume "opposite signs always means collide," but a `-2` sitting on the stack is already moving *left*, and an `8` arriving after it is moving *right*: they're moving apart, not toward each other. Only a *positive* on the stack (moving right, "waiting") followed by a *negative* incoming (moving left, "approaching") is a real collision setup.

**Debrief line:**
> *"Opposite signs are necessary but not sufficient. The one collision shape that matters is: something on the stack moving right, and something new arriving moving left — anything else is either same-direction or already moving apart."*

**Cut rule:** Do pairs 1 and 4 only — pair 1 is the clean collision case, pair 4 is the trap that catches almost everyone.

---

## Classroom Quiz (36–41 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block, covering the collision rules and the moving-apart trap case.

---

## Buffer (41–50 min) · Flex — not instructional

Unscheduled on purpose. If you land here with time on the clock, let the session end early — don't stretch content to fill it.

---

## Optional Activity — Dry-Run Relay

*Not part of the core timed flow — Concept Walkthrough's Dry Run already traces the stack step by step. Run this only if the room finishes early, or as a follow-up warm-up next session.*

**ALS format:** Dry-Run Relay — exposes whether students can execute a multi-step collision chain themselves, including a case where one incoming asteroid destroys more than one stack element in a row. "While, not if" is the last mechanical detail students need before they can implement this alone.

**Setup line:**
> *"New array: `[6, 3, -8, 2]`. Walk it with me, one element at a time — tell me what's pushed, what collides, and what survives, before I confirm."*

Run **one element at a time**:

```
6   → stack empty → push.                                  Stack: 6
3   → 3 moving right, same direction as top → push.         Stack: 6, 3
-8  → collides with top 3: |3| < |-8| → 3 explodes.
      collides with new top 6: |6| < |-8| → 6 explodes.
      Stack now empty → push -8.                            Stack: -8
2   → 2 moving right, top is -8 moving left → moving apart, no collision → push.   Stack: -8, 2
```

Final stack: `-8, 2`.

**How it surfaces:** At `-8`, ask before revealing each step: *"Does it stop after destroying `3`, or keep going?"* Correct: it keeps going — `-8` is not yet resolved, so it must keep checking the new top (`6`) until either something bigger stops it or the stack empties.

**Debrief line:**
> *"One incoming asteroid destroyed two stack elements in a row, in a single step of the outer loop — that's the `while`, not `if`, doing its job. It only stops early if it meets something bigger than itself, or something moving the same direction."*

**Cut rule:** Do only the `-8` step — it's the one that carries the whole "keep colliding until stopped" lesson; `6`, `3`, and `2` are all simple pushes.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Equal-magnitude collisions leave one survivor | Most collision intuitions expect a "winner" | Equal magnitude means **both** are destroyed — no winner |
| Same-direction asteroids can still collide if one is "catching up" | Easy to skim past "same speed" in the problem statement | Restate: identical speed means same-direction asteroids maintain constant distance forever |
| Opposite signs always means a collision | Feels like the obvious reading of "moving toward each other" | ALS 1's trap pair — a stack-top negative and an incoming positive are moving *apart* |
| An incoming asteroid only ever resolves one collision before being pushed | Underestimating pop loops generally | ALS 2's multi-destroy step — one incoming element can destroy two stack elements via a `while`, not an `if` |

---
