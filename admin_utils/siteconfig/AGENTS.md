# AGENTS.md — Site Config JSON Editor (`CONF`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/04-site-config.md` · Tasks: `docs/tasks/CONF/INDEX.md` (`python scripts/tasks.py list --module CONF`)
- Work only inside `admin_utils/siteconfig/` and `frontend/src/features/siteconfig/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_siteconfig` (off by default).
- **Privileged module:** human approval on design and merge; security reviewer sign-off; two reviewers; no shell, argv lists only where processes are involved.
- **Masking required:** use the central masking utility on every read path; add a planted-secret test.

## Pitfalls
- Secrets leakage: mask on read, atomic write, backup before write
- Bench misuse: same allowlist and approval rules as BNCH

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
