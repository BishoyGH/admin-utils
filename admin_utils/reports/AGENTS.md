# AGENTS.md — No-Code Query/Script Report Designer (`REPT`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/02-report-designer.md` · Tasks: `docs/tasks/REPT/INDEX.md` (`python scripts/tasks.py list --module REPT`)
- Work only inside `admin_utils/reports/` and `frontend/src/features/reports/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_reports`.

## Pitfalls
- Large-data performance: server-side pagination, aggregation endpoints, perf budgets

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
