# Balanced Parenthesis

**Duration** 46 min total — 39 min instruction + 7 min Classroom Quiz · **Topic** Stack — Balanced Parenthesis Validation · **Prerequisite** Implement Min Stack
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the three conditions for a bracket sequence to be valid: matching type, correct nesting order, and every closing bracket having a corresponding opening one. *(REMEMBERING)*
2. Explain why a stack — not a counter — is the right tool: order and type both matter, not just counts. *(UNDERSTANDING)*
3. Trace the push-on-open, match-and-pop-on-close algorithm on a given string, including both valid and invalid cases. *(APPLYING)*
4. Identify the three distinct failure modes — closing bracket with an empty stack, closing bracket that doesn't match the stack's top, and leftover unclosed brackets at the end — and explain why the string is invalid in each. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Implement Min Stack (0–6 min) · ALS: Polling

5 questions on **Implement Min Stack**. ~45 s each, project the distribution, never name individuals.

**Q1.** Min Stack's four required operations, all O(1), are:
`A` push, pop, top, getMin · `B` push, pop, sort, getMin · `C` insert, delete, search, getMin · `D` push, remove, peek, getMax
→ **A.**

**Q2.** In the pair-stack approach, each stack entry stores:
`A` Just the value · `B` The value and the minimum-so-far at that point · `C` The value and its index · `D` The value twice
→ **B.**

**Q3.** In the encoded-value approach, an encoded sentinel is pushed only when:
`A` Every single push · `B` The incoming value is a new minimum · `C` The stack is empty · `D` The incoming value equals the current minimum
→ **B.**

**Q4.** On `pop()`, how do you know the value you just removed was an encoded sentinel, not a real element?
`A` It's negative · `B` It's less than the current `mini` · `C` It's greater than the current `mini` · `D` You can't tell
→ **B.**

---

## Hook (6–10 min)

Write this on the board: `(){[{}])`

Ask: *"Your code editor underlines a bracket in red the instant you type something like this. How does it know, instantly, without running your program?"*

Let a few guesses land.

> *"Every compiler, every linter, every IDE runs some version of what you're building today. It's one of the oldest problems in computer science, and it's the cleanest possible demonstration of why a stack — specifically, last-in-first-out — is exactly the right shape for 'things that must close in the reverse order they opened.'"*

---

## Concept Walkthrough (10–25 min)

**Core idea:** push every opening bracket onto a stack. On a closing bracket, check the top of the stack — if it matches, pop; if it doesn't match, or the stack is already empty, the string is invalid. After the whole string, the stack must also be empty — leftover unclosed openings are invalid too.

**Worked example** — `s = "(){[{}])"`: `(` push. `)` matches top `(`, pop — stack empty. `{` push. `[` push. `{` push (stack: `{`, `[`, `{`). `}` matches top `{`, pop (stack: `{`, `[`). `]` matches top `[`, pop (stack: `{`). `)` — top is `{`, does **not** match `)` — invalid, stop.

**Say explicitly:** counting brackets isn't enough — `(){[{}])` has 3 of each type and is still invalid. Order and type both matter, not just totals.

**Checkpoint:**
> *"Suppose the string is just `"(("` — two opening brackets, nothing else. Valid or invalid?"*
> **Answer:** Invalid — the stack still has two unmatched elements when the string ends.

---

## ⚡ Active Learning Strategy 1 — Spot the Bug (25–32 min)

**ALS format:** Spot the Bug — exposes whether students can identify *which* of the three failure modes applies, not just guess valid/invalid from a glance. Naming the specific failure is the actual transferable skill here, not just voting.

**Setup line:**
> *"Four strings on the board. For each one: valid or invalid? If invalid, tell me exactly which character breaks it and which failure mode it is — empty-stack-on-close, mismatched-type-on-close, or leftover-stack-at-the-end."*

```
1.  "([])"
2.  "([)]"
3.  "((("
4.  ")("
```

45 seconds silent, then hands up. Take one student per string.

**Answers**

| # | Valid? | Reason |
|---|---|---|
| 1 | Valid | Properly nested: `(`, `[`, `]` matches `[`, `)` matches `(` |
| 2 | Invalid | At `)`: stack top is `[`, doesn't match — mismatched-type-on-close |
| 3 | Invalid | End of string, stack still has 3 unmatched `(` — leftover-stack-at-the-end |
| 4 | Invalid | At `)`: stack is empty (nothing pushed yet) — empty-stack-on-close |

**How it surfaces:** For string 2, push students to say specifically what's on top of the stack the instant `)` appears (`[`, not `(`) — this is the mismatched-type failure, distinct from string 4's empty-stack failure. Many students will say "invalid" correctly but conflate the two reasons.

**Debrief line:**
> *"Three ways this breaks: empty stack when you need to pop, wrong type on top when you pop, or leftover stack when you're done. Every invalid string in this problem is exactly one of those three — nothing else."*

**Cut rule:** Do strings 2 and 4 only — they're the two genuinely distinct mid-scan failure modes; 1 and 3 are confirmations, not new information.

---

## ⚡ Active Learning Strategy 2 — Live Coding / Dry-Run Relay (32–39 min)

**ALS format:** Live Coding / Dry-Run Relay — exposes whether students can execute the full algorithm themselves end to end, on a string they haven't seen. Closing activity: the first time students run the complete algorithm start to finish, on eight characters in a row, without the safety of a partial example.

**Setup line:**
> *"New string: `{[()()]}`. I want the stack state after every single character — call it out before I write it."*

Run **one character at a time**, taking a prediction before each:

```
{   → push                    Stack: [{]
[   → push                    Stack: [{, []
(   → push                    Stack: [{, [, (]
)   → matches top (           Stack: [{, []
(   → push                    Stack: [{, [, (]
)   → matches top (           Stack: [{, []
]   → matches top [           Stack: [{]
}   → matches top {           Stack: []
```

End of string, stack empty → **valid**.

**How it surfaces:** At each `)`, confirm out loud what's being matched against — students should say "top of stack" every time, not "the most recent `(` I can remember," which breaks down on longer strings.

**Debrief line:**
> *"Every close only ever looks at one thing: the top of the stack. Not the whole string, not memory — just the top. That's the entire algorithm, executed eight times in a row."*

**Cut rule:** Do the first four characters only (`{[()`) plus the final `}` — enough to show both a push run and a full unwind to empty.

---

## Classroom Quiz (39–46 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session, covering the three failure modes and the count-isn't-enough misconception.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Equal counts of each bracket type means the string is balanced | Feels like the natural, simpler check | `(){[{}])` — 3 of each type, still invalid |
| Any closing bracket that has *appeared before* is a valid match | Students track "have I seen this type opened" instead of "is it on top *right now*" | ALS 1, `([)]` — `[` was opened, but it's not on top when `)` arrives |
| A string with only opening brackets is "vacuously valid" since nothing ever mismatched | Nothing throws an error mid-scan | ALS 1, `(((` — explicitly checking the stack is empty *after* the loop ends |
| The stack needs to be checked for emptiness only at the very end | Natural to think of "empty" as a final-state property | ALS 1, `)(` — the empty-stack check has to happen the instant a closing bracket arrives, mid-scan |

---
