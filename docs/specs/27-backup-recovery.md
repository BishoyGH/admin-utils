---
code: BKUP
title: "Backup & Disaster Recovery"
number: 27
status: draft
privileged: true
depends_on: [CORE, BNCH]
code_path: admin_utils/backup/
frontend_path: frontend/src/features/backup/
tasks: docs/tasks/BKUP/INDEX.md
---

# Spec 27 — Backup & Disaster Recovery (`BKUP`)

## Purpose

Backup & Disaster Recovery: see feature groups below.

## Placement

- Python package: `admin_utils/backup/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/backup/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Backup & Disaster Recovery Settings`; on/off flag `enable_backup` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/backup/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 4 |
| P1 | 11 |
| P2 | 15 |

Waves: wave 4 (15), wave 11 (15)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`BNCH`](03-bench-commands.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [BKUP-001](../tasks/BKUP/BKUP-001.md) | P0 | 4 | Backup dashboard: last success, size, age, retention state per site |
| [BKUP-002](../tasks/BKUP/BKUP-002.md) | P0 | 4 | On-demand backup (database, public files, private files, config) via allowlisted runner |
| [BKUP-003](../tasks/BKUP/BKUP-003.md) | P0 | 4 | Backup list with checksums, size, creation time and verification state |
| [BKUP-004](../tasks/BKUP/BKUP-004.md) | P0 | 4 | Download protection (role, audit entry, optional re-authentication) |
| [BKUP-005](../tasks/BKUP/BKUP-005.md) | P1 | 4 | Schedule designer (hourly/daily/weekly) with windows and conflict checks |
| [BKUP-006](../tasks/BKUP/BKUP-006.md) | P1 | 4 | Retention policy (keep N daily, M weekly, K monthly) with dry-run |
| [BKUP-007](../tasks/BKUP/BKUP-007.md) | P1 | 4 | Offsite targets (S3-compatible, SFTP, cloud drives) with connection tests |
| [BKUP-008](../tasks/BKUP/BKUP-008.md) | P1 | 4 | Encryption at rest with key management guidance (keys never stored in the app) |
| [BKUP-009](../tasks/BKUP/BKUP-009.md) | P1 | 4 | Integrity verification (checksum compare, test decompress, DB dump sanity) |
| [BKUP-010](../tasks/BKUP/BKUP-010.md) | P1 | 4 | Automated restore test to a throwaway site with a pass/fail report |
| [BKUP-011](../tasks/BKUP/BKUP-011.md) | P1 | 4 | Restore wizard with preflight checks (version, free space, apps present) |
| [BKUP-012](../tasks/BKUP/BKUP-012.md) | P1 | 4 | Restore to a new site name for cloning or staging |
| [BKUP-013](../tasks/BKUP/BKUP-013.md) | P1 | 4 | Pre-change automatic backups wired into BNCH, CONF, PERM and MIGR |
| [BKUP-014](../tasks/BKUP/BKUP-014.md) | P1 | 4 | Failure alerts and missed-backup detection through NTFY |
| [BKUP-015](../tasks/BKUP/BKUP-015.md) | P1 | 4 | Storage usage forecast and quota alerts |
| [BKUP-016](../tasks/BKUP/BKUP-016.md) | P2 | 11 | Partial restore planner (single doctype or date range) using export, not raw SQL edits |
| [BKUP-017](../tasks/BKUP/BKUP-017.md) | P2 | 11 | Point-in-time recovery guidance and binlog status view (read-only) |
| [BKUP-018](../tasks/BKUP/BKUP-018.md) | P2 | 11 | RPO/RTO targets with a compliance dashboard |
| [BKUP-019](../tasks/BKUP/BKUP-019.md) | P2 | 11 | Disaster recovery runbook library (DB corruption, disk full, lost server) |
| [BKUP-020](../tasks/BKUP/BKUP-020.md) | P2 | 11 | DR drill scheduler with recorded results |
| [BKUP-021](../tasks/BKUP/BKUP-021.md) | P2 | 11 | Backup anomaly detection (sudden size drop or growth) |
| [BKUP-022](../tasks/BKUP/BKUP-022.md) | P2 | 11 | Sanitized backup export (anonymized) for support or testing |
| [BKUP-023](../tasks/BKUP/BKUP-023.md) | P2 | 11 | Backup catalog across multiple sites |
| [BKUP-024](../tasks/BKUP/BKUP-024.md) | P2 | 11 | Cost estimator for offsite storage |
| [BKUP-025](../tasks/BKUP/BKUP-025.md) | P2 | 11 | Backup immutability and object-lock status check |
| [BKUP-026](../tasks/BKUP/BKUP-026.md) | P2 | 11 | Offsite upload resume and bandwidth throttling |
| [BKUP-027](../tasks/BKUP/BKUP-027.md) | P2 | 11 | Backup tagging (before upgrade, month-end, audit) |
| [BKUP-028](../tasks/BKUP/BKUP-028.md) | P2 | 11 | Legal-hold backups exempt from retention cleanup |
| [BKUP-029](../tasks/BKUP/BKUP-029.md) | P2 | 11 | Backup restore time estimator from past tests |
| [BKUP-030](../tasks/BKUP/BKUP-030.md) | P2 | 11 | Evidence report for auditors (backups taken, tested, retained) |

## Tests

- automated restore test to a throwaway site proves every backup type is restorable; retention dry-runs never delete the newest valid backup.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Restore must be proven: automated restore test to a throwaway site; retention never deletes the newest valid backup

## Privileged module gate

- Human approval on the **design** and on the **merge** (see `docs/checklists/privileged-review.md`).
- Security reviewer agent signs off; two reviewers; off by default behind a feature flag.
- Agents never receive production credentials; use disposable benches with seeded data.

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
