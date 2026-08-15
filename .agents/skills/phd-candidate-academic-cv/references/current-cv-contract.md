# Current master CV contract

Contract version: `1.6`

Update this current specification before every CV content, evidence, layout,
DOCX, or PDF change. Increment the version without adding a historical log.

## Artifact state

- Purpose: universal graduate-school application master Academic CV.
- Privacy: private and ignored; never publish through GitHub Pages.
- Draft basename: `Minseok_Cho_Academic_CV_Draft`.
- Final basename: `Minseok_Cho_Academic_CV_Master`.
- Output directory: `files/`; DOCX and PDF stay Git-ignored.
- Page budget: two to three US Letter pages.
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

Use named override `academic_cv_master`, a plain black serif academic layout:

- Page: US Letter portrait; 1.0-inch margins; 0.492-inch header/footer distance.
- Color: black text only. No accent color anywhere.
- Font: Times New Roman for every run; body 11 pt; 1.5-line spacing throughout;
  0 pt before and 0 pt after body paragraphs.
- Name: 16 pt bold, black, centered; contact line: 11 pt, black, centered; no
  rule under the identity block.
- Section heading: 12 pt bold, uppercase, black, no letter spacing; a 0.75 pt
  black bottom rule spanning the text column; 10 pt before, 2 pt after; keep
  with next paragraph.
- Entry title: 11 pt; institution/role bold black; dates right-aligned with a
  real right tab stop, black.
- Detail: 11 pt; bullets 11 pt with real Word bullet style, 0.18-inch marker,
  0.36-inch text indent.
- Citations: 11 pt, APA style as authored in the source JSON, applicant name
  bold, followed by the full `https://doi.org/...` URL as visible hyperlink
  text (never a bare `DOI` word).
- No tables, columns, sidebars, shaded blocks, icons, or decorative color.
- No forced section page break: content flows naturally across the pages,
  relying on keep-with-next to avoid orphaned headings.
- Short labeled blocks (Technical Skills, Selected Research Software): chain
  keep-with-next through every line except the block's last so the block never
  splits across a page boundary.

## Render acceptance

- Two or three pages in DOCX-derived PDF.
- No clipped, overlapping, orphaned, or unexpectedly wrapped content.
- Consistent Times New Roman rendering and section rhythm across all pages.
- DOCX and PDF carry the same visible text and section order.
