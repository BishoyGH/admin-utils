# AGENTS.md — Log Center (`LOGS`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/36-log-center.md` · Tasks: `docs/tasks/LOGS/INDEX.md` (`python scripts/tasks.py list --module LOGS`)
- Work only inside `admin_utils/logs/` and `frontend/src/features/logs/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_logs`.
- **Masking required:** use the central masking utility on every read path; add a planted-secret test.

## Pitfalls
- Logs expose secrets or personal data: read-time masking, role gates per source group, audited reveal with re-authentication, export watermarking
- Log tooling slows production: sampling, overhead budget, bounded reads

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
