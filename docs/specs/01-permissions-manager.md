---
code: PERM
title: "Permissions Manager"
number: 01
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/permissions/
frontend_path: frontend/src/features/permissions/
tasks: docs/tasks/PERM/INDEX.md
---

# Spec 01 — Permissions Manager (`PERM`)

## Purpose

Ladder-based permission levels for every module, mapped to real-life duties, applied as Custom DocPerm rows with preview, snapshot and rollback. Ladder: `base → viewer → junior → self-support → senior → auditor` (cumulative inheritance).

## Placement

- Python package: `admin_utils/permissions/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/permissions/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Permissions Manager Settings`; on/off flag `enable_permissions` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/permissions/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 20 |
| P1 | 51 |
| P2 | 34 |

Waves: wave 1 (71), wave 11 (34)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [PERM-001](../tasks/PERM/PERM-001.md) | P0 | 1 | `Permission Level` doctype defining the six levels and their flag sets |
| [PERM-002](../tasks/PERM/PERM-002.md) | P0 | 1 | Cumulative inheritance engine (each level = parent level + own flags) |
| [PERM-003](../tasks/PERM/PERM-003.md) | P0 | 1 | Level definitions editable (add/remove flags) with validation |
| [PERM-004](../tasks/PERM/PERM-004.md) | P0 | 1 | Generate one role per level per module (e.g. `Sales Junior`) |
| [PERM-005](../tasks/PERM/PERM-005.md) | P0 | 1 | Global `Base` role generation (read/select everywhere needed) |
| [PERM-006](../tasks/PERM/PERM-006.md) | P0 | 1 | Module → doctype discovery (all installed apps, custom doctypes included) |
| [PERM-007](../tasks/PERM/PERM-007.md) | P0 | 1 | Classification of doctypes (master / transaction / submittable / child / single / report-only) |
| [PERM-008](../tasks/PERM/PERM-008.md) | P0 | 1 | Per-class default flag maps (e.g. no `submit` for non-submittable) |
| [PERM-009](../tasks/PERM/PERM-009.md) | P0 | 1 | Preview of Custom DocPerm rows to be created/changed/removed |
| [PERM-010](../tasks/PERM/PERM-010.md) | P0 | 1 | Apply engine writing Custom DocPerm idempotently |
| [PERM-011](../tasks/PERM/PERM-011.md) | P0 | 1 | Snapshot of previous Custom DocPerm state before every apply |
| [PERM-012](../tasks/PERM/PERM-012.md) | P0 | 1 | One-click rollback to any previous snapshot |
| [PERM-013](../tasks/PERM/PERM-013.md) | P0 | 1 | Dry-run mode with downloadable report |
| [PERM-014](../tasks/PERM/PERM-014.md) | P0 | 1 | Matrix UI: role × doctype × flag with colored states |
| [PERM-015](../tasks/PERM/PERM-015.md) | P0 | 1 | Bulk edit in matrix (select rows/columns, set flags) |
| [PERM-016](../tasks/PERM/PERM-016.md) | P0 | 1 | "Delete draft only" rule via `has_permission`/`on_trash` hook (docstatus 0) |
| [PERM-017](../tasks/PERM/PERM-017.md) | P0 | 1 | Block delete of cancelled docs for all levels except auditor |
| [PERM-018](../tasks/PERM/PERM-018.md) | P0 | 1 | Auditor-only: cancel, amend, delete, delete cancelled |
| [PERM-019](../tasks/PERM/PERM-019.md) | P0 | 1 | Senior: submit + advanced reports; junior: create/write only |
| [PERM-020](../tasks/PERM/PERM-020.md) | P0 | 1 | Viewer: read/report/export/print/email, no write |
| [PERM-021](../tasks/PERM/PERM-021.md) | P1 | 1 | Per-module level assignment wizard ("Make Sales team junior") |
| [PERM-022](../tasks/PERM/PERM-022.md) | P1 | 1 | Per-doctype override of level flags with reason + audit entry |
| [PERM-023](../tasks/PERM/PERM-023.md) | P1 | 1 | Role Profile builder combining level roles across modules |
| [PERM-024](../tasks/PERM/PERM-024.md) | P1 | 1 | Role profile templates (Accountant, Warehouse Clerk, HR Officer ...) |
| [PERM-025](../tasks/PERM/PERM-025.md) | P1 | 1 | Bulk assign role profiles to users (CSV or multi-select) |
| [PERM-026](../tasks/PERM/PERM-026.md) | P1 | 1 | Per-user effective permissions viewer (what can user X do on doctype Y) |
| [PERM-027](../tasks/PERM/PERM-027.md) | P1 | 1 | "Why can/can't this user..." explainer tracing the rule path |
| [PERM-028](../tasks/PERM/PERM-028.md) | P1 | 1 | Simulate-as-user permission test for a doctype/document (no impersonation) |
| [PERM-029](../tasks/PERM/PERM-029.md) | P1 | 1 | Report access mapping (reports ↔ roles) by level (basic vs advanced vs audit) |
| [PERM-030](../tasks/PERM/PERM-030.md) | P1 | 1 | Report classification (basic/advanced/audit) editor |
| [PERM-031](../tasks/PERM/PERM-031.md) | P1 | 1 | Page and Workspace access mapping to levels |
| [PERM-032](../tasks/PERM/PERM-032.md) | P1 | 1 | Dashboard and Number Card access mapping to levels |
| [PERM-033](../tasks/PERM/PERM-033.md) | P1 | 1 | Field-level `permlevel` helper: mark sensitive fields and assign level-based access |
| [PERM-034](../tasks/PERM/PERM-034.md) | P1 | 1 | Sensitive-field detector (salary, tax id, bank, password-like) |
| [PERM-035](../tasks/PERM/PERM-035.md) | P1 | 1 | User Permission (data scoping) manager: by company/department/warehouse |
| [PERM-036](../tasks/PERM/PERM-036.md) | P1 | 1 | Bulk-create User Permissions from a template |
| [PERM-037](../tasks/PERM/PERM-037.md) | P1 | 1 | Permission conflict detector (contradictory or redundant rules) |
| [PERM-038](../tasks/PERM/PERM-038.md) | P1 | 1 | Orphan detector (roles with no users, users with no roles, perms on missing doctypes) |
| [PERM-039](../tasks/PERM/PERM-039.md) | P1 | 1 | Over-privilege detector (users with auditor + junior mix, System Manager sprawl) |
| [PERM-040](../tasks/PERM/PERM-040.md) | P1 | 1 | Segregation-of-duties rule sets (creator ≠ approver ≠ canceller) with violations list |
| [PERM-041](../tasks/PERM/PERM-041.md) | P1 | 1 | Permission health score per module |
| [PERM-042](../tasks/PERM/PERM-042.md) | P1 | 1 | Compare two roles side by side |
| [PERM-043](../tasks/PERM/PERM-043.md) | P1 | 1 | Compare two users side by side |
| [PERM-044](../tasks/PERM/PERM-044.md) | P1 | 1 | Compare snapshot vs current state diff |
| [PERM-045](../tasks/PERM/PERM-045.md) | P1 | 1 | Clone permissions from one doctype/module to another |
| [PERM-046](../tasks/PERM/PERM-046.md) | P1 | 1 | Handle custom doctypes automatically on `after_migrate` |
| [PERM-047](../tasks/PERM/PERM-047.md) | P1 | 1 | Handle newly installed apps (prompt to classify and apply default level matrix) |
| [PERM-048](../tasks/PERM/PERM-048.md) | P1 | 1 | Locked doctypes list (never touched by the manager) |
| [PERM-049](../tasks/PERM/PERM-049.md) | P1 | 1 | Protected roles list (Administrator, System Manager, Guest, All never edited) |
| [PERM-050](../tasks/PERM/PERM-050.md) | P2 | 11 | Export permission matrix to CSV/XLSX/PDF for auditors |
| [PERM-051](../tasks/PERM/PERM-051.md) | P2 | 11 | Import matrix from CSV with validation and preview |
| [PERM-052](../tasks/PERM/PERM-052.md) | P2 | 11 | Scheduled permission drift check vs desired state (alerts on manual changes) |
| [PERM-053](../tasks/PERM/PERM-053.md) | P2 | 11 | Drift auto-remediation (opt-in) |
| [PERM-054](../tasks/PERM/PERM-054.md) | P2 | 11 | Approval workflow for permission changes (request → approve → apply) |
| [PERM-055](../tasks/PERM/PERM-055.md) | P2 | 11 | Time-boxed elevated access (temporary auditor role with auto-expiry) |
| [PERM-056](../tasks/PERM/PERM-056.md) | P2 | 11 | Access review campaigns (managers re-certify their team's roles) |
| [PERM-057](../tasks/PERM/PERM-057.md) | P2 | 11 | New-joiner/leaver automation: apply profile on hire, strip on disable |
| [PERM-058](../tasks/PERM/PERM-058.md) | P2 | 11 | Share/permission-link audit (document shares, public links) |
| [PERM-059](../tasks/PERM/PERM-059.md) | P2 | 11 | API key/secret holder audit with last-used info |
| [PERM-060](../tasks/PERM/PERM-060.md) | P2 | 11 | Workflow state ↔ level mapping helper (who can move which transition) |
| [PERM-061](../tasks/PERM/PERM-061.md) | P2 | 11 | Visual hierarchy diagram of ladder and role inheritance |
| [PERM-062](../tasks/PERM/PERM-062.md) | P2 | 11 | Natural-language summary of a role ("Senior Sales can create, submit ...") |
| [PERM-063](../tasks/PERM/PERM-063.md) | P2 | 11 | Per-company ladder variants (different matrices per company) |
| [PERM-064](../tasks/PERM/PERM-064.md) | P2 | 11 | Industry presets (retail, manufacturing, services, education, NGO) |
| [PERM-065](../tasks/PERM/PERM-065.md) | P2 | 11 | Permission change notifications to security admins |
| [PERM-066](../tasks/PERM/PERM-066.md) | P2 | 11 | Compliance pack mapping (SOX-like segregation checks) as report templates |
| [PERM-067](../tasks/PERM/PERM-067.md) | P2 | 11 | Role usage analytics (which permissions are actually exercised) |
| [PERM-068](../tasks/PERM/PERM-068.md) | P2 | 11 | Unused-permission recommendations (least-privilege suggestions) |
| [PERM-069](../tasks/PERM/PERM-069.md) | P2 | 11 | Permission test-suite generator (auto-create tests from the matrix) |
| [PERM-070](../tasks/PERM/PERM-070.md) | P2 | 11 | CLI: `bench --site x admin-utils apply-ladder --dry-run` |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [PERM-071](../tasks/PERM/PERM-071.md) | P1 | 1 | Role naming convention engine (`<Module> <Level>`) with collision detection |
| [PERM-072](../tasks/PERM/PERM-072.md) | P1 | 1 | Level aliases per language (Arabic role display names) |
| [PERM-073](../tasks/PERM/PERM-073.md) | P1 | 1 | Custom ladders: define additional levels or a different order per module |
| [PERM-074](../tasks/PERM/PERM-074.md) | P1 | 1 | Ladder versioning (v1, v2) with migration between versions |
| [PERM-075](../tasks/PERM/PERM-075.md) | P1 | 1 | Per-flag explanations tooltip (what does "amend" really allow) |
| [PERM-076](../tasks/PERM/PERM-076.md) | P1 | 1 | Doctype grouping into "permission domains" (Sales, Stock, Accounts) independent of modules |
| [PERM-077](../tasks/PERM/PERM-077.md) | P1 | 1 | Bulk exclusions: skip doctypes by pattern, app, or tag |
| [PERM-078](../tasks/PERM/PERM-078.md) | P1 | 1 | Special-case rules for single doctypes, settings doctypes and system doctypes |
| [PERM-079](../tasks/PERM/PERM-079.md) | P1 | 1 | Child-table doctype permission inheritance checks |
| [PERM-080](../tasks/PERM/PERM-080.md) | P1 | 1 | Link-field read dependency resolver (grant `select` on linked masters automatically) |
| [PERM-081](../tasks/PERM/PERM-081.md) | P1 | 1 | "Can't open form because link target hidden" detector |
| [PERM-082](../tasks/PERM/PERM-082.md) | P1 | 1 | Role dependency check before deleting a role (users, workflows, reports) |
| [PERM-083](../tasks/PERM/PERM-083.md) | P1 | 1 | Rename role safely across Custom DocPerm, workflows, reports, pages, scripts |
| [PERM-084](../tasks/PERM/PERM-084.md) | P1 | 1 | Merge two roles with conflict report |
| [PERM-085](../tasks/PERM/PERM-085.md) | P1 | 1 | Split a broad role into level-based roles with automatic user migration |
| [PERM-086](../tasks/PERM/PERM-086.md) | P1 | 1 | Workflow transition permission audit (roles allowed per transition vs ladder) |
| [PERM-087](../tasks/PERM/PERM-087.md) | P1 | 1 | Auto-suggest ladder level for an existing custom role by comparing flags |
| [PERM-088](../tasks/PERM/PERM-088.md) | P1 | 1 | Import existing permission setup as "baseline snapshot" before first apply |
| [PERM-089](../tasks/PERM/PERM-089.md) | P1 | 1 | Apply in staged waves (module by module) with pause/resume |
| [PERM-090](../tasks/PERM/PERM-090.md) | P1 | 1 | Post-apply verification suite (sample users per level tested against sample docs) |
| [PERM-091](../tasks/PERM/PERM-091.md) | P1 | 1 | Permission impact analysis ("this change affects 14 users and 3 reports") |
| [PERM-092](../tasks/PERM/PERM-092.md) | P1 | 1 | Change windows (only apply between configured hours) |
| [PERM-093](../tasks/PERM/PERM-093.md) | P2 | 11 | Role cost/licence view (roles that count toward paid seat plans, if applicable) |
| [PERM-094](../tasks/PERM/PERM-094.md) | P2 | 11 | Delegation: temporary delegate of a role between two users with dates |
| [PERM-095](../tasks/PERM/PERM-095.md) | P2 | 11 | Break-glass access (emergency elevation with mandatory reason, loud audit) |
| [PERM-096](../tasks/PERM/PERM-096.md) | P2 | 11 | Permission requests portal (user asks, manager approves) |
| [PERM-097](../tasks/PERM/PERM-097.md) | P2 | 11 | Team-based permission scoping (department head sees department data) |
| [PERM-098](../tasks/PERM/PERM-098.md) | P2 | 11 | Territory/warehouse/cost-center scoping templates |
| [PERM-099](../tasks/PERM/PERM-099.md) | P2 | 11 | Document-level share policy (who may share, with whom, which doctypes) |
| [PERM-100](../tasks/PERM/PERM-100.md) | P2 | 11 | Export permission change log for external auditors |
| [PERM-101](../tasks/PERM/PERM-101.md) | P2 | 11 | "Permission Diff" report between two dates |
| [PERM-102](../tasks/PERM/PERM-102.md) | P2 | 11 | Heatmap of permissions risk by doctype (delete/cancel exposure) |
| [PERM-103](../tasks/PERM/PERM-103.md) | P2 | 11 | Highlight doctypes with financial impact lacking auditor-only cancel |
| [PERM-104](../tasks/PERM/PERM-104.md) | P2 | 11 | Pre-built compliance checks (no user can create and submit payments) |
| [PERM-105](../tasks/PERM/PERM-105.md) | P2 | 11 | API-based permission assertions for CI ("role X must not delete Sales Invoice") |

## Tests

- golden-file tests of the generated Custom DocPerm set per level; property test that inheritance is monotonic (a higher level never has fewer flags); tests that `junior` cannot submit, `self-support` cannot delete submitted/cancelled, `senior` cannot cancel, only `auditor` can; rollback restores exact prior rows; idempotent re-apply yields no diff.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Permission apply breaks live access: preview, snapshot, rollback, dry-run, protected roles

## Recorded decisions (owner-approved)

- Block deleting cancelled documents through an `on_trash` hook unless the user has the Auditor level (PERM-016/017).
- Print permission starts at the **Junior** level; export starts at the **Auditor** level.

## Conflicts to resolve before implementation

- **PERM-020** says Viewer gets `read/report/export/print/email`. That contradicts the decisions above (print from Junior, export at Auditor). Resolve in the spec: the decisions win unless the owner says otherwise; update PERM-020 and the level flag sets accordingly.

## Open for the Architect

- Report classification rules (basic / advanced / audit) and their default mapping (PERM-029/030).
- One role per ladder level per module (plan default, PERM-004) versus fewer shared roles; record the choice as an ADR.

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
