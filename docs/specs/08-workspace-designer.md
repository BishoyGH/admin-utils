---
code: WKSP
title: "Workspace Designer"
number: 08
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/workspaces/
frontend_path: frontend/src/features/workspaces/
tasks: docs/tasks/WKSP/INDEX.md
---

# Spec 08 — Workspace Designer (`WKSP`)

## Purpose

Workspace Designer: see feature groups below.

## Placement

- Python package: `admin_utils/workspaces/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/workspaces/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Workspace Designer Settings`; on/off flag `enable_workspaces` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/workspaces/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 9 |
| P1 | 23 |
| P2 | 18 |

Waves: wave 5 (32), wave 11 (18)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [WKSP-001](../tasks/WKSP/WKSP-001.md) | P0 | 5 | Visual workspace designer for Workspace doctype (v15/v16 schemas via compat layer) |
| [WKSP-002](../tasks/WKSP/WKSP-002.md) | P0 | 5 | Block library: header, paragraph, shortcut, card, chart, number card, spacer, onboarding, quick list |
| [WKSP-003](../tasks/WKSP/WKSP-003.md) | P0 | 5 | Drag-and-drop layout with grid snapping |
| [WKSP-004](../tasks/WKSP/WKSP-004.md) | P0 | 5 | Block property inspector |
| [WKSP-005](../tasks/WKSP/WKSP-005.md) | P0 | 5 | Live preview (desktop/tablet/mobile widths) |
| [WKSP-006](../tasks/WKSP/WKSP-006.md) | P0 | 5 | Save as public/private workspace |
| [WKSP-007](../tasks/WKSP/WKSP-007.md) | P0 | 5 | Role-based visibility per workspace and per block |
| [WKSP-008](../tasks/WKSP/WKSP-008.md) | P0 | 5 | Duplicate workspace and version history |
| [WKSP-009](../tasks/WKSP/WKSP-009.md) | P0 | 5 | Validation of links (doctype/report/page exist, user has access) |
| [WKSP-010](../tasks/WKSP/WKSP-010.md) | P1 | 5 | Ready-made block bundles ("Sales overview", "Stock health", "HR today", "Accounts snapshot") |
| [WKSP-011](../tasks/WKSP/WKSP-011.md) | P1 | 5 | Workspace templates per role (CEO, Accountant, Warehouse, HR) |
| [WKSP-012](../tasks/WKSP/WKSP-012.md) | P1 | 5 | Shortcut builder with icon picker and counts |
| [WKSP-013](../tasks/WKSP/WKSP-013.md) | P1 | 5 | Number Card designer (function, filters, color thresholds) |
| [WKSP-014](../tasks/WKSP/WKSP-014.md) | P1 | 5 | Dashboard Chart designer (source report/doctype, group-by, time series) |
| [WKSP-015](../tasks/WKSP/WKSP-015.md) | P1 | 5 | Custom HTML block with sanitization (allowlist tags) |
| [WKSP-016](../tasks/WKSP/WKSP-016.md) | P1 | 5 | Sidebar/section organization and ordering |
| [WKSP-017](../tasks/WKSP/WKSP-017.md) | P1 | 5 | Link cards grouped by module with auto-generation from doctype list |
| [WKSP-018](../tasks/WKSP/WKSP-018.md) | P1 | 5 | Arabic labels and RTL preview |
| [WKSP-019](../tasks/WKSP/WKSP-019.md) | P1 | 5 | Import/export workspace JSON |
| [WKSP-020](../tasks/WKSP/WKSP-020.md) | P1 | 5 | Bulk apply a template to multiple roles |
| [WKSP-021](../tasks/WKSP/WKSP-021.md) | P1 | 5 | Broken-block detector after app upgrades |
| [WKSP-022](../tasks/WKSP/WKSP-022.md) | P1 | 5 | Restore to standard (module default) workspace |
| [WKSP-023](../tasks/WKSP/WKSP-023.md) | P1 | 5 | Undo/redo in designer |
| [WKSP-024](../tasks/WKSP/WKSP-024.md) | P1 | 5 | Autosave drafts with unsaved-changes guard |
| [WKSP-025](../tasks/WKSP/WKSP-025.md) | P2 | 11 | Conditional blocks (show if value > threshold) |
| [WKSP-026](../tasks/WKSP/WKSP-026.md) | P2 | 11 | Embedded report/list preview blocks |
| [WKSP-027](../tasks/WKSP/WKSP-027.md) | P2 | 11 | Personal workspace per user (self-service, limited blocks) |
| [WKSP-028](../tasks/WKSP/WKSP-028.md) | P2 | 11 | Workspace usage analytics (clicks per block) |
| [WKSP-029](../tasks/WKSP/WKSP-029.md) | P2 | 11 | A/B variants of a workspace |
| [WKSP-030](../tasks/WKSP/WKSP-030.md) | P2 | 11 | Onboarding block integration (ONBD) |
| [WKSP-031](../tasks/WKSP/WKSP-031.md) | P2 | 11 | Pinned announcements block with expiry |
| [WKSP-032](../tasks/WKSP/WKSP-032.md) | P2 | 11 | Block marketplace/community import (signed bundles) |
| [WKSP-033](../tasks/WKSP/WKSP-033.md) | P2 | 11 | Accessibility checker (alt text, contrast, order) |
| [WKSP-034](../tasks/WKSP/WKSP-034.md) | P2 | 11 | Screenshot snapshot for documentation |
| [WKSP-035](../tasks/WKSP/WKSP-035.md) | P2 | 11 | Schema migration helper v15 ↔ v16 for exported workspaces |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [WKSP-036](../tasks/WKSP/WKSP-036.md) | P1 | 5 | Block grouping and collapsible sections |
| [WKSP-037](../tasks/WKSP/WKSP-037.md) | P1 | 5 | Global filters shared across blocks (company, period) |
| [WKSP-038](../tasks/WKSP/WKSP-038.md) | P1 | 5 | Auto-refresh intervals per block |
| [WKSP-039](../tasks/WKSP/WKSP-039.md) | P1 | 5 | Block-level loading/error states and fallbacks |
| [WKSP-040](../tasks/WKSP/WKSP-040.md) | P1 | 5 | Link validation scheduler (nightly broken-link report) |
| [WKSP-041](../tasks/WKSP/WKSP-041.md) | P1 | 5 | Mobile layout editor distinct from desktop layout |
| [WKSP-042](../tasks/WKSP/WKSP-042.md) | P1 | 5 | Workspace-to-role assignment matrix |
| [WKSP-043](../tasks/WKSP/WKSP-043.md) | P1 | 5 | Default landing workspace per role |
| [WKSP-044](../tasks/WKSP/WKSP-044.md) | P2 | 11 | Drill-through from chart point to filtered list |
| [WKSP-045](../tasks/WKSP/WKSP-045.md) | P2 | 11 | Threshold-based number card coloring and sparkline |
| [WKSP-046](../tasks/WKSP/WKSP-046.md) | P2 | 11 | Reusable block presets saved by users |
| [WKSP-047](../tasks/WKSP/WKSP-047.md) | P2 | 11 | Workspace changelog with author and reason |
| [WKSP-048](../tasks/WKSP/WKSP-048.md) | P2 | 11 | Comments on blocks for team feedback in design mode |
| [WKSP-049](../tasks/WKSP/WKSP-049.md) | P2 | 11 | Import from existing standard workspace with clean-up wizard |
| [WKSP-050](../tasks/WKSP/WKSP-050.md) | P2 | 11 | Bulk rename/relabel of shortcuts for a language |

## Tests

- v15/v16 schema compat fixtures, broken-link detection.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- v15/v16 schema divergence (workspace schema): compat layer and fixtures

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
