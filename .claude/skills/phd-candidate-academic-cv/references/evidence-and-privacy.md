# Evidence and privacy contract

## Source priority

1. Use official academic records for institution, program, major, enrollment,
   credits, grades, and degree wording.
2. Use `_pages/about.md` and `_pages/publications.md` for public research,
   skills, activities, links, and publication descriptions.
3. When the sibling application repository is available, use
   `../문의/공통/지원자_사실.md` only for user-confirmed private facts and cycle
   decisions. Do not copy that file wholesale.
4. Use the user's latest explicit correction when it resolves a source conflict.

Record source paths in the ignored JSON manifest. Do not embed source PDFs,
local filesystem paths, or evidence identifiers in the visible CV.

## Academic-record boundary

- Inspect every relevant page visually when OCR or text extraction is empty or
  uncertain.
- Treat the current Hanyang enrollment certificate as evidence of the two
  majors, not as evidence of a completed degree title.
- Treat `4.07/4.50` and `95.7/100` as different source fields. Never relabel the
  latter as a GPA.
- Draft mode may consume a provisional 4.0 value supplied by the private JSON.
  Final mode requires a user-provided 4.0-scale result PDF.
- Do not numerically convert the graduate `overall grade A+` unless the later
  4.0-scale result explicitly supplies a graduate GPA.

## Privacy boundary

Keep all raw academic records and generated CVs ignored. Never copy or expose:

- date of birth or gender;
- student, certificate, file, or issue numbers;
- signatures, seals, verification codes, or QR codes;
- local absolute paths or machine usernames;
- document creator and last-modified-by metadata.

Supply sensitive literals only through the ignored JSON's
`privacy.prohibited_literals` array so the auditor can check the output without
hardcoding them in the public skill.

## Draft and final gates

- `draft`: allow a clearly provisional 4.0 GPA and a neutral undergraduate
  education description without a degree type.
- `final`: require existing evidence paths for `four_point_gpa_result_pdf` and
  `bachelor_degree_certificate_pdf`; reject provisional wording.
- Never send or upload a `draft` artifact as an application attachment.
