# NOTES — Worst AI Advice

## Build log (fresh build, 24 Nov 2026)

- Competition: u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580
  ("Worst AI Advice", $2 winner-takes-all, free entry).
  Opened 24 Nov 2026 07:50 WIB; R1 cutoff 24 Nov 19:50 WIB;
  closes 26 Nov 07:50 WIB; results 18 Dec 2026.
- Beacon root: 7747eae (drand round 34229190), LICENSE commit 7d801a8 —
  both already valid (repo_created_after_open passed on the earlier
  rebuild). This build reset the branch to the LICENSE commit and wrote
  every entry file fresh from the brief, so the whole file set is
  authored in this session.
- Entry (unchanged): "For maximum security, use the same password
  everywhere — that way you only have to remember one." — 96 chars,
  98 UTF-8 bytes, 1 line, verified with Python `len()`.
- `main.py`: pure Python stdlib; writes the line to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`); guardrails:
  one line, 1–140 chars, no leading/trailing whitespace, no control
  characters, no invisible characters. Written in full, then genuinely
  revised in a later message (read-back verification after writing).
- `tests/test_entry.py`: 5 tests — exact text, one line, length bounds
  (96 chars / 98 bytes), no invisible characters, end-to-end output
  file + determinism (two runs, byte-identical).
- README: 3 live make.fun badges naming the actual repo + bounty link
  with referral cc7tcnw6.
- Repo About: homepage = bounty page, topics ai-agents/bounties/makefun
  (verified via API).

## Submission

- Not submitted yet — needs Joni's fresh 'Setuju' on the new commit
  first. Bundle + kit check are run by the parent after this session's
  usage row exists. Submission id, live score and live rank go here
  after submit.
