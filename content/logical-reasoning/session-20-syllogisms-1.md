# Session 20 — Syllogisms-1: The Venn Diagram Method

**Duration** 50 min total — **45 min instruction + 5 min buffer** (3 min settling at the start, 2 min flex at the end) · **Topic** Syllogism structure, the four standard statement types, testing conclusions with Venn diagrams, and the "Either I or II" special case · **Prerequisite** Venn Diagrams — overlapping-circle representation, applied here to test logical validity instead of counting
**Session type** Lecture + guided practice. No source slide deck — content from GitBook Concept Explanation text. No classroom quiz bank yet — 5-min slot reserved at end. GitBook "Problem Solving" page is image-only and unrecoverable — all practice problems below are instructor-authored. · **Format** 50-min recalibrated, 2 ALS activities

| Resource | Status |
|---|---|
| Source | GitBook: `session-plans/logical-reasoning/syllogisms/syllogisms-1` (Learning Outcomes, Ideal Format, Introduction, Concept Explanation, Closure — text extracted) |
| Problem Solving bank (GitBook) | image-only, not recoverable — practice problems below are instructor-authored |
| Classroom Quiz | not yet available — 5-min slot reserved at end of session |

**Note on worked example:** the source mentions "a laptops/wireless/desktop example" for the Either-Or case without giving its exact wording (Problem Solving page is image-only). Teaching Block B below constructs a concrete, independently-verified version matching that description, flagged accordingly.

---

## Learning Objectives

By the end of this session, students will be able to:

1. Map the four standard statement types (All A are B, Some A are B, No A is B, Some A are not B) onto Venn diagrams. *(APPLYING)*
2. Test whether a given conclusion definitely follows from one or two statements, using overlapping circles. *(ANALYZING)*
3. Identify the five standard answer options, including the special "Either I or II" and "Neither I nor II" cases. *(UNDERSTANDING)*
4. Distinguish a conclusion that directly follows from one that merely forms a valid complementary pair with another. *(EVALUATING)*

---

## Classroom Settling (0–3 min) · Buffer — not instructional

Board ready. Draw two overlapping circles labelled A and B as a running reference.

---

## Warm-Up Poll — Retrieval Practice on Session 19 (3–7 min) · ALS: Polling

Say: *"Five quick ones from last session."*

**Q1.** In a Venn diagram, what does the overlap represent?
`A` Elements in neither set · `B` Elements shared by both
→ *Read:* B is correct.

**Q2.** "Exactly two" out of three groups — does that include people in all three?
`A` Yes · `B` No
→ *Read:* B is correct.

**Q3.** How do you find "neither" in a two-set problem, given a total surveyed number?
`A` Add only A and only B · `B` Subtract everyone accounted for from the total
→ *Read:* B is correct.

**Q4.** Quick riddle: "All fruits are tasty. All apples are fruits. Can I conclude: Some apples are tasty?"
`A` Yes, definitely follows · `B` No, can't be concluded · `C` Not sure
→ *Read:* A is correct. Don't over-explain yet — this is the Hook, solved formally right after.

**Q5.** How comfortable are you judging whether a conclusion is "definitely true" versus just "possible" from a statement?
`A` Very uncomfortable · `B` Okay with practice · `C` Comfortable
→ *Read:* If mostly A, slow down through Teaching Block A's Venn mappings.

**Running it** — poll tool, ~45 s per question, ~3.75 min total.

---

## Hook (7–10 min)

Say: *"All fruits are tasty. All apples are fruits. Can I conclude: Some apples are tasty?"*

Take a vote, then solve together with a quick diagram: draw "Apples" fully inside "Fruits," and "Fruits" fully inside "Tasty." *"If apples are entirely inside fruits, and fruits are entirely inside tasty things, then apples are entirely inside tasty things too. And if ALL apples are tasty, then certainly SOME apples are tasty — 'all' always implies 'some.'"* **Conclusion: Yes, it follows.**

> *"That felt obvious. Today's session is about the cases that DON'T feel obvious — where a conclusion looks plausible but isn't actually guaranteed, and the one special case where neither of two conclusions works alone, but one of them absolutely must be true."*

---

## Teaching Block A (10–19 min) — TEACH FROM NOTES BELOW

<!-- placement: inferred grouping — no source deck; grouped from GitBook Concept Explanation extraction -->
Covers: the four standard statement types, mapped to Venn diagrams → the five answer options.

**Beats to emphasise**

- **Four standard statement types, write on the board with a quick sketch for each:**
  - **All A are B** → A drawn entirely inside B.
  - **Some A are B** → A and B drawn as partially overlapping circles.
  - **No A is B** → A and B drawn as two separate, non-touching circles.
  - **Some A are not B** → A and B overlap, but part of A sticks outside B.
