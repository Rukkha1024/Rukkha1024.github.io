# Project

- 목적: 박사과정 유학 지원용 GitHub Pages résumé 제작.
- 대상: 해외 대학 교수, PI, 입학 심사자.
- 기반 템플릿: Academic Pages.
- 공개 콘텐츠: `_pages/about.md`, `_pages/cv.md`, `_publications/*.md`.
- 이 파일: 공통 규칙과 문서 경로만 기록하는 routing index.
- 목표: 150줄 이하.

# Rules

- 경력, 학력, 논문, 연구 내용 임의 생성 금지.
- 불확실한 정보는 사용자에게 확인.
- 문서와 구현이 다르면 문서 먼저 수정.
- 수정 전 계획과 미리보기 제시.
- 사용자 승인 후 파일 수정.
- 변경 후 관련 문서와 페이지 확인.
- 기존 스타일 유지. 최소 범위만 수정.
- instruction 파일은 caveman 문체 사용.
- 커밋 요청 시 한국어 커밋 메시지 사용.

# Repository map

- `README.md`: 초보자용 편집 안내.
- `_config.yml`: 이름, 프로필, 외부 링크.
- `_pages/about.md`: 홈페이지 소개와 주요 연구.
- `_pages/cv.md`: 학력과 전체 연구 활동.
- `_publications/`: 논문별 Markdown.
- `_data/navigation.yml`: 상단 메뉴.
- `_includes/`, `_layouts/`, `_sass/`, `assets/`: 테마 코어. 디자인 변경 외 수정 금지.
