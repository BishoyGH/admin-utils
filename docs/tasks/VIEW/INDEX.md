# VIEW — Enhanced Views (new, additive; core views untouched): tasks

Spec: [`12-enhanced-views.md`](../../specs/12-enhanced-views.md) · 80 tasks · done 0


## Engine

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [VIEW-001](VIEW-001.md) | P0 | 7 | todo | `Enhanced View` doctype (doctype, view type, group/axis fields, card fields, filters, owner, shared with) |
| [VIEW-002](VIEW-002.md) | P0 | 7 | todo | Generic view engine in the SPA reading any doctype via metadata |
| [VIEW-003](VIEW-003.md) | P0 | 7 | todo | Respect permissions, User Permissions and field-level access in every query |
| [VIEW-004](VIEW-004.md) | P0 | 7 | todo | Server-side filtering, sorting, pagination/virtualization |
| [VIEW-005](VIEW-005.md) | P0 | 7 | todo | Saved views per user and shared views per role |
| [VIEW-006](VIEW-006.md) | P0 | 7 | todo | Entry points: route `/manage/views/<doctype>/<view>` and optional links from workspaces |
| [VIEW-007](VIEW-007.md) | P1 | 7 | todo | Quick filters bar and advanced filter builder |
| [VIEW-008](VIEW-008.md) | P1 | 7 | todo | Realtime updates when records change |
| [VIEW-009](VIEW-009.md) | P1 | 7 | todo | View config import/export JSON |
| [VIEW-010](VIEW-010.md) | P1 | 7 | todo | Arabic/RTL support in all views |

## Enhanced Kanban

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [VIEW-011](VIEW-011.md) | P0 | 7 | todo | Columns from any Select/Link field or workflow state |
| [VIEW-012](VIEW-012.md) | P0 | 7 | todo | Drag-and-drop card move that updates the field (validated server-side) |
| [VIEW-013](VIEW-013.md) | P0 | 7 | todo | Workflow-aware moves (only allowed transitions; blocked moves explain why) |
| [VIEW-014](VIEW-014.md) | P1 | 7 | todo | Card templates (title, subtitle, badges, avatars, amounts, due dates) |
| [VIEW-015](VIEW-015.md) | P1 | 7 | todo | WIP limits per column with warnings |
| [VIEW-016](VIEW-016.md) | P1 | 7 | todo | Swimlanes (group by assignee/priority/customer) |
| [VIEW-017](VIEW-017.md) | P1 | 7 | todo | Column totals (sum of a currency/number field) |
| [VIEW-018](VIEW-018.md) | P1 | 7 | todo | Inline quick-create card per column |
| [VIEW-019](VIEW-019.md) | P1 | 7 | todo | Card quick actions (assign, comment, tag, open) |
| [VIEW-020](VIEW-020.md) | P1 | 7 | todo | Collapse/expand columns and hide empty columns |
| [VIEW-021](VIEW-021.md) | P1 | 7 | todo | Color rules by condition (overdue, high value) |
| [VIEW-022](VIEW-022.md) | P2 | 11 | todo | Card checklist and attachment previews |
| [VIEW-023](VIEW-023.md) | P2 | 11 | todo | Column automation (on move, set field/assign/notify) |
| [VIEW-024](VIEW-024.md) | P2 | 11 | todo | Archived column/lane handling |
| [VIEW-025](VIEW-025.md) | P2 | 11 | todo | Keyboard navigation and bulk move |

## Other new views

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [VIEW-026](VIEW-026.md) | P1 | 7 | todo | Table view with grouped rows, pinned columns, inline edit |
| [VIEW-027](VIEW-027.md) | P1 | 7 | todo | Calendar view (month/week/day/agenda) with drag to reschedule |
| [VIEW-028](VIEW-028.md) | P1 | 7 | todo | Timeline/Gantt view with dependencies from a link field |
| [VIEW-029](VIEW-029.md) | P1 | 7 | todo | Gallery/cards view with image field |
| [VIEW-030](VIEW-030.md) | P1 | 7 | todo | Tree view for hierarchical doctypes with drag re-parent |
| [VIEW-031](VIEW-031.md) | P1 | 7 | todo | Map view (lat/lng fields; tiles allowlisted/configurable) |
| [VIEW-032](VIEW-032.md) | P1 | 7 | todo | Pivot/summary view |
| [VIEW-033](VIEW-033.md) | P1 | 7 | todo | Dashboard view combining charts and counters per doctype |
| [VIEW-034](VIEW-034.md) | P1 | 7 | todo | Split view (list left, preview right) with keyboard navigation |
| [VIEW-035](VIEW-035.md) | P1 | 7 | todo | Inbox/triage view for assigned or pending-approval documents |
| [VIEW-036](VIEW-036.md) | P2 | 11 | todo | Workload view (assignee × time capacity) |
| [VIEW-037](VIEW-037.md) | P2 | 11 | todo | Roadmap view by milestone/quarter |
| [VIEW-038](VIEW-038.md) | P2 | 11 | todo | Matrix/heatmap view (two dimensions × measure) |
| [VIEW-039](VIEW-039.md) | P2 | 11 | todo | Mobile-optimized card list with swipe actions |
| [VIEW-040](VIEW-040.md) | P2 | 11 | todo | Presentation/TV mode (auto-refresh board for wall screens) |

