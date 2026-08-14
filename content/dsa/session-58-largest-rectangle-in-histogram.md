# Session 58 — Largest Rectangle in Histogram

**Duration** 42 min total — 37 min instruction + 5 min Classroom Quiz (cap: 45 + 5, not more) · **Topic** Stack — Largest Rectangle in Histogram (NSE/PSE two-pass approach + optimal one-pass approach) · **Prerequisite** Session 925 — Asteroid Collision
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

**Q5 (MSQ — pick all correct).** Which are true of the collision simulation?
`A` It uses a stack · `B` A single incoming asteroid can destroy more than one stack element · `C` The final stack, transferred to an array, is the answer · `D` It requires sorting the input first
→ **A, B, C.**

---

## Hook (5–8 min)

Draw a rough skyline on the board — bars of heights `2, 1, 5, 6, 2, 3` sitting side by side, each width 1.

Ask: *"Somewhere in this skyline is the single largest rectangle that fits entirely under the outline. Just eyeball it — where do you think it is, and how big?"*

Let a few guesses land (actual answer: height 5, width 2, area 10 — bars at height 5 and 6). Then:

> *"You just did that by squinting at the whole picture at once. A computer needs a rule. It turns out to depend on something you already know how to compute: for every bar, how far can a rectangle at *that bar's height* stretch left and right before it hits something shorter? That's Previous Smaller Element and Next Smaller Element — the same monotonic stack idea, run twice."*

---

## Slide Block A — Problem + NSE/PSE Approach (8–16 min) — DELIVER SLIDES AS-IS

Covers: Problem Statement → Example 1 (`[4, 2, 7, 6, 1, 5]` → area `12`) → Example 2 (`[2, 6, 4, 1, 5, 2, 7, 3]` → area `8`) → Better Approach: precompute Next Smaller Element and Previous Smaller Element for every bar using stacks; width for bar `i` = `NSE[i] - PSE[i] - 1`.

**Beats to emphasise**

- Walk Example 1's winning rectangle: height `6`, width `2` (bars at index 2 and 3, heights `7` and `6`) → area `12`. The rectangle's height is capped by the *shorter* of the two bars it spans.
- **State the core idea as one sentence:** "for every bar, if I use *its own height* as the rectangle's height, how wide can that rectangle get before it hits a shorter bar on the left, and on the right?"

**Checkpoint (at 16 min)** — cold-call:
> *"If a bar's PSE is at index 2 and its NSE is at index 7, how wide is the rectangle anchored at that bar?"*
> **Answer:** `7 - 2 - 1 = 4`.

---

## Slide Block B — NSE/PSE Dry Run (16–24 min) — DELIVER SLIDES AS-IS

Covers: Full dry run on `arr = [2, 3, 8, 10, 6, 7, 5]` — right-to-left pass builds NSE, left-to-right pass builds PSE, then area is computed per index using `height × (NSE − PSE − 1)`.

**Beats to emphasise**

- Narrate the NSE pass right-to-left: pop any stack index whose value is `≥` the current bar, the new top is the NSE index. Then the PSE pass, same mechanism, left to right.
- Compute one area together on the board: bar at index 4, height `6`, `NSE[4]=6, PSE[4]=1` → width `4` → area `24`. The deck's overall max is `25`.

**Checkpoint (at 24 min)** — cold-call:
> *"Why do we need two separate passes — one for NSE, one for PSE — instead of one?"*
> **Answer:** NSE looks forward (naturally scanned right-to-left), PSE looks backward (naturally scanned left-to-right) — mirror-image questions needing mirror-image scan directions.

---

## Bridge (24–25 min)

Say: *"You just computed both boundaries, then every area. Watch what happens when you compute each bar's area the instant you learn its right boundary — no second array, one pass."*

---

## Slide Block C — Optimal One-Pass Approach (25–33 min) — DELIVER SLIDES AS-IS

Covers: Optimal Approach — one stack, one left-to-right pass. When a bar shorter than the stack's top arrives, pop the top and *immediately* compute its area, instead of precomputing NSE and PSE as separate arrays → complexity (`push`/pop total O(N)) → code.

**Beats to emphasise**

- State the conceptual leap: the two-pass approach computes *both* boundaries for every bar before calculating any area; the optimal approach computes each bar's area the *moment* its right boundary becomes known.
- Walk the dry run's key moment: at `i=4` (value `6`), pop `10` (right boundary = index 4), compute its area immediately, then pop `8` the same way, then push `6`. At the end of the array, anything still on the stack gets the array's end as its right boundary.

**Checkpoint (at 33 min)** — cold-call:
> *"In the optimal approach, when exactly does a bar's area get computed?"*
> **Answer:** The moment it gets popped — exactly when a shorter bar arrives to its right, giving it its right boundary right then and there.

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
| NSE and PSE can both be computed in a single pass | Feels redundant to scan the array twice | Slide Block B's checkpoint — NSE looks forward, PSE looks backward, opposite scan directions |
| In the one-pass approach, area is computed once at the very end, for every bar at once | The two-pass method primed this expectation | Slide Block C — each area appears mid-pass, exactly at the pop that reveals a bar's right boundary |
| When the stack empties during a pop, the width is `0` or undefined | No left boundary feels like a broken case | The width is just the current index itself — "no smaller bar to the left" means the rectangle reaches all the way to the start |

---

## Instructor Notes

- **42-min format: 37 min instruction + 5 min Classroom Quiz, capped at 45 + 5.** Merged from the previous two-part split (35 + 30 min = 65 min combined) into one session, since the schedule treats this as a single topic per slot. Both the NSE/PSE two-pass approach and the optimal one-pass approach are kept — do not cut the two-pass approach to save time; it's what makes the one-pass approach legible as a simplification rather than a new trick.
- **This is the hardest session in this six-session block** — protect its time elsewhere in the week if the schedule allows.
- **The Classroom Quiz runs last**, as the sole closing activity — no separate exit ticket or homework block.
- **This is the fourth monotonic-stack-family problem in the sequence** (after Monotonic Stack, Next Greater Element, and Asteroid Collision) — name the recurring invariant explicitly: "pop while the top violates your order."
