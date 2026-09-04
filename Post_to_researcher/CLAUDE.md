# Post_to_researcher

우편 발송용 인쇄 CV. 커버레터는 사용자 손글씨, 대상 PI는 사용자 선택.

# 경계

- 이 폴더 밖 파일 수정 금지.
- resume.lol `Minseok`(`b55d572d-8f60-43cc-bafa-89ebe995dd7a`)이 정본. 여기서 수정 금지.
- 새 사실 생성 금지. 추가 문장은 `Minseok` markdown, `../_pages/*.md`에 있는 것만.
- 산출물 전부 git 추적. 저장소 PUBLIC, 사용자 승인됨.

# 파일

- `print_cv.md`: 본문. resume.lol `Minseok-print`(`7edf2862-0f5c-4ee9-b55a-425e3cfeae40`)와 docx의 공통 원본.
- `print_cv_extra.css`: 헤더·QR·사진·하위 리스트·페이지 나눔 규칙. 편집하는 곳.
- `print_cv.css` = `../local/cv/resume.css` + `print_cv_extra.css` + `assets/print_assets.css`. 조립물.
- `print_cv.html`: `get_resume_html` export 그대로.
- `assets/build_assets.py` → QR 2개, `profile.jpg`, `print_assets.css`. `assets/fonts/`: Open Sans TTF.
- `build_pdf.py` → `Minseok_Cho_CV_print.pdf`. `build_docx.py` → `Minseok_Cho_CV_print.docx`.

# 계약

- Letter, 0.5in, 최대 3페이지. 헤더: 좌 사진 + 사이트 QR | 중 이름·연락처·`rukkha1024.github.io` | 우 끝 메일 QR(`mailto:cho9911@gmail.com`). QR 두 개는 양끝에 떨어뜨린다.
- `Minseok`에 더한 것: 연구 방향 4 bullet, 군복무 문구, 논문별 3줄 요약 하위 리스트, HOBBIES. GitHub URL 미표기.
- 사용자 `<br>` 전부 보존.

# 절차

python은 `/opt/anaconda3/bin/python3`.

1. `get_resume`로 `Minseok` 최신본 확인 → `print_cv.md` 반영.
2. `python3 assets/build_assets.py` → `cat ../local/cv/resume.css print_cv_extra.css assets/print_assets.css > print_cv.css`.
3. `update_resume`(`Minseok-print`, `expected_updated_at` 필수) → `get_resume_html` → `print_cv.html`.
4. `python3 build_pdf.py` → `pdffonts`로 OpenSans, `pdftoppm -r 60 -png`로 페이지 확인.
5. `python3 build_docx.py` → Word로 열어 확인. AppleScript 자동 export는 시간 초과로 실패.
6. 이 폴더 경로만 stage. 한국어 커밋·push.

# 함정

- resume.lol은 `<img>` 삭제. 사진·QR은 class div + CSS background. `p`·`h3`는 flex라 `**Label:** text` 단락 금지, 리스트로.
- css 인자에 큰 base64 금지(MCP 전송 중 깨짐). 사진은 공개 URL, QR만 data URI. PDF는 `build_pdf.py`가 로컬 사진·폰트를 심는다.
- export는 PagedJS + Google Fonts `@import`. headless Chrome에선 빈 PDF. `build_pdf.py`가 둘 다 제거하고 Chrome 기본 @page 사용. body 폰트는 `!important` 필요. `--user-data-dir` 주면 멈춤.
- Word 판 폰트: `assets/fonts/*.ttf`를 `~/Library/Fonts/`에 복사(2026-09-04 완료).

# 결정

- 2026-09-04: resume.lol 판·docx 판 둘 다 만들고 사용자가 고른다. 3페이지 허용.
- 2026-09-05: QR 양끝 배치. 봉투는 손편지(200단어 이내) + CV. 상세는 `README.md`.
- 2026-09-04: 제목은 이름. 부제(`Curriculum Vitae · 날짜`) 여부 미결정.
- resume.lol 판 PDF 2페이지 확인 완료. Word 판은 구조 검사만, 시각 확인은 사용자 몫.
