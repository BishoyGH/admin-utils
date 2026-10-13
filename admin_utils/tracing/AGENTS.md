# AGENTS.md — Tracing & Profiling (`TRCE`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/38-tracing-profiling.md` · Tasks: `docs/tasks/TRCE/INDEX.md` (`python scripts/tasks.py list --module TRCE`)
- Work only inside `admin_utils/tracing/` and `frontend/src/features/tracing/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_tracing`.
- **Masking required:** use the central masking utility on every read path; add a planted-secret test.

## Pitfalls
- Tracing slows production: sampling, overhead budget with automatic back-off, time-boxed verbose modes
- Traces expose secrets: read-time masking

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
