# Current master CV contract

Contract version: `1.1`

Update this current specification before every CV content, evidence, layout,
DOCX, or PDF change. Increment the version without adding a historical log.

## Artifact state

- Purpose: universal graduate-school application master Academic CV.
- Privacy: private and ignored; never publish through GitHub Pages.
- Draft basename: `Minseok_Cho_Academic_CV_Draft`.
- Final basename: `Minseok_Cho_Academic_CV_Master`.
- Output directory: `local/cv/`.
- Page budget: exactly two US Letter pages.
- Sequence: instruction -> source JSON -> DOCX -> rendered PNG QA -> PDF ->
  rendered PNG QA.

## Content order

1. Identity and electronic contact information
2. Research Profile
3. Education
4. Peer-Reviewed Journal Articles
5. Research Experience
6. Technical Skills
7. Teaching & Community Engagement
8. Selected Research Software

Omit empty awards, presentations, grants, and references sections. Omit hobbies,
photo, date of birth, gender, student identifiers, certificate identifiers, QR
codes, and full street address.

## Education and GPA policy

- Use verified official program, institution, major, date, and grade wording.
- Do not invent `B.A.`, `B.S.`, or another bachelor's degree title before an
  English degree or graduation certificate supports it.
- Display undergraduate and graduate motor-control-related training as one
  compact category line. Do not list semesters, every course, or course grades.
- Require a 4.0-scale GPA result for a submission-ready CV.
- In draft mode only, accept a private-source value labeled
  `(provisional conversion)`. Do not present it as an official evaluation.
- Until a numeric graduate 4.0 result exists, state only the verified graduate
  credit total and overall letter grade.

## Layout tokens

Use named override `academic_cv_master` derived from `compact_reference_guide`:

- Page: US Letter portrait; 1.0-inch margins; 0.492-inch header/footer distance.
- Font: Arial; body 10.5 pt; black; single spacing; 0 pt before and 1.5 pt after.
- Name: 17 pt bold; contact line: 9 pt; centered; no title rule.
- Section heading: 10.5 pt bold, uppercase, black; 9 pt before, 2 pt after;
  keep with next paragraph.
- Entry title: 10.5 pt; institution/role bold; dates right-aligned with a real
  right tab stop.
- Detail: 10 pt; bullets 9.6 pt with real Word bullet style, 0.18-inch marker,
  0.36-inch text indent, 1.5 pt after.
- No tables, columns, sidebars, shaded blocks, icons, or color accents.
- Use one deliberate page break before `Research Experience`. Keep profile,
  education, and publications on page one; keep research experience, skills,
  engagement, and software on page two.

## Render acceptance

- Exactly two pages in DOCX-derived PDF.
- No clipped, overlapping, orphaned, or unexpectedly wrapped content.
- Consistent Arial rendering and section rhythm across both pages.
- DOCX and PDF carry the same visible text and section order.
