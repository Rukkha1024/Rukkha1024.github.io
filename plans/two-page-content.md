# 2개 Markdown 콘텐츠 구조

## 목표

- 공개 이력서 콘텐츠 원본 2개 유지.
- 소개·이력: `_pages/about.md`.
- 논문: `_pages/publications.md`.
- `_publications/` 컬렉션과 별도 CV 페이지 제거.

## 변경

1. `AGENTS.md`, `README.md` 관리 경로 갱신.
2. CV의 비논문 내용을 `_pages/about.md`에 통합.
3. 논문 2편을 `_pages/publications.md`에 직접 작성.
4. 기존 CV·논문 URL을 새 페이지로 연결.
5. 논문 컬렉션 설정과 기존 중복 파일 제거.

## 검증

- Markdown·YAML 구문 확인.
- 내부 파일 참조 확인.
- 기존 공개 URL 리디렉션 확인.
- `_publications/` 의존성 제거 확인.
