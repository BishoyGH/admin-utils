# EXTR — Additional Admin Utilities: tasks

Spec: [`13-extra-utilities.md`](../../specs/13-extra-utilities.md) · 65 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [EXTR-001](EXTR-001.md) | P1 | 8 | todo | User manager: bulk create/disable/enable users, reset passwords, force logout |
| [EXTR-002](EXTR-002.md) | P1 | 8 | todo | Session manager: list and terminate active sessions |
| [EXTR-003](EXTR-003.md) | P1 | 8 | todo | 2FA coverage report and enforcement helper |
| [EXTR-004](EXTR-004.md) | P1 | 8 | todo | Custom Field manager: list, search, bulk move, orphan detection |
| [EXTR-005](EXTR-005.md) | P1 | 8 | todo | Property Setter manager with diff vs standard and revert |
| [EXTR-006](EXTR-006.md) | P1 | 8 | todo | Customization export as fixtures with dependency check |
| [EXTR-007](EXTR-007.md) | P1 | 8 | todo | Client Script / Server Script inventory with enable/disable and risk flags |
| [EXTR-008](EXTR-008.md) | P1 | 8 | todo | Scheduled job manager (list, enable/disable, run now, history) |
| [EXTR-009](EXTR-009.md) | P1 | 8 | todo | Backup manager UI: list, download, restore guidance, retention rules |
| [EXTR-010](EXTR-010.md) | P1 | 8 | todo | Offsite backup configuration helper (S3-compatible, Dropbox, Drive) with test button |
| [EXTR-011](EXTR-011.md) | P1 | 8 | todo | Email account and domain health check (SPF/DKIM hints, test send) |
| [EXTR-012](EXTR-012.md) | P1 | 8 | todo | Print format inventory and broken-format detector |
| [EXTR-013](EXTR-013.md) | P1 | 8 | todo | Notification inventory with test-fire |
| [EXTR-014](EXTR-014.md) | P1 | 8 | todo | Workflow inventory and visual diagram viewer |
| [EXTR-015](EXTR-015.md) | P1 | 8 | todo | Data import helper: template generator, mapping, dry-run, error report |
| [EXTR-016](EXTR-016.md) | P1 | 8 | todo | Bulk update tool (field set/replace with preview and undo snapshot) |
| [EXTR-017](EXTR-017.md) | P1 | 8 | todo | Duplicate finder and merger helper for masters (customers, items, suppliers) |
| [EXTR-018](EXTR-018.md) | P1 | 8 | todo | Link integrity checker (broken links, orphaned child rows) |
| [EXTR-019](EXTR-019.md) | P1 | 8 | todo | Deleted Documents browser with restore |
| [EXTR-020](EXTR-020.md) | P1 | 8 | todo | Version/changes history explorer across doctypes |
| [EXTR-021](EXTR-021.md) | P1 | 8 | todo | Number series (naming series) manager with gap and collision checks |
| [EXTR-022](EXTR-022.md) | P1 | 8 | todo | Fiscal year/company defaults checklist |
| [EXTR-023](EXTR-023.md) | P1 | 8 | todo | System Settings and Global Defaults health review |
| [EXTR-024](EXTR-024.md) | P1 | 8 | todo | Doctype explorer (fields, links, dependencies, permissions in one screen) |
| [EXTR-025](EXTR-025.md) | P1 | 8 | todo | Database consistency tools (find docs stuck in invalid docstatus) |
| [EXTR-026](EXTR-026.md) | P1 | 8 | todo | Large attachment finder with cleanup action |
| [EXTR-027](EXTR-027.md) | P1 | 8 | todo | Orphan file cleaner (dry-run first) |
| [EXTR-028](EXTR-028.md) | P2 | 11 | todo | Data archival helper (move old logs/versions to archive tables or files) |
| [EXTR-029](EXTR-029.md) | P2 | 11 | todo | Log retention policy manager (Error Log, Activity Log, Email Queue, Version) |
| [EXTR-030](EXTR-030.md) | P2 | 11 | todo | Webhook inventory with delivery log and replay |
| [EXTR-031](EXTR-031.md) | P2 | 11 | todo | API key manager with scopes view and rotation reminders |
| [EXTR-032](EXTR-032.md) | P2 | 11 | todo | Integration health dashboard (payment, SMS, email, storage providers) |
| [EXTR-033](EXTR-033.md) | P2 | 11 | todo | Site migration assistant checklist (pre/post upgrade validation) |
| [EXTR-034](EXTR-034.md) | P2 | 11 | todo | Upgrade readiness report (custom code vs deprecated APIs) |
| [EXTR-035](EXTR-035.md) | P2 | 11 | todo | Release notes generator from audit and customization diffs |
| [EXTR-036](EXTR-036.md) | P2 | 11 | todo | Environment cloning checklist (prod → staging with anonymizer) |
| [EXTR-037](EXTR-037.md) | P2 | 11 | todo | Admin task list/runbook library with checklists |
| [EXTR-038](EXTR-038.md) | P2 | 11 | todo | Knowledge base of common admin fixes linked from error messages |
| [EXTR-039](EXTR-039.md) | P2 | 11 | todo | Scheduled digest to admins (changes, alerts, jobs, pending approvals) |
| [EXTR-040](EXTR-040.md) | P2 | 11 | todo | Public extension API so other apps can add admin tiles/pages |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [EXTR-041](EXTR-041.md) | P1 | 8 | todo | Custom DocType health checker (missing indexes, long text misuse, too many fields) |
| [EXTR-042](EXTR-042.md) | P1 | 8 | todo | Index advisor based on query patterns (suggestions only) |
| [EXTR-043](EXTR-043.md) | P1 | 8 | todo | Unused custom field finder (no data, no references) |
| [EXTR-044](EXTR-044.md) | P1 | 8 | todo | Role/user cleanup assistant (disabled users, stale API keys, inactive roles) |
| [EXTR-045](EXTR-045.md) | P1 | 8 | todo | Stuck document finder (draft documents older than N days by doctype) |
| [EXTR-046](EXTR-046.md) | P1 | 8 | todo | Scheduled event log browser with filter by job |
| [EXTR-047](EXTR-047.md) | P1 | 8 | todo | Document timeline explorer (versions, comments, communications, shares) in one view |
| [EXTR-048](EXTR-048.md) | P1 | 8 | todo | Comment/assignment cleanup tools for departed users |
| [EXTR-049](EXTR-049.md) | P1 | 8 | todo | Reassign all open work from one user to another with preview |
| [EXTR-050](EXTR-050.md) | P1 | 8 | todo | Letterhead and company branding consistency checker |
| [EXTR-051](EXTR-051.md) | P2 | 11 | todo | Currency exchange rate fetch status and gaps checker |
| [EXTR-052](EXTR-052.md) | P2 | 11 | todo | Tax template audit (unused, inconsistent, missing accounts) |
| [EXTR-053](EXTR-053.md) | P2 | 11 | todo | Chart of accounts sanity report (ungrouped, wrong root types) |
| [EXTR-054](EXTR-054.md) | P2 | 11 | todo | Item master data quality (missing UOM, group, HSN-like codes, images) |
| [EXTR-055](EXTR-055.md) | P2 | 11 | todo | Customer/supplier data quality (missing phone, tax id, duplicates) |
| [EXTR-056](EXTR-056.md) | P2 | 11 | todo | Email template library manager with variable tester |
| [EXTR-057](EXTR-057.md) | P2 | 11 | todo | Print settings and paper-size presets manager |
| [EXTR-058](EXTR-058.md) | P2 | 11 | todo | Assignment rule and auto-repeat inventory with test-run |
| [EXTR-059](EXTR-059.md) | P2 | 11 | todo | Document naming audit (inconsistent naming rules across doctypes) |
| [EXTR-060](EXTR-060.md) | P2 | 11 | todo | Server/client script static analysis for risky patterns |
| [EXTR-061](EXTR-061.md) | P2 | 11 | todo | Dormant data report (records untouched for N months) with archive action |
| [EXTR-062](EXTR-062.md) | P2 | 11 | todo | GDPR-style data export/erase request handler per person |
| [EXTR-063](EXTR-063.md) | P2 | 11 | todo | Consent and privacy settings audit |
| [EXTR-064](EXTR-064.md) | P2 | 11 | todo | Admin changelog digest of config, permission and customization changes |
| [EXTR-065](EXTR-065.md) | P2 | 11 | todo | Site "go-live checklist" with automated verifications |
