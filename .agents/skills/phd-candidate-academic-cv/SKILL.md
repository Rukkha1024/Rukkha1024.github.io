---
name: phd-candidate-academic-cv
description: "Create, revise, render, and audit Minseok Cho's private master academic CV for graduate-school applications. Use for every change to the CV's content, evidence, layout, DOCX, or PDF. Require instruction-first updates, verified source facts, a 4.0-scale GPA result for submission-ready output, privacy-safe local artifacts, DOCX-before-PDF sequencing, and render-based visual QA."
---

# Private academic CV

Treat the CV as a generated private artifact. Keep its current specification in
this skill and its applicant values in an ignored task-local JSON file.

## Apply the instruction-first gate

1. Read [current-cv-contract.md](references/current-cv-contract.md),
   [evidence-and-privacy.md](references/evidence-and-privacy.md), and
   [academic-cv-guidelines.md](references/academic-cv-guidelines.md).
2. Update `current-cv-contract.md` before changing any CV content, evidence,
   layout, DOCX, or PDF. Increment its contract version. Change `SKILL.md` too
   when the workflow changes.
3. Refuse a CV-only edit. The source JSON's `contract_version` and the DOCX
   identifier must match the current instruction version.
4. Keep personal values out of tracked skill files. Store them only in an
   ignored JSON file under `local/cv/`.

## Build in order

1. Re-read repository instructions, HEAD, status, and target diffs.
2. Verify every claim against the evidence hierarchy. Preserve conflicts or
   omissions; never infer an unsupported degree, grade, date, role, or skill.
3. Use `draft` mode while the official 4.0-scale GPA result PDF is absent.
   Label the supplied GPA as provisional. Use `final` mode only when the JSON
   points to both the 4.0-scale result PDF and the bachelor's degree evidence.
4. Build the DOCX first:

   ```bash
   uv run --with python-docx \
     .agents/skills/phd-candidate-academic-cv/scripts/build_academic_cv.py \
     --input local/cv/academic_cv_source.json \
     --output local/cv/Minseok_Cho_Academic_CV_Draft.docx
   ```

5. Audit the DOCX before conversion:

   ```bash
   uv run --with python-docx --with pypdf \
     .agents/skills/phd-candidate-academic-cv/scripts/audit_academic_cv.py \
     --docx local/cv/Minseok_Cho_Academic_CV_Draft.docx \
     --source local/cv/academic_cv_source.json
   ```

6. Render every DOCX page to PNG with the installed `documents` skill. Inspect
   every page at 100%; fix and rebuild until no clipping, overlap, broken
   glyphs, or awkward page break remains.
7. Export the approved DOCX to PDF. Never author an independent PDF. Render and
   inspect every PDF page, then audit both files together with `--pdf`.
8. Deliver only the private DOCX and PDF. Do not commit them or their evidence.

## Protect the boundary

- Keep outputs under `local/cv/`; keep transcripts, enrollment certificates,
  degree certificates, and GPA evaluations ignored.
- Exclude date of birth, gender, student IDs, certificate numbers, QR codes,
  full street addresses, photos, and source-document metadata.
- Remove creator and last-modified-by metadata while retaining the nonpersonal
  contract identifier used by the auditor.
- Remove a previously tracked public CV before treating the private master as
  the current artifact. Do not rewrite Git history without explicit approval.

## Validate and checkpoint

Run `quick_validate.py`, the skill unit tests, `git diff --check`, DOCX/PDF
audits, and full render review. Stage explicit tracked paths only. Commit and
push the instruction checkpoint before generating the CV; commit and push any
later tracked privacy or workflow change separately.
