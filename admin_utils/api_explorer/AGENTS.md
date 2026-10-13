# AGENTS.md — API Explorer & Integrations (`APIX`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/21-api-explorer.md` · Tasks: `docs/tasks/APIX/INDEX.md` (`python scripts/tasks.py list --module APIX`)
- Work only inside `admin_utils/api_explorer/` and `frontend/src/features/api_explorer/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_api_explorer`.

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
