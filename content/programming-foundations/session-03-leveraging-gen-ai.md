# Leveraging Gen AI for Accelerated Learning

**Duration** 44 min total — 39 min instruction + 5 min Classroom Quiz · **Topic** Introduction to Python — using AI to understand code, not just get it · **Prerequisite** Coding Practice Walkthrough — Part 1
**Session type** Walkthrough, no classroom quiz bank · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the difference between using AI to *get* an answer and using it to *understand* one. *(REMEMBERING)*
2. Write a prompt that asks for an explanation rather than a solution. *(APPLYING)*
3. Judge whether AI-produced code is correct by running it, not by trusting it. *(ANALYZING)*
4. Name the situations where using AI will damage their learning. *(UNDERSTANDING)*

---

## Warm-Up Poll — Retrieval Practice on Sessions 1–2 (0–6 min) · ALS: Polling

4 questions on the two sessions today leans on.

**Q1.** What are the four steps for attacking a coding problem?
`A` Read, Restate, Write, Run · `B` Think, Type, Test, Submit · `C` Copy, Paste, Run, Fix · `D` Plan, Code, Debug, Deploy
→ **A.**

**Q2.** What does `print("6 * 7")` output?
`A` `42` · `B` `6 * 7` · `C` `42.0` · `D` Error
→ **B.**

**Q3.** Python hits an error on line 4 of a 6-line program. What happens to lines 5 and 6?
`A` They run normally · `B` They never run · `C` They run with a warning · `D` Only line 6 runs
→ **B.**

**Q4.** Have you used ChatGPT or similar for coursework?
`A` Never · `B` Once or twice · `C` Regularly · `D` Every day
→ *No wrong answer — calibrates the whole session.*

---

## Hook (6–10 min)

Put a coding problem on screen. Ask a live AI tool to solve it, paste the answer in, run it. It works.

Let the room sit with that for a second. Then:

> *"So that's it, right? Course over. Except — I want one person to tell me what line three does."*

Take a volunteer. Most rooms cannot answer.

> *"That's the trap. The code works and nobody in this room understands it. In eight weeks you'll be in an interview with no AI, and this exact gap is what shows up. Today isn't about whether you use these tools — you will. It's about using them so you get smarter instead of more dependent."*

---

## Concept Walkthrough (10–25 min)

**Core idea:** AI tools shouldn't replace your understanding — use them as a tutor, not a vending machine. Three reusable prompt templates carry this: (1) ask AI to explain existing code step by step, in simple terms; (2) ask it to raise the difficulty of a quiz on a concept and explain any question you get wrong; (3) ask it to generate a practice problem calibrated to exactly what you've learned so far — filling in "current concept" and "concepts already covered." Your verification is always the run button, not how confident the answer sounds.

**Worked example:** *"Explain what the given code does, then break it down into steps and explain each step in simple terms to someone who's just learned Python."* Run it on a short snippet. Contrast with the weak version: *"Solve this problem"* — that prompt keeps you off the keyboard instead of teaching you anything.

**Checkpoint:**
> *"AI gives you five lines of code and it runs correctly. Are you done?"*
> **Answer:** No — not until you can say what each line does.

---

## ⚡ Active Learning Strategy 1 — Think-Pair-Share (25–32 min)

**ALS format:** Think-Pair-Share. Chosen because the question has no single right answer — it's a judgment call about prompt quality, and judgment calls sharpen through comparing reasoning with a peer before committing.

**Setup line:**
> *"One minute alone, two minutes with the person next to you, then I take answers. Question: you're stuck on a coding problem for ten minutes. What is the best thing to type into an AI tool — and what's the worst?"*

**Timing:** 1 min silent · 2 min pairs · 3 min report-out from three pairs.

**What good answers look like**

| Better prompt | Worse prompt |
|---|---|
| *"I wrote this and got this error. What is the error telling me?"* | *"Solve this problem."* |
| *"Explain what this line does, one word at a time."* | *"Give me the code."* |
| *"Give me a similar, simpler problem to practise."* | *"Is this right?"* (without reading it yourself) |

**Debrief line:**
> *"Notice the pattern. The good ones all keep you at the keyboard. The bad ones move you off it."*

**Cut rule:** 30 s think, 90 s pair, two reports.

---

## ⚡ Active Learning Strategy 2 — Student-Generated Prompt Design (32–39 min)

**ALS format:** Student-Generated Task Design. Chosen instead of a repeat of Think-Pair-Share because the skill here is production, not discussion — students have to construct and own a real artifact (a working prompt) rather than compare opinions on one.

**Setup line:**
> *"Here's a professional-grade prompt template with two blanks in it: `[current concept/topic]` and `[list of previous concepts/topics]`. Your job: fill both blanks for **where you actually are** — you know what you've covered so far. Write the version you'd send tonight. Three minutes."*

**What students do:** Fill in the two blanks on paper or in chat.

**How it surfaces:** Collect three. Read them out anonymously. For each ask: *"Would the problem this generates be solvable with what we know today?"*

That question is the whole activity. Students routinely write something more advanced than they've covered into the blank because it sounds impressive, then get a problem they cannot attempt — which is exactly how they end up pasting an AI answer they don't understand.

Then **run the best one live** and read the generated problem together. Ask: *can we actually solve this right now?*

**Debrief line:**
> *"The template did the hard part. The skill is being honest about what you've actually learned. Overstate it and the AI hands you something you can only copy."*

**Cut rule:** Collect two instead of three; skip the live run.

---

## Classroom Quiz (39–44 min)

**Classroom Quiz** *Reserved — not yet available.* No classroom quiz, reading material, or MCQ pool exists for this session (mirrors the source: a walkthrough/support session by design). Use this slot for an instructor-led recap instead — read out two or three student-written prompts from ALS 2 and ask the room whether each is solvable yet.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Working code means understood code | Output looks the same either way | The hook — nobody can explain line three |
| AI answers are reliable | They're fluent and confident | Naming a time AI was confidently wrong, then asking "how did you find out?" — the answer is always "I checked" |
| Using AI is cheating, full stop | Framed that way elsewhere | Reframing entirely as self-interest — this is how you avoid being stuck in an interview with no AI |
| Prompting is just asking | No exposure to a better version | ALS 1 — comparing good and bad prompts side by side |
| I'll understand it later | Deferred effort feels free | Naming the interview scenario concretely |
