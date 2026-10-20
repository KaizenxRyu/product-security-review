# LinkedIn draft, not published

I built **Secure Product Development**, a skill that helps an AI coding agent think about security while it builds a feature.

It gives the agent a working method:

• Understand who can access which data and actions.
• Put authorization and validation in the actual code path.
• Check both the allowed path and the requests that should fail.
• Hand off working code with actual test results and honest limits.

For AI-enabled apps, that also means keeping retrieval inside the right project or tenant, and enforcing tool permissions in the host rather than trusting a model's approval.

I tried the same skill context with Claude Code and Codex on a synthetic billing-assistant task. Each generated implementation passed 24 checks. That is a small practical example, not a security guarantee or a claim that every agent will follow it correctly.

The instructions, example and tests are available to adapt.

What would you add to an AI agent's everyday development workflow?

Repository: https://github.com/KaizenxRyu/secure-product-development

#AgentSkills #SecureDevelopment #AISecurity

Attach assets/secure-product-development-flow.png. Confirm the current public release and hosted checks before sharing. No LinkedIn publication is authorized by this draft.
