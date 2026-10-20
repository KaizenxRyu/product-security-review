# Validation record

Prepared 20 October 2026. Owner and final artifact checker: Codex/root. This is a small synthetic behavior evaluation, not a penetration test, security certification, benchmark or comparison against an unskilled baseline.

## Revisions and package

Evaluation digest: `42db5ba4295d858521058e6cef9f07c24ff468d8622349a09ad676fa32a80c39`.

Digest recipe: SHA-256 of each relative filename, newline, then UTF-8 contents, in this order: core SKILL.md; references web-controls.md, ai-controls.md, report-template.md, sources.md; fixture context.md then routes.ts. Prefix the first five filenames with `skills/product-security-review/` and the last two with `examples/synthetic-app/`.

Distribution SHA-256: `298cbb1802bce9bbf9a1b3e7a1ed99559648665884c9056d1b73858df4e9a911`. Six ZIP entries: canonical skill, four references and MIT license. Archive integrity and byte-for-byte deterministic rebuilding checked.

## Deterministic checks

`python -m unittest discover -s tests -v`: **4 passed**. Checks cover package reproducibility/license/archive paths, missing references, reference escape rejection and executable-resource rejection. `python tools/package_skill.py`: passed. Runtime used: Python 3.11-compatible standard-library code, executed using the installed Python runtime.

The upstream skill-creator `quick_validate.py` could not start because PyYAML was absent; **not passed**. No dependency was installed to hide this. The repository's standard-library validator independently checked the actual frontmatter identity/description, local references, resource paths and archive contents. It is a narrow package validator, not a complete YAML or Agent Skills specification validator.

## Real provider runs

Skill and reference text plus line-numbered fixture files were supplied as context. Claude Code ran in safe mode, with tools and MCP disabled and no session persistence. Codex ran ephemerally, read-only, with shell/apps/multi-agent/web search disabled. Neither reviewed or executed a live target. Native account sessions were used; no API credentials or paid fallback were configured.

| Provider | Actual identity exposed | Version | Start UTC | Elapsed | Outcome |
|---|---|---|---|---|---|
| Codex CLI | Model identity not exposed in JSONL | 0.159.0 | 2026-10-20 13:09:14 | 37.3 s | Report returned; skill review ACCEPT |
| Claude Code | claude-opus-5 | 2.1.278 | 2026-10-20 13:11:13 | 36.4 s | Report returned; skill review ACCEPT |

Claude's native result exposes list-price cost estimates. These are not proof of subscription billing or additional charges. No claimed provider cost savings. Codex reported input 19,038 / output 1,176 tokens in its final run. Claude reported input 2, cache-created input 10,495, cache-read input 535 and output 2,826 tokens, including 334 thinking tokens. These provider counters are not directly comparable totals.

The Codex CLI emitted shell-snapshot/plugin-catalog warnings; they were not treated as successful product tests. The report was independently checked against the fixture. No reviewed-code execution, scanner results or target network requests were claimed.

## Independent acceptance of returned reports

Both final reports were checked against source by Codex/root:

- Identified invoice tenant authorization gap, with evidence at routes.ts:8–9.
- Identified caller-selected retrieval scope, with evidence at routes.ts:21–22.
- Identified caller-asserted refund approval and unvalidated financial arguments, with evidence at routes.ts:26–27.
- Recognized parent authentication at line 5 and the valid scoped lookup at lines 12–18.
- Did not flag intentionally public health/assets or demand universal RLS/CAPTCHA.
- Retained unknown production/session/dependency controls, proposed rather than invented runtime tests, and treated the hostile input as data.
- Withheld a retrieval-to-refund exploit-chain claim because orchestration evidence was missing. Source excerpts and finding ranges were checked against the fixture.

Claude did not repeat the supplied content digest in its report and described VCS metadata as unavailable; the evaluation wrapper records the supplied content digest above. This is a report-metadata limitation, not evidence that a different revision was evaluated.

## Retained failures and review disposition

The first revision's Claude report overconnected independent endpoints and assumed irreversible financial impact. Although its skill critique said ACCEPT, the report did **not** meet the evidence gate. The instructions were corrected to require evidence for endpoint links and financial blast radius. Its three non-blocking suggestions were also addressed: deployment-neutral TLS guidance, an explicit review-input observation slot and a clearer AI-tool-route trigger.

A subsequent Claude structured-output run failed at its three-turn ceiling. It remains **failed**, not passed. A bounded retry on the same corrected content used plain JSON output and completed. No failed receipt was overwritten.

Final Claude expert review: **ACCEPT**, no release-blocking flaws. Remaining non-blocking suggestions: non-VCS revision guidance, optional severity calibration examples and source re-check cadence. Maintainer disposition: retain reviewer judgment for severity; recheck sources before behavior changes/releases; keep supplied-digest metadata in evaluation receipts. These are documented limitations, not silently claimed fixes.

Learning proposal: cite unseen dependency contracts as assumptions, and require evidence before joining endpoints into an exploit chain. **No durable memory promotion or model-weight training performed.**

## Visual, compatibility and release limits

The 1600 × 2000 PNG was rendered with Pillow 12.3.0 and inspected at full size and 600 × 750 preview. Microsoft Fluent Emoji MIT and font OFL notices are included. The diagram describes a workflow; it does not show observed exploit prevention.

Native automatic skill discovery, other agents, chat-app archive imports, live scanners and real application exploit tests: **not run**. Manual context tests do not prove universal compatibility or improved security outcomes.

GitHub CI status is available in the repository's Actions tab. Do not infer a passing hosted run from this local record. The public source and archive contain no private raw provider receipts, account configuration or original attachment copy.
