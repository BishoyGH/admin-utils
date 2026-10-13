# AGENTS.md — Onboarding Studio (`ONBD`)

Read the root `AGENTS.md` first. This file adds module-specific rules.

- Spec: `docs/specs/07-onboarding-studio.md` · Tasks: `docs/tasks/ONBD/INDEX.md` (`python scripts/tasks.py list --module ONBD`)
- Work only inside `admin_utils/onboarding/` and `frontend/src/features/onboarding/`; cross-module needs go through published service interfaces.
- Layering: `api/` (auth + validation only) -> `services/` -> `core/compat` -> Frappe. No `@frappe.whitelist` in `services/`.
- Every endpoint uses the central `guard()` (role + feature flag + rate limit) and the standard response envelope.
- Every mutating action writes an audit row. Strings go through i18n (EN + AR); CSS uses logical properties (RTL).
- Feature flag: `enable_onboarding`.

## Pitfalls
- Guided flows break when the UI changes: resilient anchors, anchor health dashboard, nightly playback

## Conventions and commands

_Agents: keep this section current. Record commands that work, naming rules, and mistakes to avoid._
