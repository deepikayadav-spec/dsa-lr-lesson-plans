# Session 924 — Balanced Parenthesis

**Duration** 38 min total — 33 min instruction + 5 min Classroom Quiz (cap: 45 + 5, not more) · **Topic** Stack — Balanced Parenthesis Validation · **Prerequisite** Session 923 — Implement Min Stack
**Session type** Concept lecture · **Format** Condensed — active learning strategies referenced by name, single closing quiz

---

## Learning Objectives

By the end of this session, students will be able to:

1. State the three conditions for a bracket sequence to be valid: matching type, correct nesting order, and every closing bracket having a corresponding opening one. *(REMEMBERING)*
2. Explain why a stack — not a counter — is the right tool: order and type both matter, not just counts. *(UNDERSTANDING)*
3. Trace the push-on-open, match-and-pop-on-close algorithm on a given string, including both valid and invalid cases. *(APPLYING)*
4. Identify the three distinct failure modes — closing bracket with an empty stack, closing bracket that doesn't match the stack's top, and leftover unclosed brackets at the end — and explain why the string is invalid in each. *(ANALYZING)*

---

## Warm-Up Poll — Retrieval Practice on Session 923 (0–4 min) · ALS: Polling

5 questions on **Session 923 (Implement Min Stack)**. ~45 s each, project the distribution, never name individuals.

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

**Q5.** *(MSQ — select all that apply)* True of both Min Stack approaches?
`A` `getMin()` is O(1) · `B` `push()` is O(1) · `C` They both use exactly one stack · `D` They both track a running minimum somehow
→ **A, B, D.**

---

## Hook (4–7 min)

Write this on the board: `(){[{}])`

Ask: *"Your code editor underlines a bracket in red the instant you type something like this. How does it know, instantly, without running your program?"*

Let a few guesses land.

> *"Every compiler, every linter, every IDE runs some version of what you're building today. It's one of the oldest problems in computer science, and it's the cleanest possible demonstration of why a stack — specifically, last-in-first-out — is exactly the right shape for 'things that must close in the reverse order they opened.'"*

---

## Slide Block A (7–16 min) — DELIVER SLIDES AS-IS

Covers: Problem Statement (`(`, `)`, `{`, `}`, `[`, `]` — valid if every opening has a matching closing bracket of the same type, closed in the correct order) → Example 1 (`{}()[]` → valid) → Example 2 (`(){[{}])` → invalid, the `{` and `)` don't pair) → Approach: push openings, match closings against the top.

**Beats to emphasise**

- Read Example 2's failure out loud character by character until the mismatch: `(`, `)` — closes fine. `{`, `[`, `{` — all pushed. `}` — matches the most recent `{`, pops fine. `]` — the top is now the *outer* `{`, not `[`. Mismatch.
- **Say explicitly: "count of brackets is not enough."** `(){[{}])` has three of each type — perfectly balanced counts — and is still invalid.
- Preview the two ways this can fail mid-scan, without solving them yet: (1) a closing bracket shows up when the stack is empty, (2) a closing bracket's type doesn't match what's on top.

**Checkpoint (at 16 min)** — cold-call:
> *"Why can't I just count opening and closing brackets and compare the totals?"*
> **Answer:** Equal counts don't guarantee correct order or matching types — `(){[{}])` proves it: 3 and 3, still invalid.

---

## Slide Block B (16–23 min) — DELIVER SLIDES AS-IS

Covers: Full dry run of `s = "(){[{}])"` character by character, ending in the mismatch at `]` → pseudocode → complexity (O(N) time, O(N) space) → code.

**Beats to emphasise**

- Narrate every step exactly as the deck does: `(` push. `)` matches top `(`, pop — stack empty. `{` push. `[` push. `{` push (stack: `{`, `[`, `{`). `}` matches top `{`, pop (stack: `{`, `[`). `]` matches top `[`, pop (stack: `{`). `)` — top is `{`, does **not** match `)` — invalid, stop.
- State the three failure modes explicitly: closing bracket arrives and the stack is **empty** → invalid. Closing bracket arrives and it **doesn't match the top** → invalid. After the whole string, the stack is **not empty** → also invalid.
- Complexity: one pass, one stack, O(N) time and O(N) space.

**Checkpoint (at 23 min)** — cold-call:
> *"Suppose the string is just `"(("` — two opening brackets, nothing else. Walk me through what happens, and is it valid?"*
> **Answer:** Push `(`, push `(` — stack has two elements, string ends. The stack is *not* empty, so it's invalid.

---

## ⚡ Active Learning Strategy 1 — Spot the Bug (23–28 min)

Four bracket strings on the board; students call out valid/invalid and, if invalid, which of the three failure modes applies. Exposes whether students can name the *specific* failure, not just guess valid/invalid.

---

## ⚡ Active Learning Strategy 2 — Live Coding / Dry-Run Relay (28–33 min)

A fresh 8-character string (`{[()()]}`), run one character at a time with students predicting the stack state before each reveal. Exposes whether students can execute the full algorithm end to end on their own.

---

## Classroom Quiz (33–38 min)

**Classroom Quiz** (~5 min) — 5-6 MCQs from the platform bank, run as the closing block of the session, covering the three failure modes and the count-isn't-enough misconception.

---

## Common Misconceptions

| Misconception | Why students hold it | Correct it live by |
|---|---|---|
| Equal counts of each bracket type means the string is balanced | Feels like the natural, simpler check | Slide Block A's `(){[{}])` example — 3 and 3, still invalid |
| Any closing bracket that has *appeared before* is a valid match | Students track "have I seen this type opened" instead of "is it on top *right now*" | ALS 1, `([)]` — `[` was opened, but it's not on top when `)` arrives |
| A string with only opening brackets is "vacuously valid" since nothing ever mismatched | Nothing throws an error mid-scan | ALS 1, `(((` — explicitly checking the stack is empty *after* the loop ends |
| The stack needs to be checked for emptiness only at the very end | Natural to think of "empty" as a final-state property | ALS 1, `)(` — the empty-stack check has to happen the instant a closing bracket arrives, mid-scan |

---

## Instructor Notes

- **38-min format: 33 min instruction + 5 min Classroom Quiz, capped at 45 + 5.** Active learning strategies are referenced by name and format only — run each live using your own sample strings if the ones in the original deck notes aren't at hand.
- **The Classroom Quiz runs last**, as the sole closing activity — no separate exit ticket or homework block.
- **ALS 1 (Spot the Bug) is the load-bearing activity** — naming the *specific* failure mode is the actual transferable skill here, not just voting valid/invalid.
- **This session is a template for everything that follows in interviews:** stack-based validation of nested/paired structures shows up constantly. Say this explicitly if time allows.
