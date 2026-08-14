# Project

- 목적: 박사과정 유학 지원용 GitHub Pages résumé 제작.
- 대상: 해외 대학 교수, PI, 입학 심사자.
- 기반 템플릿: Academic Pages.
- 공개 콘텐츠 원본: `_pages/about.md`, `_pages/publications.md`.
- 이 파일: 공통 규칙과 문서 경로만 기록하는 routing index.
- 목표: 150줄 이하.

# Rules

- 경력, 학력, 논문, 연구 내용 임의 생성 금지.
- 불확실한 정보는 사용자에게 확인.
- 공개 résumé는 영어로 작성. README 등 편집 안내 문서는 한국어 유지.
- 일반 콘텐츠는 Markdown으로 관리. HTML 직접 편집 금지.
- GitHub 웹 편집과 GitHub Pages 배포 기준.
- 로컬 Docker·Ruby 환경 만들지 않음.
- 댓글, 더보기, 피드, 공유, 제작 문구 사용 금지.
- 공개 이력: 소개 파일에 학력·연구 활동·기타 활동 통합.
- 논문: 논문 파일 1개에 직접 작성. 영어 3줄 요약 즉시 표시. 제목은 DOI 직접 연결. 별도 중복 링크 금지.
- 문서와 구현이 다르면 문서 먼저 수정.
- 수정 전 계획과 미리보기 제시.
- 사용자 승인 후 파일 수정.
- 변경 후 관련 문서와 페이지 확인.
- 기존 스타일 유지. 최소 범위만 수정.
- Academic CV 작업: `.agents/skills/phd-candidate-academic-cv/` 먼저 읽고 수정.
- CV 수정: skill의 current contract 먼저 수정. CV 단독 수정 금지.
- CV 입력·증명서: `local/` 또는 ignore 경로만 사용. CV 산출물: ignore된 `files/`. 공개 금지.
- instruction 파일은 caveman 문체 사용.
- 작업 완료 후 변경 파일만 한국어 메시지로 커밋·push.

# Repository map

- `README.md`: 초보자용 편집 안내.
- `_config.yml`: 이름, 프로필, 외부 링크.
- `_pages/about.md`: 소개, 학력, 연구 관심, 연구 활동, 기타 활동.
- `_pages/publications.md`: 전체 논문 목록과 영어 3줄 요약.
- `_data/navigation.yml`: 상단 메뉴.
- `.agents/skills/phd-candidate-academic-cv/`: 비공개 대학원 지원 CV instruction·생성·검증.
- `local/cv/`: 비공개 CV 입력. Git 제외.
- `files/Minseok_Cho_Academic_CV_*`: 비공개 CV DOCX·PDF. Git 제외.
- `_includes/`, `_layouts/`, `_sass/`, `assets/`: 테마 코어. 디자인 변경 외 수정 금지.

# user info 
user는 github io를 다룰 줄 모른다. 따라서 user가 명시하지 않는 한, 수정사항은 github io의 완성본을 수정해달라고 이해하면 된다. 
always commit and push without user confirmation.
