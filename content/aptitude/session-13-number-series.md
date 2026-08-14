# Session 13 — Coding & Decoding: Number Series

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** The four-tier logic hierarchy for number series (add/subtract → multiply/divide → number properties → multi-operator), missing and incorrect terms · **Prerequisite** None specific — first session of the Coding and Decoding topic
**Session type** Lecture + guided practice. No source slide deck — content from the session's concept-explanation text. No classroom quiz bank yet — 5-min slot reserved at end. the "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

---

## Learning Objectives

By the end of this session, students will be able to:

1. Apply the four-tier logic hierarchy — addition/subtraction, multiplication/division, number properties, multi-operator — in that order, to find a series' underlying pattern. *(APPLYING)*
2. Solve missing-term series using the correct tier of logic. *(APPLYING)*
3. Identify the one incorrect term in a series that otherwise follows a consistent pattern. *(ANALYZING)*
4. Recognise second-order (differences-of-differences) and alternating-logic patterns. *(ANALYZING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Write "2, 4, 8, 16, ?" as a warm visual on the board.

---

## Warm-Up Poll — Diagnostic (3–7 min) · ALS: Polling

> New topic — Coding and Decoding doesn't build directly on Directions, so this poll is diagnostic, not retrieval.

Say: *"Five quick questions before we start."*

**Q1.** 2, 4, 8, 16, ? — what comes next?
`A` 20 · `B` 24 · `C` 32 · `D` 18
→ *Read:* C is correct (×2 each time) — this is the Hook's own riddle, confirm together after the poll.

**Q2.** Have you solved a "number series" question before (school, coaching, mock test)?
`A` Never · `B` Once or twice · `C` Regularly
→ *Read:* If mostly A, spend extra time on the hierarchy before speeding into worked examples.

**Q3.** 3, 6, 9, 12, ? — what comes next?
`A` 14 · `B` 15 · `C` 16
→ *Read:* B is correct — simplest tier, confirms basic addition-pattern recognition.

**Q4.** Is 11 a prime number?
`A` Yes · `B` No
→ *Read:* A is correct — needed for the prime-sequence tier later.

**Q5.** How comfortable are you spotting a pattern when the differences between terms aren't constant (e.g. they're themselves increasing)?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, slow down through Teaching Block B's multi-operator section.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"2, 4, 8, 16, ? — you already answered this in the poll. Most of you got 32. But here's the real question: how did you know it wasn't 20, or 24? What told your brain to multiply instead of add?"*

Let 2–3 students explain their reasoning out loud.

> *"That instinct — checking the simplest explanation first, then moving to a more complex one — is exactly the skill today formalises into a repeatable method. By the end of today you'll have a fixed order to check, every single time, so you never have to guess."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

Covers: the four-tier logic hierarchy, worked from simplest to most complex.

**Beats to emphasise**

- **The core principle:** *"Always begin by checking the most basic relationship between terms, and only move to something more complex if the simple explanation fails."* Write the four tiers on the board, in order:
  1. **Addition / Subtraction** — simple constant differences.
  2. **Multiplication / Division** — constant ratios.
  3. **Number properties** — primes, perfect squares, perfect cubes, odd/even patterns.
  4. **Multiple operators** — a changing (but patterned) operation, like increasing differences.
- **Worked example, Tier 1:** *"3, 6, 9, 12, ?"* — differences are constant (+3 each time) → **15**.
- **Worked example, Tier 2:** *"2, 4, 8, 16, ?"* — ratios are constant (×2 each time) → **32**. *(This is the Hook — confirm it now with the formal method.)*
- **Worked example, Tier 3 (primes):** *"2, 3, 5, 7, 11, 13, ?"* — each term is the next prime number → **17**.
- **Worked example, Tier 3 (perfect squares):** *"1, 4, 9, 16, ?"* — each term is n² (1², 2², 3², 4²) → **25**.
- **Say explicitly:** *"Notice the order matters — if you jump straight to checking for primes on a series that's just simple addition, you'll waste time. Always check Tier 1 first, then Tier 2, and only reach for Tier 3 or 4 if the simpler tiers don't fit."*

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"5, 10, 15, 20, ? — which tier does this belong to, and what's the answer?"*
> **Answer:** Tier 1 (constant addition, +5 each time) → **25**.

---

## ⚡ ALS Activity 1 — Whiteboard Race: Which Tier? (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to identify both the correct tier AND the missing term for an assigned series, first correct board up wins the round. Chosen to build fast, disciplined tier-checking (not guessing) before Teaching Block B introduces multi-operator patterns.

**Setup line:**
> *"Pairs, boards up. I'll give you a series — write down which tier it belongs to AND the missing term. First correct board up wins. Three rounds."*

- Round 1: *"7, 14, 21, 28, ?"* → Tier 1 (constant +7) → **35**.
- Round 2: *"3, 9, 27, 81, ?"* → Tier 2 (constant ×3) → **243**.
- Round 3: *"25, 36, 49, 64, ?"* → Tier 3 (perfect squares, 5², 6², 7², 8²) → **81**.

**How it surfaces:** After each round, have the winning pair name the tier out loud before revealing the number — the tier identification is the actual skill, the arithmetic is just execution.

