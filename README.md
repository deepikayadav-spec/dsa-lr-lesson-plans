# Lesson Plans

Scoped fork of the main `lesson-plans` site — a curated subset, not the full
multi-course repo. Same static-site engine (`build.py`, markdown in, HTML
out) as the source repo — see that repo's README for the authoring
conventions (file naming, `## Heading (N–M min)` timeline markers, etc.).

```
content/
├─ programming-foundations/  first 2 sessions (Programming with Python,
│                             Coding Practice Walkthrough Part 1)
├─ dsa/                       6-session Stack & Queue block, condensed:
│  │                          (Balanced Parenthesis → Asteroid Collision →
│  │                          Largest Rectangle in Histogram → Queue Intro/
│  │                          Arrays → Queue/Linked List → Stack Using Queue)
│  │                          session numbers hidden (source IDs were
│  │                          non-sequential/confusing)
│  └─ course.json
├─ logical-reasoning/         full 24-session course, copied as-is
└─ aptitude/                  first 2 sessions (Introduction to Quantitative
                               Aptitude, Number Systems 1)
```

Every session file below the full-course Logical Reasoning follows the same
condensed format: Learning Objectives → Warm-Up Poll → Hook → Concept
Walkthrough (core idea + one worked example + one checkpoint) → 2 Active
Learning Strategies referenced by name/format, not fully scripted → a single
5-min Classroom Quiz as the closing block → Common Misconceptions. Capped at
45 min instruction + 5 min quiz. No Instructor Notes section, no Platform
units/resource table, no Exit Ticket/Homework/buffer blocks — those were
deliberately stripped to keep each plan lean.

## Build locally

```bash
python build.py
cd dist && python -m http.server 8000   # http://localhost:8000
```

`vercel.json` runs `python3 build.py` as the build command — pushing a new
markdown file is enough to deploy, no manual build step.
