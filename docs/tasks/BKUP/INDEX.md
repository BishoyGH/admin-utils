# BKUP — Backup & Disaster Recovery: tasks

Spec: [`27-backup-recovery.md`](../../specs/27-backup-recovery.md) · 30 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [BKUP-001](BKUP-001.md) | P0 | 4 | todo | Backup dashboard: last success, size, age, retention state per site |
| [BKUP-002](BKUP-002.md) | P0 | 4 | todo | On-demand backup (database, public files, private files, config) via allowlisted runner |
| [BKUP-003](BKUP-003.md) | P0 | 4 | todo | Backup list with checksums, size, creation time and verification state |
| [BKUP-004](BKUP-004.md) | P0 | 4 | todo | Download protection (role, audit entry, optional re-authentication) |
| [BKUP-005](BKUP-005.md) | P1 | 4 | todo | Schedule designer (hourly/daily/weekly) with windows and conflict checks |
| [BKUP-006](BKUP-006.md) | P1 | 4 | todo | Retention policy (keep N daily, M weekly, K monthly) with dry-run |
| [BKUP-007](BKUP-007.md) | P1 | 4 | todo | Offsite targets (S3-compatible, SFTP, cloud drives) with connection tests |
| [BKUP-008](BKUP-008.md) | P1 | 4 | todo | Encryption at rest with key management guidance (keys never stored in the app) |
| [BKUP-009](BKUP-009.md) | P1 | 4 | todo | Integrity verification (checksum compare, test decompress, DB dump sanity) |
| [BKUP-010](BKUP-010.md) | P1 | 4 | todo | Automated restore test to a throwaway site with a pass/fail report |
| [BKUP-011](BKUP-011.md) | P1 | 4 | todo | Restore wizard with preflight checks (version, free space, apps present) |
| [BKUP-012](BKUP-012.md) | P1 | 4 | todo | Restore to a new site name for cloning or staging |
| [BKUP-013](BKUP-013.md) | P1 | 4 | todo | Pre-change automatic backups wired into BNCH, CONF, PERM and MIGR |
| [BKUP-014](BKUP-014.md) | P1 | 4 | todo | Failure alerts and missed-backup detection through NTFY |
| [BKUP-015](BKUP-015.md) | P1 | 4 | todo | Storage usage forecast and quota alerts |
| [BKUP-016](BKUP-016.md) | P2 | 11 | todo | Partial restore planner (single doctype or date range) using export, not raw SQL edits |
| [BKUP-017](BKUP-017.md) | P2 | 11 | todo | Point-in-time recovery guidance and binlog status view (read-only) |
| [BKUP-018](BKUP-018.md) | P2 | 11 | todo | RPO/RTO targets with a compliance dashboard |
| [BKUP-019](BKUP-019.md) | P2 | 11 | todo | Disaster recovery runbook library (DB corruption, disk full, lost server) |
| [BKUP-020](BKUP-020.md) | P2 | 11 | todo | DR drill scheduler with recorded results |
| [BKUP-021](BKUP-021.md) | P2 | 11 | todo | Backup anomaly detection (sudden size drop or growth) |
| [BKUP-022](BKUP-022.md) | P2 | 11 | todo | Sanitized backup export (anonymized) for support or testing |
| [BKUP-023](BKUP-023.md) | P2 | 11 | todo | Backup catalog across multiple sites |
| [BKUP-024](BKUP-024.md) | P2 | 11 | todo | Cost estimator for offsite storage |
| [BKUP-025](BKUP-025.md) | P2 | 11 | todo | Backup immutability and object-lock status check |
| [BKUP-026](BKUP-026.md) | P2 | 11 | todo | Offsite upload resume and bandwidth throttling |
| [BKUP-027](BKUP-027.md) | P2 | 11 | todo | Backup tagging (before upgrade, month-end, audit) |
| [BKUP-028](BKUP-028.md) | P2 | 11 | todo | Legal-hold backups exempt from retention cleanup |
| [BKUP-029](BKUP-029.md) | P2 | 11 | todo | Backup restore time estimator from past tests |
| [BKUP-030](BKUP-030.md) | P2 | 11 | todo | Evidence report for auditors (backups taken, tested, retained) |
