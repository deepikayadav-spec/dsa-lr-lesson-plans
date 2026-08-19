# Largest Rectangle in Histogram

**Duration** 50 min total — 43 min instruction + 5 min Classroom Quiz + 2 min buffer (buffer is inside the 50, not extra) · **Topic** Stack — Largest Rectangle in Histogram (NSE/PSE two-pass approach + optimal one-pass approach) · **Prerequisite** Asteroid Collision
**Session type** Concept lecture · **Format** Class Delivery Framework — two-pass approach, bottleneck identification, transition, then a full second cycle for the optimal approach; Safe Points throughout; engagement activity reuses the session's own example

<!-- Two full approaches in 50 min is tight. The two-pass approach is deliberately kept lean here (single dry run, pseudocode, no live-coded implementation) — its job is to motivate *why* the optimal approach's shortcut works, not to be implemented. The optimal one-pass approach gets the full treatment: two-cycle dry run, live-coded C++, derived complexity. -->

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the problem: given bar heights of width 1, find the largest rectangular area that fits within the histogram's outline. *(REMEMBERING)*
2. Explain why a rectangle anchored at a given bar's height can only extend as far as the nearest shorter bar on each side. *(UNDERSTANDING)*
3. Compute Next Smaller Element (NSE) and Previous Smaller Element (PSE) using a monotonic stack, and use them to calculate a bar's maximum rectangle area. *(APPLYING)*
4. Identify the redundant work in the two-pass approach and trace the optimal one-pass approach, where a single stack replaces both NSE and PSE passes. *(ANALYZING)*

---

## Warm-Up Poll — Recap of Previous Session (0–5 min)

Live poll (Mentimeter or similar) on **Asteroid Collision**. **Don't summarize it yourself first** — run the poll cold, then read the aggregate result out loud as the recap.

**Q1.** Two asteroids of equal magnitude, moving toward each other:
`A` The larger one survives · `B` Both are destroyed · `C` Neither is affected · `D` They pass through each other
→ **B.**

**Q2.** In the stack-based simulation, when a negative (left-moving) asteroid arrives, it's compared against:
`A` Every element in the array · `B` The stack top, repeatedly, until stopped or the stack empties · `C` Only the first element pushed · `D` Nothing — it's always pushed directly
→ **B.**

**Q3.** What is the overall time complexity of the stack-based asteroid simulation?
`A` O(1) · `B` O(N) · `C` O(N²) · `D` O(N log N)
→ **B.**

Say: *"[X]% got the repeated-comparison mechanic — good, because today's problem uses that same 'keep checking the stack top' discipline, just for a different purpose."*

---

## Hook (5–7 min)

State the topic explicitly: *"Today's problem is the hardest one in this block — Largest Rectangle in Histogram."* Draw a rough skyline on the board — bars of heights `2, 1, 5, 6, 2, 3` sitting side by side, each width 1.

Ask: *"Somewhere in this skyline is the single largest rectangle that fits entirely under the outline. Just eyeball it — where do you think it is, and how big?"*

Let a few guesses land (actual answer: height 5, width 2, area 10 — bars at height 5 and 6). Name the motivation explicitly:

> *"You just did that by squinting at the whole picture at once. A computer needs a rule — and the advantage of finding one is that it works whether there are 6 bars or 6 million. Today we build that rule."*

---

## Problem Statement (7–11 min)

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

**Safe Point 1 — Problem Statement Clarity.** *Technique: Predict-the-Output, on a new input.* Draw a third array on the board — one they haven't seen: `heights = [2, 4, 2]`. Ask: *"Just by eyeballing it, before we talk about how to solve it — what's the largest rectangle here, and why?"* Give them a few seconds, take an answer.

