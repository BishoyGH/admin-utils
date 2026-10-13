---
code: MOBL
title: "Mobile & PWA"
number: 22
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/mobile/
frontend_path: frontend/src/features/mobile/
tasks: docs/tasks/MOBL/INDEX.md
---

# Spec 22 — Mobile & PWA (`MOBL`)

## Purpose

Mobile & PWA: see feature groups below.

## Placement

- Python package: `admin_utils/mobile/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/mobile/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Mobile & PWA Settings`; on/off flag `enable_mobile` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/mobile/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P1 | 6 |
| P2 | 9 |

Waves: wave 3 (3), wave 7 (12)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [MOBL-001](../tasks/MOBL/MOBL-001.md) | P1 | 3 | PWA manifest, icons and installability for `/manage` |
| [MOBL-002](../tasks/MOBL/MOBL-002.md) | P1 | 3 | Mobile-first navigation (bottom bar, drawer) |
| [MOBL-003](../tasks/MOBL/MOBL-003.md) | P1 | 3 | Touch-friendly tables (card mode) and large tap targets |
| [MOBL-004](../tasks/MOBL/MOBL-004.md) | P1 | 7 | Service worker caching of static assets only (no sensitive data) |
| [MOBL-005](../tasks/MOBL/MOBL-005.md) | P1 | 7 | Mobile-friendly monitoring and approvals screens |
| [MOBL-006](../tasks/MOBL/MOBL-006.md) | P1 | 7 | Biometric/device re-auth for sensitive actions where the browser supports it |
| [MOBL-007](../tasks/MOBL/MOBL-007.md) | P2 | 7 | Push notifications integration with NTFY |
| [MOBL-008](../tasks/MOBL/MOBL-008.md) | P2 | 7 | Offline read-only cache for selected dashboards with expiry |
| [MOBL-009](../tasks/MOBL/MOBL-009.md) | P2 | 7 | Share sheet integration for exporting reports |
| [MOBL-010](../tasks/MOBL/MOBL-010.md) | P2 | 7 | Camera barcode scan helper in views and seeder lookups |
| [MOBL-011](../tasks/MOBL/MOBL-011.md) | P2 | 7 | Install prompt and update-available banner |
| [MOBL-012](../tasks/MOBL/MOBL-012.md) | P2 | 7 | Responsive Kanban with column swipe |
| [MOBL-013](../tasks/MOBL/MOBL-013.md) | P2 | 7 | Reduced-data mode for slow connections |
| [MOBL-014](../tasks/MOBL/MOBL-014.md) | P2 | 7 | Gesture shortcuts with accessible alternatives |
| [MOBL-015](../tasks/MOBL/MOBL-015.md) | P2 | 7 | Mobile performance budgets in CI (Lighthouse mobile) |

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
