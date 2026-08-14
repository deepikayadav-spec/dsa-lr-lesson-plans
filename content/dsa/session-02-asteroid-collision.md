# Asteroid Collision

**Duration** 46 min total — 39 min instruction + 7 min Classroom Quiz · **Topic** Stack — Asteroid Collision Simulation · **Prerequisite** Balanced Parenthesis
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

## Hook (6–10 min)

Write this on the board: `[5, 10, -10, -5]` (positive = moving right, negative = moving left).

Ask: *"Picture these as literally asteroids in a straight line in space, each moving at the same speed in the direction its sign shows. Which two are ever going to meet?"*

Let students reason: `10` (moving right) and `-10` (moving left) are heading toward each other.

> *"When they meet, one of two things happens: the bigger one survives and the smaller one is destroyed, or if they're exactly equal, both are destroyed. Same-direction asteroids never catch each other. Today we simulate an entire line of these collisions, and a stack is exactly the right tool: the only asteroid a new left-mover can hit is whichever one most recently survived and is still in front of it."*

---

## Concept Walkthrough (10–25 min)

**Core idea:** keep a stack of surviving asteroids. Push positives (moving right) directly. For a negative (moving left) asteroid, keep colliding it against the stack's top — in a `while`, not an `if` — popping any smaller positive, until it either meets something bigger/equal or the stack empties.

**Worked example** — `[7, 5, 4, -5, -6, -8, -9, 12]`: `7, 5, 4` all push. `-5` collides with `4` (explodes), then `5` (equal — both explode). `-6` collides with `7` (`7` survives, `-6` explodes). `-8` collides with `7` (`7` explodes, stack empty, push `-8`). `-9` — same direction as `-8` — push. `12` — moving apart from `-9` — push. Final: `[-8, -9, 12]`.

**Checkpoint:**
> *"When `-9` arrives and the stack top is `-8`, why is there no collision?"*
> **Answer:** Both are moving left — same-direction asteroids never collide, regardless of size.

---

## ⚡ Active Learning Strategy 1 — Spot the Bug: Collide or Not? (25–32 min)

Four stack-top/incoming pairs; students classify collide vs. no-collision and, if colliding, the outcome. Exposes the "opposite signs always means collision" trap — a negative already on the stack (moving left) followed by a positive arriving (moving right) are moving *apart*, not colliding.

---

## ⚡ Active Learning Strategy 2 — Live Coding / Dry-Run Relay (32–39 min)

A fresh array (`[6, 3, -8, 2]`), walked one element at a time, students predicting each push/collision before it's confirmed. Exposes whether students grasp "while, not if" — one incoming asteroid can destroy more than one stack element in a row.

---

## Classroom Quiz (39–46 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block, covering the collision rules and the moving-apart trap case.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Equal-magnitude collisions leave one survivor | Most collision intuitions expect a "winner" | Equal magnitude means **both** are destroyed — no winner |
| Same-direction asteroids can still collide if one is "catching up" | Easy to skim past "same speed" in the problem statement | Restate: identical speed means same-direction asteroids maintain constant distance forever |
| Opposite signs always means a collision | Feels like the obvious reading of "moving toward each other" | ALS 1's trap pair — a stack-top negative and an incoming positive are moving *apart* |
| An incoming asteroid only ever resolves one collision before being pushed | Underestimating pop loops generally | ALS 2's multi-destroy step — one incoming element can destroy two stack elements via a `while`, not an `if` |

---
