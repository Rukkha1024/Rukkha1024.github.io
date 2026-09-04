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
- `assets/build_assets.py`: QR 생성, 사진 축소(`profile.jpg`), `assets/print_assets.css` 출력.
- `assets/qr_site.png`, `assets/qr_mail.png`, `assets/profile.jpg`, `assets/print_assets.css`.
- `assets/fonts/`: Open Sans variable TTF 2개 (OFL). `build_pdf.py` 전용.
- `print_cv.md`: 인쇄판 본문. resume.lol `Minseok-print`와 docx의 공통 원본.
- `print_cv_extra.css`: 헤더·QR·사진·하위 리스트·페이지 나눔 규칙. 손으로 편집하는 곳.
- `print_cv.css`: `Minseok-print`에 올리는 완성 CSS = `../local/cv/resume.css` + `print_cv_extra.css` + `assets/print_assets.css`. 조립물, 직접 편집 금지.
- `print_cv.html`: `get_resume_html` export 그대로. 수정 금지, 재생성만.
- `build_pdf.py` → `Minseok_Cho_CV_print.pdf` (resume.lol 판, headless Chrome).
- `build_docx.py` → `Minseok_Cho_CV_print.docx` (Word 판).
- resume.lol `Minseok-print` id: `7edf2862-0f5c-4ee9-b55a-425e3cfeae40` (2026-09-04 생성).

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

python은 `/opt/anaconda3/bin/python3` (segno, python-docx, Pillow, pypdf 설치됨).

1. `get_resume`로 `Minseok` 최신본 받는다. 바뀐 문장을 `print_cv.md`에 반영.
2. `python3 assets/build_assets.py` → QR·사진·`print_assets.css`.
3. `cat ../local/cv/resume.css print_cv_extra.css assets/print_assets.css > print_cv.css`.
4. `Minseok-print`에 `update_resume` (markdown=`print_cv.md`, css=`print_cv.css`, `expected_updated_at` 필수).
5. `get_resume_html` → 결과를 `print_cv.html`로 저장 (도구 결과가 파일로 떨어지면 그 파일을 복사).
6. `python3 build_pdf.py` → PDF. `pdffonts`로 OpenSans 확인, `pdftoppm -r 60 -png`로 페이지 눈으로 확인.
7. `python3 build_docx.py` → docx. Word로 열어 확인 (AppleScript 자동 export는 AppleEvent 시간 초과로 실패함. 손으로 연다).
8. 검증 후 이 폴더 경로만 stage. 한국어 메시지로 커밋·push.

# 함정 (검증됨, 2026-09-04)

- resume.lol css 인자에 큰 base64를 넣지 마라. MCP 호출 본문을 모델이 직접 옮겨 적어야 해서 20KB 사진은 깨진다. 사진은 공개 URL(`https://rukkha1024.github.io/images/profile.png`), QR(약 500B)만 data URI.
  → `Minseok-print` 웹 미리보기는 네트워크가 있어야 사진이 뜬다. PDF는 `build_pdf.py`가 로컬 사진을 심으므로 무관.
- export HTML은 PagedJS + `window.print()` 자동 호출. headless `--print-to-pdf`는 빈 866B PDF를 낸다. `build_pdf.py`가 PagedJS 스크립트를 떼고 Chrome 기본 @page 페이지네이션을 쓴다.
- Google Fonts `@import`가 있으면 headless 렌더가 끝나지 않는다. `build_pdf.py`가 이를 지우고 TTF data URI `@font-face` + `body{font-family:'Open Sans' !important}`를 넣는다. `!important` 없이는 export의 body 규칙이 폰트를 못 잡는다.
- `--user-data-dir`로 새 프로필을 주면 headless Chrome이 멈춘다. 기본 프로필로 실행.
- resume.lol은 `<img>`를 지운다. class div + CSS background만.
- `p`, `h3`는 flex. `**Label:** text` 단락은 좌우로 찢어진다 → 리스트 항목으로. 4칸 들여쓴 `- `는 하위 리스트로 렌더됨(확인).
- Word 판 폰트: Open Sans가 시스템에 없으면 대체된다. `assets/fonts/*.ttf`를 `~/Library/Fonts/`에 복사하면 된다 (2026-09-04 복사해 둠).

# 검증

- `git status --short`에 `Post_to_researcher/` 밖 경로 없음.
- HTML·docx 둘 다: 사진·QR 2개 보임, 휴대폰 스캔 동작, ≤3페이지, 인용문과 DOI가 좌우로 안 찢어짐.
- `print_cv.md` 모든 문장이 원천에 있음. 새 주장 0건.

# 결정 기록

- 2026-09-04: resume.lol 2번째 resume과 docx 둘 다 만든다. 비교 후 사용자가 고른다.
- 2026-09-04: 3페이지까지 허용. GitHub URL 미표기. QR 좌측·사진 우측.
- 2026-09-04: resume.lol 판 PDF 2페이지 확인(사진·QR·Open Sans·논문 요약 하위 불릿·페이지 경계에서 인용 분리 없음). Word 판은 구조 검사만 통과, 시각 확인은 사용자 몫.
