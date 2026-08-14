# Session 3 — Clocks-1: Angle Between Hands

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Clock structure, hand-movement rates, and the angle formula θ = |30H − (11/2)M| · **Prerequisite** None — first session of Logical Reasoning
**Session type** Lecture + guided practice. No source slide deck exists for this topic — content is sourced from the session's concept-explanation text. No classroom quiz bank exists yet — a 5-min slot is reserved at the end. The "Problem Solving" page (Q1–Q11) is image-only and unrecoverable, so every worked/practice problem below is **instructor-authored**, grounded in the verified formula. · **Format** 50-min recalibrated, 2 ALS activities

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the two hand-movement rates: minute hand 6°/min, hour hand 0.5°/min. *(REMEMBERING)*
2. Apply the formula θ = |30H − (11/2)M| to find the angle between hands at any given time. *(APPLYING)*
3. Convert a reflex angle to its acute equivalent (360° − θ) and vice versa. *(APPLYING)*
4. Translate "past"/"to" time phrasing (e.g. "10 minutes to 5") into H:M form before calculating. *(UNDERSTANDING)*
5. Judge when the direct step-by-step method is safer than the shortcut formula. *(EVALUATING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready with a large blank clock face drawn (numbers 12/3/6/9 only, no hands). Don't reclaim this time for content if the room settles faster — hold it as extra flex at the end.

---

## Warm-Up Poll — Diagnostic (3–7 min) · ALS: Polling

> **This session is the exception.** First session of the topic — no prior session to recall. This poll is diagnostic, not retrieval. No wrong answers.

Say: *"Five quick questions before we start. Nobody's graded, nobody's named."*

**Q1.** Without calculating, what's your gut guess for the angle between the hands at 3:00?
`A` 30° · `B` 60° · `C` 90° · `D` 180°
→ *Read:* Most will correctly say C (90°) — good, that's the anchor example you'll use to derive the formula.

**Q2.** Have you solved a "clock angle" problem before (school, coaching, mock test)?
`A` Never · `B` Once or twice · `C` Several times · `D` Regularly
→ *Read:* If mostly A/B, spend the full 5 min of Teaching Block A on the step-by-step method before touching the shortcut.

**Q3.** How fast do you think the minute hand moves, in degrees per minute?
`A` 1° · `B` 6° · `C` 12° · `D` Not sure
→ *Read:* C (6°) is correct math trap territory (360/30=12 is a common wrong guess); flag this explicitly when you teach it.

**Q4.** True or false: the hour hand only moves once every hour, in a single jump.
`A` True · `B` False
→ *Read:* B is correct — the hour hand creeps continuously (0.5°/min). This misconception is common and directly undermines the formula if not corrected first.

**Q5.** How do you want today's session to run?
`A` Mostly explanation · `B` Lots of live problem-solving · `C` A mix
→ *Read:* If B/C dominate, compress Teaching Block A's explanation and get to worked examples faster.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"Look at your phone or wrist right now — or picture a clock. At 2:20, without drawing anything, what's the angle between the two hands? Not 'roughly' — exactly."*

Take 2–3 shouted guesses, write them on the board without confirming or denying any.

> *"Hold onto your guess. By the end of today you'll be able to answer this in under ten seconds, exactly, for any time at all — and I'll show you the one formula that does it."*

Tie to **Q3**: *"Most of you said the minute hand moves 6° a minute — that's exactly right, and it's half of today's formula. The other half is the hour hand, and that's where almost everyone gets tripped up."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

Covers: clock structure and dial geometry → hand movement rates → deriving the angle formula → reflex vs. acute angles.

**Beats to emphasise**

- **Dial geometry.** A 12-hour clock face is 360° around, so each hour mark is 360/12 = **30°**, and each minute mark is 360/60 = **6°**. Draw this on the board clock face now — mark 12, 3, 6, 9.
- **Two different speeds.** Minute hand: full circle in 60 min → **6° per minute**. Hour hand: full circle in 12 hours (720 min) → **0.5° per minute**, i.e. 30° every hour. Say explicitly: *"The hour hand is not frozen between hour marks — it creeps the whole time. At 2:15 it's already a quarter of the way from 2 to 3."* Directly resolves poll **Q4**.
- **Step-by-step method (do this first, before the shortcut):**
  1. Minute-hand position = 6 × M
  2. Hour-hand position = 30 × H + 0.5 × M
  3. Angle = |position of minute hand − position of hour hand|
  4. If the result > 180°, subtract from 360° to get the smaller (acute/obtuse) angle instead of the reflex angle.
- **Shortcut formula:** **θ = |30H − (11/2)M|**. Derive it live on the board from the step-by-step method (it's just steps 1–3 algebraically simplified) — don't just hand it over, show *why* it works so students trust it under exam pressure.
- **Worked derivation, live, at 2:20** (this is the Hook's unanswered question — answer it now):
  - Minute hand: 6 × 20 = 120°
  - Hour hand: 30 × 2 + 0.5 × 20 = 60 + 10 = 70°
  - Difference: |120 − 70| = **50°**
  - Reflex version: 360 − 50 = **310°**
  - Cross-check with the shortcut: |30×2 − 5.5×20| = |60 − 110| = **50°** ✔ matches.
- **Time-phrase translation:** "20 minutes past 4" = 4:20. "10 minutes to 5" = 4:50 (NOT 5:10 — this is the single most common student error). Drill this translation explicitly before any problem involving "to" phrasing.

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"At 3:00 exactly, what's the angle? Use the formula, don't eyeball it."*
> **Answer:** |30×3 − 5.5×0| = |90 − 0| = **90°** ✔ matches the poll Q1 intuition.

---

## ⚡ ALS Activity 1 — Human Clock (19–25 min)

**ALS format:** Physical Demo / Kinesthetic Modeling — two students stand at the front and use their arms as the hour and minute hands; the rest of the class calls out a time and checks the "hands" against the formula. Chosen first because clocks are inherently spatial, and modeling the two different rotation speeds with actual bodies fixes the "hour hand creeps continuously" misconception (poll Q4) far more durably than a diagram.

**Setup line:**
> *"I need two volunteers. One arm each — you're the hour hand, you're the minute hand. When I call a time, you move your arm to where it should point. Everyone else checks the math."*

Mark 12/3/6/9 positions on the floor or wall (masking tape or chalk) so the "hands" (arms) have fixed reference points to point toward.

- Call **3:00** first — hour-hand student points at "3," minute-hand student points at "12." Class confirms 90° by formula.
- Call **2:20** next (the Hook's example) — hour-hand student must point *between* 2 and 3, roughly a third of the way toward 3, not straight at 2. This is the moment that lands the "continuous creep" point.
- Swap in two new volunteers, call **6:30** — hour-hand student should point roughly halfway between 6 and 7. Common wrong instinct: pointing straight at 6.

**How it surfaces:** After each call, before revealing the formula answer, ask the class: *"Is the hour-hand's position correct? Vote thumbs up/down."* Then compute the formula answer together and check the arms against it.

**Debrief line:**
> *"Notice — every time we called a time that wasn't 'o'clock,' the hour hand had already moved off its mark. That's not a rounding error, that's the whole reason the formula has that 0.5M term in it."*

**Cut rule:** If running short, do only the 2:20 call (skip 3:00 and 6:30) — 2:20 is the one that fixes the misconception, keep it no matter what.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: reflex-angle handling → worked practice problems (instructor-authored, since the source problem bank is image-only).

**Beats to emphasise**

- **Reflex angle rule, restated plainly:** the formula always gives you *one* of the two angles between the hands (the two always sum to 360°). If your answer is > 180°, the "other" angle is 360° minus it. Both are valid answers depending on what the question asks for — always check which one the question wants.
- **Worked Problem 1 (instructor-authored):** *"Find the angle between the hands at 7:45."*
  - Minute hand: 6 × 45 = 270°
  - Hour hand: 30 × 7 + 0.5 × 45 = 210 + 22.5 = 232.5°
  - Difference: |270 − 232.5| = **37.5°**
- **Worked Problem 2 (instructor-authored), reverse-phrasing drill:** *"Find the angle at 'twenty-five minutes to nine.'"*
  - Translate first: 25 min to 9 = 8:35.
  - Minute hand: 6 × 35 = 210°
  - Hour hand: 30 × 8 + 0.5 × 35 = 240 + 17.5 = 257.5°
  - Difference: |210 − 257.5| = 47.5° → this is already ≤ 180°, so it's final.

**Checkpoint (at 32 min)** — cold-call:
> *"At 9:00 exactly, is the angle 90° or 270°? Which one does the formula give you, and how would you get the other?"*
> **Answer:** Formula gives |270 − 0| = 270°, which is the reflex angle; the acute angle is 360 − 270 = **90°**. Both are "correct" — it depends what's asked.

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students commit to a numeric answer before the method is walked through, so the reveal actually corrects live misconceptions rather than confirming guesses. Deliberately different register from Activity 1 (loud/physical → quiet/individual-then-shared) to vary energy across the session.

**Setup line:**
> *"One question, on your own, two minutes, no talking. Find the angle between the hands at 4:50. Write your answer on paper or your mini-whiteboard, and when I say 'show,' hold it up."*

Give 2 minutes of silent solo work. Then: *"Show me your boards — three, two, one, show."* Scan the room for the spread of answers (there will likely be a cluster at the correct answer and a cluster from students who forgot the reflex adjustment or the "to" translation).

**The reveal, step by step:**
1. Translate: 4:50 is already H:M form, no "to" conversion needed here (deliberately included as a check that students don't over-apply the translation rule).
2. Minute hand: 6 × 50 = 300°
3. Hour hand: 30 × 4 + 0.5 × 50 = 120 + 25 = 145°
4. Difference: |300 − 145| = **155°**
5. This is ≤ 180°, so 155° is final — no reflex adjustment needed. (Students who answered 205° likely subtracted in the wrong direction or force-applied the reflex rule when it wasn't needed — call this out explicitly.)

**Debrief line:**
> *"The two most common wrong answers here come from two different bugs — forgetting the hour hand moves, or over-correcting for reflex when you didn't need to. Both are fixable the same way: always compute both hand positions from scratch, every time, don't shortcut the shortcut."*

**Cut rule:** If running short, cut the 2-minute silent window to 90 seconds but keep the vote-show and full reveal — the reveal is where the actual learning happens.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning (see Resources table). Use this slot for instructor-led review — re-run the 4:50 problem from Activity 2 once more, cold-calling a different student to narrate each step aloud — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min) — on paper or in chat before anyone leaves:

> Find the angle between the hands at 5:40. Show your two hand positions before subtracting.
> **Answer:** Minute hand 6×40=240°, hour hand 30×5+0.5×40=150+20=170°, difference |240−170|=**70°**.

Scan responses on the way out — if hour-hand positions are wrong for more than a couple of students, open Session 4 with a 60-second re-derivation of the hour-hand formula term.

**Homework**

| Task | Note |
|---|---|
| Solve: angle at 11:05, and angle at 6:18 | No platform practice set exists yet — these are instructor-set, self-check against the formula |
| Bring one real clock/watch time from today and compute its angle | Session 4 opens by collecting a few of these from the room |

Tell them: *"You now have one formula that answers this for any time on any clock. Session 4 builds on it — coincidences, right angles, and working backwards from the angle to find the time."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. If you land here with time on the clock, let the session end early — don't stretch content to fill it.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| "The hour hand only moves once an hour, in a jump" | School-level intuition — hour hand "looks" static between hour marks | ALS Activity 1's Human Clock, especially the 2:20 call |
| "10 minutes to 5" means 5:10 | "To" sounds like "after" in casual speech | Teaching Block A's explicit time-phrase translation drill |
| The formula always gives the "final" answer | Students don't check whether the result exceeds 180° | Teaching Block B's reflex-angle rule + Activity 2's over-correction bug |
| Minute hand moves 12°/min (360/30) | Confusing "30 marks" with "60 marks" on the dial | Poll Q3 + explicit 360/60=6° derivation in Teaching Block A |
| Any angle over 90° "must" need reflex adjustment | Confusing "large angle" with "reflex angle" (>180°) | Activity 2 reveal — 155° needs no adjustment, only >180° does |

---

## Instructor Notes

- **Data note:** no source slide deck exists for this topic. All content is sourced from a text extraction of the Concept Explanation / Introduction / Closure sections. The "Problem Solving" sub-page (11 questions, Q1–Q11) is **image-only and was not recoverable** — every worked example and practice problem in this plan (Teaching Block B's two problems, Activity 2's problem, the exit ticket, and homework) is **instructor-authored**, built directly from the verified formula, not transcribed from the original bank.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, deliberately different registers:** Activity 1 (Human Clock) is loud/physical/group; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual-then-shared. Don't run two of the same register back to back across sessions — vary it.
- **Formula verified independently:** θ = |30H − (11/2)M| checked against the worked 2:20 example (50°, reflex 310°) via the full step-by-step method — matches exactly.
- **This is the first session of the Logical Reasoning course** — the warm-up poll is diagnostic, not retrieval, same exception pattern used in Aptitude Session 1.
- Classroom Quiz slot is reserved-empty, same convention as every other topic on this site with no platform question bank yet — add real questions here once a bank exists, don't restructure the timeline.
