---
code: EXTR
title: "Additional Admin Utilities"
number: 13
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/extras/
frontend_path: frontend/src/features/extras/
tasks: docs/tasks/EXTR/INDEX.md
---

# Spec 13 — Additional Admin Utilities (`EXTR`)

## Purpose

Additional Admin Utilities: see feature groups below.

## Placement

- Python package: `admin_utils/extras/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/extras/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Additional Admin Utilities Settings`; on/off flag `enable_extras` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/extras/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P1 | 37 |
| P2 | 28 |

Waves: wave 8 (37), wave 11 (28)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [EXTR-001](../tasks/EXTR/EXTR-001.md) | P1 | 8 | User manager: bulk create/disable/enable users, reset passwords, force logout |
| [EXTR-002](../tasks/EXTR/EXTR-002.md) | P1 | 8 | Session manager: list and terminate active sessions |
| [EXTR-003](../tasks/EXTR/EXTR-003.md) | P1 | 8 | 2FA coverage report and enforcement helper |
| [EXTR-004](../tasks/EXTR/EXTR-004.md) | P1 | 8 | Custom Field manager: list, search, bulk move, orphan detection |
| [EXTR-005](../tasks/EXTR/EXTR-005.md) | P1 | 8 | Property Setter manager with diff vs standard and revert |
| [EXTR-006](../tasks/EXTR/EXTR-006.md) | P1 | 8 | Customization export as fixtures with dependency check |
| [EXTR-007](../tasks/EXTR/EXTR-007.md) | P1 | 8 | Client Script / Server Script inventory with enable/disable and risk flags |
| [EXTR-008](../tasks/EXTR/EXTR-008.md) | P1 | 8 | Scheduled job manager (list, enable/disable, run now, history) |
| [EXTR-009](../tasks/EXTR/EXTR-009.md) | P1 | 8 | Backup manager UI: list, download, restore guidance, retention rules |
| [EXTR-010](../tasks/EXTR/EXTR-010.md) | P1 | 8 | Offsite backup configuration helper (S3-compatible, Dropbox, Drive) with test button |
| [EXTR-011](../tasks/EXTR/EXTR-011.md) | P1 | 8 | Email account and domain health check (SPF/DKIM hints, test send) |
| [EXTR-012](../tasks/EXTR/EXTR-012.md) | P1 | 8 | Print format inventory and broken-format detector |
| [EXTR-013](../tasks/EXTR/EXTR-013.md) | P1 | 8 | Notification inventory with test-fire |
| [EXTR-014](../tasks/EXTR/EXTR-014.md) | P1 | 8 | Workflow inventory and visual diagram viewer |
| [EXTR-015](../tasks/EXTR/EXTR-015.md) | P1 | 8 | Data import helper: template generator, mapping, dry-run, error report |
| [EXTR-016](../tasks/EXTR/EXTR-016.md) | P1 | 8 | Bulk update tool (field set/replace with preview and undo snapshot) |
| [EXTR-017](../tasks/EXTR/EXTR-017.md) | P1 | 8 | Duplicate finder and merger helper for masters (customers, items, suppliers) |
| [EXTR-018](../tasks/EXTR/EXTR-018.md) | P1 | 8 | Link integrity checker (broken links, orphaned child rows) |
| [EXTR-019](../tasks/EXTR/EXTR-019.md) | P1 | 8 | Deleted Documents browser with restore |
| [EXTR-020](../tasks/EXTR/EXTR-020.md) | P1 | 8 | Version/changes history explorer across doctypes |
| [EXTR-021](../tasks/EXTR/EXTR-021.md) | P1 | 8 | Number series (naming series) manager with gap and collision checks |
| [EXTR-022](../tasks/EXTR/EXTR-022.md) | P1 | 8 | Fiscal year/company defaults checklist |
| [EXTR-023](../tasks/EXTR/EXTR-023.md) | P1 | 8 | System Settings and Global Defaults health review |
| [EXTR-024](../tasks/EXTR/EXTR-024.md) | P1 | 8 | Doctype explorer (fields, links, dependencies, permissions in one screen) |
| [EXTR-025](../tasks/EXTR/EXTR-025.md) | P1 | 8 | Database consistency tools (find docs stuck in invalid docstatus) |
| [EXTR-026](../tasks/EXTR/EXTR-026.md) | P1 | 8 | Large attachment finder with cleanup action |
| [EXTR-027](../tasks/EXTR/EXTR-027.md) | P1 | 8 | Orphan file cleaner (dry-run first) |
| [EXTR-028](../tasks/EXTR/EXTR-028.md) | P2 | 11 | Data archival helper (move old logs/versions to archive tables or files) |
| [EXTR-029](../tasks/EXTR/EXTR-029.md) | P2 | 11 | Log retention policy manager (Error Log, Activity Log, Email Queue, Version) |
| [EXTR-030](../tasks/EXTR/EXTR-030.md) | P2 | 11 | Webhook inventory with delivery log and replay |
| [EXTR-031](../tasks/EXTR/EXTR-031.md) | P2 | 11 | API key manager with scopes view and rotation reminders |
| [EXTR-032](../tasks/EXTR/EXTR-032.md) | P2 | 11 | Integration health dashboard (payment, SMS, email, storage providers) |
| [EXTR-033](../tasks/EXTR/EXTR-033.md) | P2 | 11 | Site migration assistant checklist (pre/post upgrade validation) |
| [EXTR-034](../tasks/EXTR/EXTR-034.md) | P2 | 11 | Upgrade readiness report (custom code vs deprecated APIs) |
| [EXTR-035](../tasks/EXTR/EXTR-035.md) | P2 | 11 | Release notes generator from audit and customization diffs |
| [EXTR-036](../tasks/EXTR/EXTR-036.md) | P2 | 11 | Environment cloning checklist (prod → staging with anonymizer) |
| [EXTR-037](../tasks/EXTR/EXTR-037.md) | P2 | 11 | Admin task list/runbook library with checklists |
| [EXTR-038](../tasks/EXTR/EXTR-038.md) | P2 | 11 | Knowledge base of common admin fixes linked from error messages |
| [EXTR-039](../tasks/EXTR/EXTR-039.md) | P2 | 11 | Scheduled digest to admins (changes, alerts, jobs, pending approvals) |
| [EXTR-040](../tasks/EXTR/EXTR-040.md) | P2 | 11 | Public extension API so other apps can add admin tiles/pages |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [EXTR-041](../tasks/EXTR/EXTR-041.md) | P1 | 8 | Custom DocType health checker (missing indexes, long text misuse, too many fields) |
| [EXTR-042](../tasks/EXTR/EXTR-042.md) | P1 | 8 | Index advisor based on query patterns (suggestions only) |
| [EXTR-043](../tasks/EXTR/EXTR-043.md) | P1 | 8 | Unused custom field finder (no data, no references) |
| [EXTR-044](../tasks/EXTR/EXTR-044.md) | P1 | 8 | Role/user cleanup assistant (disabled users, stale API keys, inactive roles) |
| [EXTR-045](../tasks/EXTR/EXTR-045.md) | P1 | 8 | Stuck document finder (draft documents older than N days by doctype) |
| [EXTR-046](../tasks/EXTR/EXTR-046.md) | P1 | 8 | Scheduled event log browser with filter by job |
| [EXTR-047](../tasks/EXTR/EXTR-047.md) | P1 | 8 | Document timeline explorer (versions, comments, communications, shares) in one view |
| [EXTR-048](../tasks/EXTR/EXTR-048.md) | P1 | 8 | Comment/assignment cleanup tools for departed users |
| [EXTR-049](../tasks/EXTR/EXTR-049.md) | P1 | 8 | Reassign all open work from one user to another with preview |
| [EXTR-050](../tasks/EXTR/EXTR-050.md) | P1 | 8 | Letterhead and company branding consistency checker |
| [EXTR-051](../tasks/EXTR/EXTR-051.md) | P2 | 11 | Currency exchange rate fetch status and gaps checker |
| [EXTR-052](../tasks/EXTR/EXTR-052.md) | P2 | 11 | Tax template audit (unused, inconsistent, missing accounts) |
| [EXTR-053](../tasks/EXTR/EXTR-053.md) | P2 | 11 | Chart of accounts sanity report (ungrouped, wrong root types) |
| [EXTR-054](../tasks/EXTR/EXTR-054.md) | P2 | 11 | Item master data quality (missing UOM, group, HSN-like codes, images) |
| [EXTR-055](../tasks/EXTR/EXTR-055.md) | P2 | 11 | Customer/supplier data quality (missing phone, tax id, duplicates) |
| [EXTR-056](../tasks/EXTR/EXTR-056.md) | P2 | 11 | Email template library manager with variable tester |
| [EXTR-057](../tasks/EXTR/EXTR-057.md) | P2 | 11 | Print settings and paper-size presets manager |
| [EXTR-058](../tasks/EXTR/EXTR-058.md) | P2 | 11 | Assignment rule and auto-repeat inventory with test-run |
| [EXTR-059](../tasks/EXTR/EXTR-059.md) | P2 | 11 | Document naming audit (inconsistent naming rules across doctypes) |
| [EXTR-060](../tasks/EXTR/EXTR-060.md) | P2 | 11 | Server/client script static analysis for risky patterns |
| [EXTR-061](../tasks/EXTR/EXTR-061.md) | P2 | 11 | Dormant data report (records untouched for N months) with archive action |
| [EXTR-062](../tasks/EXTR/EXTR-062.md) | P2 | 11 | GDPR-style data export/erase request handler per person |
| [EXTR-063](../tasks/EXTR/EXTR-063.md) | P2 | 11 | Consent and privacy settings audit |
| [EXTR-064](../tasks/EXTR/EXTR-064.md) | P2 | 11 | Admin changelog digest of config, permission and customization changes |
| [EXTR-065](../tasks/EXTR/EXTR-065.md) | P2 | 11 | Site "go-live checklist" with automated verifications |

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
