---
code: DASH
title: "Admin Dashboard Builder"
number: 20
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/dashboards/
frontend_path: frontend/src/features/dashboards/
tasks: docs/tasks/DASH/INDEX.md
---

# Spec 20 — Admin Dashboard Builder (`DASH`)

## Purpose

Admin Dashboard Builder: see feature groups below.

## Placement

- Python package: `admin_utils/dashboards/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/dashboards/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Admin Dashboard Builder Settings`; on/off flag `enable_dashboards` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/dashboards/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 2 |
| P1 | 8 |
| P2 | 10 |

Waves: wave 5 (10), wave 11 (10)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [DASH-001](../tasks/DASH/DASH-001.md) | P0 | 5 | Dashboard canvas with chart, number, table, text, and status widgets |
| [DASH-002](../tasks/DASH/DASH-002.md) | P0 | 5 | Data sources: reports (REPT), doctypes, monitoring metrics, custom methods (allowlisted) |
| [DASH-003](../tasks/DASH/DASH-003.md) | P1 | 5 | Global filters (date range, company, user) |
| [DASH-004](../tasks/DASH/DASH-004.md) | P1 | 5 | Widget drill-down to underlying data |
| [DASH-005](../tasks/DASH/DASH-005.md) | P1 | 5 | Role-based dashboards with default per role |
| [DASH-006](../tasks/DASH/DASH-006.md) | P1 | 5 | Templates: Admin overview, Security, Operations, Data quality, Adoption |
| [DASH-007](../tasks/DASH/DASH-007.md) | P1 | 5 | Auto-refresh with pause and last-updated stamp |
| [DASH-008](../tasks/DASH/DASH-008.md) | P1 | 5 | Export dashboard as PDF/PNG |
| [DASH-009](../tasks/DASH/DASH-009.md) | P1 | 5 | Dashboard sharing within roles |
| [DASH-010](../tasks/DASH/DASH-010.md) | P1 | 5 | Responsive layout and TV/wall-screen mode |
| [DASH-011](../tasks/DASH/DASH-011.md) | P2 | 11 | Threshold coloring and conditional widgets |
| [DASH-012](../tasks/DASH/DASH-012.md) | P2 | 11 | Annotations on charts (deployment, incident) |
| [DASH-013](../tasks/DASH/DASH-013.md) | P2 | 11 | Comparison to previous period overlay |
| [DASH-014](../tasks/DASH/DASH-014.md) | P2 | 11 | Scheduled snapshot emails |
| [DASH-015](../tasks/DASH/DASH-015.md) | P2 | 11 | Widget library extension API |
| [DASH-016](../tasks/DASH/DASH-016.md) | P2 | 11 | User adoption analytics (logins, documents created by module) |
| [DASH-017](../tasks/DASH/DASH-017.md) | P2 | 11 | Data-quality scorecards per module |
| [DASH-018](../tasks/DASH/DASH-018.md) | P2 | 11 | Permission-aware widgets (hide data the viewer cannot see) |
| [DASH-019](../tasks/DASH/DASH-019.md) | P2 | 11 | Dashboard versioning and restore |
| [DASH-020](../tasks/DASH/DASH-020.md) | P2 | 11 | Embedded dashboards in workspaces |

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
