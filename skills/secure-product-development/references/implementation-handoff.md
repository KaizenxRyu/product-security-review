# Implementation handoff

Scale this to the task. Lead with implemented behavior; a security-review report is not required for every code change.

- **Implemented:** feature/change and relevant source locations. Identify controls actually on the execution path and any intentional public behavior.
- **Boundary decisions:** trusted identity/data, object or tenant scope, permissions, side effects and required approvals. Explain consequential choices and link a project decision record when appropriate.
- **Verified:** exact checks or commands actually run, relevant source revision and results. Cover the allowed path and applicable rejection/tampering/retry paths. Distinguish a generated test from one that executed successfully.
- **Limits:** unknown provider/deployment behavior, tests not run, failed checks and work needing input. Do not invent security scores, tool output, runtime behavior or expert reviews.
- **Next action:** remaining scoped fix or verification, owner and rollback where relevant.

An optional finding for an unresolved gap should include its source excerpt/location, impact prerequisites, confidence, proportionate risk and proposed fix. Keep unrelated findings separate from the current feature. Never turn a missing preferred control into a universal requirement.
