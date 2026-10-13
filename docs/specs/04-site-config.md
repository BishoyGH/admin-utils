---
code: CONF
title: "Site Config JSON Editor"
number: 04
status: draft
privileged: true
depends_on: [CORE]
code_path: admin_utils/siteconfig/
frontend_path: frontend/src/features/siteconfig/
tasks: docs/tasks/CONF/INDEX.md
---

# Spec 04 — Site Config JSON Editor (`CONF`)

## Purpose

Site Config JSON Editor: see feature groups below.

## Placement

- Python package: `admin_utils/siteconfig/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/siteconfig/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Site Config JSON Editor Settings`; on/off flag `enable_siteconfig` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/siteconfig/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 9 |
| P1 | 12 |
| P2 | 14 |

Waves: wave 4 (17), wave 9 (4), wave 11 (14)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [CONF-001](../tasks/CONF/CONF-001.md) | P0 | 4 | Read `site_config.json` (and `common_site_config.json` read-only) with secrets masked |
| [CONF-002](../tasks/CONF/CONF-002.md) | P0 | 4 | Structured form editor generated from a known-keys schema |
| [CONF-003](../tasks/CONF/CONF-003.md) | P0 | 4 | Raw JSON editor with schema validation and error hints |
| [CONF-004](../tasks/CONF/CONF-004.md) | P0 | 4 | Automatic timestamped backup before every write |
| [CONF-005](../tasks/CONF/CONF-005.md) | P0 | 4 | Diff preview before save |
| [CONF-006](../tasks/CONF/CONF-006.md) | P0 | 4 | Restore any previous config backup |
| [CONF-007](../tasks/CONF/CONF-007.md) | P0 | 4 | Key allowlist for editing; denylist for critical keys (db credentials, encryption_key) |
| [CONF-008](../tasks/CONF/CONF-008.md) | P0 | 4 | Atomic write (temp file + rename) and permission preservation |
| [CONF-009](../tasks/CONF/CONF-009.md) | P0 | 4 | Role gate `Admin Utils Config Editor` + audit log |
| [CONF-010](../tasks/CONF/CONF-010.md) | P1 | 4 | Known keys catalog with descriptions (maintenance_mode, developer_mode, host_name, mail settings, etc.) |
| [CONF-011](../tasks/CONF/CONF-011.md) | P1 | 4 | Type-aware inputs (bool, int, list, object) |
| [CONF-012](../tasks/CONF/CONF-012.md) | P1 | 4 | Reveal-secret action with re-authentication and audit entry |
| [CONF-013](../tasks/CONF/CONF-013.md) | P1 | 4 | Config templates (production hardening, dev-friendly) |
| [CONF-014](../tasks/CONF/CONF-014.md) | P1 | 4 | Validate hostnames, URLs, emails, ports |
| [CONF-015](../tasks/CONF/CONF-015.md) | P1 | 4 | Highlight keys that require restart/migrate/build after change |
| [CONF-016](../tasks/CONF/CONF-016.md) | P1 | 4 | Config comparison between two sites (if multi-site) |
| [CONF-017](../tasks/CONF/CONF-017.md) | P1 | 4 | Config lint: warns about insecure values (developer_mode on prod, weak settings) |
| [CONF-018](../tasks/CONF/CONF-018.md) | P2 | 11 | Config change history timeline with who/why |
| [CONF-019](../tasks/CONF/CONF-019.md) | P2 | 11 | Change reason required field |
| [CONF-020](../tasks/CONF/CONF-020.md) | P2 | 11 | Scheduled temporary config changes (auto-revert) |
| [CONF-021](../tasks/CONF/CONF-021.md) | P2 | 11 | Export/import config (secrets excluded by default) |
| [CONF-022](../tasks/CONF/CONF-022.md) | P2 | 11 | Drift detection (config changed outside the UI) |
| [CONF-023](../tasks/CONF/CONF-023.md) | P2 | 11 | Safe-mode lock to make config read-only |
| [CONF-024](../tasks/CONF/CONF-024.md) | P2 | 11 | Show effective config (site + common + environment overrides) |
| [CONF-025](../tasks/CONF/CONF-025.md) | P2 | 11 | Environment variable reference viewer (read-only) |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [CONF-026](../tasks/CONF/CONF-026.md) | P1 | 9 | Key-level permissions (some keys editable by senior admins only) |
| [CONF-027](../tasks/CONF/CONF-027.md) | P1 | 9 | Validation rules per key (ranges, enums, dependencies between keys) |
| [CONF-028](../tasks/CONF/CONF-028.md) | P1 | 9 | "Requires restart" tracker and pending-restart banner |
| [CONF-029](../tasks/CONF/CONF-029.md) | P1 | 9 | Config snapshot tagging ("before upgrade", "known good") |
| [CONF-030](../tasks/CONF/CONF-030.md) | P2 | 11 | Safe-edit sandbox: validate on a temp copy before writing |
| [CONF-031](../tasks/CONF/CONF-031.md) | P2 | 11 | Config inheritance viewer (common vs site) |
| [CONF-032](../tasks/CONF/CONF-032.md) | P2 | 11 | Alert on risky key changes (Slack/email) |
| [CONF-033](../tasks/CONF/CONF-033.md) | P2 | 11 | Config policy as code (YAML) enforced and drift-reported |
| [CONF-034](../tasks/CONF/CONF-034.md) | P2 | 11 | Rotation helper for generated secrets with staged rollout notes |
| [CONF-035](../tasks/CONF/CONF-035.md) | P2 | 11 | Key usage finder (which app reads which key, best effort static scan) |

## Tests

- atomic write under simulated crash, backup created before write, secret masking, restore works.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Secrets leakage: mask on read, atomic write, backup before write
- Bench misuse: same allowlist and approval rules as BNCH

## Privileged module gate

- Human approval on the **design** and on the **merge** (see `docs/checklists/privileged-review.md`).
- Security reviewer agent signs off; two reviewers; off by default behind a feature flag.
- Agents never receive production credentials; use disposable benches with seeded data.

## Sensitive data

- Masking happens centrally at read time; tests plant secrets/personal data and assert they never reach UI, exports, alerts or AI providers.

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
