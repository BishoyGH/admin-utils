---
code: AIAS
title: "Assistive Intelligence Layer"
number: 32
status: draft
privileged: true
depends_on: [CORE, GOVN]
code_path: admin_utils/assist/
frontend_path: frontend/src/features/assist/
tasks: docs/tasks/AIAS/INDEX.md
---

# Spec 32 — Assistive Intelligence Layer (`AIAS`)

## Purpose

All assistive features are optional, off by default, provider-pluggable, and never write changes without a human-approved preview.

## Placement

- Python package: `admin_utils/assist/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/assist/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Assistive Intelligence Layer Settings`; on/off flag `enable_assist` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/assist/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P1 | 10 |
| P2 | 20 |

Waves: wave 9 (10), wave 11 (20)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`GOVN`](26-governance.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [AIAS-001](../tasks/AIAS/AIAS-001.md) | P1 | 9 | Provider abstraction with allowlisted endpoints, timeouts and cost limits |
| [AIAS-002](../tasks/AIAS/AIAS-002.md) | P1 | 9 | Data-minimization layer (what leaves the server is configurable, secrets and personal data masked) |
| [AIAS-003](../tasks/AIAS/AIAS-003.md) | P1 | 9 | Prompt and response audit log with retention controls |
| [AIAS-004](../tasks/AIAS/AIAS-004.md) | P1 | 9 | Explain-this-permission: plain-language reasoning from the PERM trace |
| [AIAS-005](../tasks/AIAS/AIAS-005.md) | P1 | 9 | Draft a report from a description, shown as a reviewable REPT definition |
| [AIAS-006](../tasks/AIAS/AIAS-006.md) | P1 | 9 | Explain a query or script in plain language and flag risks |
| [AIAS-007](../tasks/AIAS/AIAS-007.md) | P1 | 9 | Suggest translations with glossary enforcement, reviewed in TRNS workflow |
| [AIAS-008](../tasks/AIAS/AIAS-008.md) | P1 | 9 | Draft automation rules from a description, shown in the rule builder preview |
| [AIAS-009](../tasks/AIAS/AIAS-009.md) | P1 | 9 | Summarize error groups and propose likely causes |
| [AIAS-010](../tasks/AIAS/AIAS-010.md) | P1 | 9 | Summarize audit and change history for a period |
| [AIAS-011](../tasks/AIAS/AIAS-011.md) | P2 | 11 | Suggest a ladder level for a custom role from its permissions |
| [AIAS-012](../tasks/AIAS/AIAS-012.md) | P2 | 11 | Suggest workspace layout for a role from usage patterns |
| [AIAS-013](../tasks/AIAS/AIAS-013.md) | P2 | 11 | Draft onboarding flows from a module's doctypes |
| [AIAS-014](../tasks/AIAS/AIAS-014.md) | P2 | 11 | Draft documentation pages for customizations in EN/AR |
| [AIAS-015](../tasks/AIAS/AIAS-015.md) | P2 | 11 | Draft change request descriptions and risk notes from diffs |
| [AIAS-016](../tasks/AIAS/AIAS-016.md) | P2 | 11 | Natural-language search across settings, roles, customizations |
| [AIAS-017](../tasks/AIAS/AIAS-017.md) | P2 | 11 | Admin Q&A chat scoped to read-only diagnostics (no tool use that mutates) |
| [AIAS-018](../tasks/AIAS/AIAS-018.md) | P2 | 11 | Anomaly narration for MNTR and SECU alerts |
| [AIAS-019](../tasks/AIAS/AIAS-019.md) | P2 | 11 | Test case suggestions for new customizations (feeds TSTD) |
| [AIAS-020](../tasks/AIAS/AIAS-020.md) | P2 | 11 | Data-quality suggestions (likely duplicates, odd values) with human merge |
| [AIAS-021](../tasks/AIAS/AIAS-021.md) | P2 | 11 | Seeder scenario drafting from a business description |
| [AIAS-022](../tasks/AIAS/AIAS-022.md) | P2 | 11 | Print format drafting from a sample document image or description |
| [AIAS-023](../tasks/AIAS/AIAS-023.md) | P2 | 11 | Migration risk review of a change set before approval |
| [AIAS-024](../tasks/AIAS/AIAS-024.md) | P2 | 11 | Release notes drafting (EN/AR) from change sets |
| [AIAS-025](../tasks/AIAS/AIAS-025.md) | P2 | 11 | Evaluation harness (golden prompts and expected structures) to guard assistive quality |
| [AIAS-026](../tasks/AIAS/AIAS-026.md) | P2 | 11 | Per-feature opt-in and per-role access to assistive tools |
| [AIAS-027](../tasks/AIAS/AIAS-027.md) | P2 | 11 | Cost and usage dashboard for assistive calls |
| [AIAS-028](../tasks/AIAS/AIAS-028.md) | P2 | 11 | Offline/local model provider option |
| [AIAS-029](../tasks/AIAS/AIAS-029.md) | P2 | 11 | Prompt template library managed under GOVN policies |
| [AIAS-030](../tasks/AIAS/AIAS-030.md) | P2 | 11 | Safety filters for generated code and SQL (static checks before preview) |

## Tests

- golden-prompt evaluation harness; data-minimization tests prove masked fields never leave the server; generated SQL/code passes static safety filters before preview.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Assistive layer leaking data to providers: data minimisation, masking, allowlisted endpoints, opt-in per feature
- AI-agent mistakes in privileged modules: contracts first, human gate

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
