---
code: INSI
title: "Adoption & Usage Insights"
number: 28
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/insights/
frontend_path: frontend/src/features/insights/
tasks: docs/tasks/INSI/INDEX.md
---

# Spec 28 — Adoption & Usage Insights (`INSI`)

## Purpose

Adoption & Usage Insights: see feature groups below.

## Placement

- Python package: `admin_utils/insights/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/insights/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Adoption & Usage Insights Settings`; on/off flag `enable_insights` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/insights/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P1 | 8 |
| P2 | 17 |

Waves: wave 2 (4), wave 9 (4), wave 11 (17)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [INSI-001](../tasks/INSI/INSI-001.md) | P1 | 2 | Module and doctype usage dashboard (documents created, edited, submitted per period) |
| [INSI-002](../tasks/INSI/INSI-002.md) | P1 | 2 | Active users by day, week, month with role breakdown |
| [INSI-003](../tasks/INSI/INSI-003.md) | P1 | 2 | Feature adoption per module (who uses which workspace, report, view) |
| [INSI-004](../tasks/INSI/INSI-004.md) | P1 | 2 | Stale module detector (installed but unused) |
| [INSI-005](../tasks/INSI/INSI-005.md) | P1 | 9 | Slowest user-facing actions (form load, save, submit) from request logs |
| [INSI-006](../tasks/INSI/INSI-006.md) | P1 | 9 | Error rate per user, doctype and action |
| [INSI-007](../tasks/INSI/INSI-007.md) | P1 | 9 | Top validation failures (which messages users hit most) |
| [INSI-008](../tasks/INSI/INSI-008.md) | P1 | 9 | Search usage and zero-result queries |
| [INSI-009](../tasks/INSI/INSI-009.md) | P2 | 11 | Training-gap finder (users repeatedly hitting the same error) |
| [INSI-010](../tasks/INSI/INSI-010.md) | P2 | 11 | Workflow bottleneck analysis (time in each state, stuck documents) |
| [INSI-011](../tasks/INSI/INSI-011.md) | P2 | 11 | Approval turnaround metrics by approver and department |
| [INSI-012](../tasks/INSI/INSI-012.md) | P2 | 11 | Data-entry quality score per user and module (corrections, rejections) |
| [INSI-013](../tasks/INSI/INSI-013.md) | P2 | 11 | Report usage and ownerless-report detection |
| [INSI-014](../tasks/INSI/INSI-014.md) | P2 | 11 | Customization usage (is that custom field ever filled, is that script ever fired) |
| [INSI-015](../tasks/INSI/INSI-015.md) | P2 | 11 | Integration usage and failure trends |
| [INSI-016](../tasks/INSI/INSI-016.md) | P2 | 11 | Peak-load calendar and capacity planning hints |
| [INSI-017](../tasks/INSI/INSI-017.md) | P2 | 11 | Cohort view of new users' first-30-days activity |
| [INSI-018](../tasks/INSI/INSI-018.md) | P2 | 11 | Department comparison with privacy thresholds (minimum group size) |
| [INSI-019](../tasks/INSI/INSI-019.md) | P2 | 11 | Privacy controls (aggregate-only mode, retention, opt-out for sensitive roles) |
| [INSI-020](../tasks/INSI/INSI-020.md) | P2 | 11 | Insights export and scheduled digest |
| [INSI-021](../tasks/INSI/INSI-021.md) | P2 | 11 | Recommendations feed ("12 custom fields unused", "3 workflows with stuck documents") |
| [INSI-022](../tasks/INSI/INSI-022.md) | P2 | 11 | Before/after impact of a change set on usage and errors |
| [INSI-023](../tasks/INSI/INSI-023.md) | P2 | 11 | Mobile vs desktop usage split |
| [INSI-024](../tasks/INSI/INSI-024.md) | P2 | 11 | Language and RTL usage split |
| [INSI-025](../tasks/INSI/INSI-025.md) | P2 | 11 | Adoption goals and progress tracking |

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
