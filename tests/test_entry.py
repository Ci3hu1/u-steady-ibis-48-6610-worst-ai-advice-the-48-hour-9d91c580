#!/usr/bin/env python3
"""Tests for the Worst AI Advice one-line entry."""

import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

import main as entry

EXPECTED = "For maximum security, use the same password everywhere — that way you only have to remember one."


class TestEntry(unittest.TestCase):
    def test_exact_text(self):
        self.assertEqual(entry.ADVICE, EXPECTED)

    def test_one_line(self):
        self.assertNotIn("\n", entry.ADVICE)
        self.assertNotIn("\r", entry.ADVICE)

    def test_length_1_to_140(self):
        self.assertGreaterEqual(len(entry.ADVICE), 1)
        self.assertLessEqual(len(entry.ADVICE), 140)
        self.assertEqual(len(entry.ADVICE), 96)
        self.assertEqual(len(entry.ADVICE.encode("utf-8")), 98)

    def test_no_invisible_characters(self):
        self.assertFalse(any(ch in entry.INVISIBLE for ch in entry.ADVICE))
        self.assertFalse(
            any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in entry.ADVICE)
        )

    def test_output_file_and_determinism(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
            script = os.path.join(REPO_ROOT, "main.py")
            first = subprocess.run(
                [sys.executable, script],
                cwd=REPO_ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )
            with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as f:
                first_text = f.read()
            self.assertEqual(first_text, EXPECTED)
            second = subprocess.run(
                [sys.executable, script],
                cwd=REPO_ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )
            with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as f:
                second_text = f.read()
            self.assertEqual(second_text, first_text)
            self.assertEqual(first.returncode, 0)
            self.assertEqual(second.returncode, 0)


if __name__ == "__main__":
    unittest.main()
