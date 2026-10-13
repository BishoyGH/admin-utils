---
code: QAUT
title: "Built-in Self-Test & Diagnostics"
number: 23
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/selftest/
frontend_path: frontend/src/features/selftest/
tasks: docs/tasks/QAUT/INDEX.md
---

# Spec 23 — Built-in Self-Test & Diagnostics (`QAUT`)

## Purpose

Built-in Self-Test & Diagnostics: see feature groups below.

## Placement

- Python package: `admin_utils/selftest/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/selftest/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Built-in Self-Test & Diagnostics Settings`; on/off flag `enable_selftest` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/selftest/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 2 |
| P1 | 8 |
| P2 | 5 |

Waves: wave 0 (2), wave 9 (8), wave 11 (5)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [QAUT-001](../tasks/QAUT/QAUT-001.md) | P0 | 0 | In-app "Self-test" page running safe diagnostics for every enabled module |
| [QAUT-002](../tasks/QAUT/QAUT-002.md) | P0 | 0 | Environment compatibility report (Frappe version, DB, Python, Node, required apps) |
| [QAUT-003](../tasks/QAUT/QAUT-003.md) | P1 | 9 | Permission smoke test per ladder level using temporary test users (cleaned up after) |
| [QAUT-004](../tasks/QAUT/QAUT-004.md) | P1 | 9 | Guard coverage checker (every endpoint protected and flagged) |
| [QAUT-005](../tasks/QAUT/QAUT-005.md) | P1 | 9 | Audit coverage checker (every mutating action logs) |
| [QAUT-006](../tasks/QAUT/QAUT-006.md) | P1 | 9 | Secrets masking self-check |
| [QAUT-007](../tasks/QAUT/QAUT-007.md) | P1 | 9 | Job system health test (enqueue → run → result) |
| [QAUT-008](../tasks/QAUT/QAUT-008.md) | P1 | 9 | Realtime channel test |
| [QAUT-009](../tasks/QAUT/QAUT-009.md) | P1 | 9 | Config backup/restore round-trip test on a temp file |
| [QAUT-010](../tasks/QAUT/QAUT-010.md) | P1 | 9 | Seeder round-trip test (seed small batch, verify, delete) |
| [QAUT-011](../tasks/QAUT/QAUT-011.md) | P2 | 11 | Diagnostics bundle export (sanitized) for support |
| [QAUT-012](../tasks/QAUT/QAUT-012.md) | P2 | 11 | Post-upgrade verification suite triggered by `after_migrate` |
| [QAUT-013](../tasks/QAUT/QAUT-013.md) | P2 | 11 | Scheduled self-test with alert on regression |
| [QAUT-014](../tasks/QAUT/QAUT-014.md) | P2 | 11 | Contract checks against core doctype schemas used by the app |
| [QAUT-015](../tasks/QAUT/QAUT-015.md) | P2 | 11 | Accessibility self-audit (axe) runnable from admin UI on key pages |

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
