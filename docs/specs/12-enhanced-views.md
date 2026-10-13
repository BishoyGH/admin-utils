---
code: VIEW
title: "Enhanced Views (new, additive; core views untouched)"
number: 12
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/views/
frontend_path: frontend/src/features/views/
tasks: docs/tasks/VIEW/INDEX.md
---

# Spec 12 — Enhanced Views (new, additive; core views untouched) (`VIEW`)

## Purpose

Enhanced Views (new, additive; core views untouched): see feature groups below.

## Placement

- Python package: `admin_utils/views/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/views/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Enhanced Views (new, additive; core views untouched) Settings`; on/off flag `enable_views` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/views/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 9 |
| P1 | 44 |
| P2 | 27 |

Waves: wave 7 (53), wave 11 (27)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Engine

| ID | P | Wave | Task |
|---|---|---|---|
| [VIEW-001](../tasks/VIEW/VIEW-001.md) | P0 | 7 | `Enhanced View` doctype (doctype, view type, group/axis fields, card fields, filters, owner, shared with) |
| [VIEW-002](../tasks/VIEW/VIEW-002.md) | P0 | 7 | Generic view engine in the SPA reading any doctype via metadata |
| [VIEW-003](../tasks/VIEW/VIEW-003.md) | P0 | 7 | Respect permissions, User Permissions and field-level access in every query |
| [VIEW-004](../tasks/VIEW/VIEW-004.md) | P0 | 7 | Server-side filtering, sorting, pagination/virtualization |
| [VIEW-005](../tasks/VIEW/VIEW-005.md) | P0 | 7 | Saved views per user and shared views per role |
| [VIEW-006](../tasks/VIEW/VIEW-006.md) | P0 | 7 | Entry points: route `/manage/views/<doctype>/<view>` and optional links from workspaces |
| [VIEW-007](../tasks/VIEW/VIEW-007.md) | P1 | 7 | Quick filters bar and advanced filter builder |
| [VIEW-008](../tasks/VIEW/VIEW-008.md) | P1 | 7 | Realtime updates when records change |
| [VIEW-009](../tasks/VIEW/VIEW-009.md) | P1 | 7 | View config import/export JSON |
| [VIEW-010](../tasks/VIEW/VIEW-010.md) | P1 | 7 | Arabic/RTL support in all views |

### Enhanced Kanban

| ID | P | Wave | Task |
|---|---|---|---|
| [VIEW-011](../tasks/VIEW/VIEW-011.md) | P0 | 7 | Columns from any Select/Link field or workflow state |
| [VIEW-012](../tasks/VIEW/VIEW-012.md) | P0 | 7 | Drag-and-drop card move that updates the field (validated server-side) |
| [VIEW-013](../tasks/VIEW/VIEW-013.md) | P0 | 7 | Workflow-aware moves (only allowed transitions; blocked moves explain why) |
| [VIEW-014](../tasks/VIEW/VIEW-014.md) | P1 | 7 | Card templates (title, subtitle, badges, avatars, amounts, due dates) |
| [VIEW-015](../tasks/VIEW/VIEW-015.md) | P1 | 7 | WIP limits per column with warnings |
| [VIEW-016](../tasks/VIEW/VIEW-016.md) | P1 | 7 | Swimlanes (group by assignee/priority/customer) |
| [VIEW-017](../tasks/VIEW/VIEW-017.md) | P1 | 7 | Column totals (sum of a currency/number field) |
| [VIEW-018](../tasks/VIEW/VIEW-018.md) | P1 | 7 | Inline quick-create card per column |
| [VIEW-019](../tasks/VIEW/VIEW-019.md) | P1 | 7 | Card quick actions (assign, comment, tag, open) |
| [VIEW-020](../tasks/VIEW/VIEW-020.md) | P1 | 7 | Collapse/expand columns and hide empty columns |
| [VIEW-021](../tasks/VIEW/VIEW-021.md) | P1 | 7 | Color rules by condition (overdue, high value) |
| [VIEW-022](../tasks/VIEW/VIEW-022.md) | P2 | 11 | Card checklist and attachment previews |
| [VIEW-023](../tasks/VIEW/VIEW-023.md) | P2 | 11 | Column automation (on move, set field/assign/notify) |
| [VIEW-024](../tasks/VIEW/VIEW-024.md) | P2 | 11 | Archived column/lane handling |
| [VIEW-025](../tasks/VIEW/VIEW-025.md) | P2 | 11 | Keyboard navigation and bulk move |