**What to listen for:** the common wrong answer is `4` — the single tall bar, alone. The correct answer is `6` — all three bars together at height `2`, width `3`, since `2` is short enough to sit under the tall middle bar too. If the room lands on `4`, don't correct it yet — just note it out loud: *"Hold that thought — that's the exact trap we're solving for today."* If they land on `6` unprompted, that's a strong signal the problem statement has genuinely landed; move on.

---

## Concept Walkthrough — Two-Pass Approach (11–22 min)

*(Deck: Approach Slides 21–22 · Dry Run Slides 23–61 · Pseudocode Slides 62–64 · Complexity Slides 65–66)*

**Approach Exploration (~3 min).** Before revealing anything, ask: *"For one specific bar, its rectangle can stretch left and right until it hits something shorter. What would you need to know about each bar to compute that directly?"* Let guesses land — steer toward "how far until a shorter bar appears, on both sides." Give the brief version only: *"That's exactly two values per bar: the nearest strictly-shorter bar to its left, and to its right — its Next Smaller Element and Previous Smaller Element."*

**Now find one, together, by eye — don't just announce it.** Point at index `2` (height `5`) on the hook's skyline, `heights = [2, 1, 5, 6, 2, 3]`. Ask: *"Looking at the board — starting from this bar and scanning right, where's the first bar that's shorter than it?"* Let them point or call it out — index `4` (height `2`). Then: *"And scanning left?"* — index `1` (height `1`). Confirm out loud: *"You just found bar 2's Next Smaller Element and Previous Smaller Element yourselves — index 4 and index 1. That's exactly what we're about to automate for every bar at once, with a monotonic stack — the same tool from Asteroid Collision, aimed at a new job."*

**Dry Run (~4 min) — brief, proof of concept.** Before running anything, name the two variables on the board:
- **`NSE[]`** — an array. `NSE[i]` will hold the *index* of bar `i`'s Next Smaller Element to the right.
- **The stack** — holds *indexes* of bars we haven't found an NSE for yet, i.e. bars that could still turn out to be the next-smaller-to-the-right for something processed later.

Same array, `heights = [2, 1, 5, 6, 2, 3]`. Compute **NSE**, scanning right to left, popping while the stack's top is `≥` the current value:

```
i=5 (h=3) → stack empty → NSE[5]=6 (past end) → push 5.            Stack (idx): 5
i=4 (h=2) → top idx5 (h=3) ≥ 2 → pop. Stack empty → NSE[4]=6 → push 4.   Stack (idx): 4
i=3 (h=6) → top idx4 (h=2) < 6 → stop → NSE[3]=4 → push 3.          Stack (idx): 4, 3
i=2 (h=5) → top idx3 (h=6) ≥ 5 → pop. top idx4 (h=2) < 5 → stop
            → NSE[2]=4 → push 2.                                    Stack (idx): 4, 2
i=1 (h=1) → top idx2 (h=5) ≥ 1 → pop. top idx4 (h=2) ≥ 1 → pop
            → stack empty → NSE[1]=6 → push 1.                      Stack (idx): 1
i=0 (h=2) → top idx1 (h=1) < 2 → stop → NSE[0]=1 → push 0.          Stack (idx): 1, 0
```

`NSE = [1, 6, 4, 4, 6, 6]`. **PSE is the exact mirror** — same algorithm, scanning left to right instead. Don't re-derive it live; state it directly: `PSE = [-1, -1, 1, 2, 1, 4]`.

**Observations — write these on the board, in plain English:**
1. For each bar, width = distance between its NSE and its PSE, minus the two boundary bars themselves: `width = NSE[i] − PSE[i] − 1`.
2. NSE looks forward, so it's natural to scan right-to-left; PSE looks backward, so it's natural to scan left-to-right — mirror-image passes.
3. Once both arrays exist, area for bar `i` is `heights[i] × width`.

Check bar `i=2` (height `5`): `width = NSE[2] − PSE[2] − 1 = 4 − 1 − 1 = 2`, `area = 5 × 2 = 10` — matches the hook's eyeballed answer.

