# Session 58 — Largest Rectangle in Histogram

**Duration** 42 min total — 37 min instruction + 5 min Classroom Quiz · **Topic** Stack — Largest Rectangle in Histogram (NSE/PSE two-pass approach + optimal one-pass approach) · **Prerequisite** Session 925 — Asteroid Collision
**Session type** Concept lecture · **Format** Condensed — merged from a previous two-part (35 + 30 min) split into a single 45+5-capped session; active learning strategies referenced by name, single closing quiz

<!-- Merge note: previously split as session-58a (Part 1, NSE/PSE approach, 35 min) and session-58b (Part 2, optimal one-pass approach, 30 min), 65 min combined. The image's schedule shows this as one topic occupying one slot per batch, so both parts are merged back into a single session and trimmed to fit the 45+5 cap. Both approaches are kept — the two-pass approach because Part 1's instructor notes were explicit that skipping it undercuts why the one-pass approach is a genuine simplification, not a random trick. -->

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the problem: given bar heights of width 1, find the largest rectangular area that fits within the histogram's outline. *(REMEMBERING)*
2. Explain why a rectangle anchored at a given bar's height can only extend as far as the nearest shorter bar on each side. *(UNDERSTANDING)*
3. Compute Next Smaller Element (NSE) and Previous Smaller Element (PSE) using a monotonic stack, and use them to calculate a bar's maximum rectangle area. *(APPLYING)*
4. Trace the optimal one-pass approach, where a single stack replaces the two separate NSE/PSE passes, and explain why the result is identical. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Session 925 (0–5 min)

Say: *"Five quick ones on asteroid collisions before we hit the hardest problem in this block."*

**Q1.** Two asteroids of equal magnitude, moving toward each other:
`A` The larger one survives · `B` Both are destroyed · `C` Neither is affected · `D` They pass through each other
→ **B.**

**Q2.** In the stack-based simulation, when a negative (left-moving) asteroid arrives, it's compared against:
`A` Every element in the array · `B` The stack top, repeatedly, until stopped or the stack empties · `C` Only the first element pushed · `D` Nothing — it's always pushed directly
→ **B.**

**Q3.** What is the overall time complexity of the stack-based asteroid simulation?
`A` O(1) · `B` O(N) · `C` O(N²) · `D` O(N log N)
→ **B.**

**Q4.** A positive (right-moving) asteroid meeting a negative already on the stack that's also moving left:
`A` Collides — opposite signs · `B` Doesn't collide — they're moving apart · `C` Always destroys the negative one · `D` Is an invalid input
→ **B.**

---

## Hook (5–8 min)

Draw a rough skyline on the board — bars of heights `2, 1, 5, 6, 2, 3` sitting side by side, each width 1.

Ask: *"Somewhere in this skyline is the single largest rectangle that fits entirely under the outline. Just eyeball it — where do you think it is, and how big?"*

Let a few guesses land (actual answer: height 5, width 2, area 10 — bars at height 5 and 6). Then:

> *"You just did that by squinting at the whole picture at once. A computer needs a rule. It turns out to depend on something you already know how to compute: for every bar, how far can a rectangle at *that bar's height* stretch left and right before it hits something shorter? That's Previous Smaller Element and Next Smaller Element — the same monotonic stack idea, run twice."*

---

## ⚡ Active Learning Strategy — Live Coding / Dry-Run Relay (33–37 min)

A fresh, smaller array traced twice by the class — once for NSE only (right to left), once for the one-pass area computation (left to right), students predicting each pop/area before it's confirmed. Exposes whether students can run both the two-pass mechanics and the optimal one-pass mechanics themselves, not just watch the deck's example.

---

## Classroom Quiz (37–42 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block, covering both the NSE/PSE approach and the optimal one-pass trade-off.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| The largest rectangle must use the tallest bar in the array | Instinct: "biggest number should matter most" | Session hook — a shorter-but-wider rectangle can beat the tallest, narrowest bar |
| NSE and PSE can both be computed in a single pass | Feels redundant to scan the array twice | NSE looks forward, PSE looks backward — opposite scan directions |
| In the one-pass approach, area is computed once at the very end, for every bar at once | The two-pass method primed this expectation | Each area appears mid-pass, exactly at the pop that reveals a bar's right boundary |
| When the stack empties during a pop, the width is `0` or undefined | No left boundary feels like a broken case | The width is just the current index itself — "no smaller bar to the left" means the rectangle reaches all the way to the start |

---