### Other new views

| ID | P | Wave | Task |
|---|---|---|---|
| [VIEW-026](../tasks/VIEW/VIEW-026.md) | P1 | 7 | Table view with grouped rows, pinned columns, inline edit |
| [VIEW-027](../tasks/VIEW/VIEW-027.md) | P1 | 7 | Calendar view (month/week/day/agenda) with drag to reschedule |
| [VIEW-028](../tasks/VIEW/VIEW-028.md) | P1 | 7 | Timeline/Gantt view with dependencies from a link field |
| [VIEW-029](../tasks/VIEW/VIEW-029.md) | P1 | 7 | Gallery/cards view with image field |
| [VIEW-030](../tasks/VIEW/VIEW-030.md) | P1 | 7 | Tree view for hierarchical doctypes with drag re-parent |
| [VIEW-031](../tasks/VIEW/VIEW-031.md) | P1 | 7 | Map view (lat/lng fields; tiles allowlisted/configurable) |
| [VIEW-032](../tasks/VIEW/VIEW-032.md) | P1 | 7 | Pivot/summary view |
| [VIEW-033](../tasks/VIEW/VIEW-033.md) | P1 | 7 | Dashboard view combining charts and counters per doctype |
| [VIEW-034](../tasks/VIEW/VIEW-034.md) | P1 | 7 | Split view (list left, preview right) with keyboard navigation |
| [VIEW-035](../tasks/VIEW/VIEW-035.md) | P1 | 7 | Inbox/triage view for assigned or pending-approval documents |
| [VIEW-036](../tasks/VIEW/VIEW-036.md) | P2 | 11 | Workload view (assignee × time capacity) |
| [VIEW-037](../tasks/VIEW/VIEW-037.md) | P2 | 11 | Roadmap view by milestone/quarter |
| [VIEW-038](../tasks/VIEW/VIEW-038.md) | P2 | 11 | Matrix/heatmap view (two dimensions × measure) |
| [VIEW-039](../tasks/VIEW/VIEW-039.md) | P2 | 11 | Mobile-optimized card list with swipe actions |
| [VIEW-040](../tasks/VIEW/VIEW-040.md) | P2 | 11 | Presentation/TV mode (auto-refresh board for wall screens) |