**Safe Point 2 — Approach Understanding.** *Technique: Hand-Signal Check.* "Thumbs up if you can tell me why NSE scans right-to-left. Thumbs down if not." Address before continuing.

**Pseudocode (two-pass) — derive step by step:**

```
function computeNSE(heights):
    n = heights.length
    nse = array of size n
    stack = empty
    for i from n-1 down to 0:
        while stack not empty and heights[top(stack)] >= heights[i]:
            pop(stack)
        nse[i] = stack.empty() ? n : top(stack)
        push i onto stack
    return nse
    # computePSE mirrors this exactly, scanning left to right

function largestRectangleArea_twoPass(heights):
    nse = computeNSE(heights)
    pse = computePSE(heights)          # mirror of computeNSE, left to right
    maxArea = 0
    for i from 0 to heights.length - 1:
        width = nse[i] - pse[i] - 1
        maxArea = max(maxArea, heights[i] * width)
    return maxArea
```

**Safe Point 3 — Pseudocode Understanding.** *Technique: Deliberate Bug.* Ask: *"What if the width formula was `nse[i] - pse[i]`, without the `- 1`?" Is that still correct?* It's not — it would count the boundary bars themselves as part of the width. Students tracking the logic should catch the off-by-one.

**Complexity (two-pass) — brief.** Two full passes to build `nse` and `pse` (each O(N), since every index is pushed and popped from its stack at most once), plus one more pass to compute areas — three O(N) passes back to back. Overall still O(N) time, but **two extra O(N) arrays** get built and thrown away. That extra storage is the seed of the next question.

---

## Bottleneck & Transition to the Optimal Approach (22–24 min)

**Safe Point 4 — Confirm Before Transitioning.** *Technique: Physical Movement Reset.* Step away from the board, walk toward the students, and ask: *"Before we speed this up — in the two-pass version, what exactly are we doing three separate times that we probably don't need to?"* Give a few seconds of deliberate silence before calling on anyone.

**Identify the bottleneck, explicitly:** two full arrays (`nse`, `pse`) get built and stored, just so a third pass can read one value from each. The area for bar `i` doesn't actually need the *whole* `pse` array — it only needs to know what's still on the stack directly below `i` at the moment `i` gets popped, and that's already sitting right there.

**Smooth transition:**
> *"Here's the shortcut: the moment a bar gets popped during the NSE scan, we already know its right boundary — that's what triggered the pop. And whatever's left on the stack right below it, at that exact instant, is its left boundary — that *is* the PSE, we just never needed to store it separately. So instead of two passes and two arrays, we compute the area the instant a bar is popped, in the same single pass that finds NSE. One stack, one pass, zero extra arrays."*

---

## Concept Walkthrough — Optimal One-Pass Approach (24–38 min)

*(Deck: Approach Slides 69–70 · Dry Run Slides 71–88 · Pseudocode Slides 89–91 · Complexity Slides 92–94 · C++ Code Slides 95–97 · Key Takeaways Slides 98–100)*

**Dry Run — Cycle 1, brief (~2 min).** Same array, left to right this time, one stack of indices. Just prove the mechanism works, on the first few steps:

```
i=0 (h=2) → stack empty → push.                    Stack (idx): 0
i=1 (h=1) → h[0]=2 ≥ 1 → pop idx 0.
            stack now empty → area = 2 × 1 = 2      (computed immediately — no separate pass!)
            → push 1.                               Stack (idx): 1
```

That's the whole trick, already visible: index `0`'s area got computed the instant it was popped, inside the same scan that's finding NSE. Now run it fully.

**Dry Run — Cycle 2, detailed (~3 min).** Continue from where Cycle 1 left off, tracking the stack and every area computed:

