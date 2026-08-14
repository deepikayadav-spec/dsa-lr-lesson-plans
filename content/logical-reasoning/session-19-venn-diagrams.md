# Session 19 — Venn Diagrams: Sets, Overlaps & Exact Counts

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Union/intersection/complement, two-set and three-set worked problems, and exact-count phrasing ("exactly two," "only," "at least one") · **Prerequisite** None specific — first session of the Venn Diagrams topic
**Session type** Lecture + guided practice. No source slide deck — content from the session's concept-explanation text. No classroom quiz bank yet — 5-min slot reserved at end. the "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

**Note on the three-set worked example:** the source's own three-set example (aptitude/technical/HR clearance) is missing one pairwise overlap value in the extracted text, making it unsolvable as given. Teaching Block B below uses a fully self-consistent instructor-constructed three-set example instead, built in the same spirit (recruitment-style clearance data) and independently verified.

---

## Learning Objectives

By the end of this session, students will be able to:

1. Define union, intersection, and complement, and represent them with overlapping circles. *(UNDERSTANDING)*
2. Solve a two-set problem for "only A," "only B," and "neither." *(APPLYING)*
3. Solve a three-set problem by filling from the deepest overlap outward. *(APPLYING)*
4. Correctly interpret exact-count phrasing — "exactly two," "only," "at least one." *(ANALYZING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Draw two large overlapping circles, unlabelled, as a running reference.

---

## Warm-Up Poll — Diagnostic (3–7 min) · ALS: Polling

> New topic — Venn Diagrams doesn't build directly on Blood Relations, so this poll is diagnostic, not retrieval.

Say: *"Five quick questions before we start."*

**Q1.** In a Venn diagram, what does the overlapping region between two circles represent?
`A` Elements in neither set · `B` Elements shared by both sets · `C` Elements only in one set
→ *Read:* B is correct.

**Q2.** Have you solved a "how many like both / only one" survey-style question before?
`A` Never · `B` Once or twice · `C` Regularly
→ *Read:* If mostly A, spend extra time on the two-set method before speeding into three sets.

**Q3.** Quick riddle: a class survey finds 12 people like Pizza, 10 like Burgers, 5 like both. How many like ONLY Pizza?
`A` 12 · `B` 7 · `C` 5 · `D` Not sure
→ *Read:* B is correct (12−5=7). Don't confirm fully yet — this is the Hook.

**Q4.** If a question asks "exactly two" out of three groups, does that include people in all three?
`A` Yes, all three counts as two-plus · `B` No, "exactly two" means precisely two, not three
→ *Read:* B is correct — this exact distinction trips up most students; seed it now, resolve it fully in Teaching Block B.

**Q5.** How comfortable are you with three overlapping circles (not just two)?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, slow down through Teaching Block B's three-set methodology.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"We surveyed the class: 'Who likes Pizza, Burgers, or both?' 12 people like Pizza, 10 like Burgers, 5 like both. How many people like only one of them — not both?"*

Give 30 seconds, then solve together on the board: *"Only Pizza = 12 total Pizza-likers minus the 5 who also like Burgers = 7. Only Burgers = 10 minus 5 = 5. Only one, total = 7 + 5 = 12."*

> *"Three numbers, one quick diagram, and the messy-sounding question turns into simple subtraction. That's the entire power of Venn diagrams — today you'll do this with two circles, then three, then handle trickier phrasing like 'exactly two' and 'at least one.'"*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

Covers: union/intersection/complement definitions → the two-set method, worked live.

**Beats to emphasise**

- **Three essential operations, write on the board:**
  - **Union (A ∪ B):** everyone in A, or B, or both.
  - **Intersection (A ∩ B):** only the people common to both A and B.
  - **Complement:** everyone in the universal set (μ) who is outside all the circles entirely.
- **Two-set method, in order:**
  1. Draw two overlapping circles.
  2. Fill the overlap (intersection) first — it's the most specific piece of information.
  3. Subtract the overlap from each circle's total to get "only A" and "only B."
  4. If a total surveyed number is given, subtract everyone accounted for to find "neither."
- **Worked example, live (from the source, verified):** *"Among 200 students — 120 like tea, 100 like coffee, 40 like both. Find those preferring only one beverage, or neither."*
  1. Both (intersection) = **40**.
  2. Only tea = 120 − 40 = **80**.
  3. Only coffee = 100 − 40 = **60**.
  4. Only one (either, not both) = 80 + 60 = **140**.
  5. Neither = 200 − (80 + 60 + 40) = 200 − 180 = **20**.

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"150 people surveyed — 90 like reading, 70 like gaming, 30 like both. How many like neither?"*
> **Answer:** Only reading = 90−30=60. Only gaming = 70−30=40. Accounted for = 60+40+30=130. Neither = 150−130 = **20**.

---

## ⚡ ALS Activity 1 — Whiteboard Race: Two-Set Sprint (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to find "only A," "only B," and "neither" for an assigned two-set scenario, first correct board up wins the round. Chosen to drill the two-set method into fast recall before Teaching Block B introduces the harder three-set case.

**Setup line:**
> *"Pairs, boards up. I'll give you survey numbers — find 'only A,' 'only B,' and 'neither' if I give you a total. First correct board up wins. Three rounds."*

- Round 1: *"100 surveyed — 60 like cricket, 50 like football, 25 like both. Find 'only cricket' and 'only football.'"* → Only cricket = 60−25=**35**. Only football = 50−25=**25**.
- Round 2: *"Using Round 1's numbers, find 'neither.'"* → Accounted for = 35+25+25=85. Neither = 100−85=**15**.
- Round 3: *"80 surveyed — 50 like tea, 45 like coffee, 20 like both. Find 'neither.'"* → Only tea=30, only coffee=25, accounted=30+25+20=75. Neither=80−75=**5**.

**How it surfaces:** After each round, have the winning pair state which step they did first (fill the overlap) before revealing their answer — reinforces the "overlap first" discipline.

**Debrief line:**
> *"Every single one of these started the same way — fill the overlap first, then subtract. That single habit is 90% of solving any two-set Venn problem correctly."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but always require "overlap first" to be stated.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: three-set methodology, worked live, and exact-count phrasing.

**Beats to emphasise**

- **Three-set methodology, write on the board:**
  1. Draw three overlapping circles.
  2. **Start from the deepest overlap** — the very center, where all three sets meet.
  3. **Fill outer areas next**, working from the three-way overlaps outward to the two-way overlaps, then the "only" regions.
  4. Use subtraction to find anyone outside all three sets.

**The worked example (instructor-constructed, 300 candidates, three recruitment clearance stages):**

| Region | Count |
|---|---|
| All three (Aptitude ∩ Technical ∩ HR) | 20 |
| Aptitude & Technical only | 30 |
| Aptitude & HR only | 15 |
| Technical & HR only | 10 |
| Aptitude only | 60 |
| Technical only | 45 |
| HR only | 35 |
| Cleared none | 85 |

- **Worked derivation, live:**
  1. Start at the center: all three = **20**.
  2. Fill the two-way overlaps: Aptitude&Technical only=30, Aptitude&HR only=15, Technical&HR only=10.
  3. Fill the "only" regions: Aptitude only=60, Technical only=45, HR only=35.
  4. Check the total: 20+30+15+10+60+45+35 = 215 accounted for. Cleared none = 300−215 = **85**.
- **Exact-count phrasing, resolve explicitly (ties to poll Q4):**
  - **"Exactly two"** = the three two-way-only regions, NOT the center: 30+15+10 = **55**.
  - **"Only HR"** = the HR-only region alone: **35**.
  - **"At least one"** = everyone except "cleared none": 300−85 = **215**.
- **Say explicitly:** *"'Exactly two' deliberately excludes the center — someone who cleared all three cleared more than two, so they don't count. This is the single most common point students lose marks on."*

**Checkpoint (at 32 min)** — cold-call:
> *"Using the table above, how many candidates cleared at least two stages (two OR three)?"*
> **Answer:** Exactly two (55) + all three (20) = **75**.

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: Three Sports (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students solve a fresh three-set problem entirely on their own before the reveal. Deliberately different register from Activity 1's loud paired race (quiet, individual, single big reveal), and specifically targets the "exactly two" vs. "at least one" distinction from Teaching Block B.

**Setup line:**
> *"On your own, three minutes. 200 students surveyed on sports: Cricket, Football, Basketball.*
> *All three: 10. Cricket & Football only: 15. Cricket & Basketball only: 8. Football & Basketball only: 12.*
> *Cricket only: 50. Football only: 35. Basketball only: 30.*
> *Find: (1) how many played none, and (2) how many played exactly two. Write both answers, hold up when I say show."*

Give 3 minutes silent work, then: *"Show me — three, two, one, show."*

**The reveal, step by step:**
1. Sum everything accounted for: 10+15+8+12+50+35+30 = **160**.
2. **Played none** = 200 − 160 = **40**.
3. **Exactly two** = the three two-way-only regions: 15+8+12 = **35** (the center, 10, is excluded — those played all three, not exactly two).

**Debrief line:**
> *"If your 'exactly two' answer was 45 instead of 35, you added the center in by mistake — that's the trap this entire session was built around. 'Exactly' means precisely that number, no more."*

**Cut rule:** If running short, cut the silent window to 2 minutes but always ask both questions in the reveal (none, and exactly two) — the contrast between them is the point.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — pose one more "at least one" or "exactly one" question on the sports data and solve together — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> Using today's sports survey data, how many students played at least one sport?
> **Answer:** Total − none = 200 − 40 = **160**.

Scan responses on the way out — if the "start from the center" discipline isn't sticking for three-set problems, revisit briefly at the start of Session 20.

**Homework**

| Task | Note |
|---|---|
| Using the recruitment clearance table from Teaching Block B, find "only Aptitude or only Technical" (not both, not HR) | Self-check — combines two "only" regions |
| Draw your own two-set survey (any topic, any numbers) and compute "only A," "only B," and "neither" | Self-check — full application of the two-set method |

Tell them: *"Venn diagrams handle categories and counts. Session 20 moves into Syllogisms, where the exact same overlapping-circle idea is used to test whether a logical conclusion is actually valid."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| "Exactly two" includes people in all three groups | "Two or more" feels like the natural reading of "two" | Teaching Block B's explicit exclusion + Activity 2's reveal |
| A three-set problem should be filled from the outside in | Feels natural to start with the "only" regions since they're named first | Teaching Block B's explicit "deepest overlap first" rule |
| "Only A" means the same as "A" (the whole circle) | Doesn't separate the full circle total from the exclusive region | Teaching Block A's explicit subtraction step |
| "At least one" and "exactly one" mean the same thing | Both sound like a low, specific count | Teaching Block B's explicit at-least-one calculation (total minus none) contrasted with exactly-two |
| A missing pairwise overlap value means the problem can't be solved at all | Doesn't distinguish which specific question can still be answered with partial data | Instructor note — flagged directly where the source's own example fell short |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from a text extraction of the Concept Explanation/Introduction/Closure sections. The "Problem Solving" sub-page is image-only and unrecoverable. The Pizza/Burger Hook and the 200-student tea/coffee example directly match the source's own stated figures; the three-set recruitment-clearance table in Teaching Block B is **instructor-constructed** (the source's own three-set example was missing a required pairwise value in the extracted text) and independently verified to sum correctly across every region.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive, two-set only; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, three-set, targeting the "exactly two" trap specifically.
- **First session of the Venn Diagrams topic** — warm-up poll is diagnostic, not retrieval.
- Classroom Quiz slot reserved-empty per site convention.
