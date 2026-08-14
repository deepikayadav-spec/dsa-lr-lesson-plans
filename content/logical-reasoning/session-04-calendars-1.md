# Session 4 — Calendars-1: Odd Days & Day-of-the-Week

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Calendar structure, leap year rules, odd days, and finding the day of the week for any date · **Prerequisite** None specific to Clocks — first session of the Calendars sub-topic
**Session type** Lecture + guided practice. No source slide deck — content from the session's concept-explanation text. No classroom quiz bank yet — 5-min slot reserved at end. the "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

**Note on worked examples:** the source's own worked example (day-of-week for 3 Jan 2026) is verified correct, but its shown arithmetic is condensed in a way that's hard to teach cleanly. This plan re-derives the same verified answer using an explicit, fully-checkable anchor method (Jan 1, 2000 = Saturday) — every example below is independently verified against known real-world dates.

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the leap year rule (divisible by 4, not by 100, unless also by 400) and classify any given year. *(REMEMBERING)*
2. Define "odd days" and explain why they determine the weekday shift year over year. *(UNDERSTANDING)*
3. Use a fixed reference date (Jan 1, 2000 = Saturday) plus accumulated odd days to find the day of the week for any date. *(APPLYING)*
4. Apply the month-odd-days table to handle dates outside January. *(APPLYING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Write "Jan 1, 2000 = Saturday" in a corner — this anchor will be used all session.

---

## Warm-Up Poll — Diagnostic (3–7 min) · ALS: Polling

> New sub-topic — Calendars doesn't build directly on Clocks, so this poll is diagnostic, not retrieval.

Say: *"Five quick questions before we start."*

**Q1.** What day of the week were you born on? Do you know it?
`A` Yes, I know it · `B` No idea · `C` I could figure it out with a calendar app
→ *Read:* Almost everyone will say B or C — that's the gap this session closes: doing it in your head.

**Q2.** Is the year 1900 a leap year?
`A` Yes · `B` No · `C` Not sure
→ *Read:* B is correct — this is the single most common trap in this topic. If A/C dominate, spend extra time on the leap rule.

**Q3.** How many days does a normal (non-leap) year have, and how many complete weeks is that?
`A` 365 days, 52 weeks + 1 day · `B` 365 days, exactly 52 weeks · `C` 364 days, 52 weeks
→ *Read:* A is correct — seeds the "odd day" concept directly.

**Q4.** Guess: what day of the week was 15 August 1947 (India's Independence Day)?
`A` Monday · `B` Wednesday · `C` Friday · `D` Sunday
→ *Read:* C is correct. Don't reveal yet — this is today's marquee reveal in Activity 2.

**Q5.** How confident are you doing mental date-arithmetic under time pressure?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, slow down through Teaching Block A's derivation, don't rush to the shortcut.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"Everyone knows India became independent on 15 August 1947. Almost nobody knows what day of the week that was. By the end of today, you'll be able to work that out yourself — no calendar app, no internet, just logic and one number you memorise."*

Write the anchor on the board again: **"Jan 1, 2000 = Saturday."** Say: *"That one fact, plus a counting method, unlocks every date in history. Let's build the method."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

Covers: leap year rule → odd days concept → the anchor method, worked live on a verifiable date.

**Beats to emphasise**

- **Leap year rule:** divisible by 4 → leap, UNLESS divisible by 100 → not leap, UNLESS ALSO divisible by 400 → leap after all. Examples: 2024 ✅ leap (div 4, not 100). 1900 ❌ not leap (div 100, not 400) — directly resolves poll **Q2**. 2000 ✅ leap (div 400).
- **Odd days.** A normal year = 365 days = 52 complete weeks + **1 odd day**. A leap year = 366 days = 52 weeks + **2 odd days**. Every odd day "pushes" the weekday of a fixed date forward by one, year over year. *"If 1 January is a Monday this year, and it's a normal year, 1 January next year is a Tuesday. If it was a leap year, it jumps to Wednesday."*
- **The anchor method — say it plainly:** *"Pick one date whose weekday you know for certain. Count how many odd days have accumulated between then and the date you want. Add that count to the known weekday."*
- **Worked derivation, live — find the day of the week for 1 January 2026:**
  1. Anchor: Jan 1, 2000 = **Saturday**.
  2. Years elapsed: 2000 through 2025 = **26 years**.
  3. Leap years in that span: 2000, 2004, 2008, 2012, 2016, 2020, 2024 = **7 leap years** (2000 counts — divisible by 400).
  4. Ordinary years: 26 − 7 = **19**.
  5. Total odd days: (19 × 1) + (7 × 2) = 19 + 14 = **33**.
  6. 33 ÷ 7 = 4 remainder **5**.
  7. Saturday + 5 days = **Thursday**. *(Sat→Sun→Mon→Tue→Wed→Thu, count 5 steps.)*
  8. **Jan 1, 2026 = Thursday.**
- **Extending to 3 January:** Thursday + 2 more days = **Saturday**. *(Verified — matches the source's own stated answer for this date.)*

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"If Jan 1 2026 is a Thursday, what day is Jan 5 2026?"*
> **Answer:** Thursday + 4 = **Monday**.

---

## ⚡ ALS Activity 1 — Whiteboard Race: Anchor-Method Sprint (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to find the weekday of an assigned Jan 1 date using the anchor method, first correct board up wins the round. Chosen to convert the just-taught method into fast, repeatable steps before adding the month-table complexity in Teaching Block B.

**Setup line:**
> *"Pairs, boards up. I'll call a year — find what day of the week 1 January of that year falls on, using the anchor. First correct board up wins the round. Three rounds."*

- Round 1: **1 January 2010** — years elapsed 2000–2009 = 10, leap years 2000/04/08 = 3, ordinary = 7, odd days = 7+6=13, 13 mod 7 = 6, Saturday + 6 = **Friday**.
- Round 2: **1 January 2020** — years elapsed 2000–2019 = 20, leap years 2000/04/08/12/16 = 5, ordinary = 15, odd days = 15+10=25, 25 mod 7 = 4, Saturday + 4 = **Wednesday**.
- Round 3: **1 January 2030** — years elapsed 2000–2029 = 30, leap years 2000/04/.../28 = 8, ordinary = 22, odd days = 22+16=38, 38 mod 7 = 3, Saturday + 3 = **Tuesday**.

**How it surfaces:** After each round, have the winning pair narrate their year/leap-year count out loud before confirming — this exposes the counting method, not just the final answer, to the room.

**Debrief line:**
> *"Same anchor, same steps, three different years — the only thing that changes each time is how many leap years you count. Get that count right and the rest is automatic."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but always have a winning pair narrate their steps.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: extending beyond January using the month-odd-days table.

**Beats to emphasise**

- **The month table concept.** Once you know the weekday of 1 January for a year, you can reach any other date by counting the exact number of days elapsed since 1 January and taking that count mod 7. Write the cumulative days-before-month-start (non-leap year) on the board: **Jan 0 · Feb 31 · Mar 59 · Apr 90 · May 120 · Jun 151 · Jul 181 · Aug 212 · Sep 243 · Oct 273 · Nov 304 · Dec 334.** *(For a leap year, add 1 to every value from March onward.)*
- **Worked derivation, live — Christmas 2025 (25 December 2025):**
  1. First find Jan 1, 2025: years elapsed 2000–2024 = 25, leap years 2000–2024 = 7, ordinary = 18, odd days = 18+14=32, 32 mod 7 = 4, Saturday+4 = **Wednesday**.
  2. Day-of-year for 25 Dec (non-leap): 334 (days before Dec) + 25 = **359**.
  3. Offset from Jan 1: 359 − 1 = 358 days. 358 mod 7 = **1**.
  4. Wednesday + 1 = **Thursday**.
  5. **25 December 2025 = Thursday.** *(Matches the real 2025 calendar.)*
- **Say explicitly:** *"You don't need to memorise all twelve numbers under exam pressure — you only need to add up the months before the one you're working with. Most questions only need two or three of these."*

**Checkpoint (at 32 min)** — cold-call:
> *"1 January 2025 is a Wednesday. What day is 14 February 2025?"*
> **Answer:** Days before Feb = 31, +14 = 45, offset from Jan1 = 44, 44 mod 7 = 2, Wednesday + 2 = **Friday**.

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: Independence Day, 1947 (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students commit to an answer before the method is walked through. Deliberately different register from Activity 1's loud paired race (quiet, individual, single big reveal), and closes the loop opened by poll Q4 and the Hook.

**Setup line:**
> *"You predicted this at the start of class. Now prove it. On your own, three minutes: what day of the week was 15 August 1947? You'll need to work backwards from the anchor — this one takes an extra step. Write your answer, hold it up when I say show."*

Give 3 minutes of silent solo work (this is harder — going backward from 2000 to 1947). Then: *"Show me — three, two, one, show."*

**The reveal, step by step:**
1. Years between 1947 and 2000: **53 years** (1947 through 1999).
2. Leap years in that span: 1948, 1952, 1956, ..., 1996 = **13 leap years**.
3. Ordinary years: 53 − 13 = **40**.
4. Total odd days: (40 × 1) + (13 × 2) = 40 + 26 = **66**. 66 mod 7 = **3**.
5. Going *backward* from the anchor: Jan 1, 2000 (Saturday) − 3 days = **Wednesday**. So **Jan 1, 1947 = Wednesday**.
6. Day-of-year for 15 August 1947 (non-leap year — 1947 not divisible by 4): days before August = 212, + 15 = **227**. Offset from Jan 1 = 227 − 1 = 226. 226 mod 7 = **2**.
7. Wednesday + 2 = **Friday**.
8. **15 August 1947 = Friday.** ✔ matches the real historical date.

**Debrief line:**
> *"Same exact method as every date today — the only new move was going backward instead of forward. If you can count leap years in either direction, you can find the weekday for any date in history, not just recent ones."*

**Cut rule:** If running short, cut the silent window to 2 minutes but keep the full step-by-step reveal — the backward-counting move is the one genuinely new idea in this activity.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — re-run the Christmas 2025 derivation from Teaching Block B with a different date (e.g. New Year's Day 2027), cold-calling students to narrate each step — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> If 1 January 2026 is a Thursday, what day of the week is 26 January 2026 (Republic Day)?
> **Answer:** Thursday + 25 days → 25 mod 7 = 4 → Thursday + 4 = **Monday**.

Scan responses on the way out — if the "add the extra days, then mod 7" step is shaky, revisit briefly at the start of Session 5.

**Homework**

| Task | Note |
|---|---|
| Find the weekday for your own birth date (year, month, day) | Self-check using the anchor + month table method |
| Find the weekday for 2 October 1869 (Gandhi's birth date) | Self-check — requires going backward like the Activity 2 example |

Tell them: *"You now have a full toolkit for finding any date's weekday from scratch. Session 5 goes one step further — figuring out when a given year's entire calendar will repeat, without recalculating from the anchor every time."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| 1900 is a leap year (divisible by 4) | The div-by-4 rule is taught first and remembered best | Poll Q2 + Teaching Block A's explicit century-exception rule |
| Each year always shifts the weekday by exactly 1 day | Doesn't account for leap years shifting by 2 | Teaching Block A's "normal=1, leap=2" odd-day framing |
| The month table needs to be fully memorised | Looks like a long list to learn by rote | Teaching Block B's "you only need the months up to the one you need" framing |
| Counting backward in time uses a different method | Feels conceptually different from counting forward | Activity 2's explicit backward derivation using the identical formula |
| "Odd days" means something is wrong or unusual | The word "odd" suggests an error, not a remainder | Explicit definition given early: odd days = leftover days after full weeks |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from a text extraction of the Concept Explanation/Introduction/Closure sections. The "Problem Solving" sub-page is image-only and unrecoverable — all worked/practice problems in this plan are **instructor-authored**.
- **Anchor re-derivation:** the source's own worked example (3 Jan 2026 = Saturday) is correct but its shown arithmetic path is compressed and hard to teach directly. This plan re-derives the identical, verified answer using an explicit, independently-checkable anchor (Jan 1, 2000 = Saturday, a well-known reference point) — every worked example in this session (Jan 1 2026, Christmas 2025, Independence Day 1947) was independently checked against real calendar records and is internally consistent.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, with real historical payoff (15 Aug 1947).
- **First session of the Calendars sub-topic** — warm-up poll is diagnostic, not retrieval, same exception pattern as the first session of any new sub-topic thread.
- Classroom Quiz slot reserved-empty per site convention.
