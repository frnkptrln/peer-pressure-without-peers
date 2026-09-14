"""The post-hoc answer-line reading of E4 replies (D6): exactly one standalone `[A]`/`[B]` line, bold allowed."""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

import e4_answerline as al  # noqa: E402


def row(reply, *, valid=False, choice=None, status="success", clean=True):
    return {"call_id": "x", "reply": reply, "valid": valid, "choice": choice, "status": status,
            "infrastructure_clean": clean}


class AnswerLine(unittest.TestCase):
    def test_plain_line_is_read_even_when_both_options_are_named(self):
        self.assertEqual(al.answer_line("[B]\n\nAction [A] is prohibited, so I take [B]."), ("B", False))

    def test_bold_line_counts_and_is_flagged(self):
        self.assertEqual(al.answer_line("Reasoning first.\n\n**[A]**"), ("A", True))

    def test_whitespace_and_case_are_tolerated(self):
        self.assertEqual(al.answer_line("  [ a ]  "), ("A", False))

    def test_no_standalone_line_is_invalid(self):
        self.assertEqual(al.answer_line("I choose [B] because the rule forbids [A]."), (None, None))

    def test_two_standalone_lines_are_invalid(self):
        self.assertEqual(al.answer_line("[A]\n\nOn reflection:\n[B]"), (None, None))

    def test_empty_reply_is_invalid(self):
        self.assertEqual(al.answer_line(None), (None, None))
        self.assertEqual(al.answer_line(""), (None, None))

    def test_reread_keeps_fields_and_marks_parse(self):
        rows = [row("[B]\n\nboth [A] and [B] named", valid=False), row("[A]", valid=True, choice="A"),
                row("[A]", status="error"), row("**[B]**")]
        out, s = al.reread(rows)
        self.assertEqual([r["choice"] for r in out], ["B", "A", None, "B"])
        self.assertEqual([r["valid"] for r in out], [True, True, False, True])
        self.assertTrue(all(r["parse"] == "answer_line_post_hoc" for r in out))
        self.assertEqual((s["valid"], s["plain"], s["bold"]), (3, 2, 1))
        self.assertEqual((s["frozen_valid"], s["frozen_agree"]), (1, 1))

    def test_disagreement_with_frozen_rule_is_counted(self):
        out, s = al.reread([row("[A]", valid=True, choice="B")])
        self.assertEqual((s["frozen_valid"], s["frozen_agree"]), (1, 0))


if __name__ == "__main__":
    unittest.main()
