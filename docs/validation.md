# Secure Product Development validation

20 October 2026. Owner and final checker: Codex/root. Version 2.0.0 changes the skill's purpose to secure implementation throughout development. The [earlier review evaluations](legacy-review-validation.md) are historical, not evidence for this new behavior.

## Exact skill and package

Skill digest: `15c965116f5f3c6203a9397925fdb750f0bea3686e3d29a1bc166b10bc45ebcb`.

Recipe: SHA-256 of each relative filename, newline, then its UTF-8 content, in order: `skills/secure-product-development/SKILL.md`, followed by `references/web-controls.md`, `references/ai-controls.md`, `references/implementation-handoff.md`, `references/sources.md` under the same skill directory.

Archive: `dist/secure-product-development.skill`, SHA-256 `a01d26c3e32f7baf228ecd73376fd2ab8f7195b34c6d701473ce134adb7fd1a2`. Six entries: core workflow, four references and MIT license. The packaging code uses explicit Unix creator metadata, stable timestamp/permissions/order and stored entries; .gitattributes pins text line endings.

## Implementation exercise, not just a review response

Both native CLIs received the same skill context and [synthetic assignment](../examples/secure-coding-task/assignment.md). The verifier was withheld from generation. They were asked to implement health, invoice lookup, private-document search and refund-intent preparation with trusted session context and synthetic data. Runtime/tool execution was disabled during generation; neither claimed tests had run.

Codex/root inspected both returned modules before executing their tests. They contained no imports, external requests, file/process access or payment execution. The generated code was placed in separate local trial directories; only synthetic state was supplied. This was a bounded local test, not a claim of a hardened container sandbox.

| Provider | Actual model exposed | Start UTC | Generation elapsed | Executed checks |
|---|---|---|---|---|
| Codex CLI 0.159.0 | Model identity not exposed in JSONL | 13:27:39 | 32.8 s | 24 passed, 0 failed |
| Claude Code 2.1.278 | claude-opus-5 | 13:27:39 | 62.5 s | 24 passed, 0 failed |

Execution receipts: Codex code SHA-256 `6aa5c6a68167fc3e59ccfbed11fdee565ae080e8796cf1314f7142ec9fa71df9`, tested at 13:28:40 UTC; Claude code SHA-256 `43788a7f88e1b1d9f929056349143ffcc4f205efb35062a8463ac49ef4f979ae`, tested at 13:29:01 UTC. Each process exited 0 and all actual assertions passed. The published implementation is the inspected Codex result, unchanged.

The 24 checks cover public health, allowed invoice access/data minimization, missing identity, cross-tenant invoice selection, search scope and query bounds, allowed refund intent without mutation, missing permission, client-forged authority, five approval-binding mismatches and six invalid/excessive amounts. They are actual executable assertions, not a model's claim of completion. The future executor is explicitly outside this example; no money moves and no approval is consumed.

Codex usage: input 17,091 / output 1,319 tokens. Claude usage: input 2, cache-created input 7,570, cache-read input 2,477 and output 6,646 tokens, including 3,620 thinking tokens. Provider counters differ; do not treat these as a cost comparison. Native sessions were used with API-routing variables removed, no new API credentials or paid fallback configured. List-price cost estimates do not establish actual subscription billing.

## Independent review and disposition

Claude's review of the same skill digest: **ACCEPT**, no blocking flaws. It identified a non-blocking request for explicit 403/404 disclosure conventions. Maintainer disposition: keep status mapping appropriate to the framework/product; the example and assignment specify their own 401/403/404 contract. Do not make one fixture's mapping universal.

Codex's bounded critique also said ACCEPT and proposed keeping preparation distinct from execution. Proposed lessons: apply checks in the actual execution path, bind authority to actor/object/arguments, and keep preparation distinct from atomic execution. No durable memory promotion or model-weight training occurred.

The archive metadata correction previously received a `claude-opus-5` ACCEPT review at code/test digest `ec83d3832ffeb65b02eb170872be8d32d45b2d7530d5dfd6346a058144fb84f2`. The subsequent skill-name substitution and v2 package paths are covered by the current package tests and hosted checks; the earlier review is not represented as a review of those later edits.

## Package and visual checks

`python -m unittest discover -s tests -v`: **5 passed locally**. Tests cover archive reproducibility/integrity/license/paths, missing references, path escape, executable resources and simulated creator-platform variation. `python tools/package_skill.py`: passed with the hash above.

The upstream skill-creator validator could not start because PyYAML was unavailable. It remains **not run**, not passed. This repository's standard-library validator checks its own frontmatter identity/description, references and package boundaries; it is not a complete YAML/specification validator.

The new 1600 × 2000 flow PNG was rendered with Pillow 12.3.0 and visually inspected. It depicts planning, implementation and verification. Microsoft Fluent Emoji MIT and font OFL notices are included. The poster does not imply vendor endorsement or observed prevention of an exploit.

## Limits and current release evidence

This is one synthetic, framework-neutral exercise per provider, with stated trusted contracts. It does not establish general security outcomes, real identity-provider behavior, browser integration, payment execution, live deployment, compliance, penetration-test coverage or compatibility with every host. No unskilled baseline comparison was run. Automatic skill discovery and chat-app archive import were not tested. The project instruction snippet is an adoption aid; host selection is not guaranteed enforcement.

The original [Linux CI failure](https://github.com/KaizenxRyu/product-security-review/actions/runs/39429442805) is retained: four tests passed, but the 1.0 archive byte comparison failed because creator metadata varied by OS. No failure is relabeled successful. Current hosted package/example checks and protection evidence are tracked in the pull request and Actions tab. Read their actual result rather than inferring success from local checks.

Private raw generation/evaluation receipts and the original attachment are excluded from publication. No existing Kaizen memory, Workroom project, provider configuration or real application data was changed.
