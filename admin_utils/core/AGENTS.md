# AGENTS.md — Platform, Shell & Cross-Cutting (`CORE`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/00-core-platform.md` · Tasks: `docs/tasks/CORE/INDEX.md` (`python scripts/tasks.py list --module CORE`)
- Work only inside `admin_utils/core/` and `frontend/src/features/core/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_core`.

## Pitfalls
- v15/v16 schema divergence: keep every difference inside core/compat
- Secrets leakage in logs/UI: central masking utility lives here

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
