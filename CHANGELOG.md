# Changelog

## 2.0.0 — 2026-10-20

- Changed from a post-build review skill to Secure Product Development, applied during planning, implementation, verification and handoff.
- Added proportional secure-coding instructions and a project-instruction adoption snippet; security review is a supporting technique, not the default output.
- Added a real synthetic implementation task: code generated with both native CLIs passed 24 checks per implementation.
- Updated the illustrated flow, package name and installation guide. Prior review evaluations remain historical.
- Includes the reproducible ZIP correction below; skill installation grants no tools or permissions.

## 1.0.1 candidate — superseded by 2.0.0

- Fixed cross-platform archive reproducibility after hosted Linux CI detected implicit Windows/Linux ZIP creator metadata differences.
- Made creator metadata explicit and used stored entries to remove compression-version variation; added a simulated creator-platform regression test.
- Skill instructions and their evaluated behavior are unchanged. Supersedes the 1.0.0 distribution archive.

## 1.0.0 — 2026-10-20

- Enhanced Rahul Chamoli's original checklist into a portable, evidence-led review skill with optional AI-agent controls and a report template.
- Made severity and control applicability context-sensitive; removed the mandatory Claude-specific command and universal RLS/CAPTCHA assumptions.
- Added authorization and untrusted-input boundaries, unknown/test distinctions and a rule against inventing exploit chains.
- Added a synthetic fixture, real Claude Code/Codex context evaluations, retained failure dispositions and deterministic package checks.
- Added the illustrated flow poster, licensed Microsoft Fluent artwork, installation guidance and a LinkedIn draft.