- **Five possible answer options, write on the board:**
  1. Only Conclusion I follows.
  2. Only Conclusion II follows.
  3. Either I or II follows.
  4. Neither I nor II follows.
  5. Both I and II follow.
- **The testing method:** draw the statement(s) as accurately as the wording allows, then check each conclusion — does the diagram *force* the conclusion to be true, or could the diagram be drawn a different valid way that makes the conclusion false? If it's forced every time, the conclusion follows. If even one valid alternative diagram breaks it, the conclusion does NOT follow.
- **Say explicitly:** *"'Possible' is not the same as 'definite.' A conclusion only follows if there's no way to draw the diagram that makes it false — not just if there's a way to draw it that makes it true."*

**Checkpoint (at 19 min)** — 10 s silent think, cold-call two students:
> *"Statement: 'No cats are dogs.' Conclusion: 'Some cats are not dogs.' Does it follow?"*
> **Answer:** **Yes** — if the circles are completely separate (no overlap at all), then every single cat is definitely not a dog, which is a stronger version of "some cats are not dogs."

---

## ⚡ ALS Activity 1 — Whiteboard Race: Follows or Not? (19–25 min)

**ALS format:** Paired Whiteboard Race — pairs race to sketch a quick Venn diagram and judge whether a given conclusion follows, first correct board up wins the round. Chosen to build fast, disciplined diagram-testing before Teaching Block B introduces the trickier Either-Or case.

**Setup line:**
> *"Pairs, boards up. I'll give you a statement and a conclusion — sketch it, decide 'follows' or 'doesn't follow.' First correct board up wins. Three rounds."*

- Round 1: *"Statement: 'Some doctors are teachers.' Conclusion: 'Some teachers are doctors.'"* → **Follows** — overlap is symmetric, "some A are B" always also means "some B are A."
- Round 2: *"Statement: 'All roses are flowers.' Conclusion: 'All flowers are roses.'"* → **Doesn't follow** — the circles could easily be drawn with Flowers much bigger than Roses.
- Round 3: *"Statement: 'No pens are erasers.' Conclusion: 'All pens are not erasers.'"* → **Follows** — "no A is B" and "all A are not B" describe the exact same diagram.

**How it surfaces:** After each round, have the winning pair sketch their diagram on the board before stating the verdict — the sketch IS the proof, not just a supporting visual.

**Debrief line:**
> *"Round 2 is the trap most people fall into — 'all roses are flowers' feels like it should reverse, but reversing direction on an 'All' statement is exactly what breaks it. Always test by trying to draw it wrong before you trust it's right."*

**Cut rule:** If running short, cut to 2 rounds (drop Round 3), but always require the sketch before the verdict.

---

## Teaching Block B (25–32 min) — TEACH FROM NOTES BELOW

Covers: the Either-Or special case, worked live.

**Beats to emphasise**

