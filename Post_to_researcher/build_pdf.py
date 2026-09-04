"""print_cv.html (resume.lol export) → Minseok_Cho_CV_print.pdf via headless Chrome. 실행: python3 build_pdf.py

왜 손질하나:
- export는 PagedJS + window.print() 자동 호출 구조. headless print-to-pdf에서는 빈 PDF가 나온다.
  → PagedJS 스크립트를 떼고 Chrome 기본 @page 페이지네이션을 쓴다.
- Google Fonts @import는 headless에서 렌더를 멈춘다. → Open Sans TTF를 data URI @font-face로 심는다.
  export의 body 규칙만으로는 폰트가 적용되지 않아 body에 !important 규칙을 하나 더 얹는다.
- 사진은 공개 URL 대신 assets/profile.jpg를 심어 네트워크 없이도 같은 PDF가 나온다.
"""

from __future__ import annotations

import base64
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SRC = HERE / "print_cv.html"
OUT = HERE / "Minseok_Cho_CV_print.pdf"
PHOTO = HERE / "assets" / "profile.jpg"
FONTS = HERE / "assets" / "fonts"
GOOGLE_IMPORT = re.compile(r"@import url\('https://fonts\.googleapis\.com[^;]*;")
PAGEDJS_CONFIG = re.compile(r"<script>\s*window\.PagedConfig.*?</script>", re.S)
PAGEDJS_POLYFILL = re.compile(r"<script>/\*\*\s*\* @license Paged\.js.*?</script>", re.S)
PHOTO_URL = "url(https://rukkha1024.github.io/images/profile.png)"


def font_style_block() -> str:
    rules = []
    for file, style in (("OpenSans-Variable.ttf", "normal"), ("OpenSans-Italic-Variable.ttf", "italic")):
        data = base64.b64encode((FONTS / file).read_bytes()).decode()
        rules.append(
            f"@font-face {{ font-family: 'Open Sans'; font-style: {style}; font-weight: 300 800; "
            f"src: url(data:font/ttf;base64,{data}) format('truetype'); }}"
        )
    rules.append("body { font-family: 'Open Sans', sans-serif !important; }")
    return "<style>" + "\n".join(rules) + "</style>"


def build_html() -> str:
    html = SRC.read_text(encoding="utf-8")
    for pattern, label in ((PAGEDJS_CONFIG, "PagedConfig"), (PAGEDJS_POLYFILL, "Paged.js"), (GOOGLE_IMPORT, "Google Fonts import")):
        html, n = pattern.subn("", html)
        assert n == 1, f"{label}: expected 1 match, got {n}"
    assert html.count(PHOTO_URL) == 1, "photo url not found"
    photo_uri = "data:image/jpeg;base64," + base64.b64encode(PHOTO.read_bytes()).decode()
    html = html.replace(PHOTO_URL, f"url({photo_uri})")
    return html.replace("</head>", font_style_block() + "</head>", 1)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "cv.html"
        page.write_text(build_html(), encoding="utf-8")
        cmd = [
            CHROME, "--headless=new", "--disable-gpu", "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=10000", "--no-pdf-header-footer",
            f"--print-to-pdf={OUT}", page.as_uri(),
        ]
        subprocess.run(cmd, check=True, timeout=120, capture_output=True)
    print("wrote", OUT, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
