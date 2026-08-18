# Largest Rectangle in Histogram

**Duration** 50 min total — 43 min instruction + 5 min Classroom Quiz + 2 min buffer · **Topic** Stack — Largest Rectangle in Histogram (NSE/PSE two-pass approach + optimal one-pass approach) · **Prerequisite** Asteroid Collision
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

## Warm-Up Poll — Retrieval Practice on Asteroid Collision (0–6 min)

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

## Hook (6–9 min)

Draw a rough skyline on the board — bars of heights `2, 1, 5, 6, 2, 3` sitting side by side, each width 1.

Ask: *"Somewhere in this skyline is the single largest rectangle that fits entirely under the outline. Just eyeball it — where do you think it is, and how big?"*

Let a few guesses land (actual answer: height 5, width 2, area 10 — bars at height 5 and 6). Then:

> *"You just did that by squinting at the whole picture at once. A computer needs a rule. It turns out to depend on something you already know how to compute: for every bar, how far can a rectangle at *that bar's height* stretch left and right before it hits something shorter? That's Previous Smaller Element and Next Smaller Element — the same monotonic stack idea, run twice."*

---

## Problem Statement (9–13 min)

*(Deck: Slide 4 — problem definition; Slides 5–20 — the deck's own animated examples)*

Given an array of non-negative integers `heights` representing histogram bars of width 1 standing side by side, find the area of the largest rectangle that fits entirely under the outline.

**Input:** an array of integers `heights` — each bar's height, width fixed at 1.
**Output:** an integer — the maximum rectangular area achievable.

**Example 1**
Input: `heights = [2, 1, 5, 6, 2, 3]`
Output: `10`
Why: the rectangle spanning the two bars of height `5` and `6` (both at least height 5) gives width `2 × 5 = 10` — the largest of any combination here.

**Example 2**
Input: `heights = [2, 4]`
Output: `4`
Why: bar `2` alone gives area `2`; bar `4` alone gives area `4`; both together are capped at the shorter bar's height, `min(2,4) × 2 = 4`. Best is `4`.

---

## Concept Walkthrough (13–36 min)

*(Deck: Two-pass NSE/PSE — Approach Slides 21–22, Dry Run Slides 23–61, Pseudocode Slides 62–64, Complexity Slides 65–66, C++ Code Slides 67–68. One-pass optimal — Approach Slides 69–70, Dry Run Slides 71–88, Pseudocode Slides 89–91, Complexity Slides 92–94, C++ Code Slides 95–97, Summary Slides 98–100)*

**Core idea (two-pass):** for every bar, width = `NSE[i] - PSE[i] - 1`, where NSE/PSE are the nearest strictly-smaller bar to the right/left, each found with a monotonic stack in one pass. **Core idea (one-pass, optimal):** instead of precomputing both arrays, pop-and-compute — when a shorter bar arrives, pop the taller one off the stack and compute its area immediately, using the current index as its right boundary.

**Dry Run** — one-pass approach on `heights = [2, 1, 5, 6, 2, 3]`. Show the status of the stack after every update:

```
i=0 (h=2) → stack empty → push                          Stack (idx): 0
i=1 (h=1) → h[0]=2 ≥ 1 → pop idx 0
            area = 2 × 1 = 2   (stack now empty, width = i)
            → push 1                                     Stack (idx): 1
i=2 (h=5) → h[1]=1 < 5 → push                             Stack (idx): 1, 2
i=3 (h=6) → h[2]=5 < 6 → push                             Stack (idx): 1, 2, 3
i=4 (h=2) → h[3]=6 ≥ 2 → pop idx 3
            area = 6 × (4−2−1) = 6
            → h[2]=5 ≥ 2 → pop idx 2
            area = 5 × (4−1−1) = 10
            → h[1]=1 < 2 → push                           Stack (idx): 1, 4
i=5 (h=3) → h[4]=2 < 3 → push                             Stack (idx): 1, 4, 5
end        → pop idx 5: area = 3 × (6−4−1) = 3
           → pop idx 4: area = 2 × (6−1−1) = 8
           → pop idx 1: area = 1 × 6 = 6
```

Maximum area across all pops: `10` — matches the hook's eyeballed answer.

**Pseudocode (optimal one-pass)** — the version actually implemented; the two-pass NSE/PSE version above is scaffolding for *why* it works:

```
function largestRectangleArea(heights):
    stack = empty stack of indices
    append 0 to heights                    # sentinel: forces a final flush
    maxArea = 0
    for i from 0 to heights.length - 1:
        while stack not empty and heights[top(stack)] >= heights[i]:
            topIdx = pop(stack)
            height = heights[topIdx]
            width = stack.empty() ? i : i - top(stack) - 1
            maxArea = max(maxArea, height * width)
        push i onto stack
    return maxArea
```

**Deriving the code** — build this live in the coding playground, straight from the pseudocode above; don't just read out a finished block:

```cpp
int largestRectangleArea(vector<int>& heights) {
    stack<int> st;                 // stores indices
    heights.push_back(0);          // sentinel: forces a final flush
    int maxArea = 0;

    for (int i = 0; i < (int)heights.size(); i++) {
        while (!st.empty() && heights[st.top()] >= heights[i]) {
            int height = heights[st.top()];
            st.pop();
            int width = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        st.push(i);
    }
    return maxArea;
}
```

Each index is pushed once and popped at most once — O(N) time, O(N) space.

**Checkpoint:**
> *"Why does the two-pass approach need separate NSE and PSE scans, in opposite directions?"*
> **Answer:** NSE looks forward (natural to scan right-to-left), PSE looks backward (natural to scan left-to-right) — mirror-image questions.

---

## ⚡ Active Learning Strategy — Dry-Run Relay (36–43 min)

**ALS format:** Dry-Run Relay, run twice on the same fresh array — once for NSE only, once for the one-pass area computation — so students execute both the two-pass mechanics and the optimal one-pass mechanics themselves, not just watch the deck's example.

**Part A — Compute NSE Yourself.**
> *"New array: `[3, 1, 4, 2]`. I want NSE for every index, scanning right to left. Call out what gets popped and what the answer is, before I confirm."*

Run **right to left, one index at a time** (indices 3, 2, 1, 0; values `2, 4, 1, 3`):

```
i=3 (val=2) → stack empty → NSE[3] = 4 (past end) → push 3.        Stack: [3]
i=2 (val=4) → top (idx 3, val 2) < 4 → no pop → NSE[2] = 3 → push 2.   Stack: [3, 2]
i=1 (val=1) → top (idx 2, val 4) ≥ 1 → pop.
              top (idx 3, val 2) ≥ 1 → pop.
              stack empty → NSE[1] = 4 (past end) → push 1.         Stack: [1]
i=0 (val=3) → top (idx 1, val 1) < 3 → no pop → NSE[0] = 1 → push 0.   Stack: [1, 0]
```

Final NSE: `[1, 4, 3, 4]`.

**How it surfaces:** At `i=1` (value `1`), ask before revealing: *"How many pops happen, and why?"* Correct: two pops — both `4` and `2` are `≥ 1`, so both get thrown away before landing on an empty stack.

**Part B — One Pass, Compute as You Go.**
> *"Same array, left to right, one pass. Every time something gets popped, tell me its area before I confirm — height × (current index − new top index − 1), or height × current index if the stack goes empty."*

Run **left to right, one index at a time**:

```
i=0 (val=3) → stack empty → push.                                    Stack: [0]
i=1 (val=1) → top (idx 0, val 3) ≥ 1 → pop.
              stack empty → area = 3 × 1 = 3 (width = current index 1)
              → push 1.                                              Stack: [1]
i=2 (val=4) → top (idx 1, val 1) < 4 → no pop → push.                 Stack: [1, 2]
i=3 (val=2) → top (idx 2, val 4) ≥ 2 → pop.
              new top (idx 1, val 1) < 2 → area = 4 × (3 − 1 − 1) = 4
              → push 3.                                              Stack: [1, 3]
End of array → remaining: pop idx 3 (val 2): new top idx 1 → area = 2 × (4 − 1 − 1) = 4
              pop idx 1 (val 1): stack empty → area = 1 × 4 = 4
```

Maximum area across all pops: `4`.

**How it surfaces:** At `i=1`, ask before revealing: *"The stack goes empty after this pop — what's the width?"* Correct: when the stack empties, there's no left boundary at all, so the width is simply the current index itself.

**Debrief line:**
> *"Same discipline as before — the stack only ever holds bars that could still matter. Part A found boundaries and stopped; Part B does the exact same pops but turns each one straight into an area, no second array needed."*

**Cut rule:** If running short, do only Part A's `i=1` step and Part B's `i=1` step plus the end-of-array cleanup — together they cover the multi-pop mechanism and both the "normal pop" and "stack goes empty" cases.

---

## Classroom Quiz (43–48 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block, covering both the NSE/PSE approach and the optimal one-pass trade-off.

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. If you land here with time on the clock, let the session end early — don't stretch content to fill it.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| The largest rectangle must use the tallest bar in the array | Instinct: "biggest number should matter most" | Session hook — a shorter-but-wider rectangle can beat the tallest, narrowest bar |
| NSE and PSE can both be computed in a single pass | Feels redundant to scan the array twice | NSE looks forward, PSE looks backward — opposite scan directions |
| In the one-pass approach, area is computed once at the very end, for every bar at once | The two-pass method primed this expectation | Each area appears mid-pass, exactly at the pop that reveals a bar's right boundary |
| When the stack empties during a pop, the width is `0` or undefined | No left boundary feels like a broken case | The width is just the current index itself — "no smaller bar to the left" means the rectangle reaches all the way to the start |

---
