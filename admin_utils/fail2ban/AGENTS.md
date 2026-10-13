# AGENTS.md — Fail2ban Integration (`F2B`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/11-fail2ban.md` · Tasks: `docs/tasks/F2B/INDEX.md` (`python scripts/tasks.py list --module F2B`)
- Work only inside `admin_utils/fail2ban/` and `frontend/src/features/fail2ban/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_fail2ban` (off by default).
- **Privileged module:** human approval on design and merge; security reviewer sign-off; two reviewers; no shell, argv lists only where processes are involved.

## Pitfalls
- Bench/fail2ban misuse (critical): minimal sudoers rule limited to named fail2ban-client subcommands, off by default

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
