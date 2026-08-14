# Lesson Plans

Scoped fork of the main `lesson-plans` site — a curated subset, not the full
multi-course repo. Same static-site engine (`build.py`, markdown in, HTML
out) as the source repo — see that repo's README for the authoring
conventions (file naming, `## Heading (N–M min)` timeline markers, etc.).

```
content/
├─ programming-foundations/  first 2 sessions (Programming with Python,
│  │                          Coding Practice Walkthrough Part 1), condensed
│  └─ practice-session-playbook.md   general instructor guide (Guides section)
├─ dsa/                       6-session Stack & Queue block, condensed:
│  │                          (Balanced Parenthesis → Asteroid Collision →
│  │                          Largest Rectangle in Histogram → Queue Intro/
│  │                          Arrays → Queue/Linked List → Stack Using Queue)
│  │                          session numbers hidden (source IDs were
│  │                          non-sequential/confusing)
│  └─ practice-session-playbook.md   general instructor guide (Guides section)
└─ aptitude/                  "Quantitative and logical reasoning" — one
   │                          merged course page:
   │                          1-2  Quantitative Aptitude (condensed)
   │                          3-26 Logical Reasoning, full 24-session course,
   │                               renumbered +2 to follow on from Aptitude's
   │                               own 2 sessions, copied as-is otherwise
   └─ practice-session-playbook.md   general instructor guide (Guides section)
```

The condensed session files (Programming Foundations' 2, all of DSA,
Aptitude's first 2) follow the same format: Learning Objectives → Warm-Up
Poll → Hook → Concept Walkthrough (core idea + one worked example + one
checkpoint) → 2 Active Learning Strategies referenced by name/format, not
fully scripted → a single 5-min Classroom Quiz as the closing block →
Common Misconceptions. Capped at 45 min instruction + 5 min quiz. No
Instructor Notes section, no Platform units/resource table, no Exit
Ticket/Homework/buffer blocks — deliberately stripped to keep each plan
lean. The relocated Logical Reasoning sessions (now under `aptitude/`) keep
their original full format untouched, just renumbered.

`practice-session-playbook.md` — a duration-agnostic instructor guide for
running practice/problem-solving blocks (pods, anchors, red-slip signal,
ladder checks, live solve, exit gate) — is copied identically into all three
course folders and shows up under each course's **Guides** section, since
it isn't tied to any one course's content.

## Build locally

```bash
python build.py
cd dist && python -m http.server 8000   # http://localhost:8000
```

`vercel.json` runs `python3 build.py` as the build command — pushing a new
markdown file is enough to deploy, no manual build step.
