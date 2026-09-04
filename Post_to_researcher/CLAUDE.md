# Post_to_researcher

우편용 인쇄 CV. 이 폴더 전용 instruction. 진행하며 계속 고친다.

# 목적

- PI에게 종이 우편 발송. 커버레터는 사용자 손글씨. 대상 PI는 사용자 선택.
- 이 폴더는 CV만 만든다. 편지·주소·발송 기록은 여기서 다루지 않는다.
- 산출물은 git 추적. 저장소 PUBLIC. 사용자 승인됨 (2026-09-04).

# 경계

- 이 폴더 밖 파일 수정 금지. SKILL.md, AGENTS.md, CLAUDE.md(루트), `_config.yml`, `.gitignore`, `_pages/`, `local/` 전부 건드리지 않는다.
- resume.lol `Minseok`(`b55d572d-8f60-43cc-bafa-89ebe995dd7a`)은 정본. 여기서 수정 금지.
- 인쇄판은 파생 변형. 새 사실 생성 금지. 추가 문장은 아래 원천에 이미 있는 문장에서만 가져온다.

# 원천

- resume.lol `Minseok` markdown (`get_resume`로 매번 최신본 재조회).
- `../_pages/about.md`: 연구 방향 4 bullet, 군복무 문구, Hobbies.
- `../_pages/publications.md`: 논문별 3줄 요약.
- `../_pages/grants.md`: 연구비.
- `../images/profile.png`: 헤더 사진 (실제 JPEG, 378×496).

# 산출물 (이 폴더 소유)

- `CLAUDE.md`: 이 파일.
- `assets/build_assets.py`: QR 생성 + 사진·QR base64 → `assets/print_assets.css`.
- `assets/qr_site.png`, `assets/qr_mail.png`, `assets/profile.jpg`, `assets/print_assets.css`.
- `print_cv.md`: 인쇄판 본문. resume.lol `Minseok-print`와 docx의 공통 원본.
- `print_cv.css`: `Minseok-print`용 CSS (`Minseok` CSS + 헤더 규칙 + `print_assets.css`).
- `print_cv.html`: `get_resume_html` export. 수정 금지, 재생성만.
- `build_docx.py` → `Minseok_Cho_CV_print.docx`.
- `Minseok_Cho_CV_print.pdf` (resume.lol 판), `Minseok_Cho_CV_print_docx.pdf` (Word 판).
- resume.lol `Minseok-print` id: (생성 후 기입)

# 내용 계약

- 헤더 3열: 좌 QR 2개 (사이트 `https://rukkha1024.github.io`, 메일 `mailto:cho9911@gmail.com`) | 중 이름·연락처·`rukkha1024.github.io` 텍스트 | 우 사진.
- RESEARCH PROFILE 뒤에 `Directions I want to take further` 4 bullet.
- EDUCATION 한양대 줄에 `(including two years of mandatory military service)`.
- JOURNAL ARTICLES 각 인용 아래 3줄 요약 하위 리스트.
- 끝에 `## HOBBIES` 3개.
- GitHub 프로젝트 URL 표기 안 함. 문구만.
- 나머지 섹션은 `Minseok`과 동일. 사용자 `<br>` 전부 보존.

# 레이아웃 계약

- Letter, 여백 0.5in. 최대 3페이지. 마지막 페이지 절반 이상 비지 않게.
- 사진·QR은 CSS `background-image` data URI + class div만. `<img>`는 resume.lol이 지운다.
- resume.lol CSS 함정: `p`·`h3`는 flex. `**Label:** text` 단락은 좌우로 찢어짐 → 리스트 항목으로. 리스트 안 빈 줄 금지 (`<li><p>` 함정).
- docx: Letter 0.5in, 헤더는 테두리 없는 3열 표, 섹션 제목 `#1155CC` + 하단선. resume.lol 판과 같은 톤.

# 절차

1. `get_resume`로 `Minseok` 최신본 받는다. `print_cv.md` 갱신.
2. `python3 assets/build_assets.py` (segno 필요. `/opt/anaconda3/bin/python3 -m pip install segno`).
3. `Minseok-print` 갱신 (`update_resume`, `expected_updated_at` 필수). `get_resume_html` → `print_cv.html`. 브라우저 인쇄 → PDF.
4. `python3 build_docx.py` → docx. Word로 열어 확인 → PDF.
5. 검증 후 이 폴더 경로만 stage. 한국어 메시지로 커밋·push.

# 검증

- `git status --short`에 `Post_to_researcher/` 밖 경로 없음.
- HTML·docx 둘 다: 사진·QR 2개 보임, 휴대폰 스캔 동작, ≤3페이지, 인용문과 DOI가 좌우로 안 찢어짐.
- `print_cv.md` 모든 문장이 원천에 있음. 새 주장 0건.

# 결정 기록

- 2026-09-04: resume.lol 2번째 resume과 docx 둘 다 만든다. 비교 후 사용자가 고른다.
- 2026-09-04: 3페이지까지 허용. GitHub URL 미표기. QR 좌측·사진 우측.
