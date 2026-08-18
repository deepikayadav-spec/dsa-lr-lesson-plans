# DSA Lesson Plan Guide

**For instructors, read once before your first session in this block.** This explains what's in each of the 6 lesson plans and why — not how to run a practice block (see the separate **Practice Session Playbook** for that; this block is lecture, not practice).

---

## 1. Two formats in this block — know which one you're reading

- **Sessions 1, 2, 6** (Balanced Parenthesis, Asteroid Collision, Stack Using Queue) use the **original condensed format** — see §2.
- **Sessions 3, 4, 5** (Largest Rectangle in Histogram, Queue — Array, Queue — Linked List) were rebuilt against instructor feedback and the **Class Delivery Framework** — richer, with explicit Safe Points, a written Observations step, and scripted engagement dialogue. See §3.

Both formats run 50 min total, buffer inside the 50 (never additive), and treat Key Takeaways as mandatory. If 1, 2, or 6 get revised later, bring them up to the §3 standard rather than inventing a third shape.

---

## 2. Anatomy — original format (Sessions 1, 2, 6)

**Learning Objectives** — 4 outcomes, tagged REMEMBERING → UNDERSTANDING → APPLYING → ANALYZING. Not delivered to students; this is what the rest of the plan is built to hit.

**Warm-Up Poll (0–6 min)** — 4–5 MCQs on the *previous* session, run as a live poll using **Mentimeter or a similar live-polling tool**. Retrieval practice, not new material.

**Hook (6–9 min)** — a short question or board example that motivates *why today's problem needs a new tool*, before any formal definition. Scripted, close to verbatim.

**Problem Statement (9–13 min)** — input, output, what makes an output correct, and **2 worked input/output examples**. Delivered before Concept Walkthrough, not folded into it. A *(Deck: Slides …)* line under the heading tells you which slides of the session's actual deck this maps to.

**Concept Walkthrough (13 min → varies)** — the algorithm itself, in a fixed sub-order:
1. **Core idea** — the one-paragraph insight.
2. **Dry Run** — a specific input traced step by step, showing the status of the stack/queue after *every* update (see §5 for the notation).
3. **Pseudocode** — derived from the core idea, language-neutral.
4. **Deriving the code** — the C++ implementation, built live in the coding playground from the pseudocode, not read out as a finished block.
5. **Key Takeaways** — **mandatory**. A short bullet list matching the session's own deck (its Key Takeaways slides, near the end).
6. **Checkpoint** — one cold-call question that tests whether the core idea landed, asked live before moving on.

**Active Learning Strategy (~7 min)** — exactly **one** hands-on activity, not two. Named formats repeat (Spot the Bug, Predict & Discuss, Dry-Run Relay), each stating up front what skill it exposes. Every activity includes a **Cut rule**.

**Classroom Quiz (~5 min)** — 5–6 MCQs from the platform bank, live, closing block.

**Buffer** — unscheduled on purpose, inside the 50 min. **Do not fill it with content.**

**Common Misconceptions** — a table, one row per wrong mental model, tied to the specific moment that corrects it live.

---

## 3. Anatomy — Class Delivery Framework format (Sessions 3, 4, 5)

Same overall shell (Warm-Up → Hook → Problem Statement → Concept Walkthrough → Engagement → Quiz → Buffer), but every beat now does more work, and **Safe Points** run throughout rather than a single end-of-block checkpoint.

**Warm-Up Poll (0–5 min)** — **recap via questioning, not instructor summary.** Run the poll cold; read the aggregate result out loud as the recap. Don't re-teach the previous session yourself first — the numbers *are* the recap.

**Hook (5–8 min)** — states the topic name explicitly ("Today we're learning X"), then names the concept's real-world advantage concretely, not just an analogy.

**Problem Statement (~4 min)** — input/output + 2 examples, same as §2, plus **Safe Point 1**: a specific technique (usually Paraphrase-Back), checking understanding before any approach is discussed. Don't proceed on a shaky paraphrase.

