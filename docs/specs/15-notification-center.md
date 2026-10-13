---
code: NTFY
title: "Notification Center"
number: 15
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/notifications/
frontend_path: frontend/src/features/notifications/
tasks: docs/tasks/NTFY/INDEX.md
---

# Spec 15 — Notification Center (`NTFY`)

## Purpose

Notification Center: see feature groups below.

## Placement

- Python package: `admin_utils/notifications/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/notifications/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Notification Center Settings`; on/off flag `enable_notifications` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/notifications/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 3 |
| P1 | 8 |
| P2 | 9 |

Waves: wave 2 (10), wave 8 (10)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [NTFY-001](../tasks/NTFY/NTFY-001.md) | P0 | 2 | Central admin notification inbox for alerts from all modules |
| [NTFY-002](../tasks/NTFY/NTFY-002.md) | P0 | 2 | Channels: in-app, email, webhook (Slack/Telegram/Teams via configurable URL) |
| [NTFY-003](../tasks/NTFY/NTFY-003.md) | P0 | 2 | Severity levels and routing rules |
| [NTFY-004](../tasks/NTFY/NTFY-004.md) | P1 | 2 | Quiet hours and escalation rules |
| [NTFY-005](../tasks/NTFY/NTFY-005.md) | P1 | 2 | Deduplication and rate limiting of repeated alerts |
| [NTFY-006](../tasks/NTFY/NTFY-006.md) | P1 | 2 | Acknowledge/snooze/resolve actions |
| [NTFY-007](../tasks/NTFY/NTFY-007.md) | P1 | 2 | Per-user subscription preferences |
| [NTFY-008](../tasks/NTFY/NTFY-008.md) | P1 | 2 | Message templates with variables, EN/AR |
| [NTFY-009](../tasks/NTFY/NTFY-009.md) | P1 | 2 | Delivery log with retries and failure reasons |
| [NTFY-010](../tasks/NTFY/NTFY-010.md) | P1 | 2 | Test-send for each channel |
| [NTFY-011](../tasks/NTFY/NTFY-011.md) | P1 | 8 | Digest mode (hourly/daily) grouping similar alerts |
| [NTFY-012](../tasks/NTFY/NTFY-012.md) | P2 | 8 | On-call schedule and rotation |
| [NTFY-013](../tasks/NTFY/NTFY-013.md) | P2 | 8 | Escalate unacknowledged critical alerts to next person |
| [NTFY-014](../tasks/NTFY/NTFY-014.md) | P2 | 8 | Alert correlation (group by root cause) |
| [NTFY-015](../tasks/NTFY/NTFY-015.md) | P2 | 8 | Webhook signature and secret handling |
| [NTFY-016](../tasks/NTFY/NTFY-016.md) | P2 | 8 | WhatsApp/SMS provider adapter interface |
| [NTFY-017](../tasks/NTFY/NTFY-017.md) | P2 | 8 | Push notifications for the PWA |
| [NTFY-018](../tasks/NTFY/NTFY-018.md) | P2 | 8 | Notification analytics (volume, MTTA, MTTR) |
| [NTFY-019](../tasks/NTFY/NTFY-019.md) | P2 | 8 | Silence rules by label/module/time |
| [NTFY-020](../tasks/NTFY/NTFY-020.md) | P2 | 8 | Public status page generator (opt-in, sanitized) |

## Tests

- No module-specific highlights beyond the shared strategy; follow the security matrix and Definition of Done.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