### Shared capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [VIEW-041](../tasks/VIEW/VIEW-041.md) | P1 | 7 | Bulk select with actions (assign, tag, status change, export) |
| [VIEW-042](../tasks/VIEW/VIEW-042.md) | P1 | 7 | Export current view to CSV/XLSX/PDF/image |
| [VIEW-043](../tasks/VIEW/VIEW-043.md) | P1 | 7 | Print-friendly view layout |
| [VIEW-044](../tasks/VIEW/VIEW-044.md) | P1 | 7 | Grouping/sorting presets per view type |
| [VIEW-045](../tasks/VIEW/VIEW-045.md) | P2 | 11 | Subscriptions: notify when cards matching a filter change |
| [VIEW-046](../tasks/VIEW/VIEW-046.md) | P2 | 11 | Embed a view in a workspace block |
| [VIEW-047](../tasks/VIEW/VIEW-047.md) | P2 | 11 | Public read-only share link with expiry (opt-in, token based) |
| [VIEW-048](../tasks/VIEW/VIEW-048.md) | P2 | 11 | View templates per module (Sales pipeline, Support board, Task board) |
| [VIEW-049](../tasks/VIEW/VIEW-049.md) | P2 | 11 | Performance mode for 10k+ records (windowing, aggregation endpoints) |
| [VIEW-050](../tasks/VIEW/VIEW-050.md) | P2 | 11 | View usage analytics |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [VIEW-051](../tasks/VIEW/VIEW-051.md) | P1 | 7 | Kanban: card cover image/field and attachment thumbnails |
| [VIEW-052](../tasks/VIEW/VIEW-052.md) | P1 | 7 | Kanban: multiple card layouts (compact, detailed) per view |
| [VIEW-053](../tasks/VIEW/VIEW-053.md) | P1 | 7 | Kanban: column sorting rules (priority, due date, manual order persisted) |
| [VIEW-054](../tasks/VIEW/VIEW-054.md) | P1 | 7 | Kanban: persistent manual card ordering without altering core fields (own order table) |
| [VIEW-055](../tasks/VIEW/VIEW-055.md) | P1 | 7 | Kanban: filters pinned per board and per user |
| [VIEW-056](../tasks/VIEW/VIEW-056.md) | P1 | 7 | Kanban: board-level summary header (counts, totals, overdue) |
| [VIEW-057](../tasks/VIEW/VIEW-057.md) | P1 | 7 | Kanban: multi-select drag of several cards |
| [VIEW-058](../tasks/VIEW/VIEW-058.md) | P1 | 7 | Kanban: undo last move toast |
| [VIEW-059](../tasks/VIEW/VIEW-059.md) | P1 | 7 | Kanban: blocked-move reasons shown from validation errors |
| [VIEW-060](../tasks/VIEW/VIEW-060.md) | P2 | 11 | Kanban: card age indicators and stale highlighting |
| [VIEW-061](../tasks/VIEW/VIEW-061.md) | P2 | 11 | Kanban: column permissions (who can move into "Approved") |
| [VIEW-062](../tasks/VIEW/VIEW-062.md) | P2 | 11 | Kanban: sub-board linking (card opens a child board) |
| [VIEW-063](../tasks/VIEW/VIEW-063.md) | P2 | 11 | Kanban: burndown and cumulative flow charts |
| [VIEW-064](../tasks/VIEW/VIEW-064.md) | P2 | 11 | Kanban: SLA timers per column |
| [VIEW-065](../tasks/VIEW/VIEW-065.md) | P2 | 11 | Kanban: card templates per doctype shipped for Sales Order, Task, Issue, Lead, Opportunity |
| [VIEW-066](../tasks/VIEW/VIEW-066.md) | P1 | 7 | Calendar: multiple date fields (start/end) and all-day handling |
| [VIEW-067](../tasks/VIEW/VIEW-067.md) | P1 | 7 | Calendar: color by field or status, legend and toggles |
| [VIEW-068](../tasks/VIEW/VIEW-068.md) | P1 | 7 | Calendar: create document by selecting a time range |
| [VIEW-069](../tasks/VIEW/VIEW-069.md) | P2 | 11 | Calendar: resource view (rows = assignee/room/vehicle) |
| [VIEW-070](../tasks/VIEW/VIEW-070.md) | P2 | 11 | Calendar: holiday overlay and working-hours shading |
| [VIEW-071](../tasks/VIEW/VIEW-071.md) | P2 | 11 | Calendar: iCal read-only feed export (token protected) |
| [VIEW-072](../tasks/VIEW/VIEW-072.md) | P1 | 7 | Gantt: critical path highlighting and dependency lines |
| [VIEW-073](../tasks/VIEW/VIEW-073.md) | P1 | 7 | Gantt: baseline vs actual comparison |
| [VIEW-074](../tasks/VIEW/VIEW-074.md) | P2 | 11 | Gantt: zoom levels (day/week/month/quarter) and today marker |
| [VIEW-075](../tasks/VIEW/VIEW-075.md) | P1 | 7 | Table: saved column sets, frozen columns, row density |
| [VIEW-076](../tasks/VIEW/VIEW-076.md) | P1 | 7 | Table: bulk inline edit with validation and per-cell errors |
| [VIEW-077](../tasks/VIEW/VIEW-077.md) | P1 | 7 | Table: conditional row styling and icons |
| [VIEW-078](../tasks/VIEW/VIEW-078.md) | P1 | 7 | Table: group by with subtotals and collapse all |
| [VIEW-079](../tasks/VIEW/VIEW-079.md) | P2 | 11 | Table: formula columns (view-only, safe expressions) |
| [VIEW-080](../tasks/VIEW/VIEW-080.md) | P2 | 11 | Table: copy/paste from spreadsheets into rows with validation |

## Tests

- drag-drop e2e, permission-filtered result sets, workflow-blocked moves, virtualization performance test with 10k+ rows.
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