```
i=2 (h=5) → h[1]=1 < 5 → push.                             Stack (idx): 1, 2
i=3 (h=6) → h[2]=5 < 6 → push.                              Stack (idx): 1, 2, 3
i=4 (h=2) → h[3]=6 ≥ 2 → pop idx 3.
            area = 6 × (4−2−1) = 6
            → h[2]=5 ≥ 2 → pop idx 2.
            area = 5 × (4−1−1) = 10
            → h[1]=1 < 2 → push.                            Stack (idx): 1, 4
i=5 (h=3) → h[4]=2 < 3 → push.                              Stack (idx): 1, 4, 5
end        → pop idx 5: area = 3 × (6−4−1) = 3
           → pop idx 4: area = 2 × (6−1−1) = 8
           → pop idx 1: area = 1 × 6 = 6
```

Maximum area across all pops: `10` — matches the hook's eyeballed answer, and the two-pass approach's answer for bar `i=2`.

**Observations — write these on the board, in plain English:**
1. Scan left to right with a single stack of indices, kept in increasing height order.
2. When a shorter bar arrives, pop the taller one — that pop is its NSE, found *and* used in the same moment.
3. Its left boundary is whatever's now left on the stack (or the very start, if the stack goes empty) — compute the area right there, no second array.
4. After the scan ends, keep popping and computing until the stack is empty — those are the bars that never found a smaller bar to their right.

**Safe Point 5 — Approach Understanding.** *Technique: Hand-Signal Check.* "Thumbs up if you can tell me what the width is when the stack goes empty during a pop. Thumbs down if not."
**Answer:** the current index itself — there's no bar to the left that's smaller, so the rectangle reaches all the way back to the start.

**Pseudocode — derive step by step, not all at once.** First just the scan and the pop condition:

```
function largestRectangleArea(heights):
    stack = empty stack of indices
    append 0 to heights                    # sentinel: forces a final flush
    maxArea = 0
    for i from 0 to heights.length - 1:
        while stack not empty and heights[top(stack)] >= heights[i]:
```

Then the area computation inside the loop, referring back to Observation 3:

```
            topIdx = pop(stack)
            height = heights[topIdx]
            width = stack.empty() ? i : i - top(stack) - 1
            maxArea = max(maxArea, height * width)
        push i onto stack
    return maxArea
```

**Safe Point 6 — Pseudocode Understanding.** *Technique: Deliberate Bug.* Ask: *"What if I dropped the sentinel `0` appended to `heights`? Would the last bars on the stack ever get their area computed?"* They wouldn't — without a value smaller than everything remaining, the final pops never trigger, and those bars' areas are silently lost.

**Deriving the Code (~4 min) — build this live, in the coding playground, straight from the pseudocode above. Do not read out a finished block.** Relate every line back to the pseudocode line it came from:

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

**Complexity — derive it, don't state it (~2 min).** Take the concrete example: `n = 6` bars. Every index is pushed onto the stack exactly once — 6 pushes total. Every index is popped at most once — at most 6 pops total. That's at most `6 + 6 = 12` stack operations for 6 bars, not `6 × 6 = 36` (which is what a brute-force "check every pair of bars" approach would cost). Generalize: `n` pushes plus at most `n` pops is `2n` operations — drop the constant, that's O(N) time, O(N) space for the stack. Compare directly against the two-pass approach: same O(N) time, but one stack instead of two extra arrays.

