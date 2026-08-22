"""Gate the CV skill: byte-identical mirror, declared resume id, no stale DOCX pipeline."""

from __future__ import annotations

import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CANONICAL = REPO / ".agents/skills/phd-candidate-cv"
MIRROR = REPO / ".claude/skills/phd-candidate-cv"
RESUME_ID = "b55d572d-8f60-43cc-bafa-89ebe995dd7a"


def tree(root: Path) -> dict[str, bytes]:
    return {
        str(p.relative_to(root)): p.read_bytes()
        for p in sorted(root.rglob("*"))
        if p.is_file()
    }


class CvSkillTest(unittest.TestCase):
    def test_canonical_skill_exists(self) -> None:
        self.assertTrue((CANONICAL / "SKILL.md").is_file())
        self.assertTrue((CANONICAL / "agents/openai.yaml").is_file())

    def test_claude_mirror_is_byte_identical(self) -> None:
        self.assertEqual(tree(CANONICAL), tree(MIRROR))

    def test_skill_declares_resume_id(self) -> None:
        self.assertIn(RESUME_ID, (CANONICAL / "SKILL.md").read_text(encoding="utf-8"))

    def test_instruction_mirrors_match(self) -> None:
        self.assertEqual(
            (REPO / "AGENTS.md").read_bytes(), (REPO / "CLAUDE.md").read_bytes()
        )

    def test_no_stale_academic_cv_references(self) -> None:
        needle = "phd-candidate-" + "academic-cv"
        here = Path(__file__).resolve()
        stale = []
        for path in REPO.rglob("*"):
            if not path.is_file() or ".git/" in str(path) or "__pycache__" in str(path):
                continue
            if path.suffix not in {".md", ".py", ".yml", ".yaml"}:
                continue
            if path.resolve() == here:
                continue
            if needle in path.read_text(encoding="utf-8", errors="ignore"):
                stale.append(str(path.relative_to(REPO)))
        self.assertEqual(stale, [])


if __name__ == "__main__":
    unittest.main()