**Debrief line:**
> *"Every single series you just solved took less than ten seconds once you named the tier correctly. Naming the tier isn't a side step — it IS the solving step."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but always require the tier to be named before the answer.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: multi-operator series, second-order patterns, and finding the incorrect term.

**Beats to emphasise**

- **Multi-operator series (Tier 4).** The operation itself changes, but the *change* follows its own pattern.
- **Worked example, live (from the source, verified):** *"2, 5, 10, 17, 26, ?"*
  1. Differences: 5−2=3, 10−5=5, 17−10=7, 26−17=9.
  2. The differences themselves form a pattern: **3, 5, 7, 9** — increasing by 2 each time (a second-order pattern).
  3. Next difference: 9+2 = **11**.
  4. Next term: 26 + 11 = **37**.
- **Finding the incorrect term — a different question type.** Instead of finding what comes next, you're told a full series and must find which ONE term breaks an otherwise consistent pattern.
- **Worked example, live:** *"3, 6, 12, 24, 50, 96 — one term is wrong. Which one, and what should it be?"*
  1. Check Tier 2 first: 3→6 (×2), 6→12 (×2), 12→24 (×2), 24→**50**? Should be ×2 = 48, not 50. 50→96 is roughly ×2 again (48×2=96 would fit, but 50×2=100≠96) — this confirms **50 is the outlier**, not 96.
  2. Correct series: 3, 6, 12, 24, **48**, 96 — consistent ×2 throughout.

**Checkpoint (at 32 min)** — cold-call:
> *"4, 8, 12, 16, 22, 24 — one term is wrong. Which one?"*
> **Answer:** Pattern is +4 each time (4,8,12,16,20,24) → **22 is wrong**, should be 20.

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: Spot the Fake (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students commit to which term is wrong before the method is walked through. Deliberately different register from Activity 1's loud paired race (quiet, individual, single big reveal), and targets the "incorrect term" question type specifically, since it requires more careful checking than a simple missing-term question.

**Setup line:**
> *"On your own, ninety seconds. Series: 5, 10, 20, 42, 80, 160. One term is wrong. Which one, and what should it actually be? Write your answer, hold it up when I say show."*

Give 90 seconds silent work, then: *"Show me — three, two, one, show."*

**The reveal, step by step:**
1. Check Tier 2 (constant ratio): 5→10 (×2), 10→20 (×2), 20→**42**? Should be ×2 = 40, not 42.
2. Confirm forward: 42→80 is not a clean ×2 either (42×2=84≠80), but 40×2=80 fits perfectly.
3. Confirm again: 80→160 (×2) ✔ consistent.
4. **42 is the outlier — it should be 40.** Corrected series: 5, 10, 20, 40, 80, 160.

**Debrief line:**
> *"The trap in 'incorrect term' questions is that the error can throw off your very next check too, if you're not careful — always verify against terms further away, not just the one immediately next to the suspect, before you commit to an answer."*

**Cut rule:** If running short, cut the silent window to 60 seconds but always show the full double-check (both the term before AND after the suspect) in the reveal — that double-check is the actual lesson.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — pose one more multi-operator series and solve together — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> 1, 8, 27, 64, ? — what comes next, and which tier does it belong to?
> **Answer:** Perfect cubes (1³, 2³, 3³, 4³) → Tier 3 → **125 (5³)**.

Scan responses on the way out — if the tier-checking order isn't sticking, revisit briefly at the start of Session 14.

**Homework**

| Task | Note |
|---|---|
| Solve: 6, 11, 16, 21, ? and 4, 12, 36, 108, ? | Self-check — one is Tier 1, one is Tier 2, identify which |
| Find the incorrect term: 2, 4, 6, 9, 10, 12 | Self-check using the double-check method from Activity 2 |

Tell them: *"Number series is about letters wearing numbers, and next session it's numbers wearing letters — Session 14 is Alphabet Series, where the exact same tier logic applies to the alphabet instead."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| You should try the most "interesting" pattern (primes, squares) first | Advanced patterns feel more impressive/likely to be the "real" answer | Teaching Block A's explicit tier-order rule (simplest first) |
| A multi-operator series has no pattern at all, it's random | Doesn't recognise the differences themselves can form a pattern | Teaching Block B's second-order (difference-of-differences) framing |
| "Incorrect term" questions can be solved by checking one neighbour only | Assumes the first mismatch found is automatically the error | ALS Activity 2's explicit double-check-both-sides method |
| Every series needs the full four-tier check even when Tier 1 obviously fits | Habit of over-verifying instead of trusting a clean fit | Teaching Block A's "only move to the next tier if the simple one fails" framing |
| Finding a missing term and finding an incorrect term are the same skill | Both involve "the pattern," feels like one question type | Teaching Block B's explicit distinction between the two question types |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from a text extraction of the Concept Explanation/Introduction/Closure sections. The "Problem Solving" sub-page is image-only and unrecoverable — all worked/practice problems in this plan are **instructor-authored**, though the 2-5-10-17-26→37 multi-operator example directly matches the source's own stated figures.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, focused on the trickier "incorrect term" question type.
- **First session of the Coding and Decoding topic** — warm-up poll is diagnostic, not retrieval.
- Classroom Quiz slot reserved-empty per site convention.
