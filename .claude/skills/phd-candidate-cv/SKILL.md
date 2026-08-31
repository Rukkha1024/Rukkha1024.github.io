---
name: phd-candidate-cv
description: "Read, edit, render, and snapshot Minseok Cho's private graduate-application CV on resume.lol. Use for every CV content, wording, section, ordering, layout, or export change. Owns the canonical resume id, the fact sources, the privacy boundary, the concurrent-edit guard, and the flex-CSS traps of the current template."
---

# Private CV on resume.lol

CV lives on resume.lol. No local generator. No DOCX pipeline. No contract version.

- Resume id `b55d572d-8f60-43cc-bafa-89ebe995dd7a`, name `Minseok`.
- Three documents: `markdown` content, `css` styling, `meta_css` `@page` rules.
- MCP server `resume-lol` reaches it. Installed for Claude Code and Codex.
- User edits the same resume in the web editor. Cloud state wins over any local copy.

## Edit in order

1. `get_resume` first. Read what is there now. Keep `updated_at`.
2. Change `markdown` only. Touch `css` or `meta_css` only when the user asks.
3. `update_resume` with `expected_updated_at`. On conflict re-pull, merge, retry. Never force.
4. `get_resume_html`. Save locally. Open in a browser. Look at the render.
5. Refresh the ignored snapshot under `local/cv/`.

Never pass `css` or `meta_css` as arguments unless changing them is the task.

## Keep facts true

- Sources: official academic records, `_pages/about.md`, `_pages/publications.md`, `_pages/grants.md`, the user's latest explicit correction.
- Never invent a degree, grade, date, role, publication, tool, or skill.
- Preserve conflicts and omissions. Ask the user instead of filling a gap.
- Keep the GPA labeled `(provisional conversion)` until an official 4.0-scale result exists.
- The CV may carry less than the public résumé. That is tailoring, not a conflict. A fact the CV adds is a new claim: confirm it, then propagate to `_pages/`.

## Respect the current CSS

Template CSS is the resume.lol default. Open Sans, blue `#1155cc` section headings and rules, blue bold links, 10 pt, letter, 0.5 in margins. Do not restyle it unasked.

`p` and `h3` are both `display: flex; justify-content: space-between`. That dictates the markdown:

- `### **Institution** Dates` pushes dates to the right edge. Two flex items, no tab stop needed.
- A paragraph holding one text node is safe.
- `**Label:** text` as a paragraph tears to both edges. Write it as a `- ` list item.
- A citation holds text plus a link. Write it as a `- ` list item.
- Keep lists tight. A blank line between items makes `<li><p>`, and the `p` flex rule then flings the citation and its DOI to opposite edges.
- Center a line with `<span class="spacer"></span>` on both sides. Do not use `.headerInfo`; its `position: absolute` collides with `h1`.

## Keep the user's `<br>`

`<br>` alone on a line is the user's spacing device. Verified safe: between list items it splits one list into two tight `<ul>` blocks and adds a gap; after an `h3` it opens space before the bullets. It does not create the `<li><p>` trap.

Keep every `<br>` the user placed. Never tidy them away, never merge the lists they separate.

## Stay private

- The CV is private. Never publish it through GitHub Pages.
- Keep records, exports, and snapshots under `local/` or an ignored `files/` path.
- Exclude date of birth, gender, student and certificate numbers, signatures, seals, QR codes, full street address, photo.
- Never create a share link without the user's explicit approval. Prefer a password and forced redaction when one is approved.

## Validate and checkpoint

Run the skill test, confirm the `.claude` mirror is byte-identical, and confirm `AGENTS.md` equals `CLAUDE.md`. Stage explicit tracked paths only. Commit and push in Korean.
