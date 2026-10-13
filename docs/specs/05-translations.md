---
code: TRNS
title: "Scoped Translation System"
number: 05
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/translations/
frontend_path: frontend/src/features/translations/
tasks: docs/tasks/TRNS/INDEX.md
---

# Spec 05 — Scoped Translation System (`TRNS`)

## Purpose

Scoped Translation System: see feature groups below.

## Placement

- Python package: `admin_utils/translations/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/translations/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Scoped Translation System Settings`; on/off flag `enable_translations` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/translations/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 8 |
| P1 | 22 |
| P2 | 15 |

Waves: wave 7 (30), wave 11 (15)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [TRNS-001](../tasks/TRNS/TRNS-001.md) | P0 | 7 | `Scoped Translation` doctype (source text, translated text, language, scope type, scope target) |
| [TRNS-002](../tasks/TRNS/TRNS-002.md) | P0 | 7 | Scope types: global, module, doctype, report, page, workspace, custom app |
| [TRNS-003](../tasks/TRNS/TRNS-003.md) | P0 | 7 | Resolution order: doctype → module → global → core fallback |
| [TRNS-004](../tasks/TRNS/TRNS-004.md) | P0 | 7 | Context-aware lookup used by the app SPA and generated views |
| [TRNS-005](../tasks/TRNS/TRNS-005.md) | P0 | 7 | Translation editor grid with inline editing and search |
| [TRNS-006](../tasks/TRNS/TRNS-006.md) | P0 | 7 | Filter by language, scope, status (missing/translated/reviewed) |
| [TRNS-007](../tasks/TRNS/TRNS-007.md) | P0 | 7 | Source string extractor for a doctype (labels, descriptions, options, buttons) |
| [TRNS-008](../tasks/TRNS/TRNS-008.md) | P0 | 7 | Cache with explicit invalidation on save |
| [TRNS-009](../tasks/TRNS/TRNS-009.md) | P1 | 7 | Missing-translation finder per module/doctype |
| [TRNS-010](../tasks/TRNS/TRNS-010.md) | P1 | 7 | Coverage dashboard (% translated per language/scope) |
| [TRNS-011](../tasks/TRNS/TRNS-011.md) | P1 | 7 | Import/export CSV/PO/JSON per scope |
| [TRNS-012](../tasks/TRNS/TRNS-012.md) | P1 | 7 | Bulk find/replace across translations with preview |
| [TRNS-013](../tasks/TRNS/TRNS-013.md) | P1 | 7 | Translation memory (suggest previous translations of similar strings) |
| [TRNS-014](../tasks/TRNS/TRNS-014.md) | P1 | 7 | Glossary of enforced terms (e.g., "Customer" → "عميل") with violation checks |
| [TRNS-015](../tasks/TRNS/TRNS-015.md) | P1 | 7 | Placeholder/variable integrity check (`{0}`, `%s`) between source and target |
| [TRNS-016](../tasks/TRNS/TRNS-016.md) | P1 | 7 | RTL/LTR mixed-text sanity check |
| [TRNS-017](../tasks/TRNS/TRNS-017.md) | P1 | 7 | Review workflow (draft → reviewed → approved) |
| [TRNS-018](../tasks/TRNS/TRNS-018.md) | P1 | 7 | Per-translator assignment and progress tracking |
| [TRNS-019](../tasks/TRNS/TRNS-019.md) | P1 | 7 | Preview translated doctype form/list in context |
| [TRNS-020](../tasks/TRNS/TRNS-020.md) | P1 | 7 | Translate custom fields, property setters and workflow states/actions |
| [TRNS-021](../tasks/TRNS/TRNS-021.md) | P1 | 7 | Translate print formats, email templates and notifications |
| [TRNS-022](../tasks/TRNS/TRNS-022.md) | P1 | 7 | Translate select options and link titles |
| [TRNS-023](../tasks/TRNS/TRNS-023.md) | P2 | 11 | Optional machine-translation provider hook (off by default, review required) |
| [TRNS-024](../tasks/TRNS/TRNS-024.md) | P2 | 11 | Version history and revert per translation |
| [TRNS-025](../tasks/TRNS/TRNS-025.md) | P2 | 11 | Conflict detection when core translation updates after upgrade |
| [TRNS-026](../tasks/TRNS/TRNS-026.md) | P2 | 11 | Pluralization and gender forms support |
| [TRNS-027](../tasks/TRNS/TRNS-027.md) | P2 | 11 | Arabic-specific helpers (diacritics normalization, numerals choice) |
| [TRNS-028](../tasks/TRNS/TRNS-028.md) | P2 | 11 | Translation unit tests generated from glossary |
| [TRNS-029](../tasks/TRNS/TRNS-029.md) | P2 | 11 | Export a scope as an installable translation fixture for other sites |
| [TRNS-030](../tasks/TRNS/TRNS-030.md) | P2 | 11 | Audit of who changed which translation |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [TRNS-031](../tasks/TRNS/TRNS-031.md) | P1 | 7 | Translation scopes inheritance diagram |
| [TRNS-032](../tasks/TRNS/TRNS-032.md) | P1 | 7 | Auto-detect strings needing translation from a newly installed app |
| [TRNS-033](../tasks/TRNS/TRNS-033.md) | P1 | 7 | Context hints for translators (screenshot + field path) |
| [TRNS-034](../tasks/TRNS/TRNS-034.md) | P1 | 7 | Length/overflow warnings for button and column labels |
| [TRNS-035](../tasks/TRNS/TRNS-035.md) | P1 | 7 | Side-by-side view: English, Arabic, current override |
| [TRNS-036](../tasks/TRNS/TRNS-036.md) | P1 | 7 | Bulk status change and reviewer assignment |
| [TRNS-037](../tasks/TRNS/TRNS-037.md) | P1 | 7 | Search by partial source or translation text with regex option |
| [TRNS-038](../tasks/TRNS/TRNS-038.md) | P1 | 7 | Translate DocType names, field labels and section titles at module scope |
| [TRNS-039](../tasks/TRNS/TRNS-039.md) | P2 | 11 | Translation of user-generated select options (custom lists) |
| [TRNS-040](../tasks/TRNS/TRNS-040.md) | P2 | 11 | Number/date/currency format overrides per scope |
| [TRNS-041](../tasks/TRNS/TRNS-041.md) | P2 | 11 | Translator comments and discussion threads |
| [TRNS-042](../tasks/TRNS/TRNS-042.md) | P2 | 11 | Quality checks (double spaces, punctuation, trailing characters) |
| [TRNS-043](../tasks/TRNS/TRNS-043.md) | P2 | 11 | Release notes of translation changes between versions |
| [TRNS-044](../tasks/TRNS/TRNS-044.md) | P2 | 11 | Fallback chain configuration (ar-EG → ar → en) |
| [TRNS-045](../tasks/TRNS/TRNS-045.md) | P2 | 11 | Per-user preferred language override honored by the SPA |

## Tests

- resolution order matrix, placeholder integrity, cache invalidation.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Translation scoping semantic mismatch: own resolution layer, clear docs, tests

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
