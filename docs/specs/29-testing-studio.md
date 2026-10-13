---
code: TSTD
title: "Testing Studio"
number: 29
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/teststudio/
frontend_path: frontend/src/features/teststudio/
tasks: docs/tasks/TSTD/INDEX.md
---

# Spec 29 — Testing Studio (`TSTD`)

## Purpose

Testing Studio: see feature groups below.

## Placement

- Python package: `admin_utils/teststudio/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/teststudio/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Testing Studio Settings`; on/off flag `enable_teststudio` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/teststudio/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 3 |
| P1 | 11 |
| P2 | 11 |

Waves: wave 2 (6), wave 6 (10), wave 11 (9)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [TSTD-001](../tasks/TSTD/TSTD-001.md) | P0 | 6 | Test registry listing generated and hand-written tests per app and module |
| [TSTD-002](../tasks/TSTD/TSTD-002.md) | P0 | 2 | Run backend tests from the UI as background jobs with live output (test sites only) |
| [TSTD-003](../tasks/TSTD/TSTD-003.md) | P0 | 2 | Hard block on running destructive tests against production-flagged environments |
| [TSTD-004](../tasks/TSTD/TSTD-004.md) | P1 | 6 | Generate permission tests from the PERM ladder matrix |
| [TSTD-005](../tasks/TSTD/TSTD-005.md) | P1 | 6 | Generate workflow tests from workflow definitions (every transition, allowed and denied) |
| [TSTD-006](../tasks/TSTD/TSTD-006.md) | P1 | 6 | Generate validation tests from mandatory, unique and link rules per doctype |
| [TSTD-007](../tasks/TSTD/TSTD-007.md) | P1 | 6 | Generate report tests (runs without error, totals reconcile against fixtures) |
| [TSTD-008](../tasks/TSTD/TSTD-008.md) | P1 | 6 | Generate print format render tests (renders, page count, no template errors) |
| [TSTD-009](../tasks/TSTD/TSTD-009.md) | P1 | 6 | Generate notification and automation rule tests with simulated events |
| [TSTD-010](../tasks/TSTD/TSTD-010.md) | P1 | 2 | Test data builders backed by the DATA seeder (deterministic) |
| [TSTD-011](../tasks/TSTD/TSTD-011.md) | P1 | 2 | Test results history with trends, flaky-test detection and failure grouping |
| [TSTD-012](../tasks/TSTD/TSTD-012.md) | P1 | 6 | Export generated tests into a target custom app (via BLDR) in the right folders |
| [TSTD-013](../tasks/TSTD/TSTD-013.md) | P1 | 2 | Customization coverage view (which customizations have tests) |
| [TSTD-014](../tasks/TSTD/TSTD-014.md) | P1 | 2 | Pre-promotion test gate in MIGR (block if tests fail) |
| [TSTD-015](../tasks/TSTD/TSTD-015.md) | P2 | 11 | E2E flow recorder that produces Playwright specs for common admin journeys |
| [TSTD-016](../tasks/TSTD/TSTD-016.md) | P2 | 11 | Visual snapshot management (approve, reject, diff) for pages and print formats |
| [TSTD-017](../tasks/TSTD/TSTD-017.md) | P2 | 11 | Accessibility test runner against key pages |
| [TSTD-018](../tasks/TSTD/TSTD-018.md) | P2 | 11 | Security test pack runner (authz matrix, injection payloads on custom endpoints) |
| [TSTD-019](../tasks/TSTD/TSTD-019.md) | P2 | 6 | Load test scenario generator from seeded data profiles |
| [TSTD-020](../tasks/TSTD/TSTD-020.md) | P2 | 11 | Mutation-style checks for permission rules (flip a flag, tests must fail) |
| [TSTD-021](../tasks/TSTD/TSTD-021.md) | P2 | 11 | Test environment provisioner (clone and seed a throwaway site) |
| [TSTD-022](../tasks/TSTD/TSTD-022.md) | P2 | 11 | Scheduled regression runs with NTFY alerts |
| [TSTD-023](../tasks/TSTD/TSTD-023.md) | P2 | 11 | Test impact analysis (which tests to run for a given change set) |
| [TSTD-024](../tasks/TSTD/TSTD-024.md) | P2 | 6 | Test documentation generator (what is covered, what is not) |
| [TSTD-025](../tasks/TSTD/TSTD-025.md) | P2 | 11 | Export results as JUnit/HTML for external CI |

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
