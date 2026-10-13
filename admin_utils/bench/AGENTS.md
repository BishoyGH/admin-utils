# AGENTS.md — Run Bench Commands From UI (`BNCH`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/03-bench-commands.md` · Tasks: `docs/tasks/BNCH/INDEX.md` (`python scripts/tasks.py list --module BNCH`)
- Work only inside `admin_utils/bench/` and `frontend/src/features/bench/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_bench` (off by default).
- **Privileged module:** human approval on design and merge; security reviewer sign-off; two reviewers; no shell, argv lists only where processes are involved.

## Pitfalls
- Bench misuse / RCE vector (critical): allowlist, argv lists, never a shell, sub-roles, off by default, pen-test

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
