---
code: PRNT
title: "Print Format & Document Output Designer"
number: 18
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/printing/
frontend_path: frontend/src/features/printing/
tasks: docs/tasks/PRNT/INDEX.md
---

# Spec 18 — Print Format & Document Output Designer (`PRNT`)

## Purpose

Print Format & Document Output Designer: see feature groups below.

## Placement

- Python package: `admin_utils/printing/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/printing/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Print Format & Document Output Designer Settings`; on/off flag `enable_printing` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/printing/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 1 |
| P1 | 14 |
| P2 | 10 |

Waves: wave 5 (15), wave 11 (10)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [PRNT-001](../tasks/PRNT/PRNT-001.md) | P0 | 5 | Print format gallery with live preview from real or seeded documents |
| [PRNT-002](../tasks/PRNT/PRNT-002.md) | P1 | 5 | Visual print layout builder (header, body table, totals, footer) |
| [PRNT-003](../tasks/PRNT/PRNT-003.md) | P1 | 5 | Brand tokens integration (logo, colors, fonts from THEM) |
| [PRNT-004](../tasks/PRNT/PRNT-004.md) | P1 | 5 | Arabic/RTL and bilingual print templates |
| [PRNT-005](../tasks/PRNT/PRNT-005.md) | P1 | 5 | Page size, margins, orientation presets (A4, A5, thermal 80mm) |
| [PRNT-006](../tasks/PRNT/PRNT-006.md) | P1 | 5 | Thermal receipt template builder for POS |
| [PRNT-007](../tasks/PRNT/PRNT-007.md) | P1 | 5 | Barcode and QR block with validated payloads |
| [PRNT-008](../tasks/PRNT/PRNT-008.md) | P1 | 5 | Conditional sections (show if field/value) |
| [PRNT-009](../tasks/PRNT/PRNT-009.md) | P1 | 5 | Child table styling (column widths, number formats, zebra rows) |
| [PRNT-010](../tasks/PRNT/PRNT-010.md) | P1 | 5 | Totals and tax summary block generator |
| [PRNT-011](../tasks/PRNT/PRNT-011.md) | P1 | 5 | Amount-in-words helper (English and Arabic) |
| [PRNT-012](../tasks/PRNT/PRNT-012.md) | P1 | 5 | Signature and stamp blocks |
| [PRNT-013](../tasks/PRNT/PRNT-013.md) | P1 | 5 | Letterhead manager with preview |
| [PRNT-014](../tasks/PRNT/PRNT-014.md) | P1 | 5 | Print format validation (missing fields, overflow, broken Jinja) |
| [PRNT-015](../tasks/PRNT/PRNT-015.md) | P1 | 5 | PDF generation test runner with page count and size checks |
| [PRNT-016](../tasks/PRNT/PRNT-016.md) | P2 | 11 | Template variables browser (fields available per doctype) |
| [PRNT-017](../tasks/PRNT/PRNT-017.md) | P2 | 11 | Safe Jinja snippet library with sandbox preview |
| [PRNT-018](../tasks/PRNT/PRNT-018.md) | P2 | 11 | Print format version history and restore |
| [PRNT-019](../tasks/PRNT/PRNT-019.md) | P2 | 11 | Clone standard print format into editable custom copy |
| [PRNT-020](../tasks/PRNT/PRNT-020.md) | P2 | 11 | Bulk assign default print format per doctype/role |
| [PRNT-021](../tasks/PRNT/PRNT-021.md) | P2 | 11 | Watermark options (DRAFT, COPY, CANCELLED) driven by docstatus |
| [PRNT-022](../tasks/PRNT/PRNT-022.md) | P2 | 11 | Visual regression snapshots of print outputs |
| [PRNT-023](../tasks/PRNT/PRNT-023.md) | P2 | 11 | Email body template designer shared with print styling |
| [PRNT-024](../tasks/PRNT/PRNT-024.md) | P2 | 11 | Multi-copy printing rules (customer, accounts, warehouse) |
| [PRNT-025](../tasks/PRNT/PRNT-025.md) | P2 | 11 | Print usage analytics |

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
