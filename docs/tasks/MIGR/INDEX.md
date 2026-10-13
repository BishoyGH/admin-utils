# MIGR — Environment Promotion & Sync: tasks

Spec: [`25-environment-promotion.md`](../../specs/25-environment-promotion.md) · 30 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [MIGR-001](MIGR-001.md) | P0 | 6 | todo | Environment registry (dev, staging, prod) with role, URL and policy per environment |
| [MIGR-002](MIGR-002.md) | P0 | 6 | todo | Change set object: a named, versioned bundle of customizations, permissions, workspaces, translations |
| [MIGR-003](MIGR-003.md) | P0 | 6 | todo | Build a change set from a selection or from a BLDR export |
| [MIGR-004](MIGR-004.md) | P0 | 6 | todo | Change set dry-run on the target (what would be created, updated, removed) |
| [MIGR-005](MIGR-005.md) | P0 | 6 | todo | Secrets and site-specific values excluded or replaced by placeholders |
| [MIGR-006](MIGR-006.md) | P1 | 6 | todo | Apply with automatic backup and snapshot of touched records |
| [MIGR-007](MIGR-007.md) | P1 | 6 | todo | One-click rollback of an applied change set |
| [MIGR-008](MIGR-008.md) | P1 | 6 | todo | Ordered application (roles before permissions, doctypes before custom fields, workflows after states) |
| [MIGR-009](MIGR-009.md) | P1 | 6 | todo | Conflict resolution UI (target changed independently: keep, overwrite, merge) |
| [MIGR-010](MIGR-010.md) | P1 | 6 | todo | Compare environments side by side (customizations, roles, settings, installed apps) |
| [MIGR-011](MIGR-011.md) | P1 | 6 | todo | Post-apply verification checks and smoke tests |
| [MIGR-012](MIGR-012.md) | P1 | 6 | todo | Approval gates by environment (prod requires an approver who is not the author) |
| [MIGR-013](MIGR-013.md) | P1 | 6 | todo | Deployment windows and freeze periods |
| [MIGR-014](MIGR-014.md) | P1 | 6 | todo | Promotion history with who, what, when and result |
| [MIGR-015](MIGR-015.md) | P1 | 6 | todo | Environment drift report (prod changed directly outside promotion) |
| [MIGR-016](MIGR-016.md) | P1 | 6 | todo | Transport over a signed package file (no direct site-to-site credentials required) |
| [MIGR-017](MIGR-017.md) | P2 | 11 | todo | Optional direct push between sites using scoped API credentials with allowlisted endpoints |
| [MIGR-018](MIGR-018.md) | P2 | 11 | todo | Partial promotion (select a subset of a change set) |
| [MIGR-019](MIGR-019.md) | P2 | 11 | todo | Change set templates ("new workflow", "new report pack") |
| [MIGR-020](MIGR-020.md) | P2 | 11 | todo | Automatic change-set creation from monitored customization edits (draft only) |
| [MIGR-021](MIGR-021.md) | P2 | 11 | todo | Version pinning of target app versions before apply |
| [MIGR-022](MIGR-022.md) | P2 | 11 | todo | Canary promotion (apply to a clone first, run checks, then the real site) |
| [MIGR-023](MIGR-023.md) | P2 | 11 | todo | Environment health gate (don't promote while alerts are open) |
| [MIGR-024](MIGR-024.md) | P2 | 11 | todo | Release notes generation from change sets (EN/AR) |
| [MIGR-025](MIGR-025.md) | P2 | 11 | todo | Scheduled promotions with notification |
| [MIGR-026](MIGR-026.md) | P2 | 11 | todo | Cross-version promotion warnings (v15 source to v16 target schema differences) |
| [MIGR-027](MIGR-027.md) | P2 | 11 | todo | Environment-specific variable sets (URLs, emails, feature flags) applied during promotion |
| [MIGR-028](MIGR-028.md) | P2 | 11 | todo | Promotion analytics (frequency, failure rate, time-to-prod) |
| [MIGR-029](MIGR-029.md) | P2 | 11 | todo | Signed change sets with verification before apply |
| [MIGR-030](MIGR-030.md) | P2 | 11 | todo | Disaster-style "rebuild from change sets" mode that recreates a site's customizations from history |
