# AGENTS.md — Theme Studio (`THEM`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/06-theme-studio.md` · Tasks: `docs/tasks/THEM/INDEX.md` (`python scripts/tasks.py list --module THEM`)
- Work only inside `admin_utils/theme/` and `frontend/src/features/theme/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_theme`.

## Pitfalls
- Frappe UI breaking changes: pin versions, visual diffs on upgrade PRs

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
