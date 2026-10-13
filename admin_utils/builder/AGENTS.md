# AGENTS.md — App Builder & Customization Export (`BLDR`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/24-app-builder.md` · Tasks: `docs/tasks/BLDR/INDEX.md` (`python scripts/tasks.py list --module BLDR`)
- Work only inside `admin_utils/builder/` and `frontend/src/features/builder/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_builder` (off by default).
- **Privileged module:** human approval on design and merge; security reviewer sign-off; two reviewers; no shell, argv lists only where processes are involved.

## Pitfalls
- Generated apps contain unreviewed or unsafe code: fixed templates, review gate for scripts, sensitive-data scan, sandboxed output dir
- App creation/installation on production: environment-policy block, approvals, mandatory backup, canary on a clone

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
