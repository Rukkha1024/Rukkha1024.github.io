from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from docx import Document


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/phd-candidate-academic-cv"
BUILD = SKILL / "scripts/build_academic_cv.py"
AUDIT = SKILL / "scripts/audit_academic_cv.py"


def sample_source() -> dict:
    return {
        "contract_version": "1.2",
        "mode": "draft",
        "name": "Sample Applicant",
        "contact": {
            "location": "City, Country",
            "email": "sample@example.com",
            "website": "example.com",
            "github": "github.com/example",
        },
        "research_profile": "Studies human movement with reproducible analysis.",
        "education": [
            {
                "institution": "Example University",
                "dates": "2024-present",
                "credential": "Graduate study",
                "details": ["Advisor: Example Advisor"],
                "gpa": "GPA: 3.62/4.00 (provisional conversion)",
            }
        ],
        "relevant_coursework": "Relevant coursework: motor control and biomechanics.",
        "publications": [
            {
                "citation": "Sample Applicant. (2026). Example article. Example Journal.",
                "url": "https://doi.org/10.0000/example",
            }
        ],
        "research_experience": [
            {
                "heading": "Example University - Research",
                "dates": "2024-present",
                "subtitle": "Graduate researcher",
                "bullets": ["Analyzed movement data and documented reproducible results."],
            }
        ],
        "skills": [{"label": "Analysis", "text": "Python and signal processing"}],
        "engagement": [
            {
                "heading": "Community workshop",
                "dates": "2025",
                "bullets": ["Taught evidence-based movement exercises."],
            }
        ],
        "software": [
            {
                "name": "Example tool",
                "display_url": "github.com/example/tool",
                "url": "https://github.com/example/tool",
            }
        ],
        "evidence": {
            "four_point_gpa_result_pdf": None,
            "bachelor_degree_certificate_pdf": None,
        },
        "privacy": {"prohibited_literals": ["PRIVATE-STUDENT-ID"]},
    }


class AcademicCVSkillTests(unittest.TestCase):
    def test_instruction_first_contract_is_declared(self) -> None:
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL / "references/current-cv-contract.md").read_text(encoding="utf-8")
        self.assertIn("Update `current-cv-contract.md` before changing any CV", skill)
        self.assertIn("Require a 4.0-scale GPA result", contract)
        self.assertIn("Contract version: `1.2`", contract)
        self.assertIn("--output files/Minseok_Cho_Academic_CV_Draft.docx", skill)

    def test_build_and_audit_draft(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source.json"
            output = tmp_path / "cv.docx"
            source.write_text(json.dumps(sample_source()), encoding="utf-8")
            subprocess.run(
                ["python", str(BUILD), "--input", str(source), "--output", str(output)],
                check=True,
            )
            subprocess.run(
                ["python", str(AUDIT), "--docx", str(output), "--source", str(source)],
                check=True,
            )
            doc = Document(output)
            self.assertEqual(
                doc.core_properties.identifier,
                "phd-candidate-academic-cv-contract:1.2",
            )
            self.assertNotIn("PRIVATE-STUDENT-ID", "\n".join(p.text for p in doc.paragraphs))

    def test_final_mode_requires_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            data = sample_source()
            data["mode"] = "final"
            data["education"][0]["gpa"] = "GPA: 3.80/4.00"
            source = tmp_path / "source.json"
            source.write_text(json.dumps(data), encoding="utf-8")
            result = subprocess.run(
                ["python", str(BUILD), "--input", str(source), "--output", str(tmp_path / "cv.docx")],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("final mode requires existing evidence", result.stderr)


if __name__ == "__main__":
    unittest.main()
