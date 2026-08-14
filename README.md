# DSA + Logical Reasoning — Lesson Plans

Scoped fork of the main `lesson-plans` site: **only** the DSA Stack & Queue block
(Balanced Parenthesis → Asteroid Collision → Largest Rectangle in Histogram →
Queue Intro/Arrays → Queue/Linked List → Stack Using Queue) and the full
Logical Reasoning course. Same static-site engine (`build.py`, markdown in,
HTML out) as the source repo — see that repo's README for the authoring
conventions (file naming, `## Heading (N–M min)` timeline markers, etc.).

```
content/
├─ dsa/                     6 sessions, condensed to a 45+5 min cap each:
│  │                        content + delivery time + instructions, active
│  │                        learning strategies referenced by name, single
│  │                        5-min Classroom Quiz as the closing block.
│  ├─ course.json
│  ├─ session-924-balanced-parenthesis.md
│  ├─ session-925-asteroid-collision.md
│  ├─ session-58-largest-rectangle-in-histogram.md   (merged from a prior 2-part split)
│  ├─ session-59-queue-intro-and-implementation-using-arrays.md
│  ├─ session-60-queue-implementation-using-linked-list.md
│  └─ session-61-stack-using-queue.md
└─ logical-reasoning/       full 24-session course, copied as-is
```

## Build locally

```bash
python build.py
cd dist && python -m http.server 8000   # http://localhost:8000
```

`vercel.json` runs `python3 build.py` as the build command — pushing a new
markdown file is enough to deploy, no manual build step.
