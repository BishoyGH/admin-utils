---
code: IMEX
title: "Import / Export Center"
number: 19
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/importexport/
frontend_path: frontend/src/features/importexport/
tasks: docs/tasks/IMEX/INDEX.md
---

# Spec 19 — Import / Export Center (`IMEX`)

## Purpose

Import / Export Center: see feature groups below.

## Placement

- Python package: `admin_utils/importexport/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/importexport/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Import / Export Center Settings`; on/off flag `enable_importexport` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/importexport/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 4 |
| P1 | 10 |
| P2 | 6 |

Waves: wave 5 (14), wave 11 (6)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [IMEX-001](../tasks/IMEX/IMEX-001.md) | P0 | 5 | Unified import wizard (upload → map → validate → dry-run → import → report) |
| [IMEX-002](../tasks/IMEX/IMEX-002.md) | P0 | 5 | Template generator for any doctype with example rows |
| [IMEX-003](../tasks/IMEX/IMEX-003.md) | P0 | 5 | Column mapping with fuzzy matching and saved mappings |
| [IMEX-004](../tasks/IMEX/IMEX-004.md) | P0 | 5 | Row-level validation report with downloadable error file |
| [IMEX-005](../tasks/IMEX/IMEX-005.md) | P1 | 5 | Support CSV, XLSX and JSON with encoding detection (UTF-8/Windows-1256) |
| [IMEX-006](../tasks/IMEX/IMEX-006.md) | P1 | 5 | Arabic digit normalization and whitespace cleanup options |
| [IMEX-007](../tasks/IMEX/IMEX-007.md) | P1 | 5 | Link-field resolution by name, code, or alternate key |
| [IMEX-008](../tasks/IMEX/IMEX-008.md) | P1 | 5 | Duplicate handling modes (skip, update, error) |
| [IMEX-009](../tasks/IMEX/IMEX-009.md) | P1 | 5 | Child table import in same file (grouped rows) |
| [IMEX-010](../tasks/IMEX/IMEX-010.md) | P1 | 5 | Chunked background import with resume after failure |
| [IMEX-011](../tasks/IMEX/IMEX-011.md) | P1 | 5 | Import batches tagged and reversible where possible |
| [IMEX-012](../tasks/IMEX/IMEX-012.md) | P1 | 5 | Scheduled imports from approved folder/URL with allowlist |
| [IMEX-013](../tasks/IMEX/IMEX-013.md) | P1 | 5 | Bulk export with column selection, filters and format options |
| [IMEX-014](../tasks/IMEX/IMEX-014.md) | P1 | 5 | Export templates per role (e.g. accountants' invoice export) |
| [IMEX-015](../tasks/IMEX/IMEX-015.md) | P2 | 11 | Cross-site migration pack (export doctypes + data + customizations) |
| [IMEX-016](../tasks/IMEX/IMEX-016.md) | P2 | 11 | Data diff before import (what will change) |
| [IMEX-017](../tasks/IMEX/IMEX-017.md) | P2 | 11 | Large file streaming and memory guard |
| [IMEX-018](../tasks/IMEX/IMEX-018.md) | P2 | 11 | Import from other ERPs mapping presets (generic CSV profiles) |
| [IMEX-019](../tasks/IMEX/IMEX-019.md) | P2 | 11 | Export encryption (password-protected archive) for sensitive data |
| [IMEX-020](../tasks/IMEX/IMEX-020.md) | P2 | 11 | Import/export audit and retention policy |

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
