# AGENTS.md — Backup & Disaster Recovery (`BKUP`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/27-backup-recovery.md` · Tasks: `docs/tasks/BKUP/INDEX.md` (`python scripts/tasks.py list --module BKUP`)
- Work only inside `admin_utils/backup/` and `frontend/src/features/backup/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_backup` (off by default).
- **Privileged module:** human approval on design and merge; security reviewer sign-off; two reviewers; no shell, argv lists only where processes are involved.

## Pitfalls
- Restore must be proven: automated restore test to a throwaway site; retention never deletes the newest valid backup

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