- **Either-Or validity criteria, write on the board:** *"Either I or II follows" applies ONLY when two conditions are both true: (1) neither conclusion follows on its own, AND (2) the two conclusions form a complementary pair — meaning at least one of them absolutely must be true, and they can't both be true at the same time.*
- **Worked example, live (instructor-constructed, matching the source's described "laptops/wireless/desktop" scenario):** *"All laptops are wireless devices. Some wireless devices are desktops."* Conclusions: **I. Some laptops are desktops. II. No laptop is a desktop.**
  1. Sketch: Laptops fully inside Wireless Devices. Wireless Devices partially overlaps Desktops — but where exactly that overlap sits relative to Laptops isn't fixed by the statements.
  2. Test Conclusion I alone: could the overlap between Wireless Devices and Desktops happen to include some Laptops? **Yes, possible** — but not guaranteed, since the overlap could just as easily sit entirely outside the Laptops circle. So I does NOT definitely follow.
  3. Test Conclusion II alone: could the diagram be drawn so that NO laptop is a desktop? **Yes, possible** — but equally, it's also possible to draw it so that some laptops ARE desktops. So II does NOT definitely follow either.
  4. **Check the complementary pair condition:** "Some laptops are desktops" and "No laptop is a desktop" are exact opposites — one of them MUST be true (either some overlap exists, or it doesn't), and they can never both be true simultaneously.
  5. **Answer: Either I or II follows.**

**Checkpoint (at 32 min)** — cold-call:
> *"What two conditions must both be true for 'Either I or II follows' to be the correct answer?"*
> **Answer:** **Neither conclusion follows on its own, AND the two conclusions form a genuine complementary pair** (one must be true, both can't be true).

---

## ⚡ ALS Activity 2 — Silent Solve → Vote-Lock → Reveal: Either-Or or Not? (32–40 min)

**ALS format:** Silent Solve, Vote-Lock, Then Reveal — students test a conclusion pair that LOOKS like an Either-Or case but isn't, forcing careful application of the criteria rather than pattern-matching on appearance. Deliberately different register from Activity 1's loud paired race (quiet, individual, single big reveal).

**Setup line:**
> *"On your own, two minutes. Statement: 'All pens are pencils. No pencil is a marker.' Conclusions: I. No pen is a marker. II. Some pens are markers. What's the answer — only I, only II, either, neither, or both? Write your answer and reasoning, hold it up when I say show."*

Give 2 minutes silent work, then: *"Show me — three, two, one, show."*

**The reveal, step by step:**
1. Sketch: Pens fully inside Pencils. Pencils completely separate from Markers (no overlap at all).
2. Since Pens is entirely inside Pencils, and Pencils has zero overlap with Markers, Pens must ALSO have zero overlap with Markers.
3. **Conclusion I ("No pen is a marker") is definitely, forcibly true** — there's no way to draw this diagram where it's false.
4. Conclusion II ("Some pens are markers") is therefore definitely false.
5. **Answer: Only Conclusion I follows** — this is NOT an Either-Or case, even though I and II look like a complementary pair on the surface.

**Debrief line:**
> *"This is the exact trap Either-Or questions are designed to catch you in — I and II here DO look complementary, but I is directly, forcibly provable on its own. Either-Or only applies when NEITHER conclusion can be proven alone. Always test each conclusion individually first, before ever reaching for 'Either-Or' as your answer."*

**Cut rule:** If running short, skip the silent window and solve it together on the board — but always show the direct proof of Conclusion I explicitly, since that's what rules out the Either-Or trap.

---

## Classroom Quiz (40–45 min) · Reserved — not yet available

No quiz bank exists yet for Logical Reasoning. Use this slot for instructor-led review — pose one more genuine Either-Or case (different subject matter from Teaching Block B) and solve together — or fold into Buffer and end early.

---

## Exit Ticket + Homework (45–48 min)

**Exit ticket** (~1 min):

> Statement: "Some students are athletes." Conclusion: "Some athletes are students." Does it follow?
> **Answer:** **Yes, follows** — "Some A are B" is always symmetric with "Some B are A" (same reasoning as Activity 1 Round 1).

Scan responses on the way out — if the Either-Or vs. directly-provable distinction isn't sticking, revisit briefly at the start of Session 21.

**Homework**

| Task | Note |
|---|---|
| Statement: "All squares are rectangles. No rectangle is a triangle." Conclusions: I. No square is a triangle. II. Some squares are triangles. Solve. | Self-check — same structure as Activity 2, verify you get "Only I follows" |
| Construct your own genuine Either-Or pair (two conclusions, neither provable alone, but complementary) | Self-check — tests real understanding of the criteria, not just pattern recognition |

Tell them: *"You've now got the Venn method fully down. Session 21 introduces a faster shortcut for single-statement syllogisms — the Tick and Cross method — so you're not sketching a full diagram every single time."*

---

## Buffer (48–50 min) · Flex — not instructional

Unscheduled on purpose. End early if reached with time on the clock.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Any two "opposite-looking" conclusions automatically trigger "Either I or II" | Surface pattern-matching instead of testing each conclusion individually | ALS Activity 2's explicit trap and reveal |
| "Possible" is the same as "definitely follows" | Confuses one valid diagram with every valid diagram | Teaching Block A's explicit "forced every time" testing rule |
| "All A are B" can be reversed to "All B are A" | Feels symmetric the way "Some" statements are | Activity 1 Round 2's explicit counter-example |
| Every syllogism question has exactly one "right-looking" answer choice, found by feel | Skips the actual diagram-testing step | Teaching Block A's explicit diagram-first method throughout |
| Either-Or requires ANY two conclusions that can't both be true | Only tests one half of the two required conditions | Teaching Block B's explicit two-condition checklist |

---

## Instructor Notes

- **Data note:** no source slide deck exists. Content sourced from GitBook Concept Explanation/Introduction/Closure text extraction. GitBook's "Problem Solving" sub-page is image-only and unrecoverable. The Hook (fruits/apples) and the four Venn statement-type mappings directly match the source's own stated content; the "laptops/wireless/desktop" Either-Or worked example is **instructor-constructed**, built to match the source's described scenario, and independently verified for logical consistency.
- **50-min format: 45 min instruction + 5 min buffer** (3 min settling, 2 min flex).
- **Two ALS activities, different registers:** Activity 1 (Paired Whiteboard Race) is fast/competitive; Activity 2 (Silent Solve → Vote-Lock → Reveal) is quiet/individual, deliberately testing the Either-Or trap with a case that isn't actually Either-Or.
- **First session of the Syllogisms topic** — warm-up poll is retrieval practice on Session 19 (Venn Diagrams), since the overlapping-circle skill carries over directly.
- Classroom Quiz slot reserved-empty per site convention.
