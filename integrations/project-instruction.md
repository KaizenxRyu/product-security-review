# Adopt the workflow in a project

After installing the skill in the host's documented project-local skills directory, add the following to the project's AGENTS.md, CLAUDE.md or equivalent agent instruction file. Merge it with existing guidance; do not replace the file or grant new tool permissions.

> For relevant product implementation work, load and follow the `secure-product-development` skill while planning, writing and verifying code. Apply controls in the actual execution path, use trusted identity and project/tenant scope, and verify the allowed and rejection paths. Scale checks to the change. Keep tools and external actions within the user's authorization, and report actual verification and unresolved limits.

Skills guide a model; they are not an enforcement layer. Host discovery and instruction handling vary. Verify the agent actually loads the skill, and use tests, CI, permissions and runtime controls for enforcement. This repository does not modify global/provider configuration automatically.