## Shared capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [VIEW-041](VIEW-041.md) | P1 | 7 | todo | Bulk select with actions (assign, tag, status change, export) |
| [VIEW-042](VIEW-042.md) | P1 | 7 | todo | Export current view to CSV/XLSX/PDF/image |
| [VIEW-043](VIEW-043.md) | P1 | 7 | todo | Print-friendly view layout |
| [VIEW-044](VIEW-044.md) | P1 | 7 | todo | Grouping/sorting presets per view type |
| [VIEW-045](VIEW-045.md) | P2 | 11 | todo | Subscriptions: notify when cards matching a filter change |
| [VIEW-046](VIEW-046.md) | P2 | 11 | todo | Embed a view in a workspace block |
| [VIEW-047](VIEW-047.md) | P2 | 11 | todo | Public read-only share link with expiry (opt-in, token based) |
| [VIEW-048](VIEW-048.md) | P2 | 11 | todo | View templates per module (Sales pipeline, Support board, Task board) |
| [VIEW-049](VIEW-049.md) | P2 | 11 | todo | Performance mode for 10k+ records (windowing, aggregation endpoints) |
| [VIEW-050](VIEW-050.md) | P2 | 11 | todo | View usage analytics |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [VIEW-051](VIEW-051.md) | P1 | 7 | todo | Kanban: card cover image/field and attachment thumbnails |
| [VIEW-052](VIEW-052.md) | P1 | 7 | todo | Kanban: multiple card layouts (compact, detailed) per view |
| [VIEW-053](VIEW-053.md) | P1 | 7 | todo | Kanban: column sorting rules (priority, due date, manual order persisted) |
| [VIEW-054](VIEW-054.md) | P1 | 7 | todo | Kanban: persistent manual card ordering without altering core fields (own order table) |
| [VIEW-055](VIEW-055.md) | P1 | 7 | todo | Kanban: filters pinned per board and per user |
| [VIEW-056](VIEW-056.md) | P1 | 7 | todo | Kanban: board-level summary header (counts, totals, overdue) |
| [VIEW-057](VIEW-057.md) | P1 | 7 | todo | Kanban: multi-select drag of several cards |
| [VIEW-058](VIEW-058.md) | P1 | 7 | todo | Kanban: undo last move toast |
| [VIEW-059](VIEW-059.md) | P1 | 7 | todo | Kanban: blocked-move reasons shown from validation errors |
| [VIEW-060](VIEW-060.md) | P2 | 11 | todo | Kanban: card age indicators and stale highlighting |
| [VIEW-061](VIEW-061.md) | P2 | 11 | todo | Kanban: column permissions (who can move into "Approved") |
| [VIEW-062](VIEW-062.md) | P2 | 11 | todo | Kanban: sub-board linking (card opens a child board) |
| [VIEW-063](VIEW-063.md) | P2 | 11 | todo | Kanban: burndown and cumulative flow charts |
| [VIEW-064](VIEW-064.md) | P2 | 11 | todo | Kanban: SLA timers per column |
| [VIEW-065](VIEW-065.md) | P2 | 11 | todo | Kanban: card templates per doctype shipped for Sales Order, Task, Issue, Lead, Opportunity |
| [VIEW-066](VIEW-066.md) | P1 | 7 | todo | Calendar: multiple date fields (start/end) and all-day handling |
| [VIEW-067](VIEW-067.md) | P1 | 7 | todo | Calendar: color by field or status, legend and toggles |
| [VIEW-068](VIEW-068.md) | P1 | 7 | todo | Calendar: create document by selecting a time range |
| [VIEW-069](VIEW-069.md) | P2 | 11 | todo | Calendar: resource view (rows = assignee/room/vehicle) |
| [VIEW-070](VIEW-070.md) | P2 | 11 | todo | Calendar: holiday overlay and working-hours shading |
| [VIEW-071](VIEW-071.md) | P2 | 11 | todo | Calendar: iCal read-only feed export (token protected) |
| [VIEW-072](VIEW-072.md) | P1 | 7 | todo | Gantt: critical path highlighting and dependency lines |
| [VIEW-073](VIEW-073.md) | P1 | 7 | todo | Gantt: baseline vs actual comparison |
| [VIEW-074](VIEW-074.md) | P2 | 11 | todo | Gantt: zoom levels (day/week/month/quarter) and today marker |
| [VIEW-075](VIEW-075.md) | P1 | 7 | todo | Table: saved column sets, frozen columns, row density |
| [VIEW-076](VIEW-076.md) | P1 | 7 | todo | Table: bulk inline edit with validation and per-cell errors |
| [VIEW-077](VIEW-077.md) | P1 | 7 | todo | Table: conditional row styling and icons |
| [VIEW-078](VIEW-078.md) | P1 | 7 | todo | Table: group by with subtotals and collapse all |
| [VIEW-079](VIEW-079.md) | P2 | 11 | todo | Table: formula columns (view-only, safe expressions) |
| [VIEW-080](VIEW-080.md) | P2 | 11 | todo | Table: copy/paste from spreadsheets into rows with validation |
