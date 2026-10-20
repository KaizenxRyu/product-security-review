# LinkedIn draft, not published

I built a small skill for a question I keep coming back to when using AI to build software:

“What should we check before calling this ready?”

Product Security Review gives a coding agent a review playbook. It asks the agent to trace access controls and data boundaries, show the source evidence behind a finding, and separate confirmed gaps from things it cannot verify.

For AI-enabled apps, it also looks at retrieval isolation, untrusted instructions and who actually authorizes a tool action.

The output should be practical: what the risk is, where it comes from, how to fix it and what still needs testing.

I started this in Claude, then made the instructions provider-neutral. The same supplied skill context was tried with Claude Code and Codex on a synthetic fixture. That is a small behavior check, not a claim that every agent will use it correctly.

It is not a scanner or a security guarantee. It is a way to ask for a more disciplined review.

Which checks would you add?

Repository: https://github.com/KaizenxRyu/product-security-review

#AISecurity #AgentSkills #SecureDevelopment

Attach: assets/product-security-review-flow.png. Confirm the public repository is available before sharing this draft. Do not claim measured improvement without a controlled comparison.
