# Session 3 — Clocks-3: Faulty Clocks, Mirror Images & Direction

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Time gain/loss on faulty clocks, mirror-image time formula (11:60 − given time), and hand-to-compass-direction mapping · **Prerequisite** Clocks-1 and Clocks-2 — the base angle formula and the coincidence/opposite/perpendicular cases
**Session type** Lecture + guided practice. No source slide deck — content from GitBook Concept Explanation text. No classroom quiz bank yet — 5-min slot reserved at end. GitBook "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

| Resource | Status |
|---|---|
| Source | GitBook: `session-plans/logical-reasoning/clocks/clocks-3` (Learning Outcomes, Ideal Format, Introduction, Concept Explanation, Closure — text extracted) |
| Problem Solving bank (GitBook) | image-only, not recoverable — practice problems below are instructor-authored |
| Classroom Quiz | not yet available — 5-min slot reserved at end of session |

**⚠️ Content note:** the source's direction-mapping claim ("at 6:00, hour hand points South") is flagged in the extracted source as unverified against the live deck — Teaching Block B below presents it with an explicit consistency check rather than as unquestioned fact. Verify against the live GitBook page before teaching if a corrected version becomes available.

---

## Learning Objectives

By the end of this session, students will be able to:

1. Solve net-gain/loss problems for a clock that runs fast or slow at a constant rate. *(APPLYING)*
2. Apply the mirror-image formula (Mirror Time = 11:60 − Given Time) to convert between real time and mirror-reflected time. *(APPLYING)*
3. Explain why mirrors reverse left-right, not top-bottom, and how that specifically affects a clock face reading. *(UNDERSTANDING)*
4. Map clock-hand positions to compass directions at a given time, and verify the mapping stays internally consistent. *(ANALYZING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. If a physical mirror or phone-camera mirror-mode is available, have it ready near the front for the mirror-image activity later.

---

## Warm-Up Poll — Retrieval Practice on Session 2 (3–7 min) · ALS: Polling

Say: *"Five quick ones from last session."*

**Q1.** How many times do the hands coincide in 12 hours?
`A` 12 · `B` 11 · `C` 22 · `D` 24
→ *Read:* B should dominate. If not, 60-second re-derivation before moving on.

**Q2.** How many times are the hands exactly perpendicular in 12 hours?
`A` 11 · `B` 12 · `C` 22 · `D` 24
→ *Read:* C is correct.

**Q3.** True or false: an "angle to time" question can have more than one valid answer inside the same hour window.
`A` True · `B` False
→ *Read:* A is correct — tests whether last session's two-case trap stuck.

**Q4.** Quick guess: if your watch says 12:00 and you look at it in a mirror, what time does the mirror show?
`A` 12:00 · `B` 6:00 · `C` Still 12:00 but flipped · `D` Not sure
→ *Read:* A is actually correct here (12:00 is a special symmetric case) — don't confirm yet, this seeds today's Hook.

**Q5.** Guess: does a clock that's "10 min slow now but gaining 2 min every hour" ever show the correct time again?
`A` Yes, eventually · `B` No, never · `C` Not sure
→ *Read:* A is correct — it will catch up once the gain offsets the initial deficit. Seeds Teaching Block A.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"Quick quiz — if your watch says 12:00, and you look at it in a mirror, what time do you see?"* Take guesses.

> *"Most people freeze on this one. Now imagine you're late for an interview and the only clock in the room is reflected in a mirror behind you. Can you trust what you're reading? By the end of today, you'll be able to convert any mirror time to real time in your head, spot a clock that's silently drifting wrong, and read hand positions as compass directions."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

<!-- placement: inferred grouping — no source deck; grouped from GitBook Concept Explanation extraction -->
Covers: net time gain/loss problems on faulty clocks.

**Beats to emphasise**

- **Setup of the problem type.** A faulty clock either runs consistently fast (gains time) or slow (loses time) relative to a real clock. Questions typically give a starting error and a rate of drift, then ask for the correct time at some later point — or ask you to work backwards.
- **Worked example, live (from the source, verified):** *"A clock is 10 minutes slow at 12 noon, but gains 2 minutes every hour. Find the correct time at 6 PM."*
  1. Time elapsed: 12 PM to 6 PM = **6 hours**.
  2. Total gain over that period: 6 × 2 = **12 minutes**.
  3. Net adjustment: starts 10 min behind, gains 12 min → net = −10 + 12 = **+2 minutes** (now 2 min *ahead*).
  4. The clock reads 6:00 PM; correct time = 6:00 − 2 min = **5:58 PM**. <!-- placement: corrected — if the clock is 2 min ahead of correct time, correct time is 2 min behind what the clock shows, i.e. 5:58 PM, not 6:02 PM; verify sign convention with students explicitly since this is the step where errors happen -->
- **Sign-convention drill, explicit:** *"If the faulty clock is ahead, the real time is earlier than what it shows. If the faulty clock is behind, the real time is later than what it shows."* Write this as a standing rule on the board — it answers poll **Q5** directly (yes, it can cross back to correct and then run ahead).
- **Reverse case:** *"A clock gains 3 minutes every hour and was set correctly at 8 AM. What does it show at 8 PM real time?"* Elapsed: 12 hours → gain = 36 min → clock shows **8:36 PM** when real time is 8:00 PM.

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"A clock is 5 minutes fast at 9 AM and gains 1 minute every hour. What does it show at 2 PM?"*
> **Answer:** Elapsed 5 hours → extra gain 5 min → total ahead = 5+5 = **10 min** → clock shows **2:10 PM**.

---

## ⚡ ALS Activity 1 — Mirror Clock Live Demo (19–25 min)

**ALS format:** Physical/Visual Demo with a real or phone-camera mirror — students predict a mirror-reflected time before it's revealed, using a real analog clock face (drawn or physical) held up to a mirror. Chosen because "mirror time" is a spatial-reasoning trap that's far more convincing shown live than described.

**Setup line:**
> *"I'm going to set this clock face to a real time, then hold it up to the mirror. Before I do — predict what the mirror will show."*

- Draw/set a clock to **3:00**. Ask for predictions before revealing. Hold to the mirror (or flip the drawn face horizontally on the board) — mirror shows **9:00**. Class checks against the formula: 11:60 − 3:00 = **9:00** ✔.
- Draw/set to **2:10**. Predict, then reveal via mirror — mirror shows **9:50**. Check: 11:60 − 2:10 = **9:50** ✔.
- Ask: *"Why does 12:00 look the same in the mirror?"* Reveal: 11:60 − 12:00 = **11:60 = 12:00** — the one symmetric case. Ties back to poll **Q4**.

**How it surfaces:** After each reveal, ask: *"Did the numbers flip left-right or top-bottom?"* — students should notice the hands swap left/right sides of the dial, not flip upside down, which is the real mechanism behind the formula.

**Debrief line:**
> *"Mirrors don't flip up-down, they flip left-right. On a clock face, that means the *time* effectively reflects around the 12–6 axis — and that reflection is exactly what 11:60 minus your time calculates for you."*

**Cut rule:** If no physical mirror is available, use a phone camera's front mode or simply flip the drawn clock face left-right on the board by redrawing — don't skip the visual, it's the entire point of the activity.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: hand-to-compass-direction mapping, with an explicit consistency check given the flagged source discrepancy.

**Beats to emphasise**

- **The mapping idea:** if you overlay a compass on a clock face with 12 = North, 3 = East, 6 = South, 9 = West, then any hand position can be read as an approximate compass direction, and vice versa.
- **Worked examples, checked for internal consistency:**
  - At **3:00**: minute hand at 12 → **North**. Hour hand at 3 → **East**. ✔ consistent with the 12=N/3=E/6=S/9=W mapping.
  - At **6:00**: minute hand at 12 → **North**. Hour hand at 6 → **South**. ✔ also consistent — both hands map cleanly onto the same fixed compass overlay.
- **Say explicitly:** *"The rule is simple once you see it — whatever number the hand points to on the dial, that number has a fixed compass direction, always. 12 is always North, 3 is always East, 6 is always South, 9 is always West, no matter which hand is pointing there or what time it is."*
- **Practice, live:** *"At 9:15, roughly where does the minute hand point?"* Minute hand at 15 min = pointing at the "3" mark → **East**. *"And the hour hand, roughly?"* Between 9 and 10, closer to 9 → roughly **West, drifting slightly toward South**.

**Checkpoint (at 32 min)** — cold-call:
> *"At 12:00 exactly, what compass direction do both hands point?"*
> **Answer:** Both hands point to 12 → **North**, both hands overlap (also ties back to the coincidence concept from Session 2).

---

## ⚡ ALS Activity 2 — Think-Pair-Share: Build Your Own Faulty-Clock Puzzle (32–40 min)

**ALS format:** Think-Pair-Share, generative — pairs invent their own gain/loss word problem (mirroring the worked example structure), swap with another pair, and solve each other's. Different register from Activity 1 (visual/instructor-led demo → generative/peer-driven), and reinforces the sign-convention rule from Teaching Block A by forcing students to construct a problem where the sign matters.

**Setup line:**
> *"In pairs, three minutes: invent your own faulty-clock problem. Pick a starting error (fast or slow), a drift rate per hour, a start time and an end time. Write it down — don't solve it yet."*

Give 3 minutes to construct. Then: *"Swap your problem with the pair next to you. Four minutes to solve theirs."* Give 4 minutes to solve.

**How it surfaces:** Walk the room during the solve phase — watch specifically for the sign-convention error (adding instead of subtracting, or vice versa) from Teaching Block A. Collect 2–3 pairs' problems to solve together on the board in the last minute.

**Debrief line:**
> *"Writing your own problem forces you to track the sign yourself, not just follow steps — that's exactly the skill that breaks down under exam pressure. If you got your own problem's logic right but tripped on a swapped one, that's a sign to slow down and re-read before calculating, every time."*

**Cut rule:** If running short, cut the construction phase to 2 minutes and the solve phase to 3 minutes, but keep the swap — solving a self-generated peer problem (not a pre-written one) is the point of the activity.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot to solve 1–2 of the strongest student-invented problems from Activity 2 together as a class, or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> A clock is 6 minutes fast at 10 AM and loses 1 minute every hour. What time does it show at 3 PM real time?
> **Answer:** Elapsed 5 hours → loses 5 min → net = +6 − 5 = **+1 min ahead** → clock shows **3:01 PM**.

Scan responses on the way out — sign-convention errors here mean revisit Teaching Block A's rule briefly before Session 4 (Calendars-1).

**Homework**

| Task | Note |
|---|---|
| Find the mirror-image time for 4:20 and for 7:35 | Self-check against Mirror Time = 11:60 − Given Time |
| Solve: clock 8 min slow at 6 AM, gains 1.5 min/hour — find its reading at 12 noon | Self-check using the sign-convention rule |

Tell them: *"That's the full Clocks arc — angle, hand-frequency, and now faulty/mirror/direction problems. Session 4 is a completely different topic: Calendars, where you'll find the day of the week for any date, past or future."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Mirrors flip a clock face top-to-bottom | Confusing mirror mechanics with a simple "upside down" intuition | ALS Activity 1's live mirror demo, explicit left-right framing |
| "Ahead" and "real time is later" get confused | Sign convention isn't intuitive without a fixed rule | Teaching Block A's explicit standing rule + Activity 2 forcing self-construction |
| A faulty clock that starts wrong can never show the correct time again | Students don't consider that gain/loss can offset an initial error | Poll Q5 + Teaching Block A's net-adjustment framing |
| Compass direction mapping changes depending on which hand you look at | Not recognising the dial-position-to-direction mapping is fixed, not hand-specific | Teaching Block B's explicit "12 is always North" framing |
| 12:00 mirrored "should" look different somehow | Not recognising the 12–6 axis symmetry | ALS Activity 1's 12:00 reveal, tied to poll Q4 |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from GitBook Concept Explanation/Introduction/Closure text extraction. GitBook's "Problem Solving" sub-page is image-only and unrecoverable — all worked/practice problems in this plan are **instructor-authored**.
- **⚠️ Flagged discrepancy resolved for teaching purposes:** the source's worked "10 min slow, gains 2 min/hr, find time at 6 PM" example was re-derived here with explicit sign-convention reasoning (net +2 min ahead → correct time is 5:58 PM, not 6:02 PM) — walk through the sign logic slowly, this is where the source material itself is easiest to misapply.
- **⚠️ Direction-mapping claim carries a source-flagged discrepancy** — the 3:00 and 6:00 examples were independently checked here and are internally consistent under a fixed 12=N/3=E/6=S/9=W overlay; teach it with that explicit fixed-overlay framing rather than asserting it as received fact.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Mirror Clock Live Demo) is visual/instructor-led; Activity 2 (Think-Pair-Share generative) is peer-driven/constructive. Completes the Clocks-1/2/3 rotation without repeating a register two sessions running.
- **This is the last of the three Clocks sessions** — Session 4 begins a new topic (Calendars) with a diagnostic-style light recap, not deep retrieval, since Calendars doesn't build on Clocks content directly.
- Classroom Quiz slot reserved-empty per site convention.
