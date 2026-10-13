# AGENTS.md — Environment Promotion & Sync (`MIGR`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/25-environment-promotion.md` · Tasks: `docs/tasks/MIGR/INDEX.md` (`python scripts/tasks.py list --module MIGR`)
- Work only inside `admin_utils/promotion/` and `frontend/src/features/promotion/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_promotion` (off by default).
- **Privileged module:** human approval on design and merge; security reviewer sign-off; two reviewers; no shell, argv lists only where processes are involved.

## Pitfalls
- App installation on production: environment-policy block, approvals, mandatory backup, canary on a clone

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
