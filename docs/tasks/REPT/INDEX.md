# REPT — No-Code Query/Script Report Designer: tasks

Spec: [`02-report-designer.md`](../../specs/02-report-designer.md) · 70 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [REPT-001](REPT-001.md) | P0 | 5 | todo | Report designer page with doctype picker and join builder |
| [REPT-002](REPT-002.md) | P0 | 5 | todo | Visual column picker with drag-and-drop ordering |
| [REPT-003](REPT-003.md) | P0 | 5 | todo | Filter builder (AND/OR groups, operators by field type) |
| [REPT-004](REPT-004.md) | P0 | 5 | todo | Sorting and group-by configuration |
| [REPT-005](REPT-005.md) | P0 | 5 | todo | Aggregations (sum, count, avg, min, max, distinct) |
| [REPT-006](REPT-006.md) | P0 | 5 | todo | Live preview with row limit and timing info |
| [REPT-007](REPT-007.md) | P0 | 5 | todo | Save as native Frappe Query Report (SQL) via supported fields only |
| [REPT-008](REPT-008.md) | P0 | 5 | todo | Save as Script Report scaffold with generated Python (read-only queries) |
| [REPT-009](REPT-009.md) | P0 | 5 | todo | Parameterized SQL generation (no string interpolation) |
| [REPT-010](REPT-010.md) | P1 | 5 | todo | Report filters designer (date range, link, select, multi-select, default values) |
| [REPT-011](REPT-011.md) | P1 | 5 | todo | Joins via Link fields auto-detected from doctype metadata |
| [REPT-012](REPT-012.md) | P1 | 5 | todo | Child table inclusion (flatten rows) |
| [REPT-013](REPT-013.md) | P1 | 5 | todo | Calculated columns with a safe expression language |
| [REPT-014](REPT-014.md) | P1 | 5 | todo | Conditional formatting rules (color, icon, bold) |
| [REPT-015](REPT-015.md) | P1 | 5 | todo | Totals row, subtotals and grouped rows |
| [REPT-016](REPT-016.md) | P1 | 5 | todo | Currency/number/date formatting per column |
| [REPT-017](REPT-017.md) | P1 | 5 | todo | Chart attachment (bar, line, pie, donut) with mapping UI |
| [REPT-018](REPT-018.md) | P1 | 5 | todo | Report access: roles assigned by level (links PERM-029) |
| [REPT-019](REPT-019.md) | P1 | 5 | todo | Query validator: only SELECT, no DDL/DML, no multiple statements |
| [REPT-020](REPT-020.md) | P1 | 5 | todo | Query cost estimator (EXPLAIN) with slow-query warning |
| [REPT-021](REPT-021.md) | P1 | 5 | todo | Column-level permission respect (hide permlevel-protected columns) |
| [REPT-022](REPT-022.md) | P1 | 5 | todo | Row-level security respect (User Permissions applied to generated query) |
| [REPT-023](REPT-023.md) | P1 | 5 | todo | Versioned report definitions with history and restore |
| [REPT-024](REPT-024.md) | P1 | 5 | todo | Clone report / clone standard report into custom editable copy |
| [REPT-025](REPT-025.md) | P1 | 5 | todo | Report templates gallery (AR aging, stock ledger, sales by item ...) |
| [REPT-026](REPT-026.md) | P1 | 5 | todo | Import/export report definition as JSON |
| [REPT-027](REPT-027.md) | P1 | 5 | todo | Raw SQL expert mode with syntax highlighting and schema sidebar |
| [REPT-028](REPT-028.md) | P1 | 5 | todo | Script report expert mode with sandboxed test run |
| [REPT-029](REPT-029.md) | P2 | 11 | todo | Scheduled report email (PDF/XLSX/CSV) via Auto Email Report integration |
| [REPT-030](REPT-030.md) | P2 | 11 | todo | Report parameters presets ("This month", "Last quarter") |
| [REPT-031](REPT-031.md) | P2 | 11 | todo | Drill-down links from rows to documents/other reports |
| [REPT-032](REPT-032.md) | P2 | 11 | todo | Pivot mode |
| [REPT-033](REPT-033.md) | P2 | 11 | todo | Report dependency map (which reports use which doctypes/fields) |
| [REPT-034](REPT-034.md) | P2 | 11 | todo | Breaking-change detector when a field used by a report is removed/renamed |
| [REPT-035](REPT-035.md) | P2 | 11 | todo | Report usage analytics (runs, users, avg time) |
| [REPT-036](REPT-036.md) | P2 | 11 | todo | Unused/slow report cleanup suggestions |
| [REPT-037](REPT-037.md) | P2 | 11 | todo | Arabic column labels and RTL print format |
| [REPT-038](REPT-038.md) | P2 | 11 | todo | Print/PDF layout designer for the report |
| [REPT-039](REPT-039.md) | P2 | 11 | todo | Share report via link with role-based access |
| [REPT-040](REPT-040.md) | P2 | 11 | todo | Report favorites and categories |
| [REPT-041](REPT-041.md) | P2 | 11 | todo | Report comments and annotations |
| [REPT-042](REPT-042.md) | P2 | 11 | todo | Test-data run against seeded dataset (links DATA module) |
| [REPT-043](REPT-043.md) | P2 | 11 | todo | Audit trail of who ran which report with which filters |
| [REPT-044](REPT-044.md) | P2 | 11 | todo | Export history and download log |
| [REPT-045](REPT-045.md) | P2 | 11 | todo | Report diff between two versions |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [REPT-046](REPT-046.md) | P1 | 5 | todo | Visual relationship diagram of tables used in the report |
| [REPT-047](REPT-047.md) | P1 | 5 | todo | Suggested joins ranking by cardinality and index availability |
| [REPT-048](REPT-048.md) | P1 | 5 | todo | Derived datasets (reusable sub-queries) shared across reports |
| [REPT-049](REPT-049.md) | P1 | 5 | todo | Column dictionary (business names, descriptions) shown in the designer |
| [REPT-050](REPT-050.md) | P1 | 5 | todo | Parameter types: date presets, multi-company, fiscal year, cost center tree |
| [REPT-051](REPT-051.md) | P1 | 5 | todo | Report-level default filters per role |
| [REPT-052](REPT-052.md) | P1 | 5 | todo | Prepared/cached results for heavy reports with refresh schedule |
| [REPT-053](REPT-053.md) | P1 | 5 | todo | Cache invalidation hints (dependent doctypes changed) |
| [REPT-054](REPT-054.md) | P1 | 5 | todo | Running-total and rank window-style calculations (done safely in Python) |
| [REPT-055](REPT-055.md) | P1 | 5 | todo | Period-over-period comparison columns (MoM, YoY) |
| [REPT-056](REPT-056.md) | P1 | 5 | todo | Budget vs actual helper template |
| [REPT-057](REPT-057.md) | P1 | 5 | todo | Aging bucket builder (30/60/90 configurable) |
| [REPT-058](REPT-058.md) | P1 | 5 | todo | Hierarchical report with expand/collapse (accounts, item groups) |
| [REPT-059](REPT-059.md) | P1 | 5 | todo | Multi-currency conversion options with rate date choice |
| [REPT-060](REPT-060.md) | P1 | 5 | todo | Null/zero handling rules and "hide empty rows" |
| [REPT-061](REPT-061.md) | P2 | 11 | todo | Report builder from natural-language description (assistive, reviewed before save) |
| [REPT-062](REPT-062.md) | P2 | 11 | todo | Explain query in plain language |
| [REPT-063](REPT-063.md) | P2 | 11 | todo | Test report against fixtures with expected output assertions |
| [REPT-064](REPT-064.md) | P2 | 11 | todo | Regression snapshots of report output across app upgrades |
| [REPT-065](REPT-065.md) | P2 | 11 | todo | Report bundles (package several reports + workspace + permissions) |
| [REPT-066](REPT-066.md) | P2 | 11 | todo | Subscription: user subscribes to a report with filters and frequency |
| [REPT-067](REPT-067.md) | P2 | 11 | todo | Threshold alerts on report totals |
| [REPT-068](REPT-068.md) | P2 | 11 | todo | Embed report result as a number card or chart on a workspace |
| [REPT-069](REPT-069.md) | P2 | 11 | todo | Report translations scoped via TRNS |
| [REPT-070](REPT-070.md) | P2 | 11 | todo | Execution quotas per role to protect the database |
