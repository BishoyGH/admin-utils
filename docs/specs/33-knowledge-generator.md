---
code: KNOW
title: "Documentation & Knowledge Generator"
number: 33
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/knowledge/
frontend_path: frontend/src/features/knowledge/
tasks: docs/tasks/KNOW/INDEX.md
---

# Spec 33 — Documentation & Knowledge Generator (`KNOW`)

## Purpose

Documentation & Knowledge Generator: see feature groups below.

## Placement

- Python package: `admin_utils/knowledge/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/knowledge/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Documentation & Knowledge Generator Settings`; on/off flag `enable_knowledge` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/knowledge/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P1 | 7 |
| P2 | 13 |

Waves: wave 3 (7), wave 11 (13)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [KNOW-001](../tasks/KNOW/KNOW-001.md) | P1 | 3 | Site documentation generator: modules, doctypes, workflows, roles, reports, integrations |
| [KNOW-002](../tasks/KNOW/KNOW-002.md) | P1 | 3 | Role handbook per ladder level (what you can and cannot do), EN/AR |
| [KNOW-003](../tasks/KNOW/KNOW-003.md) | P1 | 3 | Workflow documentation with diagrams and responsible roles |
| [KNOW-004](../tasks/KNOW/KNOW-004.md) | P1 | 3 | Customization catalogue with purpose and owner (from GOVN registry) |
| [KNOW-005](../tasks/KNOW/KNOW-005.md) | P1 | 3 | Data dictionary pages generated from doctype metadata |
| [KNOW-006](../tasks/KNOW/KNOW-006.md) | P1 | 3 | Export documentation as Markdown, PDF or a static site |
| [KNOW-007](../tasks/KNOW/KNOW-007.md) | P1 | 3 | Publish documentation into the app's own help drawer |
| [KNOW-008](../tasks/KNOW/KNOW-008.md) | P2 | 11 | Screenshot automation for docs (Playwright-driven, seeded data) |
| [KNOW-009](../tasks/KNOW/KNOW-009.md) | P2 | 11 | Doc freshness checks (documentation older than the thing it describes) |
| [KNOW-010](../tasks/KNOW/KNOW-010.md) | P2 | 11 | Runbook and SOP library with owners and review dates |
| [KNOW-011](../tasks/KNOW/KNOW-011.md) | P2 | 11 | FAQ builder from recurring errors and support questions |
| [KNOW-012](../tasks/KNOW/KNOW-012.md) | P2 | 11 | Glossary shared with TRNS |
| [KNOW-013](../tasks/KNOW/KNOW-013.md) | P2 | 11 | Training material generator (slides outline, checklists) per role |
| [KNOW-014](../tasks/KNOW/KNOW-014.md) | P2 | 11 | Docs-as-code export into generated custom apps (via BLDR) |
| [KNOW-015](../tasks/KNOW/KNOW-015.md) | P2 | 11 | Link checker for documentation and in-app help |
| [KNOW-016](../tasks/KNOW/KNOW-016.md) | P2 | 11 | Versioned docs per release |
| [KNOW-017](../tasks/KNOW/KNOW-017.md) | P2 | 11 | Search across documentation with highlight |
| [KNOW-018](../tasks/KNOW/KNOW-018.md) | P2 | 11 | Contextual help mapping (page → doc article) |
| [KNOW-019](../tasks/KNOW/KNOW-019.md) | P2 | 11 | Feedback on articles ("was this helpful") with admin review queue |
| [KNOW-020](../tasks/KNOW/KNOW-020.md) | P2 | 11 | Auto-generated "what changed" pages after each promotion |

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
