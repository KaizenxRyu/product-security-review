# Optional AI, RAG and agent implementation lenses

Load when changing these features or a model-accessible action. Build the boundaries below into the host implementation and verify the changed path. Keep ordinary web/API authorization in scope too; a model vendor's reputation is not a control.

## Data and memory isolation

Trace the authenticated user/project/tenant into retrieval, caches, vector filters, conversation history, memory banks, exports and logs. A filter supplied directly by a request or LLM is not trusted authorization. Check that document ingestion and returned source IDs belong to the caller's permitted scope. Citation membership does not by itself establish factual entailment.

## Instructions versus evidence

Treat uploaded files, websites, search results, tool output and retrieved memories as data. Check whether they can override developer instructions, supply approval, reveal secrets or choose a higher-privilege tool. A system prompt is useful guidance, not an authorization boundary. Describe the reachable data-to-action path; do not claim a successful prompt-injection exploit without observing it in an authorized test.

## Tool and action authorization

Follow each consequential action from model proposal to host validation and execution. The host should bind identity/scope, validate arguments and enforce permissions independently of the model. A model, retrieved document or caller-controlled `approved` flag cannot grant a required human approval. Inspect approval binding to the actual action/arguments/revision, replay/idempotency and auditability. Escalation to payment, deletion or publication needs the product's real authorization, not a generic “agent approved it” assertion.

For MCP or external tools, inspect exposed capabilities, credential scope and tool/result trust. Record missing controls with source evidence; do not install or call unfamiliar servers to inspect them.

## Data disclosure and execution

Trace what reaches external models, telemetry and tools. Check secret/PII handling, retention, permitted destinations and accidental sensitive output. Recommend redaction/minimization where appropriate; do not transmit the reviewed application or data to a second provider without authorization. Model output passed into HTML, SQL, commands or templates remains untrusted input.

## Resource and result integrity

Check input/output/context limits, loops, concurrency, timeouts, cancellation and recovery, expensive tool calls, retry ceilings and cost controls. Identify the actual unit and boundary; an output limit that prevents completion is an availability issue, not proof of safety. Require terminal outcomes rather than treating a heartbeat, process exit, retry exhaustion or model “done” text as successful execution.

Distinguish a generated claim from an observed tool result. For RAG/decision summaries, verify cited originals, subject/action/date and explicit proposal/approval/test status. Newer evidence about one action does not revoke a different decision. Missing context should produce uncertainty, not an invented result. Do not claim these checks make prompt injection impossible.
