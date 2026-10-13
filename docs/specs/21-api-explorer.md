---
code: APIX
title: "API Explorer & Integrations"
number: 21
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/api_explorer/
frontend_path: frontend/src/features/api_explorer/
tasks: docs/tasks/APIX/INDEX.md
---

# Spec 21 — API Explorer & Integrations (`APIX`)

## Purpose

API Explorer & Integrations: see feature groups below.

## Placement

- Python package: `admin_utils/api_explorer/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/api_explorer/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `API Explorer & Integrations Settings`; on/off flag `enable_api_explorer` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/api_explorer/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 1 |
| P1 | 10 |
| P2 | 9 |

Waves: wave 8 (11), wave 11 (9)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [APIX-001](../tasks/APIX/APIX-001.md) | P0 | 8 | API explorer for whitelisted methods and REST resources with try-it panel (permission-respecting) |
| [APIX-002](../tasks/APIX/APIX-002.md) | P1 | 8 | Auto-generated documentation from doctype metadata |
| [APIX-003](../tasks/APIX/APIX-003.md) | P1 | 8 | API key and secret management UI with scopes and expiry |
| [APIX-004](../tasks/APIX/APIX-004.md) | P1 | 8 | Request logs per key with latency and status |
| [APIX-005](../tasks/APIX/APIX-005.md) | P1 | 8 | Rate limit configuration per key/role |
| [APIX-006](../tasks/APIX/APIX-006.md) | P1 | 8 | Webhook designer (event, filter, payload template, secret) |
| [APIX-007](../tasks/APIX/APIX-007.md) | P1 | 8 | Webhook test tool with sample payload and response viewer |
| [APIX-008](../tasks/APIX/APIX-008.md) | P1 | 8 | Webhook delivery log with replay and failure reasons |
| [APIX-009](../tasks/APIX/APIX-009.md) | P1 | 8 | Payload template safe preview (no arbitrary code) |
| [APIX-010](../tasks/APIX/APIX-010.md) | P1 | 8 | OpenAPI export for custom endpoints and doctypes |
| [APIX-011](../tasks/APIX/APIX-011.md) | P1 | 8 | Postman/Insomnia collection export |
| [APIX-012](../tasks/APIX/APIX-012.md) | P2 | 11 | Sandbox mode returning seeded data only |
| [APIX-013](../tasks/APIX/APIX-013.md) | P2 | 11 | API deprecation tracker for custom endpoints |
| [APIX-014](../tasks/APIX/APIX-014.md) | P2 | 11 | Idempotency and retry guidance viewer |
| [APIX-015](../tasks/APIX/APIX-015.md) | P2 | 11 | IP allowlist per API key |
| [APIX-016](../tasks/APIX/APIX-016.md) | P2 | 11 | OAuth client inventory and review |
| [APIX-017](../tasks/APIX/APIX-017.md) | P2 | 11 | Inbound webhook receiver registry with signature verification |
| [APIX-018](../tasks/APIX/APIX-018.md) | P2 | 11 | Integration connectors catalog (read-only status, config checklist) |
| [APIX-019](../tasks/APIX/APIX-019.md) | P2 | 11 | API usage analytics by endpoint/key |
| [APIX-020](../tasks/APIX/APIX-020.md) | P2 | 11 | Contract tests generated from OpenAPI export |

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
