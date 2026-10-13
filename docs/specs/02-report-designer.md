---
code: REPT
title: "No-Code Query/Script Report Designer"
number: 02
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/reports/
frontend_path: frontend/src/features/reports/
tasks: docs/tasks/REPT/INDEX.md
---

# Spec 02 — No-Code Query/Script Report Designer (`REPT`)

## Purpose

No-Code Query/Script Report Designer: see feature groups below.

## Placement

- Python package: `admin_utils/reports/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/reports/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `No-Code Query/Script Report Designer Settings`; on/off flag `enable_reports` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/reports/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 9 |
| P1 | 34 |
| P2 | 27 |

Waves: wave 5 (43), wave 11 (27)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [REPT-001](../tasks/REPT/REPT-001.md) | P0 | 5 | Report designer page with doctype picker and join builder |
| [REPT-002](../tasks/REPT/REPT-002.md) | P0 | 5 | Visual column picker with drag-and-drop ordering |
| [REPT-003](../tasks/REPT/REPT-003.md) | P0 | 5 | Filter builder (AND/OR groups, operators by field type) |
| [REPT-004](../tasks/REPT/REPT-004.md) | P0 | 5 | Sorting and group-by configuration |
| [REPT-005](../tasks/REPT/REPT-005.md) | P0 | 5 | Aggregations (sum, count, avg, min, max, distinct) |
| [REPT-006](../tasks/REPT/REPT-006.md) | P0 | 5 | Live preview with row limit and timing info |
| [REPT-007](../tasks/REPT/REPT-007.md) | P0 | 5 | Save as native Frappe Query Report (SQL) via supported fields only |
| [REPT-008](../tasks/REPT/REPT-008.md) | P0 | 5 | Save as Script Report scaffold with generated Python (read-only queries) |
| [REPT-009](../tasks/REPT/REPT-009.md) | P0 | 5 | Parameterized SQL generation (no string interpolation) |
| [REPT-010](../tasks/REPT/REPT-010.md) | P1 | 5 | Report filters designer (date range, link, select, multi-select, default values) |
| [REPT-011](../tasks/REPT/REPT-011.md) | P1 | 5 | Joins via Link fields auto-detected from doctype metadata |
| [REPT-012](../tasks/REPT/REPT-012.md) | P1 | 5 | Child table inclusion (flatten rows) |
| [REPT-013](../tasks/REPT/REPT-013.md) | P1 | 5 | Calculated columns with a safe expression language |
| [REPT-014](../tasks/REPT/REPT-014.md) | P1 | 5 | Conditional formatting rules (color, icon, bold) |
| [REPT-015](../tasks/REPT/REPT-015.md) | P1 | 5 | Totals row, subtotals and grouped rows |
| [REPT-016](../tasks/REPT/REPT-016.md) | P1 | 5 | Currency/number/date formatting per column |
| [REPT-017](../tasks/REPT/REPT-017.md) | P1 | 5 | Chart attachment (bar, line, pie, donut) with mapping UI |
| [REPT-018](../tasks/REPT/REPT-018.md) | P1 | 5 | Report access: roles assigned by level (links PERM-029) |
| [REPT-019](../tasks/REPT/REPT-019.md) | P1 | 5 | Query validator: only SELECT, no DDL/DML, no multiple statements |
| [REPT-020](../tasks/REPT/REPT-020.md) | P1 | 5 | Query cost estimator (EXPLAIN) with slow-query warning |
| [REPT-021](../tasks/REPT/REPT-021.md) | P1 | 5 | Column-level permission respect (hide permlevel-protected columns) |
| [REPT-022](../tasks/REPT/REPT-022.md) | P1 | 5 | Row-level security respect (User Permissions applied to generated query) |
| [REPT-023](../tasks/REPT/REPT-023.md) | P1 | 5 | Versioned report definitions with history and restore |
| [REPT-024](../tasks/REPT/REPT-024.md) | P1 | 5 | Clone report / clone standard report into custom editable copy |
| [REPT-025](../tasks/REPT/REPT-025.md) | P1 | 5 | Report templates gallery (AR aging, stock ledger, sales by item ...) |
| [REPT-026](../tasks/REPT/REPT-026.md) | P1 | 5 | Import/export report definition as JSON |
| [REPT-027](../tasks/REPT/REPT-027.md) | P1 | 5 | Raw SQL expert mode with syntax highlighting and schema sidebar |
| [REPT-028](../tasks/REPT/REPT-028.md) | P1 | 5 | Script report expert mode with sandboxed test run |
| [REPT-029](../tasks/REPT/REPT-029.md) | P2 | 11 | Scheduled report email (PDF/XLSX/CSV) via Auto Email Report integration |
| [REPT-030](../tasks/REPT/REPT-030.md) | P2 | 11 | Report parameters presets ("This month", "Last quarter") |
| [REPT-031](../tasks/REPT/REPT-031.md) | P2 | 11 | Drill-down links from rows to documents/other reports |
| [REPT-032](../tasks/REPT/REPT-032.md) | P2 | 11 | Pivot mode |
| [REPT-033](../tasks/REPT/REPT-033.md) | P2 | 11 | Report dependency map (which reports use which doctypes/fields) |
| [REPT-034](../tasks/REPT/REPT-034.md) | P2 | 11 | Breaking-change detector when a field used by a report is removed/renamed |
| [REPT-035](../tasks/REPT/REPT-035.md) | P2 | 11 | Report usage analytics (runs, users, avg time) |
| [REPT-036](../tasks/REPT/REPT-036.md) | P2 | 11 | Unused/slow report cleanup suggestions |
| [REPT-037](../tasks/REPT/REPT-037.md) | P2 | 11 | Arabic column labels and RTL print format |
| [REPT-038](../tasks/REPT/REPT-038.md) | P2 | 11 | Print/PDF layout designer for the report |
| [REPT-039](../tasks/REPT/REPT-039.md) | P2 | 11 | Share report via link with role-based access |
| [REPT-040](../tasks/REPT/REPT-040.md) | P2 | 11 | Report favorites and categories |
| [REPT-041](../tasks/REPT/REPT-041.md) | P2 | 11 | Report comments and annotations |
| [REPT-042](../tasks/REPT/REPT-042.md) | P2 | 11 | Test-data run against seeded dataset (links DATA module) |
| [REPT-043](../tasks/REPT/REPT-043.md) | P2 | 11 | Audit trail of who ran which report with which filters |
| [REPT-044](../tasks/REPT/REPT-044.md) | P2 | 11 | Export history and download log |
| [REPT-045](../tasks/REPT/REPT-045.md) | P2 | 11 | Report diff between two versions |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [REPT-046](../tasks/REPT/REPT-046.md) | P1 | 5 | Visual relationship diagram of tables used in the report |
| [REPT-047](../tasks/REPT/REPT-047.md) | P1 | 5 | Suggested joins ranking by cardinality and index availability |
| [REPT-048](../tasks/REPT/REPT-048.md) | P1 | 5 | Derived datasets (reusable sub-queries) shared across reports |
| [REPT-049](../tasks/REPT/REPT-049.md) | P1 | 5 | Column dictionary (business names, descriptions) shown in the designer |
| [REPT-050](../tasks/REPT/REPT-050.md) | P1 | 5 | Parameter types: date presets, multi-company, fiscal year, cost center tree |
| [REPT-051](../tasks/REPT/REPT-051.md) | P1 | 5 | Report-level default filters per role |
| [REPT-052](../tasks/REPT/REPT-052.md) | P1 | 5 | Prepared/cached results for heavy reports with refresh schedule |
| [REPT-053](../tasks/REPT/REPT-053.md) | P1 | 5 | Cache invalidation hints (dependent doctypes changed) |
| [REPT-054](../tasks/REPT/REPT-054.md) | P1 | 5 | Running-total and rank window-style calculations (done safely in Python) |
| [REPT-055](../tasks/REPT/REPT-055.md) | P1 | 5 | Period-over-period comparison columns (MoM, YoY) |
| [REPT-056](../tasks/REPT/REPT-056.md) | P1 | 5 | Budget vs actual helper template |
| [REPT-057](../tasks/REPT/REPT-057.md) | P1 | 5 | Aging bucket builder (30/60/90 configurable) |
| [REPT-058](../tasks/REPT/REPT-058.md) | P1 | 5 | Hierarchical report with expand/collapse (accounts, item groups) |
| [REPT-059](../tasks/REPT/REPT-059.md) | P1 | 5 | Multi-currency conversion options with rate date choice |
| [REPT-060](../tasks/REPT/REPT-060.md) | P1 | 5 | Null/zero handling rules and "hide empty rows" |
| [REPT-061](../tasks/REPT/REPT-061.md) | P2 | 11 | Report builder from natural-language description (assistive, reviewed before save) |
| [REPT-062](../tasks/REPT/REPT-062.md) | P2 | 11 | Explain query in plain language |
| [REPT-063](../tasks/REPT/REPT-063.md) | P2 | 11 | Test report against fixtures with expected output assertions |
| [REPT-064](../tasks/REPT/REPT-064.md) | P2 | 11 | Regression snapshots of report output across app upgrades |
| [REPT-065](../tasks/REPT/REPT-065.md) | P2 | 11 | Report bundles (package several reports + workspace + permissions) |
| [REPT-066](../tasks/REPT/REPT-066.md) | P2 | 11 | Subscription: user subscribes to a report with filters and frequency |
| [REPT-067](../tasks/REPT/REPT-067.md) | P2 | 11 | Threshold alerts on report totals |
| [REPT-068](../tasks/REPT/REPT-068.md) | P2 | 11 | Embed report result as a number card or chart on a workspace |
| [REPT-069](../tasks/REPT/REPT-069.md) | P2 | 11 | Report translations scoped via TRNS |
| [REPT-070](../tasks/REPT/REPT-070.md) | P2 | 11 | Execution quotas per role to protect the database |

## Tests

- generated SQL is parameterized; non-SELECT rejected; row- and column-level security respected; round trip designer → saved report → run.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Large-data performance: server-side pagination, aggregation endpoints, perf budgets

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
