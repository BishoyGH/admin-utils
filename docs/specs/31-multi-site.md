---
code: MSIT
title: "Multi-Site & Multi-Company Management"
number: 31
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/multisite/
frontend_path: frontend/src/features/multisite/
tasks: docs/tasks/MSIT/INDEX.md
---

# Spec 31 — Multi-Site & Multi-Company Management (`MSIT`)

## Purpose

Multi-Site & Multi-Company Management: see feature groups below.

## Placement

- Python package: `admin_utils/multisite/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/multisite/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Multi-Site & Multi-Company Management Settings`; on/off flag `enable_multisite` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/multisite/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P1 | 10 |
| P2 | 15 |

Waves: wave 9 (10), wave 11 (15)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [MSIT-001](../tasks/MSIT/MSIT-001.md) | P1 | 9 | Site registry for all sites on a bench with status, apps, versions and owners |
| [MSIT-002](../tasks/MSIT/MSIT-002.md) | P1 | 9 | Cross-site health overview (backups, jobs, alerts, versions) |
| [MSIT-003](../tasks/MSIT/MSIT-003.md) | P1 | 9 | Site comparison (apps, settings, roles, customizations) |
| [MSIT-004](../tasks/MSIT/MSIT-004.md) | P1 | 9 | New-site provisioning wizard through allowlisted bench commands |
| [MSIT-005](../tasks/MSIT/MSIT-005.md) | P1 | 9 | Site templates (apps, settings, roles, ladder, workspaces, theme, seed profile) |
| [MSIT-006](../tasks/MSIT/MSIT-006.md) | P1 | 9 | Site clone workflow (backup, restore under new name, anonymize, reconfigure) |
| [MSIT-007](../tasks/MSIT/MSIT-007.md) | P1 | 9 | Company setup wizard (chart of accounts, fiscal year, defaults, warehouses) |
| [MSIT-008](../tasks/MSIT/MSIT-008.md) | P1 | 9 | Company defaults checker (missing accounts, cost centers, tax templates) |
| [MSIT-009](../tasks/MSIT/MSIT-009.md) | P1 | 9 | Per-company permission scoping templates (links PERM-035/098) |
| [MSIT-010](../tasks/MSIT/MSIT-010.md) | P1 | 9 | Per-company theme, print and translation settings (links THEM, PRNT, TRNS) |
| [MSIT-011](../tasks/MSIT/MSIT-011.md) | P2 | 11 | Tenant onboarding pipeline (provision, apply template, seed demo, hand over) |
| [MSIT-012](../tasks/MSIT/MSIT-012.md) | P2 | 11 | Bulk operations across sites (run an approved runbook on a selected set) |
| [MSIT-013](../tasks/MSIT/MSIT-013.md) | P2 | 11 | Staggered rollout (apply a change set to sites in waves) |
| [MSIT-014](../tasks/MSIT/MSIT-014.md) | P2 | 11 | Site retirement workflow (final backup, DNS checklist, data deletion proof) |
| [MSIT-015](../tasks/MSIT/MSIT-015.md) | P2 | 11 | Site-level feature flags for this app's modules |
| [MSIT-016](../tasks/MSIT/MSIT-016.md) | P2 | 11 | Site tagging and grouping (customer, region, tier) |
| [MSIT-017](../tasks/MSIT/MSIT-017.md) | P2 | 11 | Version skew report (sites on different app versions) |
| [MSIT-018](../tasks/MSIT/MSIT-018.md) | P2 | 11 | Site resource usage ranking |
| [MSIT-019](../tasks/MSIT/MSIT-019.md) | P2 | 11 | Cross-site user directory (where does this person have access) |
| [MSIT-020](../tasks/MSIT/MSIT-020.md) | P2 | 11 | Cross-site audit search |
| [MSIT-021](../tasks/MSIT/MSIT-021.md) | P2 | 11 | Billing/usage export per site for hosting operators |
| [MSIT-022](../tasks/MSIT/MSIT-022.md) | P2 | 11 | Domain and SSL inventory per site |
| [MSIT-023](../tasks/MSIT/MSIT-023.md) | P2 | 11 | Site migration assistant (move site to a new bench or server with checks) |
| [MSIT-024](../tasks/MSIT/MSIT-024.md) | P2 | 11 | Multi-bench awareness (read-only registry of other benches via agent) |
| [MSIT-025](../tasks/MSIT/MSIT-025.md) | P2 | 11 | Hosted-customer self-service portal (limited actions with strict scopes) |

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
