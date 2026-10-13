---
code: MIGR
title: "Environment Promotion & Sync"
number: 25
status: draft
privileged: true
depends_on: [CORE, BLDR, GOVN, BKUP, TSTD]
code_path: admin_utils/promotion/
frontend_path: frontend/src/features/promotion/
tasks: docs/tasks/MIGR/INDEX.md
---

# Spec 25 — Environment Promotion & Sync (`MIGR`)

## Purpose

Environment Promotion & Sync: see feature groups below.

## Placement

- Python package: `admin_utils/promotion/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/promotion/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Environment Promotion & Sync Settings`; on/off flag `enable_promotion` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/promotion/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 5 |
| P1 | 11 |
| P2 | 14 |

Waves: wave 6 (16), wave 11 (14)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`BLDR`](24-app-builder.md) must provide what this module consumes before dependent tasks start
- [`GOVN`](26-governance.md) must provide what this module consumes before dependent tasks start
- [`BKUP`](27-backup-recovery.md) must provide what this module consumes before dependent tasks start
- [`TSTD`](29-testing-studio.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [MIGR-001](../tasks/MIGR/MIGR-001.md) | P0 | 6 | Environment registry (dev, staging, prod) with role, URL and policy per environment |
| [MIGR-002](../tasks/MIGR/MIGR-002.md) | P0 | 6 | Change set object: a named, versioned bundle of customizations, permissions, workspaces, translations |
| [MIGR-003](../tasks/MIGR/MIGR-003.md) | P0 | 6 | Build a change set from a selection or from a BLDR export |
| [MIGR-004](../tasks/MIGR/MIGR-004.md) | P0 | 6 | Change set dry-run on the target (what would be created, updated, removed) |
| [MIGR-005](../tasks/MIGR/MIGR-005.md) | P0 | 6 | Secrets and site-specific values excluded or replaced by placeholders |
| [MIGR-006](../tasks/MIGR/MIGR-006.md) | P1 | 6 | Apply with automatic backup and snapshot of touched records |
| [MIGR-007](../tasks/MIGR/MIGR-007.md) | P1 | 6 | One-click rollback of an applied change set |
| [MIGR-008](../tasks/MIGR/MIGR-008.md) | P1 | 6 | Ordered application (roles before permissions, doctypes before custom fields, workflows after states) |
| [MIGR-009](../tasks/MIGR/MIGR-009.md) | P1 | 6 | Conflict resolution UI (target changed independently: keep, overwrite, merge) |
| [MIGR-010](../tasks/MIGR/MIGR-010.md) | P1 | 6 | Compare environments side by side (customizations, roles, settings, installed apps) |
| [MIGR-011](../tasks/MIGR/MIGR-011.md) | P1 | 6 | Post-apply verification checks and smoke tests |
| [MIGR-012](../tasks/MIGR/MIGR-012.md) | P1 | 6 | Approval gates by environment (prod requires an approver who is not the author) |
| [MIGR-013](../tasks/MIGR/MIGR-013.md) | P1 | 6 | Deployment windows and freeze periods |
| [MIGR-014](../tasks/MIGR/MIGR-014.md) | P1 | 6 | Promotion history with who, what, when and result |
| [MIGR-015](../tasks/MIGR/MIGR-015.md) | P1 | 6 | Environment drift report (prod changed directly outside promotion) |
| [MIGR-016](../tasks/MIGR/MIGR-016.md) | P1 | 6 | Transport over a signed package file (no direct site-to-site credentials required) |
| [MIGR-017](../tasks/MIGR/MIGR-017.md) | P2 | 11 | Optional direct push between sites using scoped API credentials with allowlisted endpoints |
| [MIGR-018](../tasks/MIGR/MIGR-018.md) | P2 | 11 | Partial promotion (select a subset of a change set) |
| [MIGR-019](../tasks/MIGR/MIGR-019.md) | P2 | 11 | Change set templates ("new workflow", "new report pack") |
| [MIGR-020](../tasks/MIGR/MIGR-020.md) | P2 | 11 | Automatic change-set creation from monitored customization edits (draft only) |
| [MIGR-021](../tasks/MIGR/MIGR-021.md) | P2 | 11 | Version pinning of target app versions before apply |
| [MIGR-022](../tasks/MIGR/MIGR-022.md) | P2 | 11 | Canary promotion (apply to a clone first, run checks, then the real site) |
| [MIGR-023](../tasks/MIGR/MIGR-023.md) | P2 | 11 | Environment health gate (don't promote while alerts are open) |
| [MIGR-024](../tasks/MIGR/MIGR-024.md) | P2 | 11 | Release notes generation from change sets (EN/AR) |
| [MIGR-025](../tasks/MIGR/MIGR-025.md) | P2 | 11 | Scheduled promotions with notification |
| [MIGR-026](../tasks/MIGR/MIGR-026.md) | P2 | 11 | Cross-version promotion warnings (v15 source to v16 target schema differences) |
| [MIGR-027](../tasks/MIGR/MIGR-027.md) | P2 | 11 | Environment-specific variable sets (URLs, emails, feature flags) applied during promotion |
| [MIGR-028](../tasks/MIGR/MIGR-028.md) | P2 | 11 | Promotion analytics (frequency, failure rate, time-to-prod) |
| [MIGR-029](../tasks/MIGR/MIGR-029.md) | P2 | 11 | Signed change sets with verification before apply |
| [MIGR-030](../tasks/MIGR/MIGR-030.md) | P2 | 11 | Disaster-style "rebuild from change sets" mode that recreates a site's customizations from history |

## Tests

- generated apps install and pass their own CI on v15 and v16; re-export is idempotent (zero diff); AST-based `hooks.py` edits preserve unrelated content; the sensitive-data scan catches planted secrets; promote then rollback restores the exact prior state.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- App installation on production: environment-policy block, approvals, mandatory backup, canary on a clone

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
