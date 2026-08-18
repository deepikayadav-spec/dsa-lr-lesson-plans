# DSA Lesson Plan Guide

**For instructors, read once before your first session in this block.** This explains what's in each of the 6 lesson plans and why — not how to run a practice block (see the separate **Practice Session Playbook** for that; this block is lecture, not practice).

---

## 1. Anatomy of a session — same 9 sections, every time

Read a session top to bottom once; after that you'll recognize the shape instantly.

**Learning Objectives** — 4 outcomes, tagged REMEMBERING → UNDERSTANDING → APPLYING → ANALYZING. Not delivered to students; this is what the rest of the plan is built to hit.

**Warm-Up Poll (0–6 min)** — 4–5 MCQs on the *previous* session, run as a live poll using **Mentimeter or a similar live-polling tool** — project the question, students answer on their phones/laptops, results shown live. Not a show-of-hands. Retrieval practice, not new material.

**Hook (6–9 min)** — a short question or board example that motivates *why today's problem needs a new tool*, before any formal definition. Scripted, close to verbatim.

**Problem Statement (9–13 min)** — the actual problem, stated cleanly: input, output, what makes an output correct, and **2 worked input/output examples**. This exists so students know exactly what they're being asked to solve before you explain how — deliver it before Concept Walkthrough, not folded into it. A *(Deck: Slides …)* line under the heading tells you which slides of the session's actual deck this maps to — flip there, don't paraphrase from memory.

**Concept Walkthrough (13 min → varies)** — the algorithm itself, in a fixed sub-order every time:
1. **Core idea** — the one-paragraph insight.
2. **Dry Run** — a specific input traced step by step, showing the status of the stack/queue after *every* update (see §2 for the notation).
3. **Pseudocode** — derived from the core idea, language-neutral.
4. **Deriving the code** — the C++ implementation, built live in the coding playground from the pseudocode, not read out as a finished block.
5. **Checkpoint** — one cold-call question that tests whether the core idea actually landed, asked live before moving on.

Same as Problem Statement, a *(Deck: …)* line under the heading gives the real slide ranges for each of these five, in order — so you know exactly when to flip the deck forward.

This block's length is the one thing that varies session to session (17–23 min) — it's sized to the algorithm's real complexity, not padded or compressed to a fixed number.

**Active Learning Strategy (~7 min)** — exactly **one** hands-on activity, not two. Named formats repeat across sessions (Spot the Bug, Predict & Discuss, Dry-Run Relay) — each names its format up front and states exactly what skill it exposes. Every activity includes a **Cut rule**: what to drop first if you're running behind.

**Classroom Quiz (~5 min)** — 5–6 MCQs pulled from the platform bank live in class, closing block.

**Buffer** — unscheduled on purpose. **Do not fill it with more content.** If you land here with time left, let the session end early. It exists because real delivery time varies session to session and pod to pod — protecting it is what keeps the fixed minute marks (Hook at 6, Concept Walkthrough at 13, etc.) honest for the *next* session too.

**Common Misconceptions** — a table, one row per wrong mental model, each tied to the specific moment in the session (which example, which activity) that corrects it live. Read this before class — it tells you what to listen for while circulating.

---

## 2. Reading the stack/queue traces

Every Dry Run and activity shows the status of the stack/queue after each update as a **plain top→bottom (or front→back) list — never wrapped in `[ ]`.** An empty stack/queue is written explicitly as `(empty)`, never a blank list.

This is deliberate, not stylistic: several of these problems take `[` and `]` as literal *input* characters (Balanced Parenthesis most obviously). Using square brackets as the container notation *too* reads as ambiguous to a first-time student — is `[` data or notation? Plain lists sidestep the question entirely, so the convention is kept everywhere in this block, even in sessions where the input itself has no brackets.

---

## 3. Optional Activity — what it's for

Sessions 1, 2, 4, 5, and 6 each carry a second activity, demoted to an **Optional Activity** section at the end (after Common Misconceptions, no clock time attached — it won't show up on the on-page timeline). This is real, usable material, not a discard pile:

- Run it if the room finishes the core flow early.
- Run it as a 5-minute warm-up recap at the start of the *next* session.
- Skip it outright — nothing in the core 50-minute flow depends on it.

It was demoted, not deleted, specifically because it duplicated a skill Concept Walkthrough's Dry Run already covers (usually a step-by-step trace) — the kept activity is the one that exercises a genuinely distinct skill (classifying failure modes, a live bug hunt, a complexity discussion). Session 3 (Largest Rectangle) never had a second activity to begin with — its one Dry-Run Relay already runs in two parts.

---

## 4. Quick reference

| Section | Fixed at | Notes |
|---|---|---|
| Warm-Up Poll | 0–6 min | Previous session only |
| Hook | 6–9 min | Scripted, board or question |
| Problem Statement | 9–13 min | Input/output + 2 examples, always |
| Concept Walkthrough | 13 min → varies | Core idea → Dry Run → pseudocode → deriving the code → checkpoint |
| Active Learning Strategy | ~7 min | One activity, has a Cut rule |
| Classroom Quiz | ~5 min | Platform bank, live |
| Buffer | remainder → 50 min | Never filled with content |
| Optional Activity | untimed, end of doc | Run if time permits or as next-session warm-up |

---

## 5. This guide vs. the Practice Session Playbook

This document explains the **lecture** sessions above — one instructor, one room, delivering a concept. The **Practice Session Playbook** is a different document for a different session type: a timed, silent work block where students attempt problems themselves and you check progress pod by pod. Don't mix the two formats — a lecture session doesn't have pods or a progress tracker, and a practice block doesn't have a Concept Walkthrough.
