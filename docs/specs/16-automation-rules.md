---
code: AUTO
title: "Automation & Rules Builder"
number: 16
status: draft
privileged: false
depends_on: [CORE, NTFY]
code_path: admin_utils/automation/
frontend_path: frontend/src/features/automation/
tasks: docs/tasks/AUTO/INDEX.md
---

# Spec 16 — Automation & Rules Builder (`AUTO`)

## Purpose

Automation & Rules Builder: see feature groups below.

## Placement

- Python package: `admin_utils/automation/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/automation/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Automation & Rules Builder Settings`; on/off flag `enable_automation` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/automation/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 6 |
| P1 | 11 |
| P2 | 13 |

Waves: wave 8 (17), wave 11 (13)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`NTFY`](15-notification-center.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [AUTO-001](../tasks/AUTO/AUTO-001.md) | P0 | 8 | Rule builder: trigger → condition → action with visual editor |
| [AUTO-002](../tasks/AUTO/AUTO-002.md) | P0 | 8 | Triggers: doc event, schedule, webhook, threshold, manual |
| [AUTO-003](../tasks/AUTO/AUTO-003.md) | P0 | 8 | Safe condition language (no arbitrary code) with test sandbox |
| [AUTO-004](../tasks/AUTO/AUTO-004.md) | P0 | 8 | Actions: set field, assign, notify, create doc, call allowlisted method |
| [AUTO-005](../tasks/AUTO/AUTO-005.md) | P0 | 8 | Dry-run with simulated documents and result preview |
| [AUTO-006](../tasks/AUTO/AUTO-006.md) | P0 | 8 | Execution log with inputs, outputs, errors |
| [AUTO-007](../tasks/AUTO/AUTO-007.md) | P1 | 8 | Rule priority and conflict detection |
| [AUTO-008](../tasks/AUTO/AUTO-008.md) | P1 | 8 | Enable/disable and schedule windows per rule |
| [AUTO-009](../tasks/AUTO/AUTO-009.md) | P1 | 8 | Rate limits and loop prevention (rule triggering itself) |
| [AUTO-010](../tasks/AUTO/AUTO-010.md) | P1 | 8 | Approval-step action integrated with workflows |
| [AUTO-011](../tasks/AUTO/AUTO-011.md) | P1 | 8 | Rule templates: auto-assign, escalate overdue, reminder, close stale, tag by value |
| [AUTO-012](../tasks/AUTO/AUTO-012.md) | P1 | 8 | Per-rule permissions (who can edit/enable) |
| [AUTO-013](../tasks/AUTO/AUTO-013.md) | P1 | 8 | Bulk apply a rule to existing records with preview |
| [AUTO-014](../tasks/AUTO/AUTO-014.md) | P1 | 8 | Rule versioning and rollback |
| [AUTO-015](../tasks/AUTO/AUTO-015.md) | P1 | 8 | Impact analysis (how many documents match now) |
| [AUTO-016](../tasks/AUTO/AUTO-016.md) | P1 | 8 | Failure handling: retry policy, dead-letter list |
| [AUTO-017](../tasks/AUTO/AUTO-017.md) | P1 | 8 | Variable library (current user, today, doc fields, related doc fields) |
| [AUTO-018](../tasks/AUTO/AUTO-018.md) | P2 | 11 | Multi-step flows with branching and wait steps |
| [AUTO-019](../tasks/AUTO/AUTO-019.md) | P2 | 11 | Delayed actions ("3 days after status change") |
| [AUTO-020](../tasks/AUTO/AUTO-020.md) | P2 | 11 | Rule performance profiler (execution time per rule) |
| [AUTO-021](../tasks/AUTO/AUTO-021.md) | P2 | 11 | Rule dependency graph |
| [AUTO-022](../tasks/AUTO/AUTO-022.md) | P2 | 11 | Export/import rules as JSON |
| [AUTO-023](../tasks/AUTO/AUTO-023.md) | P2 | 11 | Rule testing with recorded events replay |
| [AUTO-024](../tasks/AUTO/AUTO-024.md) | P2 | 11 | Audit trail for rule changes |
| [AUTO-025](../tasks/AUTO/AUTO-025.md) | P2 | 11 | Integration with Kanban column automation (VIEW-023) |
| [AUTO-026](../tasks/AUTO/AUTO-026.md) | P2 | 11 | Email-to-document rules (parse subject/body) with allowlist |
| [AUTO-027](../tasks/AUTO/AUTO-027.md) | P2 | 11 | Scheduled data cleanup rules (archive/close) with safeguards |
| [AUTO-028](../tasks/AUTO/AUTO-028.md) | P2 | 11 | Natural-language rule drafting (assistive, always reviewed) |
| [AUTO-029](../tasks/AUTO/AUTO-029.md) | P2 | 11 | Rule analytics (fires per day, success rate) |
| [AUTO-030](../tasks/AUTO/AUTO-030.md) | P2 | 11 | Rule marketplace/templates catalog |

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
