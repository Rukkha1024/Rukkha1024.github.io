# 조민석 Academic Résumé

공개 사이트: <https://rukkha1024.github.io/>

Academic Pages로 만든 박사과정 유학 지원용 résumé입니다. 평소에는 HTML을
수정하지 않고 Markdown과 YAML만 편집합니다.

## 자주 수정하는 파일

- 소개, 학력, 연구 활동, 기타 활동: `_pages/about.md`
- 전체 논문 목록과 영어 3줄 요약: `_pages/publications.md`
- 이름, 소개, GitHub, 이메일: `_config.yml` 상단의 `title`, `description`,
  `author` 항목
- 상단 메뉴: `_data/navigation.yml`
- 프로필 사진: `images/profile.png`

`_includes/`, `_layouts/`, `_sass/`, `assets/`는 화면을 만드는 테마 파일입니다.
디자인을 바꾸는 작업이 아니면 수정하지 않습니다.

## GitHub에서 수정하기

1. 수정할 파일을 엽니다.
2. 오른쪽 위 연필 아이콘을 누릅니다.
3. Markdown 내용을 수정합니다.
4. `Commit changes`를 누릅니다.
5. 잠시 후 공개 사이트에서 결과를 확인합니다.

프로필 사진은 `images/profile.png`를 같은 이름의 실제 사진으로 교체하면
됩니다. 이메일이나 Scholar·ORCID 주소가 준비되면 `_config.yml`의 해당 값을
입력합니다.

## 논문 추가·수정하기

1. `_pages/publications.md`를 엽니다.
2. 기존 논문 블록 하나를 복제합니다.
3. DOI에 직접 연결된 제목, 학술지명, 연도, 권장 인용을 수정합니다.
4. 제목 바로 아래의 영어 3줄 요약을 수정하고 커밋합니다.

논문 목록에는 영어 3줄 요약이 바로 표시되고, 논문 제목은 DOI 주소로
연결됩니다. 논문별 파일이나 HTML은 수정하지 않습니다.

## 사용하지 않는 기능

- 댓글과 공유 버튼
- 블로그와 RSS 피드
- 강의, 발표, 포트폴리오 샘플
- Docker와 로컬 Ruby 빌드

기반 템플릿: [Academic Pages v0.9](https://github.com/academicpages/academicpages.github.io/releases/tag/v0.9)