**Concept Walkthrough** — longest block, in a fixed sub-order:
1. **Approach Exploration** — ask students what they'd try first, *before* revealing anything. Bank their guess (right or wrong — it gets revisited later, usually in the Engagement Activity). Give only a **one-line brief** of the real approach, never the full solution up front — a student who doesn't know the solution yet can't absorb a complete walkthrough of it.
2. **Dry Run** — a specific input traced step by step. Simple mechanics get one cycle; a genuinely complex algorithm (LRH's optimal approach) gets **two cycles** — a brief one that just proves the mechanism works, then a detailed one tracking every pointer/index and hitting the edge cases.
3. **Observations** — written on the board in plain English, *before* pseudocode. This is the bridge: students can't hold an entire dry run in memory while pseudocode gets derived, so the observations are what pseudocode derivation actually refers back to.
4. **Safe Point** (Hand-Signal Check, usually) — confirms the approach landed before pseudocode starts.
5. **Pseudocode** — derived **piece by piece, not all at once** — each piece tied back to a specific observation.
6. **Safe Point** (Deliberate Bug, usually) — an intentionally wrong line, to check whether students are actually tracking the logic or just nodding along.
7. **Deriving the Code** — built live in the coding playground, every line related back to the pseudocode line it came from. Language gaps (unfamiliar syntax) get addressed before they'd otherwise surface mid-derivation.
8. **Complexity — derived, not stated.** A concrete example size, real operations counted, the pattern generalized. Never just "this is O(N)."
9. **Key Takeaways** — mandatory, matching the deck's own slides.
10. **Safe Point** (Quiet-Bench Check-In, usually) — a low-stakes question, asked walking toward a less-interactive part of the room.

**LRH only** repeats steps 2–9 twice: a deliberately lean pass for the brute-force/two-pass approach (dry run + pseudocode, no live coding — its job is to motivate the shortcut, not to be implemented), then an explicit **Bottleneck & Transition** beat (its own Safe Point, Physical Movement Reset), then the full nine-step cycle for the optimal approach.

**Engagement Activity (~5 min)** — not "Active Learning Strategy." **Reuses the session's own worked example — no new content, no added time.** Framed as "what if" prompts building on what's already covered. Scripted with the instructor's exact dialogue *and* anticipated student responses, including plausible-but-wrong ones and how to redirect them — not just the correct answer.

**Classroom Quiz (~5 min)**, **Buffer (inside the 50, not additive)** — same as §2.

---

## 4. Safe Point techniques — rotate these, don't reuse the same one twice in a row

| Technique | How it works |
|---|---|
| **Paraphrase-Back** | Pick a student, ask them to restate the problem/approach in their own words, "as if explaining it for the first time." |
| **Hand-Signal Check** | Thumbs up if understood, a different signal (thumbs down) if lost — scan the room fast. |
| **Deliberate Bug** | Show an intentionally wrong line (flipped condition, missing reset, wrong index) and ask "is this correct?" Silence or a reflexive yes is not a real check — this is. |
| **Quiet-Bench Check-In** | Walk toward a less-interactive part of the room, ask a low-stakes question there specifically. |
| **Physical Movement Reset** | Step away from the board, walk toward the students, ask the question, then hold a few seconds of deliberate silence before calling on anyone. |
| **Walk the Room** | During hands-on coding, walk between benches and glance at progress — catches confusion students won't volunteer. |

A plain "Any doubts?" is not a Safe Point — it almost always returns silence or a reflexive yes. Use one of the above instead.

---

## 5. Reading the stack/queue traces

Every Dry Run and activity shows the status of the stack/queue after each update as a **plain top→bottom (or front→back) list — never wrapped in `[ ]`.** An empty stack/queue is written explicitly as `(empty)`, never a blank list.

This is deliberate, not stylistic: several of these problems take `[` and `]` as literal *input* characters (Balanced Parenthesis most obviously). Using square brackets as the container notation too reads as ambiguous to a first-time student. Plain lists sidestep the question, so the convention is kept everywhere in this block.

---

## 6. Optional Activity — what it's for

Sessions 1, 2, 4, 5, and 6 each carry a second activity, demoted to an **Optional Activity** section at the end (after Common Misconceptions, no clock time attached — it won't show up on the on-page timeline). This is real, usable material, not a discard pile:

- Run it if the room finishes the core flow early.
- Run it as a 5-minute warm-up recap at the start of the *next* session.
- Skip it outright — nothing in the core 50-minute flow depends on it.

It was demoted, not deleted, specifically because it duplicated a skill the Dry Run already covers — the kept activity (Engagement Activity in §3 sessions, Active Learning Strategy in §2 sessions) exercises a genuinely distinct skill instead. **Session 3 (LRH) has no Optional Activity at all** — between the two-approach Concept Walkthrough and the Engagement Activity, there's no leftover material to demote.

---

## 7. Quick reference

**Sessions 1, 2, 6 (original format):**

| Section | Fixed at | Notes |
|---|---|---|
| Warm-Up Poll | 0–6 min | Previous session only |
| Hook | 6–9 min | Scripted, board or question |
| Problem Statement | 9–13 min | Input/output + 2 examples, always |
| Concept Walkthrough | 13 min → varies | Core idea → Dry Run → pseudocode → deriving the code → Key Takeaways (mandatory) → checkpoint |
| Active Learning Strategy | ~7 min | One activity, has a Cut rule |
| Classroom Quiz | ~5 min | Platform bank, live |
| Buffer | remainder → 50 min | Never filled with content |
| Optional Activity | untimed, end of doc | Run if time permits or as next-session warm-up |

**Sessions 3, 4, 5 (Class Delivery Framework format):**

| Section | Fixed at | Notes |
|---|---|---|
| Warm-Up Poll | 0–5 min | Recap via questioning — poll cold, no pre-summary |
| Hook | ~3 min | Names the topic + a concrete advantage |
| Problem Statement | ~4 min | + Safe Point 1 (Paraphrase-Back) |
| Concept Walkthrough | longest block | Approach Exploration → Dry Run → Observations → Safe Point → Pseudocode → Safe Point → Deriving the Code → Complexity (derived) → Key Takeaways → Safe Point. LRH: two full cycles + Bottleneck & Transition. |
| Engagement Activity | ~5 min | Reuses the session's own example, scripted dialogue + anticipated responses |
| Classroom Quiz | ~5 min | Platform bank, live |
| Buffer | remainder → 50 min | Inside the 50, never additive, never filled with content |
| Optional Activity | untimed, end of doc | Sessions 4, 5 only — LRH has none |

---

## 8. This guide vs. the Practice Session Playbook

This document explains the **lecture** sessions above — one instructor, one room, delivering a concept. The **Practice Session Playbook** is a different document for a different session type: a timed, silent work block where students attempt problems themselves and you check progress pod by pod. Don't mix the two formats — a lecture session doesn't have pods or a progress tracker, and a practice block doesn't have a Concept Walkthrough.
