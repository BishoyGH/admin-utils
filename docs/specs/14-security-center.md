---
code: SECU
title: "Security Center"
number: 14
status: draft
privileged: true
depends_on: [CORE]
code_path: admin_utils/security/
frontend_path: frontend/src/features/security/
tasks: docs/tasks/SECU/INDEX.md
---

# Spec 14 — Security Center (`SECU`)

## Purpose

Security Center: see feature groups below.

## Placement

- Python package: `admin_utils/security/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/security/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Security Center Settings`; on/off flag `enable_security` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/security/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 5 |
| P1 | 15 |
| P2 | 10 |

Waves: wave 1 (5), wave 4 (15), wave 11 (10)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [SECU-001](../tasks/SECU/SECU-001.md) | P0 | 1 | Security dashboard: score, open findings, trend |
| [SECU-002](../tasks/SECU/SECU-002.md) | P0 | 1 | Password policy review (length, complexity, expiry settings) with recommendations |
| [SECU-003](../tasks/SECU/SECU-003.md) | P0 | 1 | 2FA enforcement coverage and exemptions report |
| [SECU-004](../tasks/SECU/SECU-004.md) | P0 | 1 | Login security settings review (lockout, session timeout, IP restrictions) |
| [SECU-005](../tasks/SECU/SECU-005.md) | P0 | 1 | Admin/System Manager account inventory and activity summary |
| [SECU-006](../tasks/SECU/SECU-006.md) | P1 | 4 | Inactive user detection and auto-disable policy |
| [SECU-007](../tasks/SECU/SECU-007.md) | P1 | 4 | Shared account detector (multiple IPs/devices rapidly) |
| [SECU-008](../tasks/SECU/SECU-008.md) | P1 | 4 | API key and token inventory with last-used and owner |
| [SECU-009](../tasks/SECU/SECU-009.md) | P1 | 4 | Open guest-access check (doctypes/pages/methods exposed to Guest) |
| [SECU-010](../tasks/SECU/SECU-010.md) | P1 | 4 | Whitelisted method exposure scanner (allow_guest, unprotected methods) |
| [SECU-011](../tasks/SECU/SECU-011.md) | P1 | 4 | File exposure scan (public files that look private) |
| [SECU-012](../tasks/SECU/SECU-012.md) | P1 | 4 | Secrets-in-data scanner (tokens/passwords pasted into text fields, opt-in) |
| [SECU-013](../tasks/SECU/SECU-013.md) | P1 | 4 | Security headers and cookie flags check |
| [SECU-014](../tasks/SECU/SECU-014.md) | P1 | 4 | HTTPS/HSTS and certificate checks |
| [SECU-015](../tasks/SECU/SECU-015.md) | P1 | 4 | Dangerous settings check (developer mode, allow_tests, server scripts enabled) |
| [SECU-016](../tasks/SECU/SECU-016.md) | P1 | 4 | Server Script and Client Script risk review |
| [SECU-017](../tasks/SECU/SECU-017.md) | P1 | 4 | Webhook endpoint review (HTTP vs HTTPS, secrets configured) |
| [SECU-018](../tasks/SECU/SECU-018.md) | P1 | 4 | Audit trail anomaly detection (bulk deletes, off-hours admin actions) |
| [SECU-019](../tasks/SECU/SECU-019.md) | P1 | 4 | Failed login analytics with IP reputation hooks (local lists) |
| [SECU-020](../tasks/SECU/SECU-020.md) | P1 | 4 | Security findings workflow (open, accepted risk, fixed) with owner and due date |
| [SECU-021](../tasks/SECU/SECU-021.md) | P2 | 11 | Periodic security scan scheduler and report email |
| [SECU-022](../tasks/SECU/SECU-022.md) | P2 | 11 | Hardening checklist mapped to OWASP ASVS and CIS-style controls |
| [SECU-023](../tasks/SECU/SECU-023.md) | P2 | 11 | Security baseline snapshot and drift alerts |
| [SECU-024](../tasks/SECU/SECU-024.md) | P2 | 11 | Incident response playbook runner (lock user, rotate keys, revoke sessions) |
| [SECU-025](../tasks/SECU/SECU-025.md) | P2 | 11 | Emergency "lockdown mode" (read-only site, block non-admin logins) |
| [SECU-026](../tasks/SECU/SECU-026.md) | P2 | 11 | IP allowlist manager for admin routes |
| [SECU-027](../tasks/SECU/SECU-027.md) | P2 | 11 | Honeypot field/endpoint alerts (opt-in) |
| [SECU-028](../tasks/SECU/SECU-028.md) | P2 | 11 | Data classification tags per doctype/field (public, internal, confidential) |
| [SECU-029](../tasks/SECU/SECU-029.md) | P2 | 11 | Export of security evidence pack for audits |
| [SECU-030](../tasks/SECU/SECU-030.md) | P2 | 11 | Third-party app risk inventory (installed apps, versions, known advisories feed) |

## Tests

- No module-specific highlights beyond the shared strategy; follow the security matrix and Definition of Done.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Secrets leakage and privilege escalation: human gate on design and merge

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
