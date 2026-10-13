# AGENTS.md — Assistive Intelligence Layer (`AIAS`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/32-assistive-intelligence.md` · Tasks: `docs/tasks/AIAS/INDEX.md` (`python scripts/tasks.py list --module AIAS`)
- Work only inside `admin_utils/assist/` and `frontend/src/features/assist/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_assist` (off by default).
- **Privileged module:** human approval on design and merge; security reviewer sign-off; two reviewers; no shell, argv lists only where processes are involved.
- **Masking required:** use the central masking utility on every read path; add a planted-secret test.

## Pitfalls
- Assistive layer leaking data to providers: data minimisation, masking, allowlisted endpoints, opt-in per feature
- AI-agent mistakes in privileged modules: contracts first, human gate

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
