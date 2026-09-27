---
name: article-to-koubo
description: Convert Markdown articles or content drafts into teleprompter-ready Chinese 口播稿 files. Use when the user asks to turn an original article, Markdown script, draft, or content file into pure-text 口播稿 / 提词器稿 / 每行不超过15字稿件. The skill must never edit or overwrite the source file; it always creates a new sibling file named 原文件名-口播稿.md.
---

# Article To Koubo

Convert a source article into a pure-text Chinese voiceover script for teleprompters.

## Hard Rules

- Treat the source file as read-only. Do not modify, normalize, reformat, rename, or overwrite it.
- Always create a new sibling file named `<source base name>-口播稿.md`.
- If the target file already exists, inspect it first. Overwrite it only when the user clearly asked to regenerate that same 口播稿; otherwise ask or create a versioned sibling.
- Preserve the original meaning. Do not add new facts, new examples, new claims, or new calls to action.
- Keep wording as close to the source as possible while converting Markdown structure into spoken plain text.
- Remove the article title and Markdown-only structure.
- Every non-empty output line must be 15 characters or fewer by PowerShell `.Length`.
- Output plain text only. No Markdown headings, bullets, blockquotes, images, code fences, tables, bold markers, or section-label brackets.

## Conversion Workflow

1. Read the source file with `Get-Content -Raw`.
2. Determine the target path by appending `-口播稿.md` before the extension in the same directory.
3. Remove non-spoken elements:
   - top-level article title
   - Markdown headings and decorative section labels
   - horizontal rules
   - image references such as `![[...]]` or `![](...)`
   - code fences and install commands unless the user explicitly asks to keep commands for口播
   - Markdown emphasis markers such as `**`
4. Convert useful section headings into natural spoken transitions only when needed for continuity. Example: `解决方案揭晓` can become `而我的做法是，`.
5. Split long sentences into teleprompter-friendly lines. Prefer semantic breaks over arbitrary character slicing.
6. Keep blank lines only where they help oral pacing.
7. Write only the target file.
8. Run `scripts/validate_koubo.ps1` against the target file.
9. If validation fails, fix only the target file and validate again.
10. Report the target path and validation result.

## Style Rules

- Use short, spoken Chinese lines.
- Keep punctuation where it helps pacing.
- Prefer one idea per line.
- Preserve product/tool names exactly when possible, such as `Codex`, `Agent`, `飞书`, `B 站`, `Obsidian`.
- Do not polish into a different voice. This is a format conversion, not a rewrite.
- Do not perform title optimization, hook optimization, summary writing, or content expansion under this skill.

## Validation

Run:

```powershell
.\.agents\skills\article-to-koubo\scripts\validate_koubo.ps1 -Path "<target-file>"
```

The validator checks:

- file exists and is not empty
- no non-empty line exceeds 15 characters
- no common Markdown residues remain

The validator does not inspect or modify the source file.
