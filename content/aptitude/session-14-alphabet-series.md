# Session 14 — Coding & Decoding: Alphabet Series

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** The EJOTY shortcut, forward/alternate letter patterns, reverse alphabet numbering, and wraparound logic · **Prerequisite** Number Series — the tier-based pattern-checking discipline, applied here to letters
**Session type** Lecture + guided practice. No source slide deck — content from the session's concept-explanation text. No classroom quiz bank yet — 5-min slot reserved at end. the "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

---

## Learning Objectives

By the end of this session, students will be able to:

1. Use the EJOTY shortcut (E=5, J=10, O=15, T=20, Y=25) to find a letter's position without counting from A. *(APPLYING)*
2. Convert letters to numeric positions and identify forward-series patterns. *(APPLYING)*
3. Recognise alternate-position patterns where odd and even positions follow separate rules. *(ANALYZING)*
4. Apply reverse alphabet numbering (A=26 ... Z=1) and wraparound logic (beyond Z, or before A). *(APPLYING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Write the alphabet A–Z across the board with position numbers 1–26 underneath, for quick reference all session.

---

## Warm-Up Poll — Retrieval Practice on Session 13 (3–7 min) · ALS: Polling

Say: *"Five quick ones from last session."*

**Q1.** 3, 6, 9, 12, ? — what comes next, and which tier?
`A` 14, Tier 2 · `B` 15, Tier 1 · `C` 16, Tier 3
→ *Read:* B is correct.

**Q2.** What order should you check the four tiers in?
`A` Multiply/divide first, always · `B` Simplest (add/subtract) first, then increasingly complex · `C` Whichever tier looks most interesting
→ *Read:* B is correct.

**Q3.** If A=1, B=2, C=3 ... what number is J?
`A` 9 · `B` 10 · `C` 11
→ *Read:* B is correct — seeds today's topic directly.

**Q4.** Quick riddle: if A=1, B=2, C=3... what's the sum of the letter positions in the word "CAT"?
`A` 20 · `B` 22 · `C` 24 · `D` Not sure
→ *Read:* C is correct. Don't confirm yet — this is the Hook, solved together right after.

**Q5.** How comfortable are you counting letter positions quickly (e.g. "what number is R?") without counting from A each time?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, spend extra time on the EJOTY shortcut in Teaching Block A.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"If A=1, B=2, C=3, and so on — what's the sum of the letter positions in the word CAT?"*

Give students 30 seconds, then solve together: *"C is the 3rd letter. A is the 1st. T is the 20th. 3 + 1 + 20 = 24."*

> *"You just solved your first alphabet series question — and you didn't need to count from A to T on your fingers to do it, because by the end of today, you won't need to count from A at all. There's a shortcut that gets you there in seconds."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

Covers: the EJOTY shortcut → forward series patterns.

**Beats to emphasise**

- **The EJOTY shortcut — write it on the board exactly like this:** **E=5, J=10, O=15, T=20, Y=25.** These five letters are evenly spaced 5 apart through the alphabet — memorise just these five, and you can find any letter's position by counting a short distance from the nearest one, instead of counting from A every time.
- **Worked example, live:** *"What position is R?"* R is 3 letters before T (T=20). 20 − 3 = **17**. Confirm: R is indeed the 17th letter.
- **Worked example, live:** *"What position is L?"* L is 2 letters after J (J=10). 10 + 2 = **12**. Confirm: L is indeed the 12th letter.
- **Forward series patterns.** Once letters are converted to numbers, the exact same Tier 1/Tier 2 logic from Number Series applies.
- **Worked example, live (from the source, verified):** *"A, C, E, G, ?"* — positions are 1, 3, 5, 7 — constant +2 each step → next position 9 → **I**.

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"Using EJOTY, what position is W, and what letter comes 3 positions after W?"*
> **Answer:** W is 3 before Y (Y=25) → position **22**. 3 positions after = position 25 → **Y**.

---

## ⚡ ALS Activity 1 — Whiteboard Race: EJOTY Sprint (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to find a letter's position (or a position's letter) using the EJOTY shortcut, first correct board up wins the round. Chosen to drill the shortcut into fast recall before Teaching Block B introduces more complex patterns.

**Setup line:**
> *"Pairs, boards up, EJOTY visible. I'll call a letter or a position — find the match using the shortcut, not by counting from A. First correct board up wins. Three rounds."*

- Round 1: *"What position is N?"* → N is 1 after J-ish... actually nearest anchor is O(15), N is 1 before O → **14**.
- Round 2: *"What letter is at position 8?"* → 3 before J(10) → **H**.
- Round 3: *"What position is V?"* → V is 5 after T(20) → **22**.

**How it surfaces:** After each round, ask the winning pair which EJOTY anchor they used — reinforces choosing the *nearest* anchor, not always the same one.

**Debrief line:**
> *"Five letters memorised, and now every single letter in the alphabet is at most 4 steps away from one of them. That's the whole shortcut."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but always require students to name which anchor letter they used.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: alternate-position patterns, reverse alphabet numbering, and wraparound logic.

**Beats to emphasise**

- **Alternate patterns — two rules running at once.** *"A, D, B, F, C, H"* — this looks irregular until you split it into two interleaved series: odd positions in the sequence (A, B, C — 1st, 3rd, 5th terms) follow one rule (+1 each: A→B→C), and even positions (D, F, H — 2nd, 4th, 6th terms) follow a different rule (+2 each: D→F→H). *"Always check if a series makes more sense split into two alternating tracks before giving up on it."*
- **Reverse alphabet numbering.** Sometimes a question flips the whole system: **A=26, B=25, C=24, ... Z=1.** The relationship to the normal position is simple: **Reverse position = 27 − Normal position.**
- **Worked example, live:** *"In reverse numbering, what's the value of D?"* D's normal position is 4. Reverse = 27 − 4 = **23**.
- **Wraparound logic.** If a series' pattern pushes past Z, wrap back around: **Z+1 = A, Z+2 = B**, and so on — treat the alphabet as a loop of 26, not a hard stop.
- **Worked example, live:** *"If you start at X and move forward 5 positions, where do you land?"* X=24. 24+5=29. Since 29 > 26, wrap: 29−26=**3** → **C**.

**Checkpoint (at 32 min)** — cold-call:
> *"In reverse alphabet numbering, what letter has value 20?"*
> **Answer:** Reverse = 27 − Normal → 20 = 27 − Normal → Normal = **7** → **G**.

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: Crack the Reverse Code (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students commit to an answer before the method is walked through. Deliberately different register from Activity 1's loud paired race (quiet, individual, single big reveal), and combines reverse-numbering with wraparound in one problem.

**Setup line:**
> *"On your own, two minutes. Using reverse alphabet numbering (A=26 ... Z=1), find the sum of the reverse-values of the letters in the word 'BAG'. Write your answer, hold it up when I say show."*

Give 2 minutes silent work, then: *"Show me — three, two, one, show."*

**The reveal, step by step:**
1. B's normal position = 2 → reverse = 27−2 = **25**.
2. A's normal position = 1 → reverse = 27−1 = **26**.
3. G's normal position = 7 → reverse = 27−7 = **20**.
4. Sum = 25+26+20 = **71**.

**Debrief line:**
> *"Same CAT-style sum from the Hook, just with the reverse rule instead of the normal one. The method never changes — convert every letter first, then combine. That discipline is what makes these questions fast instead of confusing."*

**Cut rule:** If running short, cut the silent window to 90 seconds but always show the letter-by-letter conversion in the reveal, not just the final sum — the conversion is the actual skill.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — pose one more alternate-pattern series and solve together — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> Using EJOTY, what position is Q?
> **Answer:** Q is 5 before Y(25)? No — nearest anchor is O(15), Q is 2 after O → **17**.

Scan responses on the way out — if the "nearest anchor" instinct isn't landing, revisit briefly at the start of Session 15.

**Homework**

| Task | Note |
|---|---|
| Find the sum of the normal positions of the letters in your own first name | Self-check using EJOTY |
| B, E, C, G, D, I — split into two alternating tracks and find the pattern in each | Self-check using the alternate-pattern method from Teaching Block B |

Tell them: *"You now read letters as numbers as fluently as you read numbers as numbers. Session 15 combines both — Odd Man Out and Analogy, where you'll spot which item breaks a pattern, or how two pairs relate."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| You must count from A every time to find a letter's position | Not yet trusting the EJOTY shortcut | ALS Activity 1's repeated drilling, always requiring the anchor to be named |
| An alternating series (A,D,B,F,C,H) has no real pattern | Doesn't think to split into two interleaved tracks | Teaching Block B's explicit two-track framing |
| Reverse alphabet numbering means literally reading the alphabet backwards in your head | Overcomplicates instead of using the 27−position formula | Teaching Block B's explicit "Reverse = 27 − Normal" formula |
| Going past Z means the series has ended or is invalid | No exposure to circular/wraparound logic before this session | Teaching Block B's explicit wraparound worked example |
| Alphabet series is a totally different skill from number series | Letters "feel" different from numbers | Hook + Teaching Block A's explicit "convert to numbers, same tier logic" framing |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from a text extraction of the Concept Explanation/Introduction/Closure sections. The "Problem Solving" sub-page is image-only and unrecoverable — all worked/practice problems in this plan are **instructor-authored**, though the CAT=24 Hook and the A,C,E,G→I forward series directly match the source's own stated examples.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, combining reverse-numbering and multi-letter summation.
- **Second session of the Coding and Decoding topic** — warm-up poll is retrieval practice on Session 13 (Number Series), since the tier-logic discipline carries over directly.
- Classroom Quiz slot reserved-empty per site convention.
