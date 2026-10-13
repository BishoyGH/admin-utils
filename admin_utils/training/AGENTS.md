# AGENTS.md — Training Academy (`TRAIN`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/34-training-academy.md` · Tasks: `docs/tasks/TRAIN/INDEX.md` (`python scripts/tasks.py list --module TRAIN`)
- Work only inside `admin_utils/training/` and `frontend/src/features/training/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_training`.

## Pitfalls
- Training sandbox causes real-world side effects (email, webhooks, payments): dedicated company/site, outbound blocking, isolation tests
- Training content goes stale: owners, review dates, release-based "what changed" flows

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
