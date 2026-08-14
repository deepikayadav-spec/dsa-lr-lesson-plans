# Session 22 — Cubes: Cuts, Pieces & Painted Faces

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Cube structure, cutting formulas (forward and reverse), and painted-cube counting (corner/edge/face/interior pieces) · **Prerequisite** None specific — first and only session of the Cubes topic
**Session type** Lecture + guided practice. No source slide deck — content from GitBook Concept Explanation text. No classroom quiz bank yet — 5-min slot reserved at end. GitBook "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

| Resource | Status |
|---|---|
| Source | GitBook: `session-plans/logical-reasoning/cubes` (Learning Outcomes, Ideal Format, Introduction, Concept Explanation, Closure — text extracted) |
| Problem Solving bank (GitBook) | image-only, not recoverable — practice problems below are instructor-authored |
| Classroom Quiz | not yet available — 5-min slot reserved at end of session |

**⚠️ Resolved discrepancy:** the source's "Ideal Format" page states "Minimum cuts needed: nl + nw + nh," while its "Concept Explanation" page states "Min cuts = Nl + Nw + Nh − 3." This plan resolves it directly: if Nl, Nw, Nh are the number of *pieces* along each axis, the number of *cuts* along that axis is one fewer (Nl−1, etc.), so total cuts = (Nl−1)+(Nw−1)+(Nh−1) = Nl+Nw+Nh−3. The "−3" version is correct once "N" is understood as piece-count per axis; this plan teaches it with that explicit derivation rather than as a memorised, unexplained formula.

---

## Learning Objectives

By the end of this session, students will be able to:

