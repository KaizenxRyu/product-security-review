# Maintenance and release

1. Read project guidance and keep the core skill provider-neutral.
2. Validate the skill/package and run meaningful synthetic behavior checks after instruction changes. Keep actual provider/model/version, artifact hash and outcomes. Never publish raw credentials or local provider homes.
3. Build dist/secure-product-development.skill using the packaging tool. Include only the current workflow directory, references and license; exclude .work, old review packages and provider receipts. Compare the hosted rebuilt archive with the committed download.
4. Rebuild the flow PNG after changing its text/assets; visually inspect it at full size and mobile scale. Preserve third-party notices and avoid endorsement claims.
5. Review the exact skill revision before publication. Publish actual limitations and compatibility evidence, not inferred test coverage.

6. After instruction changes, evaluate an implementation task rather than only requesting a review report. Inspect generated code before executing it. Run actual allowed/rejection tests in isolated synthetic copies, keep failed receipts, and distinguish preparation from consequential execution.

Installing the skill does not execute tools or configure an account. Rollback is removing its copied project skill folder; preserve any local edits first. Do not delete global/provider configuration or replace an unrelated skill. Existing release archives remain reproducible from the pinned source and package tool.
