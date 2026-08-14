# Session 6 — Data Interpretation: Tables

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Reading tabular data, and applying averages/percentages/comparisons to answer table-based questions · **Prerequisite** None specific — first session of the Data Interpretation sub-topic (draws on general percentage/ratio/average familiarity)
**Session type** Lecture + guided practice. No source slide deck — content from GitBook Concept Explanation text. No classroom quiz bank yet — 5-min slot reserved at end. GitBook "Problem Solving" page is image-only and unrecoverable — all practice problems and the data table below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

| Resource | Status |
|---|---|
| Source | GitBook: `session-plans/logical-reasoning/data-interpretation/di-tables` (Learning Outcomes, Ideal Format, Introduction, Concept Explanation, Closure — text extracted) |
| Problem Solving bank (GitBook) | image-only, not recoverable — practice table and problems below are instructor-authored |
| Classroom Quiz | not yet available — 5-min slot reserved at end of session |

---

## Learning Objectives

By the end of this session, students will be able to:

1. Identify rows, columns, and headers in a data table and state what each represents. *(REMEMBERING)*
2. Apply the four-step method — read, understand the question, apply the right math, ignore the noise — to a table-based question. *(APPLYING)*
3. Calculate percentage change, averages, and comparisons directly from tabular data. *(APPLYING)*
4. Decide when exact calculation is needed versus when quick approximation is safe. *(EVALUATING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Draw a simple empty 4-row × 4-column table grid to have on hand.

---

## Warm-Up Poll — Diagnostic (3–7 min) · ALS: Polling

> New sub-topic — Data Interpretation doesn't build directly on Calendars, so this poll is diagnostic, not retrieval.

Say: *"Five quick questions before we start."*

**Q1.** Have you seen a "Data Interpretation" question in a mock test or exam before?
`A` Never · `B` Once or twice · `C` Regularly
→ *Read:* If mostly A, spend extra time on the four-step method before speeding into worked examples.

**Q2.** In a table, what do rows usually represent versus columns?
`A` Rows = categories, columns = time periods, or vice versa depending on the table · `B` They're interchangeable, doesn't matter · `C` Not sure
→ *Read:* A is the correct framing (context-dependent) — seeds Teaching Block A's structure beat.

**Q3.** Quick gut check: if a value goes from 200 to 240, is that a 20% or 40% increase?
`A` 20% · `B` 40% · `C` Not sure
→ *Read:* A is correct. If B/C dominate, the classic "difference over original, not over new value" error needs explicit correction in Teaching Block A.

**Q4.** When a question gives you a big table but only asks about two specific cells, what should you do first?
`A` Read every number in the table carefully · `B` Find only the two cells the question needs · `C` Calculate the average of the whole table
→ *Read:* B is correct — this is the "ignore the noise" step, a major time-saver under exam pressure.

**Q5.** How comfortable are you scanning a table quickly under time pressure?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, slow down through the worked table in Teaching Block A.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"If I gave you your own last six months of expenses — groceries, shopping, subscriptions — could you instantly tell me where you're overspending? Probably not instantly. That's exactly the skill today builds: reading a table of numbers and pulling out the one answer that matters, fast."*

Put the worked sales table (below) on the board, covered/blank for now. Say: *"By the end of today, you'll scan a table like this in seconds and know exactly which cells to touch."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

<!-- placement: inferred grouping — no source deck; grouped from GitBook Concept Explanation extraction; the data table itself is instructor-authored since the source's table examples are image-only -->
Covers: table structure → the four-step method → percentage-change worked example.

**Beats to emphasise**

- **Table structure.** "Rows = different entries (months, products, regions). Columns = categories or parameters (sales, cost, profit)." Point at the table below and name its rows/columns explicitly.
- **Four-step method, write on the board:**
  1. **Read the table carefully** — skim headers first, don't read every cell yet.
  2. **Understand the question type** — does it need an average, a percentage, or a comparison?
  3. **Apply the right math** — use the correct formula, don't guess.
  4. **Ignore the noise** — touch only the cells the question actually needs.

**The worked table (instructor-authored, regional sales, ₹ thousands):**

| Region | Jan | Feb | Mar |
|---|---|---|---|
| North | 200 | 220 | 240 |
| South | 180 | 190 | 210 |
| East | 150 | 160 | 175 |
| West | 300 | 310 | 295 |

- **Worked example, live:** *"What was the percentage increase in North's sales from January to March?"*
  1. Question type: percentage change.
  2. Formula: **% change = [(New − Old) / Old] × 100**.
  3. Apply: [(240 − 200) / 200] × 100 = (40/200) × 100 = **20%**.
- **Common error, flag explicitly:** dividing by the *new* value (240) instead of the *original* value (200) gives a wrong 16.7% — always divide by the starting point.

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"Using the same table, what's the percentage increase in South's sales from January to March?"*
> **Answer:** [(210 − 180) / 180] × 100 = (30/180) × 100 = **16.67%**.

---

## ⚡ ALS Activity 1 — Whiteboard Race: Table Scan Sprint (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to answer a table-based question using the four-step method, first correct board up wins the round. Chosen to build fast, disciplined table-scanning before Teaching Block B introduces averages and multi-step comparisons.

**Setup line:**
> *"Pairs, boards up, same table on the board. I'll call a question — find the answer fast. First correct board up wins the round. Three rounds."*

- Round 1: *"What was East's sales in February?"* → straight lookup, **160**.
- Round 2: *"What's the average of North's three months (Jan/Feb/Mar)?"* → (200+220+240)/3 = 660/3 = **220**.
- Round 3: *"By how much did West's sales change from Feb to Mar, in absolute terms?"* → 295 − 310 = **−15 (a decrease of 15)**.

**How it surfaces:** After each round, ask the winning pair which of the four steps they used first — reinforces that "understand the question type" always comes before calculating.

**Debrief line:**
> *"Notice Round 3 — West actually went down, not up. If you didn't read the question carefully and just assumed growth, you'd get the sign wrong. That's exactly what 'read carefully' protects against."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but keep the "why did West go down" observation — it previews Activity 2's trap directly.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: multi-row comparisons, exact calculation vs. smart approximation.

**Beats to emphasise**

- **Comparing across rows, not just within one.** Many real questions ask "which region performed best" — this needs the same percentage-change formula applied to *every* row, then compared.
- **Worked comparison, live, using the same table — which region grew the most (%) from Jan to Mar?**
  - North: (240−200)/200 × 100 = **20%**
  - South: (210−180)/180 × 100 = **16.67%**
  - East: (175−150)/150 × 100 = **16.67%**
  - West: (295−300)/300 × 100 = **−1.67%** (a decline)
  - **North grew the most, at 20%.**
- **Exact vs. approximate — decision rule:** *"If the answer options in a question are close together (e.g. 19%, 20%, 21%), you need the exact calculation. If they're far apart (e.g. 5%, 20%, 50%), a quick mental estimate is enough — don't waste time being precise when you don't need to be."*

**Checkpoint (at 32 min)** — cold-call:
> *"Looking at the table, which region's sales actually decreased between two of the three months?"*
> **Answer:** **West** — dropped from 310 (Feb) to 295 (Mar).

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: The Full-Scan Trap (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students commit to an answer before the method is walked through. Deliberately different register from Activity 1's loud paired race (quiet, individual, single reveal), and targets the most common real exam mistake: answering from a partial scan instead of the full table.

**Setup line:**
> *"On your own, ninety seconds, same table. Which region had the highest percentage growth from January to March? Don't just eyeball the biggest numbers — calculate. Write your answer, hold it up when I say show."*

Give 90 seconds silent work, then: *"Show me — three, two, one, show."* Expect a mix — some will pick West (biggest raw numbers) without noticing it declined.

**The reveal, step by step:**
1. North: 20% growth.
2. South: 16.67% growth.
3. East: 16.67% growth — **tied with South, easy to miss if you stop scanning early**.
4. West: −1.67% — **actually declined**, despite having the largest raw sales figures every single month.
5. **North wins at 20%.** *"The region with the biggest numbers on the table had the worst performance by growth. If you only looked at the biggest raw values, you'd have picked wrong."*

**Debrief line:**
> *"This is the trap DI tables are built around — big absolute numbers don't mean big growth. Always calculate before comparing, never eyeball a 'winner.'"*

**Cut rule:** If running short, skip the 90-second silent window and solve it together on the board — but always show all four regions' numbers side by side before revealing the winner.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — pose one more comparison question on the same table (e.g. "rank all four regions by Feb-to-Mar growth") and solve together — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> Using today's table, what's the average of East's three months?
> **Answer:** (150+160+175)/3 = 485/3 = **161.67**.

Scan responses on the way out — if the "divide by original, not new" rule is still shaky, revisit briefly at the start of Session 7.

**Homework**

| Task | Note |
|---|---|
| Rank all four regions by their Jan-to-Feb percentage growth | Self-check using the same formula as today |
| Find the combined average of all 12 cells in the table | Self-check — tests the "ignore the noise" discipline in reverse (this one genuinely needs every cell) |

Tell them: *"Tables are just one way data shows up in exams. Session 7 moves to graphs — bar and line — where the same math applies, but you have to read the values off axes first."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| % change = difference ÷ new value | Confusing "new" with "the base to divide by" | Teaching Block A's explicit common-error flag |
| Bigger raw numbers = better performance | Natural visual bias toward large figures | ALS Activity 2's full-scan reveal (West has biggest numbers, worst growth) |
| Every question needs the whole table read | Feels "safer" to read everything first | Teaching Block A's "ignore the noise" step + Activity 1 Round 1's direct-lookup drill |
| Approximation is always "less correct" than exact calculation | School habit of always showing full working | Teaching Block B's explicit exact-vs-approximate decision rule |
| A tie between two rows (like East/South at 16.67%) will be obvious at a glance | Assumes ties are rare or visually obvious | Activity 2's reveal explicitly calling out the East/South tie |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from GitBook Concept Explanation/Introduction/Closure text extraction. GitBook's "Problem Solving" sub-page is image-only and unrecoverable — the data table and every worked/practice problem in this plan are **instructor-authored**, though the % increase formula and its 20% worked value directly match the source's own stated example (North Jan→Mar, 200→240).
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, targeting the full-scan trap specifically.
- **First session of the Data Interpretation sub-topic** — warm-up poll is diagnostic, not retrieval.
- **The West region's Feb→Mar decline is a deliberately placed trap**, reused across Activity 1 Round 3, Teaching Block B's checkpoint, and Activity 2's reveal — it's the throughline of the whole session, don't cut all three instances if running short.
- Classroom Quiz slot reserved-empty per site convention.
