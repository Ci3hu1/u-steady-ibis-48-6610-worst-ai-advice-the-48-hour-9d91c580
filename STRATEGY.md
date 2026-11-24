# STRATEGY — Worst AI Advice

## The entry

One line of the worst possible AI advice, written deadpan, as if it were
genuinely helpful:

> "For maximum security, use the same password everywhere — that way you only have to remember one."

96 characters, 1 line, no trailing newline. It is the whole entry.

## Why this line

The brief asks for the *worst* advice an AI could give. The winning move
is not to be absurd — it is to be plausible. Password reuse is the single
most common real-world security failure, and the line sells it with the
exact logic a lazy user tells themselves: one password is easier to
remember. The joke lands because the "maximum security" framing is the
precise opposite of what the advice does. A judge reading it gets the
twist in one beat: the advice is confident, specific, and catastrophically
wrong.

## What was tried and dropped

- A longer, multi-clause version ("also write it on a sticky note") was
  dropped: every extra clause dilutes the punch, and the gate caps the
  line at 140 characters. One clean sentence wins.
- A version without the em dash ("everywhere. That way...") was dropped:
  the dash keeps the sentence flowing as a single breath, which is how the
  advice would actually sound.
- No second line, no punchline after the fact. The entry is one line by
  the gate, and the line has to carry the whole joke.

## Edge and checks

- Pure Python stdlib, deterministic: the program writes the same 96
  characters (98 UTF-8 bytes) on every run.
- Guardrails in `main.py`: exactly one line, 1–140 chars, no leading or
  trailing whitespace, no control characters, no invisible characters
  (zero-width / BOM code points, which are not control characters yet
  change the byte length).
- Tests (`tests/test_entry.py`, 5 tests): exact text, one line, length
  bounds (96 chars / 98 bytes), no invisible characters, and a real
  end-to-end run that writes `/output/entry.txt` twice and compares the
  bytes.

## Expected outcome

A short, judge-feel one-liner: concrete image (one password everywhere),
one twist (framed as "maximum security"). $2 winner-takes-all, free
entry; the field is small and the entry is cheap to run, so the upside is
a single win in a small table.
