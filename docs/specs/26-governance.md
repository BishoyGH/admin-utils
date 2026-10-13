---
code: GOVN
title: "Change Management & Governance"
number: 26
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/governance/
frontend_path: frontend/src/features/governance/
tasks: docs/tasks/GOVN/INDEX.md
---

# Spec 26 — Change Management & Governance (`GOVN`)

## Purpose

Change Management & Governance: see feature groups below.

## Placement

- Python package: `admin_utils/governance/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/governance/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Change Management & Governance Settings`; on/off flag `enable_governance` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/governance/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 3 |
| P1 | 13 |
| P2 | 14 |

Waves: wave 1 (13), wave 6 (3), wave 11 (14)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [GOVN-001](../tasks/GOVN/GOVN-001.md) | P0 | 1 | Change request doctype (title, reason, scope, risk, owner, planned window, rollback plan) |
| [GOVN-002](../tasks/GOVN/GOVN-002.md) | P0 | 1 | Link change requests to change sets, permission applies, bench runbooks and config edits |
| [GOVN-003](../tasks/GOVN/GOVN-003.md) | P0 | 1 | Approval workflow with configurable approvers per risk level |
| [GOVN-004](../tasks/GOVN/GOVN-004.md) | P1 | 1 | Risk scoring from the type and scope of change (permissions, config, bench = higher) |
| [GOVN-005](../tasks/GOVN/GOVN-005.md) | P1 | 6 | Change calendar with conflict detection and freeze periods |
| [GOVN-006](../tasks/GOVN/GOVN-006.md) | P1 | 6 | Emergency change path with mandatory post-review |
| [GOVN-007](../tasks/GOVN/GOVN-007.md) | P1 | 6 | Pre-implementation checklist and post-implementation verification checklist |
| [GOVN-008](../tasks/GOVN/GOVN-008.md) | P1 | 1 | Segregation of duties (author cannot approve or deploy their own change) |
| [GOVN-009](../tasks/GOVN/GOVN-009.md) | P1 | 1 | Automatic evidence capture (diffs, logs, screenshots, test results) attached to the request |
| [GOVN-010](../tasks/GOVN/GOVN-010.md) | P1 | 1 | Change history per object (who changed this role, workflow, config key and why) |
| [GOVN-011](../tasks/GOVN/GOVN-011.md) | P1 | 1 | Reason-required prompts on privileged edits across all modules |
| [GOVN-012](../tasks/GOVN/GOVN-012.md) | P1 | 1 | Policy library (naming rules, ladder rules, retention rules) as machine-checkable policies |
| [GOVN-013](../tasks/GOVN/GOVN-013.md) | P1 | 1 | Policy violation reports with owners and due dates |
| [GOVN-014](../tasks/GOVN/GOVN-014.md) | P1 | 1 | Exceptions register (approved deviations with expiry) |
| [GOVN-015](../tasks/GOVN/GOVN-015.md) | P1 | 1 | Review cycles for roles, workflows, scripts and integrations |
| [GOVN-016](../tasks/GOVN/GOVN-016.md) | P1 | 1 | Ownership registry (who owns each customization, report, workspace, script) |
| [GOVN-017](../tasks/GOVN/GOVN-017.md) | P2 | 11 | Orphaned-ownership detection when owners leave |
| [GOVN-018](../tasks/GOVN/GOVN-018.md) | P2 | 11 | Post-incident review template linked to MNTR incidents |
| [GOVN-019](../tasks/GOVN/GOVN-019.md) | P2 | 11 | Audit pack generator (changes in a period with approvals and evidence) |
| [GOVN-020](../tasks/GOVN/GOVN-020.md) | P2 | 11 | Auditor read-only portal with scoped access and expiry |
| [GOVN-021](../tasks/GOVN/GOVN-021.md) | P2 | 11 | Control library mapped to common frameworks (ISO 27001-style, SOC 2-style) as guidance |
| [GOVN-022](../tasks/GOVN/GOVN-022.md) | P2 | 11 | Control testing schedule and results |
| [GOVN-023](../tasks/GOVN/GOVN-023.md) | P2 | 11 | Compliance calendar (certificate renewals, key rotations, access reviews) |
| [GOVN-024](../tasks/GOVN/GOVN-024.md) | P2 | 11 | Data retention policies with enforcement jobs and legal-hold flags |
| [GOVN-025](../tasks/GOVN/GOVN-025.md) | P2 | 11 | Legal-hold manager that blocks deletion of selected records |
| [GOVN-026](../tasks/GOVN/GOVN-026.md) | P2 | 11 | Vendor/integration register with data-sharing notes |
| [GOVN-027](../tasks/GOVN/GOVN-027.md) | P2 | 11 | Risk register for the site itself (top risks, owners, mitigations) |
| [GOVN-028](../tasks/GOVN/GOVN-028.md) | P2 | 11 | Decision log (why a setting or structure was chosen) |
| [GOVN-029](../tasks/GOVN/GOVN-029.md) | P2 | 11 | Governance dashboard (open changes, overdue reviews, violations) |
| [GOVN-030](../tasks/GOVN/GOVN-030.md) | P2 | 11 | Quarterly governance report export |

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
