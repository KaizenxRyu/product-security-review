# Web and API control lenses

Use these as investigation prompts. Applicability, impact and severity depend on the actual product. This is a focused review, not a complete ASVS assessment.

## Identity and authorization

- Inventory public, authenticated and privileged entry points. Trace framework routing, parent middleware, reverse-proxy boundaries and shared services before classifying a route. Confirm protected operations fail closed; intentionally public health checks/assets are not missing-auth findings.
- For user/tenant data, follow reads, writes, lists, search, exports, background jobs and file access. Resolve identity and tenant membership from a trusted server-side source. Check object/action/role ownership, including guessed IDs and service-credential bypass paths. Caller-supplied tenant IDs are not proof of membership.
- With database RLS, inspect effective policies, roles, ownership and bypass credentials. Without RLS, assess actual server-side authorization and whether clients can bypass it to reach the database. Missing RLS alone is not a confirmed critical gap.
- Inspect token verification and session handling appropriate to the chosen identity provider: issuer, audience, expiry, signature/key handling, cookie attributes, session invalidation and privilege changes. Assess CSRF for cookie-authenticated state changes; a public read-only route is different. Do not invent missing crypto when an unseen library/provider implements it: mark unknown and identify the dependency.
- Gate administration server-side. UI visibility or a role supplied by a request body is not authorization. Check account recovery and privileged operations for protections appropriate to their impact.

## Inputs, outputs and outbound access

- Trace untrusted values to SQL/NoSQL, command execution, templates, browser HTML and deserializers. Distinguish parameter-bound values and allowlisted identifiers from unsafe interpolation. Escaping must match the sink; generic “sanitize everything” is not a concrete fix.
- Check mass assignment and business logic: ownership, prices, totals, quotas and permissions must derive from trusted server state. Validate types, bounds and allowed fields where they enter the application.
- Assess reflected/stored XSS, HTML-rich content and framework escape bypasses. Identify data origin and the sanitizer/encoding boundary before reporting unsafe HTML.
- For URL fetching, previews, integrations and webhooks that call outbound URLs, inspect SSRF controls, permitted destinations/protocols, redirects, DNS/IP changes and access to loopback/private/metadata endpoints as relevant. Do not probe infrastructure without authorization.
- For uploads, inspect server-side size/content/type controls, name/path normalization, download authorization and non-executable storage. Content processing and malware controls depend on file type and downstream use; extension-only trust is weak evidence of type validation.

## Data, configuration and exposure

- Distinguish confidential objects from intentionally public website assets. Review bucket policies, object authorization, signed-URL scope/expiry, encryption and retention when relevant. Public assets alone are not a breach.
- Inspect secret sources, accidental client bundles, logs, error bodies and backups. Report location and secret class, never the value. Treat environment examples as examples unless there is evidence of a real credential. Do not rotate, revoke or contact a service without authorization.
- Assess TLS termination/redirects, proxy trust, HSTS and sensitive headers/caching for the actual deployment and data involved. Source code often cannot prove deployed controls; record unknowns and the evidence needed rather than assuming either safety or a deployed gap.
- Evaluate CORS against actual caller origins, authentication and sensitive responses. Browsers reject wildcard-origin credentialed responses; that invalid combination alone does not demonstrate successful credential theft. CORS is not authentication or a general CSRF defense.
- Review CSP, anti-framing, MIME sniffing and referrer policy for the application's rendering model. Equivalent mechanisms can satisfy the same control; missing one preferred header is not automatically High severity. Check debug/errors in the actual production path.

## Abuse, integrations and supply chain

- Identify costly/sensitive routes, login/recovery, email dispatch and resource-creation limits. Assess rate limits, quotas, idempotency, bounded work and bot controls where needed. CAPTCHA is an option, not a requirement for every public form.
- Verify webhook authenticity with the provider's specified signature/raw-body or equivalent authentication mechanism. Assess replay/timestamp protection and idempotency for the action involved. Confirm through official documentation when uncertain; a signature-header name alone is not evidence of verification.
- Inspect privileged-action logging: attributable actor, action, object, outcome and safe retention. Ensure secrets/sensitive payloads are not indiscriminately logged.
- Review lockfiles, advisory evidence and dependency reachability. An audit's clean output does not prove there are no unknown vulnerabilities; absent advisories or unrun tools remain unknown. Do not upgrade dependencies during a read-only review.
- If CI/deployment is in scope, inspect token permissions, secret exposure, untrusted contribution paths, artifact trust and immutable action/dependency references. Lack of deployment files is a coverage limit, not proof that production lacks these controls.
