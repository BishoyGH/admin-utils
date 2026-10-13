---
code: FORM
title: "DocType & Form Designer Helpers"
number: 17
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/forms/
frontend_path: frontend/src/features/forms/
tasks: docs/tasks/FORM/INDEX.md
---

# Spec 17 — DocType & Form Designer Helpers (`FORM`)

## Purpose

DocType & Form Designer Helpers: see feature groups below.

## Placement

- Python package: `admin_utils/forms/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/forms/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `DocType & Form Designer Helpers Settings`; on/off flag `enable_forms` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/forms/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 1 |
| P1 | 15 |
| P2 | 9 |

Waves: wave 5 (16), wave 11 (9)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [FORM-001](../tasks/FORM/FORM-001.md) | P0 | 5 | DocType explorer with fields, links, dependencies, permissions in one screen |
| [FORM-002](../tasks/FORM/FORM-002.md) | P1 | 5 | Field usage analyzer (filled %, distinct values, last used) |
| [FORM-003](../tasks/FORM/FORM-003.md) | P1 | 5 | Layout designer for custom forms (sections, columns, tabs) writing supported Customize Form settings |
| [FORM-004](../tasks/FORM/FORM-004.md) | P1 | 5 | Field visibility rules builder (depends_on) with safe expression helper and tester |
| [FORM-005](../tasks/FORM/FORM-005.md) | P1 | 5 | Mandatory-depends rules builder |
| [FORM-006](../tasks/FORM/FORM-006.md) | P1 | 5 | Read-only rules builder |
| [FORM-007](../tasks/FORM/FORM-007.md) | P1 | 5 | Default value rules helper (today, user, company, last used) |
| [FORM-008](../tasks/FORM/FORM-008.md) | P1 | 5 | Field rename/move impact analysis (reports, scripts, print formats, workflows) |
| [FORM-009](../tasks/FORM/FORM-009.md) | P1 | 5 | Custom field creation wizard with presets (status, category, note, amount) |
| [FORM-010](../tasks/FORM/FORM-010.md) | P1 | 5 | Bulk add custom fields across doctypes with preview |
| [FORM-011](../tasks/FORM/FORM-011.md) | P1 | 5 | Link filter builder for Link fields |
| [FORM-012](../tasks/FORM/FORM-012.md) | P1 | 5 | Select options manager with usage counts and safe removal |
| [FORM-013](../tasks/FORM/FORM-013.md) | P1 | 5 | Naming rule designer and preview of generated names |
| [FORM-014](../tasks/FORM/FORM-014.md) | P1 | 5 | Quick-entry form designer (minimal fields for fast creation) |
| [FORM-015](../tasks/FORM/FORM-015.md) | P1 | 5 | List view settings designer (columns, badges, indicators) |
| [FORM-016](../tasks/FORM/FORM-016.md) | P1 | 5 | Search fields and title field configuration helper |
| [FORM-017](../tasks/FORM/FORM-017.md) | P2 | 11 | Form template library (customer intake, expense claim, visit report) |
| [FORM-018](../tasks/FORM/FORM-018.md) | P2 | 11 | Form version snapshot and rollback of customizations |
| [FORM-019](../tasks/FORM/FORM-019.md) | P2 | 11 | Compare customization between two sites |
| [FORM-020](../tasks/FORM/FORM-020.md) | P2 | 11 | Dependency map of doctypes (who links to whom) |
| [FORM-021](../tasks/FORM/FORM-021.md) | P2 | 11 | Dead field and dead doctype detection |
| [FORM-022](../tasks/FORM/FORM-022.md) | P2 | 11 | Doctype documentation generator (Markdown/PDF per doctype) |
| [FORM-023](../tasks/FORM/FORM-023.md) | P2 | 11 | Data dictionary export (all doctypes, fields, types, descriptions) |
| [FORM-024](../tasks/FORM/FORM-024.md) | P2 | 11 | Arabic label helper using TRNS glossary |
| [FORM-025](../tasks/FORM/FORM-025.md) | P2 | 11 | Customization test generator (creates a test doc through the customized form) |

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
