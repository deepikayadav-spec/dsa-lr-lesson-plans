# Session 9 — Ranking: Position in a Row

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Ranking from either end, total-persons formulas, position-between-two-people, and position swaps · **Prerequisite** None specific — first session of the Ranking topic
**Session type** Lecture + guided practice. No source slide deck — content from GitBook Concept Explanation text. No classroom quiz bank yet — 5-min slot reserved at end. GitBook "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

| Resource | Status |
|---|---|
| Source | GitBook: `session-plans/logical-reasoning/ranking` (Learning Outcomes, Ideal Format, Introduction, Concept Explanation, Closure — text extracted) |
| Problem Solving bank (GitBook) | image-only, not recoverable — practice problems below are instructor-authored |
| Classroom Quiz | not yet available — 5-min slot reserved at end of session |

---

## Learning Objectives

By the end of this session, students will be able to:

1. Convert a rank from one end of a row to the rank from the other end, given the total. *(APPLYING)*
2. Apply Total = Left rank + Right rank − 1 when both ranks describe the *same* person. *(APPLYING)*
3. Apply Total = Left rank + Right rank + Between-count when the ranks describe *two different* people. *(APPLYING)*
4. Recalculate a rank after two people swap positions in a row. *(APPLYING)*
5. Distinguish which of the two "total" formulas applies to a given question. *(EVALUATING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Draw a simple row of blank position markers (dashes) to represent a line/queue.

---

## Warm-Up Poll — Diagnostic (3–7 min) · ALS: Polling

> New topic — Ranking doesn't build directly on Data Interpretation, so this poll is diagnostic, not retrieval.

Say: *"Five quick questions before we start."*

**Q1.** If you're 5th from the front of a queue of 12 people, roughly how far from the back are you?
`A` 5th · `B` 7th · `C` 8th · `D` Not sure
→ *Read:* B is correct (12−5+1=8th... wait check live, don't confirm the exact number yet, just gauge instinct.

**Q2.** Have you solved a "ranking in a row" question before (school, coaching, mock test)?
`A` Never · `B` Once or twice · `C` Regularly
→ *Read:* If mostly A, spend extra time on the conversion formula before speeding up.

**Q3.** If two different formulas both use the words "left rank" and "right rank," what's the one thing you'd want to check before picking which one to use?
`A` Whether it's the same person or two different people · `B` Whether the row is long or short · `C` Not sure
→ *Read:* A is the exact distinction this session teaches — don't confirm yet, let Teaching Block B land it.

**Q4.** Quick riddle to hold onto: you're 5th from the left in a queue, your friend is 7th from the right, and there are 11 people between you two. Guess — roughly how many people are in the queue total?
`A` 13 · `B` 18 · `C` 23 · `D` Not sure
→ *Read:* C is correct. Don't reveal — this is the Hook's unanswered question, solved fully in Activity 2.

**Q5.** How comfortable are you visualizing a row of people from a word problem, without drawing it?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, lean hard on board diagrams throughout today's session.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"You're 5th in a queue from the left. Your friend is 7th from the right. There are exactly 11 people standing between the two of you. How many people are in the queue, total?"*

Take 2–3 shouted guesses, write them on the board without confirming or denying.

> *"Hold onto your guess. This looks like a simple counting problem, but it actually needs two different formulas to solve correctly — and picking the wrong one is the single most common mistake on this topic. By the time we're done today, you'll solve this exact riddle in under 15 seconds."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

<!-- placement: inferred grouping — no source deck; grouped from GitBook Concept Explanation extraction -->
Covers: ranking from one end → converting between ends → the same-person total formula.

**Beats to emphasise**

- **Ranking from one end.** A row/queue can be ranked from the left or from the right — the same person has two different rank numbers depending on which end you count from.
- **Conversion formula, write on the board:** **Rank from Right = Total − Rank from Left + 1** (and symmetrically, Rank from Left = Total − Rank from Right + 1).
- **Worked example, live (from the source, verified):** *"Rahul is 7th from the left in a row of 20 students. What's his rank from the right?"*
  - Rank from right = 20 − 7 + 1 = **14th**.
- **Same-person total formula.** If you're told *one person's* rank from the left AND their rank from the right, you can find the total row size directly: **Total = Rank from Left + Rank from Right − 1**. *(The −1 exists because that one person gets counted once in each rank — without subtracting, you'd double-count them.)*
- **Worked example, live:** *"A student is 9th from the left and 15th from the right. How many students are in the row?"*
  - Total = 9 + 15 − 1 = **23**.
- **Say explicitly:** *"Notice — this −1 formula only works when both ranks describe the SAME person. Keep that in your head, because Teaching Block B is going to give you a formula that looks almost identical but is used for a completely different situation."*

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"Priya is 12th from the left in a row of 30. What's her rank from the right?"*
> **Answer:** 30 − 12 + 1 = **19th**.

---

## ⚡ ALS Activity 1 — Whiteboard Race: Flip the Rank (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to convert a rank from one end to the other, or find the total from one person's two ranks, first correct board up wins the round. Chosen to drill the conversion and same-person-total formulas into fast recall before Teaching Block B introduces the two-person case.

**Setup line:**
> *"Pairs, boards up. I'll give you either a conversion problem or a same-person-total problem. First correct board up wins. Three rounds."*

- Round 1: *"A person is 6th from the left in a row of 25. Find their rank from the right."* → 25−6+1 = **20th**.
- Round 2: *"A person is 4th from the left and 21st from the right. Find the total."* → 4+21−1 = **24**.
- Round 3: *"A person is 17th from the right in a row of 30. Find their rank from the left."* → 30−17+1 = **14th**.

**How it surfaces:** After each round, have the winning pair state out loud which formula they used — reinforces that Round 2 is a genuinely different formula from Rounds 1 and 3, not just the same one rearranged.

**Debrief line:**
> *"Two formulas so far, both starting from 'rank from one end plus rank from the other end.' The next one looks almost the same on paper — but it's for a totally different kind of question. Watch closely."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but always require the formula to be named out loud.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: position between two *different* people, and position swaps.

**Beats to emphasise**

- **The two-person case — a different formula entirely.** When the left-rank and right-rank describe **two different people**, and you're also told how many people stand *between* them, use: **Total = Left rank + Right rank + Between-count** — no subtraction this time, because there's no double-counted person to remove.
- **Worked example, live (from the source, verified):** *"In a group of 14, person A is 4th from the left, person B is 9th from the right. How many people sit between them?"*
  1. First convert B's rank to "from the left": 14 − 9 + 1 = **6th from the left**.
  2. A is at position 4, B is at position 6 → only position 5 sits between them → **1 person between them**.
  3. Cross-check using the formula in reverse: Total = 4 + 9 + 1 = **14** ✔ matches the given total.
- **Watch for trap words:** "exactly between," "inclusive," "only those in between" all change whether you count the two named people themselves or not — always re-read the question before finalising the count.
- **Position swaps.** *"The row doesn't change — only the two people's positions are exchanged."* If two people swap seats, each one simply takes on the other's old rank; nobody else in the row moves.
- **Worked example, live:** *"In a row of 30 students, Aisha is 12th from the left and Meera is 18th from the left. They swap places. What is Meera's new rank from the left?"*
  - Meera now occupies Aisha's old seat → Meera's new rank = **12th**.

**Checkpoint (at 32 min)** — cold-call:
> *"Which formula do you use when the question gives you ranks for two different people, plus a between-count — the '−1' one or the '+between' one?"*
> **Answer:** The **'+between'** one — Total = Left rank + Right rank + Between-count.

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: Solve the Hook (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students commit to a number before the method is walked through, closing the loop opened at the start of class. Deliberately different register from Activity 1's loud paired race (quiet, individual, single big reveal).

**Setup line:**
> *"Back to the start of class. You're 5th from the left, your friend is 7th from the right, 11 people stand between you. On your own, ninety seconds — how many people total? Write your answer, hold it up when I say show."*

Give 90 seconds of silent solo work, then: *"Show me — three, two, one, show."* Compare to the guesses written on the board at the start of class.

**The reveal, step by step:**
1. This is the **two-different-people** case — you and your friend are two separate people, not one person measured from both ends.
2. Correct formula: **Total = Left rank + Right rank + Between-count**.
3. Total = 5 + 7 + 11 = **23**.
4. *"If anyone used the −1 formula instead and got 21, that's the trap this whole session was built to catch — that formula is only for a single person's two ranks, not two different people."*

**Debrief line:**
> *"Same numbers, two totally different answers depending on which formula you pick. The math was never the hard part today — knowing which formula applies was."*

**Cut rule:** If running short, skip the 90-second silent window and solve it together on the board — but always show the wrong (−1 formula) answer alongside the right one, so the contrast is explicit.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — pose one more two-person between-count problem with different numbers and solve together — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> A single student is 8th from the left and 13th from the right. How many students are in the row?
> **Answer:** 8 + 13 − 1 = **20**. *(Same-person case — the −1 formula.)*

Scan responses on the way out — if students use the +between formula here by mistake, that's the core distinction not yet landed; revisit briefly at the start of Session 10.

**Homework**

| Task | Note |
|---|---|
| Two different people: one is 6th from the left, the other is 10th from the right, with 15 people between them. Find the total. | Self-check using Total = Left + Right + Between |
| In a row of 40, two students swap positions — one was 5th from the left, the other 5th from the right. Find each student's new rank from the left. | Self-check — position-swap logic from Teaching Block B |

Tell them: *"Ranking is about picking the right formula for the right setup, not memorising numbers. Session 10 moves to Directions — tracking movement and turns, a different kind of spatial reasoning."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| The −1 total formula always applies, regardless of one person or two | Both formulas "look" similar (left + right, a small adjustment) | ALS Activity 2's explicit wrong-vs-right contrast |
| "Between" always means the same thing regardless of question wording | Doesn't register that "inclusive," "exactly," "only" change the count | Teaching Block B's explicit trap-words callout |
| A position swap changes everyone else's rank in the row too | Assumes swapping ripples through the whole line like a physical shuffle | Teaching Block B's explicit "only the two swap, nobody else moves" framing |
| Rank-from-right is always Total minus rank-from-left (no +1) | Off-by-one error, forgetting the person themselves is a position | Teaching Block A's explicit "+1" emphasis in the conversion formula |
| Two-person "between" problems can be solved without converting to the same end first | Tries to subtract ranks measured from opposite ends directly | Teaching Block B's explicit two-step (convert, then subtract/count) worked example |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from GitBook Concept Explanation/Introduction/Closure text extraction. GitBook's "Problem Solving" sub-page (8 questions, Q1–Q8) is image-only and unrecoverable — all worked/practice problems in this plan are **instructor-authored**, though the Rahul (7th/20 row) and 4th-from-left/9th-from-right/14-total examples directly match the source's own stated figures.
- **The two-formula distinction (same-person −1 vs. two-person +between) is the pedagogical core of this session** — it's built into the Hook, both Teaching Blocks, and Activity 2's reveal. Protect this thread above all else if running behind.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, and deliberately closes the exact riddle posed in the Hook.
- **First and only session for this topic** (Ranking is a single-session topic per the course structure) — warm-up poll is diagnostic, not retrieval.
- Classroom Quiz slot reserved-empty per site convention.
