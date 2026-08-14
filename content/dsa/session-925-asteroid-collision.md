# Session 925 — Asteroid Collision

**Duration** 43 min total — 38 min instruction + 5 min Classroom Quiz (cap: 45 + 5, not more) · **Topic** Stack — Asteroid Collision Simulation · **Prerequisite** Session 924 — Balanced Parenthesis
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the collision rules: smaller asteroid destroyed, equal-size asteroids both destroyed, same-direction asteroids never collide. *(REMEMBERING)*
2. Explain why a stack models this problem naturally — the most recently surviving asteroid is exactly what a new left-moving asteroid must be compared against first. *(UNDERSTANDING)*
3. Distinguish the three "no collision" cases (same direction, moving apart, one already destroyed) from the two collision-resolution cases. *(ANALYZING)*
4. Trace the stack-based simulation on a given array, including a case where one incoming asteroid destroys more than one stack element in a row. *(APPLYING)*

---

## Warm-Up Poll — Retrieval Practice on Session 924 (0–4 min) · ALS: Polling

5 questions on **Session 924 (Balanced Parenthesis)**. ~45 s each, project the distribution, never name individuals.

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

**Q5.** *(MSQ — select all that apply)* True failure modes for bracket validation?
`A` Closing bracket with an empty stack · `B` Closing bracket that doesn't match the top · `C` Leftover unclosed brackets at the end · `D` Too many total characters
→ **A, B, C.**

---

## Hook (4–7 min)

Write this on the board: `[5, 10, -10, -5]` (positive = moving right, negative = moving left).

Ask: *"Picture these as literally asteroids in a straight line in space, each moving at the same speed in the direction its sign shows. Which two are ever going to meet?"*

Let students reason: `10` (moving right) and `-10` (moving left) are heading toward each other.

> *"When they meet, one of two things happens: the bigger one survives and the smaller one is destroyed, or if they're exactly equal, both are destroyed. Same-direction asteroids never catch each other. Today we simulate an entire line of these collisions, and a stack is exactly the right tool: the only asteroid a new left-mover can hit is whichever one most recently survived and is still in front of it."*

---

## Slide Block A (7–14 min) — DELIVER SLIDES AS-IS

Covers: Problem Statement (array of integers — size is magnitude, sign is direction; same speed; collisions destroy the smaller, or both if equal; same-direction asteroids never collide) → Example 1 (`[4, 8, -3, 9, 7, -8]` → `[4, 8, 9]`) → Example 2 (`[20, 5, 10, -10, -20]` → `[]`).

**Beats to emphasise**

- Walk Example 1's chain: `8` and `-3` collide → `-3` explodes. `7` and `-8` collide → `7` explodes. `9` and `-8` collide → `-8` explodes. Final: `[4, 8, 9]`.
- **Say explicitly why Example 2 ends empty:** every remaining pair keeps colliding until the last two (`20`, `-20`) are exactly equal — both explode.
- Name the three "nothing happens" cases: same direction, moving apart, and "already resolved."

**Checkpoint (at 14 min)** — cold-call:
> *"In Example 1, why doesn't `4` ever collide with anything?"*
> **Answer:** `4` is moving right, and every surviving asteroid to its right is also eventually moving right (or already destroyed) — they're moving apart or same-direction.

---

## Slide Block B (14–21 min) — DELIVER SLIDES AS-IS

Covers: Approach (stack of survivors; push positives directly; for negatives, resolve collisions against the stack top before deciding whether to push) → full dry run on `[7, 5, 4, -5, -6, -8, -9, 12]` → pseudocode (`while`-loop collision resolution) → complexity (O(N) time, O(N) space).

**Beats to emphasise**

- Narrate the dry run's collision chain: `7, 5, 4` push. `-5` collides with `4` (explodes), then `5` (equal — both explode). `-6` collides with `7` (`7` survives, `-6` explodes). `-8` collides with `7` (`7` explodes, stack empty, push `-8`). `-9` — same direction as `-8` — push. `12` — moving apart from `-9` — push. Final: `[-8, -9, 12]`.
- Point at the `while` loop explicitly: an incoming negative doesn't check the stack top once — it keeps colliding and popping as long as the top is positive and smaller.

**Checkpoint (at 21 min)** — cold-call:
> *"When `-9` arrives and the stack top is `-8`, why is there no collision?"*
> **Answer:** Both are moving left — same-direction asteroids never collide, regardless of size.

---

## ⚡ Active Learning Strategy 1 — Spot the Bug: Collide or Not? (21–27 min)

Four stack-top/incoming pairs; students classify collide vs. no-collision and, if colliding, the outcome. Exposes the "opposite signs always means collision" trap — a negative already on the stack (moving left) followed by a positive arriving (moving right) are moving *apart*, not colliding.

---

## ⚡ Active Learning Strategy 2 — Live Coding / Dry-Run Relay (27–33 min)

A fresh array (`[6, 3, -8, 2]`), walked one element at a time, students predicting each push/collision before it's confirmed. Exposes whether students grasp "while, not if" — one incoming asteroid can destroy more than one stack element in a row.

---

## Classroom Quiz (33–38 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block, covering the collision rules and the moving-apart trap case.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Equal-magnitude collisions leave one survivor | Most collision intuitions expect a "winner" | Slide Block B's dry run — equal magnitude means **both** are destroyed |
| Same-direction asteroids can still collide if one is "catching up" | Easy to skim past "same speed" in the problem statement | Restate: identical speed means same-direction asteroids maintain constant distance forever |
| Opposite signs always means a collision | Feels like the obvious reading of "moving toward each other" | ALS 1's trap pair — a stack-top negative and an incoming positive are moving *apart* |
| An incoming asteroid only ever resolves one collision before being pushed | Underestimating pop loops generally | ALS 2's multi-destroy step — one incoming element can destroy two stack elements via a `while`, not an `if` |

---

## Instructor Notes

- **43-min format: 38 min instruction + 5 min Classroom Quiz, capped at 45 + 5.** Active learning strategies are referenced by name and format only.
- **The Classroom Quiz runs last**, as the sole closing activity — no separate exit ticket or homework block.
- **ALS 1's trap pair is the single most important few minutes of this session.** Almost every student will initially say "opposite signs, must collide" — do not rush past the correction.
- **Bridge to the next session:** Largest Rectangle in Histogram uses a monotonic stack again, in yet another physical framing — make the recurring pattern explicit.
