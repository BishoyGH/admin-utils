# AGENTS.md — Print Format & Document Output Designer (`PRNT`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/18-print-output-designer.md` · Tasks: `docs/tasks/PRNT/INDEX.md` (`python scripts/tasks.py list --module PRNT`)
- Work only inside `admin_utils/printing/` and `frontend/src/features/printing/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_printing`.

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