**Key Takeaways** *(mandatory — matches the deck's own Key Takeaways slides, state these explicitly):*
- Every bar's maximum width is decided by its Previous Smaller Element (PSE) on the left and Next Smaller Element (NSE) on the right.
- PSE and NSE for all bars are computed in O(N) time using a monotonic stack of indices.
- `width = NSE[i] − PSE[i] − 1`, `area = height × width` for every bar — take the maximum.
- In the optimal one-pass approach, whenever a smaller bar is seen, pop taller bars and compute each one's area, treating it as the smallest height in its own rectangle.
- In both approaches, each index is pushed and popped at most once — O(N) time, O(N) extra space overall.

---

## ⚡ Engagement Activity (38–43 min)

*Reuses the exact array from the Dry Runs above, plus one new small array chosen to trigger a specific edge case — no unrelated content, so minimal extra time added.*

**Format:** What-If Discussion · **Exposes:** whether students understand *why* the algorithm works, not just that it produces `10` on the one array they've now seen three times.

**Prompt 1 — say this:**
> *"What if the histogram was strictly decreasing — `heights = [3, 2, 1]`? Quick guess before we trace it: does every bar just form its own separate little rectangle, or could some of them combine into something bigger?"*

Let guesses land — the common instinct is "each bar stands alone, since nothing's ever taller to its right." Then trace it together:

```
i=0 (h=3) → push.                                          Stack (idx): 0
i=1 (h=2) → h[0]=3 ≥ 2 → pop idx0. width=i=1 → area=3×1=3.
            push 1.                                        Stack (idx): 1
i=2 (h=1) → h[1]=2 ≥ 1 → pop idx1. width=i=2 → area=2×2=4.
            push 2.                                        Stack (idx): 2
end        → pop idx2. width=3(n) → area=1×3=3.
```

**Reveal:** maximum area is `4`, not `3` — the bar of height `2` doesn't stand alone, it stretches across width `2` (covering both itself and the taller bar of height `3` behind it, since a rectangle only needs bars *at least* as tall as it is). Debrief: *"'Strictly decreasing' feels like it should mean 'no combining possible' — it doesn't. Width comes from how far back a rectangle can reach while staying under the outline, not from whether neighbours are taller or shorter."*

**Prompt 2 — say this:**
> *"What if two adjacent bars are exactly the same height — `heights = [2, 2]`? Does the algorithm still find the rectangle spanning both, or does it treat them as two separate bars?"*

Trace together: `i=0` pushes. `i=1` (h=2): `h[0]=2 ≥ 2` → **pop triggers even on a tie** → area `= 2 × 1 = 2`, push 1. End (sentinel): pop idx1, stack empty → width `= 2` (n) → area `= 2 × 2 = 4`. **Maximum is `4`** — both bars combined. Debrief: *"That `≥`, not `>`, in the pop condition is exactly what lets equal-height neighbours merge into one wide rectangle instead of being treated as two separate ones."*

**Debrief line:**
> *"Both what-ifs are really the same lesson from two directions: width isn't about 'how many bars look similar' — it's strictly about how far the current bar's height can reach before hitting something *actually* shorter. Decreasing arrays can still combine; equal-height arrays combine on purpose."*

**Cut rule:** If running short, do Prompt 1 only — it directly counters the more common misconception; Prompt 2 is a confirming case, not a new insight.

---

## Classroom Quiz (43–48 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block, covering both the NSE/PSE approach and the optimal one-pass trade-off.

---

## Buffer (48–50 min) · Flex — not instructional, inside the 50-minute block

Unscheduled on purpose. If you land here with time on the clock, let the session end early — don't stretch content to fill it. If students have open questions, this is where they get handled.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| The largest rectangle must use the tallest bar in the array | Instinct: "biggest number should matter most" | Session hook — a shorter-but-wider rectangle can beat the tallest, narrowest bar |
| NSE and PSE can both be computed in a single pass | Feels redundant to scan the array twice | Two-Pass Approach's Observations — NSE looks forward, PSE looks backward, opposite scan directions |
| A strictly decreasing (or increasing) array means every bar stands alone, no combining | Feels intuitive — nothing "matches" its neighbour | Engagement Activity Prompt 1 — `[3,2,1]` still combines into a width-2 rectangle |
| In the one-pass approach, area is computed once at the very end, for every bar at once | The two-pass method primed this expectation | Dry Run Cycle 1 — the very first pop already computes an area, mid-scan |
| When the stack empties during a pop, the width is `0` or undefined | No left boundary feels like a broken case | The width is just the current index itself — "no smaller bar to the left" means the rectangle reaches all the way to the start |

---
