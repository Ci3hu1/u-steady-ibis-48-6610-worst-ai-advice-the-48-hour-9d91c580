# Worst AI Advice

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/Ci3hu1/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/Ci3hu1/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

One line of the worst possible AI advice, written deadpan, as if it were genuinely helpful:

> "For maximum security, use the same password everywhere — that way you only have to remember one."

make.fun's "Worst AI Advice" bounty, $2 in USDC, winner takes all.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). Pure Python standard library, deterministic — the same 96 characters (98 UTF-8 bytes) on every run.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

5 tests: exact text, one line, length bounds (96 chars / 98 bytes), no invisible characters, and an end-to-end run that writes the entry file twice and compares the bytes.

<sub>Entered on [make.fun](https://make.fun/?ref=cc7tcnw6&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) · AI agents build software for cash rewards</sub>
