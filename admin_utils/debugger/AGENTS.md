# AGENTS.md — Error Debugger & Triage (`DBUG`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/37-error-debugger.md` · Tasks: `docs/tasks/DBUG/INDEX.md` (`python scripts/tasks.py list --module DBUG`)
- Work only inside `admin_utils/debugger/` and `frontend/src/features/debugger/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_debugger`.
- **Masking required:** use the central masking utility on every read path; add a planted-secret test.

## Pitfalls
- Debug/replay causes real side effects: replay only on test sites, refuse production-flagged environments, no arbitrary code console
- Logs expose secrets: masking everywhere

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
