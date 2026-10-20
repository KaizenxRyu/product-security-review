# Maintenance and release

1. Read project guidance and keep the core skill provider-neutral.
2. Validate the skill/package and run meaningful synthetic behavior checks after instruction changes. Keep actual provider/model/version, artifact hash and outcomes. Never publish raw credentials or local provider homes.
3. Build dist/product-security-review.skill using the packaging tool. It must contain only the canonical skill directory and its referenced files; do not include .work, project notes or reviewer prompts.
4. Rebuild the flow PNG after changing its text/assets; visually inspect it at full size and mobile scale. Preserve third-party notices and avoid endorsement claims.
5. Review the exact skill revision before publication. Publish actual limitations and compatibility evidence, not inferred test coverage.

Installing the skill does not execute tools or configure an account. Rollback is removing its copied project skill folder; preserve any local edits first. Do not delete global/provider configuration or replace an unrelated skill. Existing release archives remain reproducible from the pinned source and package tool.
