# PERM — Permissions Manager: tasks

Spec: [`01-permissions-manager.md`](../../specs/01-permissions-manager.md) · 105 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [PERM-001](PERM-001.md) | P0 | 1 | todo | `Permission Level` doctype defining the six levels and their flag sets |
| [PERM-002](PERM-002.md) | P0 | 1 | todo | Cumulative inheritance engine (each level = parent level + own flags) |
| [PERM-003](PERM-003.md) | P0 | 1 | todo | Level definitions editable (add/remove flags) with validation |
| [PERM-004](PERM-004.md) | P0 | 1 | todo | Generate one role per level per module (e.g. `Sales Junior`) |
| [PERM-005](PERM-005.md) | P0 | 1 | todo | Global `Base` role generation (read/select everywhere needed) |
| [PERM-006](PERM-006.md) | P0 | 1 | todo | Module → doctype discovery (all installed apps, custom doctypes included) |
| [PERM-007](PERM-007.md) | P0 | 1 | todo | Classification of doctypes (master / transaction / submittable / child / single / report-only) |
| [PERM-008](PERM-008.md) | P0 | 1 | todo | Per-class default flag maps (e.g. no `submit` for non-submittable) |
| [PERM-009](PERM-009.md) | P0 | 1 | todo | Preview of Custom DocPerm rows to be created/changed/removed |
| [PERM-010](PERM-010.md) | P0 | 1 | todo | Apply engine writing Custom DocPerm idempotently |
| [PERM-011](PERM-011.md) | P0 | 1 | todo | Snapshot of previous Custom DocPerm state before every apply |
| [PERM-012](PERM-012.md) | P0 | 1 | todo | One-click rollback to any previous snapshot |
| [PERM-013](PERM-013.md) | P0 | 1 | todo | Dry-run mode with downloadable report |
| [PERM-014](PERM-014.md) | P0 | 1 | todo | Matrix UI: role × doctype × flag with colored states |
| [PERM-015](PERM-015.md) | P0 | 1 | todo | Bulk edit in matrix (select rows/columns, set flags) |
| [PERM-016](PERM-016.md) | P0 | 1 | todo | "Delete draft only" rule via `has_permission`/`on_trash` hook (docstatus 0) |
| [PERM-017](PERM-017.md) | P0 | 1 | todo | Block delete of cancelled docs for all levels except auditor |
| [PERM-018](PERM-018.md) | P0 | 1 | todo | Auditor-only: cancel, amend, delete, delete cancelled |
| [PERM-019](PERM-019.md) | P0 | 1 | todo | Senior: submit + advanced reports; junior: create/write only |
| [PERM-020](PERM-020.md) | P0 | 1 | todo | Viewer: read/report/export/print/email, no write |
| [PERM-021](PERM-021.md) | P1 | 1 | todo | Per-module level assignment wizard ("Make Sales team junior") |
| [PERM-022](PERM-022.md) | P1 | 1 | todo | Per-doctype override of level flags with reason + audit entry |
| [PERM-023](PERM-023.md) | P1 | 1 | todo | Role Profile builder combining level roles across modules |
| [PERM-024](PERM-024.md) | P1 | 1 | todo | Role profile templates (Accountant, Warehouse Clerk, HR Officer ...) |
| [PERM-025](PERM-025.md) | P1 | 1 | todo | Bulk assign role profiles to users (CSV or multi-select) |
| [PERM-026](PERM-026.md) | P1 | 1 | todo | Per-user effective permissions viewer (what can user X do on doctype Y) |
| [PERM-027](PERM-027.md) | P1 | 1 | todo | "Why can/can't this user..." explainer tracing the rule path |
| [PERM-028](PERM-028.md) | P1 | 1 | todo | Simulate-as-user permission test for a doctype/document (no impersonation) |
| [PERM-029](PERM-029.md) | P1 | 1 | todo | Report access mapping (reports ↔ roles) by level (basic vs advanced vs audit) |
| [PERM-030](PERM-030.md) | P1 | 1 | todo | Report classification (basic/advanced/audit) editor |
| [PERM-031](PERM-031.md) | P1 | 1 | todo | Page and Workspace access mapping to levels |
| [PERM-032](PERM-032.md) | P1 | 1 | todo | Dashboard and Number Card access mapping to levels |
| [PERM-033](PERM-033.md) | P1 | 1 | todo | Field-level `permlevel` helper: mark sensitive fields and assign level-based access |
| [PERM-034](PERM-034.md) | P1 | 1 | todo | Sensitive-field detector (salary, tax id, bank, password-like) |
| [PERM-035](PERM-035.md) | P1 | 1 | todo | User Permission (data scoping) manager: by company/department/warehouse |
| [PERM-036](PERM-036.md) | P1 | 1 | todo | Bulk-create User Permissions from a template |
| [PERM-037](PERM-037.md) | P1 | 1 | todo | Permission conflict detector (contradictory or redundant rules) |
| [PERM-038](PERM-038.md) | P1 | 1 | todo | Orphan detector (roles with no users, users with no roles, perms on missing doctypes) |
| [PERM-039](PERM-039.md) | P1 | 1 | todo | Over-privilege detector (users with auditor + junior mix, System Manager sprawl) |
| [PERM-040](PERM-040.md) | P1 | 1 | todo | Segregation-of-duties rule sets (creator ≠ approver ≠ canceller) with violations list |
| [PERM-041](PERM-041.md) | P1 | 1 | todo | Permission health score per module |
| [PERM-042](PERM-042.md) | P1 | 1 | todo | Compare two roles side by side |
| [PERM-043](PERM-043.md) | P1 | 1 | todo | Compare two users side by side |
| [PERM-044](PERM-044.md) | P1 | 1 | todo | Compare snapshot vs current state diff |
| [PERM-045](PERM-045.md) | P1 | 1 | todo | Clone permissions from one doctype/module to another |
| [PERM-046](PERM-046.md) | P1 | 1 | todo | Handle custom doctypes automatically on `after_migrate` |
| [PERM-047](PERM-047.md) | P1 | 1 | todo | Handle newly installed apps (prompt to classify and apply default level matrix) |
| [PERM-048](PERM-048.md) | P1 | 1 | todo | Locked doctypes list (never touched by the manager) |
| [PERM-049](PERM-049.md) | P1 | 1 | todo | Protected roles list (Administrator, System Manager, Guest, All never edited) |
| [PERM-050](PERM-050.md) | P2 | 11 | todo | Export permission matrix to CSV/XLSX/PDF for auditors |
| [PERM-051](PERM-051.md) | P2 | 11 | todo | Import matrix from CSV with validation and preview |
| [PERM-052](PERM-052.md) | P2 | 11 | todo | Scheduled permission drift check vs desired state (alerts on manual changes) |
| [PERM-053](PERM-053.md) | P2 | 11 | todo | Drift auto-remediation (opt-in) |
| [PERM-054](PERM-054.md) | P2 | 11 | todo | Approval workflow for permission changes (request → approve → apply) |
| [PERM-055](PERM-055.md) | P2 | 11 | todo | Time-boxed elevated access (temporary auditor role with auto-expiry) |
| [PERM-056](PERM-056.md) | P2 | 11 | todo | Access review campaigns (managers re-certify their team's roles) |
| [PERM-057](PERM-057.md) | P2 | 11 | todo | New-joiner/leaver automation: apply profile on hire, strip on disable |
| [PERM-058](PERM-058.md) | P2 | 11 | todo | Share/permission-link audit (document shares, public links) |
| [PERM-059](PERM-059.md) | P2 | 11 | todo | API key/secret holder audit with last-used info |
| [PERM-060](PERM-060.md) | P2 | 11 | todo | Workflow state ↔ level mapping helper (who can move which transition) |
| [PERM-061](PERM-061.md) | P2 | 11 | todo | Visual hierarchy diagram of ladder and role inheritance |
| [PERM-062](PERM-062.md) | P2 | 11 | todo | Natural-language summary of a role ("Senior Sales can create, submit ...") |
| [PERM-063](PERM-063.md) | P2 | 11 | todo | Per-company ladder variants (different matrices per company) |
| [PERM-064](PERM-064.md) | P2 | 11 | todo | Industry presets (retail, manufacturing, services, education, NGO) |
| [PERM-065](PERM-065.md) | P2 | 11 | todo | Permission change notifications to security admins |
| [PERM-066](PERM-066.md) | P2 | 11 | todo | Compliance pack mapping (SOX-like segregation checks) as report templates |
| [PERM-067](PERM-067.md) | P2 | 11 | todo | Role usage analytics (which permissions are actually exercised) |
| [PERM-068](PERM-068.md) | P2 | 11 | todo | Unused-permission recommendations (least-privilege suggestions) |
| [PERM-069](PERM-069.md) | P2 | 11 | todo | Permission test-suite generator (auto-create tests from the matrix) |
| [PERM-070](PERM-070.md) | P2 | 11 | todo | CLI: `bench --site x admin-utils apply-ladder --dry-run` |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [PERM-071](PERM-071.md) | P1 | 1 | todo | Role naming convention engine (`<Module> <Level>`) with collision detection |
| [PERM-072](PERM-072.md) | P1 | 1 | todo | Level aliases per language (Arabic role display names) |
| [PERM-073](PERM-073.md) | P1 | 1 | todo | Custom ladders: define additional levels or a different order per module |
| [PERM-074](PERM-074.md) | P1 | 1 | todo | Ladder versioning (v1, v2) with migration between versions |
| [PERM-075](PERM-075.md) | P1 | 1 | todo | Per-flag explanations tooltip (what does "amend" really allow) |
| [PERM-076](PERM-076.md) | P1 | 1 | todo | Doctype grouping into "permission domains" (Sales, Stock, Accounts) independent of modules |
| [PERM-077](PERM-077.md) | P1 | 1 | todo | Bulk exclusions: skip doctypes by pattern, app, or tag |
| [PERM-078](PERM-078.md) | P1 | 1 | todo | Special-case rules for single doctypes, settings doctypes and system doctypes |
| [PERM-079](PERM-079.md) | P1 | 1 | todo | Child-table doctype permission inheritance checks |
| [PERM-080](PERM-080.md) | P1 | 1 | todo | Link-field read dependency resolver (grant `select` on linked masters automatically) |
| [PERM-081](PERM-081.md) | P1 | 1 | todo | "Can't open form because link target hidden" detector |
| [PERM-082](PERM-082.md) | P1 | 1 | todo | Role dependency check before deleting a role (users, workflows, reports) |
| [PERM-083](PERM-083.md) | P1 | 1 | todo | Rename role safely across Custom DocPerm, workflows, reports, pages, scripts |
| [PERM-084](PERM-084.md) | P1 | 1 | todo | Merge two roles with conflict report |
| [PERM-085](PERM-085.md) | P1 | 1 | todo | Split a broad role into level-based roles with automatic user migration |
| [PERM-086](PERM-086.md) | P1 | 1 | todo | Workflow transition permission audit (roles allowed per transition vs ladder) |
| [PERM-087](PERM-087.md) | P1 | 1 | todo | Auto-suggest ladder level for an existing custom role by comparing flags |
| [PERM-088](PERM-088.md) | P1 | 1 | todo | Import existing permission setup as "baseline snapshot" before first apply |
| [PERM-089](PERM-089.md) | P1 | 1 | todo | Apply in staged waves (module by module) with pause/resume |
| [PERM-090](PERM-090.md) | P1 | 1 | todo | Post-apply verification suite (sample users per level tested against sample docs) |
| [PERM-091](PERM-091.md) | P1 | 1 | todo | Permission impact analysis ("this change affects 14 users and 3 reports") |
| [PERM-092](PERM-092.md) | P1 | 1 | todo | Change windows (only apply between configured hours) |
| [PERM-093](PERM-093.md) | P2 | 11 | todo | Role cost/licence view (roles that count toward paid seat plans, if applicable) |
| [PERM-094](PERM-094.md) | P2 | 11 | todo | Delegation: temporary delegate of a role between two users with dates |
| [PERM-095](PERM-095.md) | P2 | 11 | todo | Break-glass access (emergency elevation with mandatory reason, loud audit) |
| [PERM-096](PERM-096.md) | P2 | 11 | todo | Permission requests portal (user asks, manager approves) |
| [PERM-097](PERM-097.md) | P2 | 11 | todo | Team-based permission scoping (department head sees department data) |
| [PERM-098](PERM-098.md) | P2 | 11 | todo | Territory/warehouse/cost-center scoping templates |
| [PERM-099](PERM-099.md) | P2 | 11 | todo | Document-level share policy (who may share, with whom, which doctypes) |
| [PERM-100](PERM-100.md) | P2 | 11 | todo | Export permission change log for external auditors |
| [PERM-101](PERM-101.md) | P2 | 11 | todo | "Permission Diff" report between two dates |
| [PERM-102](PERM-102.md) | P2 | 11 | todo | Heatmap of permissions risk by doctype (delete/cancel exposure) |
| [PERM-103](PERM-103.md) | P2 | 11 | todo | Highlight doctypes with financial impact lacking auditor-only cancel |
| [PERM-104](PERM-104.md) | P2 | 11 | todo | Pre-built compliance checks (no user can create and submit payments) |
| [PERM-105](PERM-105.md) | P2 | 11 | todo | API-based permission assertions for CI ("role X must not delete Sales Invoice") |