1. State a cube's basic structure: 6 faces, 12 edges, 8 vertices. *(REMEMBERING)*
2. Apply the forward cutting formula to find the maximum pieces from a given number of cuts per axis. *(APPLYING)*
3. Apply the reverse formula to find the number of cuts from a known piece-grid size. *(APPLYING)*
4. Calculate how many smaller cubes have 3, 2, 1, or 0 painted faces after a painted cube is cut into an n×n×n grid. *(APPLYING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Sketch a simple 3D cube outline as a running reference.

---

## Warm-Up Poll — Diagnostic (3–7 min) · ALS: Polling

> New topic — Cubes doesn't build directly on Syllogisms, so this poll is diagnostic, not retrieval.

Say: *"Five quick questions before we start."*

**Q1.** How many faces does a cube have?
`A` 4 · `B` 6 · `C` 8
→ *Read:* B is correct.

**Q2.** How many edges does a cube have?
`A` 8 · `B` 10 · `C` 12
→ *Read:* C is correct.

**Q3.** How many vertices (corners) does a cube have?
`A` 6 · `B` 8 · `C` 12
→ *Read:* B is correct.

**Q4.** Quick riddle: you paint a large cube red on all six faces, then cut it into equal smaller cubes. Guess — how many of the small cubes end up with NO red paint at all?
`A` None · `B` 1 · `C` Depends on how many cuts · `D` Not sure
→ *Read:* C is correct — most guess A or B. Don't confirm the number yet, this is the Hook, resolved fully in Teaching Block B.

**Q5.** How comfortable are you visualising a 3D cube being sliced into smaller pieces, without an actual physical model?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, lean hard on board sketches throughout today's session.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"You're holding a large Rubik's Cube. You paint it red on all six sides. Now you cut it equally into smaller cubes. How many of those little cubes will have no red paint on them at all?"*

Take 2–3 guesses (common wrong answers: "none," "1"), write them on the board without confirming.

> *"The real answer depends entirely on how many pieces you cut it into — and there's an exact formula for it, plus formulas for how many pieces have exactly 1, 2, or 3 painted faces. By the end of today you'll compute all four numbers for any size cube, in seconds."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

<!-- placement: inferred grouping — no source deck; grouped from GitBook Concept Explanation extraction -->
Covers: basic structure → forward and reverse cutting formulas.

**Beats to emphasise**

- **Basic structure, write on the board:** a cube has **6 faces** (squares), **12 edges**, **8 vertices** (corners).
- **Forward cutting formula.** If you cut a cube nl times along its length, nw times along its width, and nh times along its height (each cut a straight slice all the way through), the maximum number of pieces is: **(nl + 1) × (nw + 1) × (nh + 1)**. *(Each cut along one axis adds exactly one more slice in that direction.)*
- **Worked example, live:** *"You make 2 cuts along the length, 1 along the width, and 3 along the height. How many pieces?"* (2+1) × (1+1) × (3+1) = 3 × 2 × 4 = **24 pieces.**
- **Reverse formula — going from pieces back to cuts.** If a cube is cut into a grid of Nl × Nw × Nh pieces (Nl pieces along the length, etc.), then the number of cuts along each axis is one fewer than the piece count on that axis: cuts = (Nl−1) + (Nw−1) + (Nh−1) = **Nl + Nw + Nh − 3**.
- **Worked example, live:** *"A cube is cut into a 4 × 3 × 2 grid of pieces — 24 pieces total. How many straight cuts were made?"* Cuts = 4+3+2−3 = **6**. Verify directly: cuts along length = 4−1=3, width = 3−1=2, height = 2−1=1, total = 3+2+1=**6** ✔.

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"A cube is cut into a 5 × 5 × 5 grid (125 pieces). How many cuts were made?"*
> **Answer:** 5+5+5−3 = **12** cuts (4 along each of the three axes).

---

## ⚡ ALS Activity 1 — Whiteboard Race: Painted Cube Sprint (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to compute all four painted-cube counts (corner/edge/face/interior) for an assigned n×n×n grid size, first correct board up wins the round. Chosen to build fast recall of the four formulas before Teaching Block B derives and explains them properly.

**Setup line:**
> *"Pairs, boards up. I'll give you a grid size (n×n×n, all six outer faces painted before cutting). Find corner (3 painted), edge (2 painted), face (1 painted), and interior (0 painted) counts. First correct board up wins. Three rounds."*

*(Give the four formulas on the board as a lookup reference for this activity — the derivation itself is Teaching Block B's job; this activity is pure execution speed.)* **Corner = 8 · Edge = 12(n−2) · Face = 6(n−2)² · Interior = (n−2)³**

- Round 1: *"n = 3 (27 total pieces)."* → Corner=8, Edge=12(1)=**12**, Face=6(1)=**6**, Interior=**1**. Check: 8+12+6+1=27 ✔.
- Round 2: *"n = 5 (125 total pieces)."* → Corner=8, Edge=12(3)=**36**, Face=6(9)=**54**, Interior=**27**. Check: 8+36+54+27=125 ✔.
- Round 3: *"n = 2 (8 total pieces) — a trap round."* → Corner=8, Edge=12(0)=**0**, Face=6(0)=**0**, Interior=**0**. Check: 8+0+0+0=8 ✔. *"At n=2, EVERY piece is a corner piece — there's no room left for edge, face, or interior pieces at all."*

**How it surfaces:** After Round 3, ask the class: *"Why did edge, face, and interior all come out to zero?"* — confirms understanding that (n−2) becomes 0 or negative for small cubes, not just a mechanical formula plug-in.

**Debrief line:**
> *"Round 3 is the one to remember — a 2×2×2 cube is the smallest case where the formulas still make sense, and every single piece is a corner. That's not a coincidence, it's baked into the geometry."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but if you do keep only 2, keep Round 3 over Round 2 — the n=2 edge case teaches more than another routine calculation.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: deriving the painted-cube formulas, and resolving the Hook.

**Beats to emphasise**

- **Painted cube formulas, derive each one, don't just state them:**
  - **Corner pieces (3 faces painted) = 8, always.** A cube has exactly 8 corners, regardless of how many pieces it's cut into — each corner piece touches exactly 3 of the original outer faces.
  - **Edge pieces (2 faces painted) = 12(n−2).** A cube has 12 edges; along each edge, the two corner pieces are excluded, leaving (n−2) pieces per edge with exactly 2 painted faces.
  - **Face pieces (1 face painted) = 6(n−2)².** A cube has 6 faces; on each face, strip away the outer border (which belongs to edge/corner pieces), leaving a (n−2)×(n−2) inner square of pieces with exactly 1 painted face.
  - **Interior pieces (0 faces painted) = (n−2)³.** Strip away one full layer from every side, and what's left is a smaller (n−2)×(n−2)×(n−2) cube, entirely unpainted.
- **Resolving the Hook, live:** *"Let's say you cut your cube into a 4×4×4 grid — 64 small cubes. How many have NO paint at all?"*
  1. Interior = (4−2)³ = 2³ = **8**.
  2. Full check: Corner=8, Edge=12(2)=24, Face=6(4)=24, Interior=8. Total = 8+24+24+8=**64** ✔ matches.
  3. **Answer: 8 small cubes have no paint at all** — the exact center 2×2×2 block.

**Checkpoint (at 32 min)** — cold-call:
> *"Why is the corner-piece count always exactly 8, no matter how big n gets?"*
> **Answer:** **A cube always has exactly 8 corners** — cutting it into more pieces doesn't add or remove corners, it only changes how many pieces sit along each edge/face/interior.

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: Reverse + Painted Combo (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students solve a two-part problem entirely on their own, combining the reverse-cuts formula from Teaching Block A with the painted-face formulas from Teaching Block B. Deliberately different register from Activity 1's loud paired race (quiet, individual, single big reveal).

**Setup line:**
> *"On your own, three minutes, two parts. Part 1: A cube is cut into a 5 × 2 × 3 grid — how many straight cuts were made? Part 2: Separately, a 6×6×6 painted cube (216 pieces) is cut apart — how many pieces have exactly 1 painted face? Write both answers, hold up when I say show."*

Give 3 minutes silent work, then: *"Show me — three, two, one, show."*

**The reveal, step by step:**
1. **Part 1:** cuts = 5+2+3−3 = **7**. Verify: cuts along each axis = 4+1+2 = 7 ✔.
2. **Part 2:** Face pieces = 6(n−2)² = 6(4)² = 6×16 = **96**.

**Debrief line:**
> *"Two completely different formulas, but both came from the same habit — write down exactly what n or Nl/Nw/Nh represents before plugging into anything. Mixing up 'pieces per axis' with 'cuts per axis' is the single most common error on this topic, and it's exactly what today's resolved discrepancy was about."*

**Cut rule:** If running short, keep only Part 1 (drop Part 2), but always show the explicit "cuts = pieces−1 per axis" reasoning in the reveal — that's the resolved-discrepancy lesson from the top of this session.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — pose one more painted-cube calculation at a different n and solve together — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> A painted cube is cut into a 4×4×4 grid. How many pieces have exactly 2 painted faces?
> **Answer:** Edge = 12(n−2) = 12(2) = **24**.

Scan responses on the way out — if the reverse-cuts formula (Nl+Nw+Nh−3) is still shaky, revisit briefly at the start of Session 23.

**Homework**

| Task | Note |
|---|---|
| A cube is cut into a 6×4×5 grid. Find the total cuts made, and the total pieces. | Self-check using both the forward and reverse formulas |
| For a 7×7×7 painted cube, find all four counts (corner, edge, face, interior) and confirm they sum to 343 | Self-check — full application of all four painted-cube formulas |

Tell them: *"Cubes wraps up the spatial-reasoning side of this course. Session 23 moves into Puzzles — combining everything you've learned (relationships, positions, patterns) into multi-clue logic puzzles."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| "Min cuts = Nl+Nw+Nh" (no −3) is the correct reverse formula | This is literally what one of the source's own pages states | The resolved-discrepancy note at the top of this file, taught with explicit derivation |
| Corner-piece count changes with cube size | Assumes bigger cubes have "more" of everything | Teaching Block B's explicit "always exactly 8" derivation |
| (n−2) formulas "break" for small n (like n=2) | Doesn't test the formula at its edge case | ALS Activity 1 Round 3's explicit n=2 walkthrough |
| Cuts-per-axis and pieces-per-axis are the same number | Conflates the two without checking the off-by-one relationship | Teaching Block A's explicit "cuts = pieces − 1" derivation |
| Painted-face formulas only work for perfect cubes, not general 3D grids | True in this session's scope, but not always flagged explicitly | Explicit "n×n×n" framing throughout all worked examples |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from GitBook Concept Explanation/Introduction/Closure text extraction. GitBook's "Problem Solving" sub-page is image-only and unrecoverable — all worked/practice problems in this plan are **instructor-authored**, though the basic structure (6/12/8) and all four painted-cube formulas directly match the source's own stated figures.
- **⚠️ The min-cuts discrepancy flagged in the source is resolved in this plan** (see the note at the top of this file) — teach the −3 version with its derivation, not as a memorised fact.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive, execution-focused; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, combining both halves of the session's content.
- **First and only session for this topic** (Cubes is a single-session topic per the course structure) — warm-up poll is diagnostic, not retrieval.
- Classroom Quiz slot reserved-empty per site convention.
