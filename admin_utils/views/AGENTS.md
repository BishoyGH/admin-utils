# AGENTS.md — Enhanced Views (new, additive; core views untouched) (`VIEW`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/12-enhanced-views.md` · Tasks: `docs/tasks/VIEW/INDEX.md` (`python scripts/tasks.py list --module VIEW`)
- Work only inside `admin_utils/views/` and `frontend/src/features/views/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_views`.

## Pitfalls
- Large-data performance: server-side pagination, aggregation endpoints, perf budgets

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
