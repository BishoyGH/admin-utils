---
code: DATA
title: "Data Seeder"
number: 09
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/seeder/
frontend_path: frontend/src/features/seeder/
tasks: docs/tasks/DATA/INDEX.md
---

# Spec 09 — Data Seeder (`DATA`)

## Purpose

Data Seeder: see feature groups below.

## Placement

- Python package: `admin_utils/seeder/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/seeder/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Data Seeder Settings`; on/off flag `enable_seeder` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/seeder/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 12 |
| P1 | 33 |
| P2 | 20 |

Waves: wave 2 (45), wave 11 (20)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [DATA-001](../tasks/DATA/DATA-001.md) | P0 | 2 | Seeder UI: choose doctype(s), count, locale (en/ar), seed value |
| [DATA-002](../tasks/DATA/DATA-002.md) | P0 | 2 | Field-aware generator by fieldtype (Data, Int, Float, Currency, Date, Select, Link, Table, ...) |
| [DATA-003](../tasks/DATA/DATA-003.md) | P0 | 2 | Link-field resolution (pick existing records or auto-create dependencies) |
| [DATA-004](../tasks/DATA/DATA-004.md) | P0 | 2 | Dependency graph ordering (create masters before transactions) |
| [DATA-005](../tasks/DATA/DATA-005.md) | P0 | 2 | Child table row generation with min/max rows |
| [DATA-006](../tasks/DATA/DATA-006.md) | P0 | 2 | Respect mandatory, unique, read-only and validation rules |
| [DATA-007](../tasks/DATA/DATA-007.md) | P0 | 2 | Run as background job with progress and per-record error capture |
| [DATA-008](../tasks/DATA/DATA-008.md) | P0 | 2 | "Seed batch" tagging so all seeded records can be listed and deleted |
| [DATA-009](../tasks/DATA/DATA-009.md) | P0 | 2 | One-click delete of a seed batch (respecting links/docstatus) |
| [DATA-010](../tasks/DATA/DATA-010.md) | P0 | 2 | Production guard (blocked unless environment allows, typed confirmation) |
| [DATA-011](../tasks/DATA/DATA-011.md) | P0 | 2 | Arabic data provider: names, addresses, companies, items, phone formats |
| [DATA-012](../tasks/DATA/DATA-012.md) | P0 | 2 | English data provider via Faker with locale options |
| [DATA-013](../tasks/DATA/DATA-013.md) | P1 | 2 | Deterministic seeding with a seed value for reproducible datasets |
| [DATA-014](../tasks/DATA/DATA-014.md) | P1 | 2 | Per-field generator override (fixed value, list, range, regex, formula) |
| [DATA-015](../tasks/DATA/DATA-015.md) | P1 | 2 | Dataset profiles (small/medium/large) with sensible ratios |
| [DATA-016](../tasks/DATA/DATA-016.md) | P1 | 2 | Scenario packs: retail store, wholesale distributor, clinic, school, restaurant, contractor |
| [DATA-017](../tasks/DATA/DATA-017.md) | P1 | 2 | Realistic date distribution (business days, seasonality, growth trend) |
| [DATA-018](../tasks/DATA/DATA-018.md) | P1 | 2 | Realistic numeric distributions (price tiers, quantity curves) |
| [DATA-019](../tasks/DATA/DATA-019.md) | P1 | 2 | Transaction cycle simulation (quote → order → delivery → invoice → payment) |
| [DATA-020](../tasks/DATA/DATA-020.md) | P1 | 2 | Stock simulation (receipts, issues, transfers) with valid balances |
| [DATA-021](../tasks/DATA/DATA-021.md) | P1 | 2 | Accounting-valid seeding (balanced GL, correct accounts, fiscal year) |
| [DATA-022](../tasks/DATA/DATA-022.md) | P1 | 2 | HR simulation (employees, attendance, leave, payroll) |
| [DATA-023](../tasks/DATA/DATA-023.md) | P1 | 2 | User and role seeding for permission tests (links PERM) |
| [DATA-024](../tasks/DATA/DATA-024.md) | P1 | 2 | Submit/cancel simulation to produce all docstatus variants |
| [DATA-025](../tasks/DATA/DATA-025.md) | P1 | 2 | Workflow-aware seeding (distribute documents across states) |
| [DATA-026](../tasks/DATA/DATA-026.md) | P1 | 2 | Attachment/image placeholder generation |
| [DATA-027](../tasks/DATA/DATA-027.md) | P1 | 2 | Arabic/English mixed dataset option |
| [DATA-028](../tasks/DATA/DATA-028.md) | P1 | 2 | Email/phone/tax-id generators that cannot hit real addresses (safe domains/reserved ranges) |
| [DATA-029](../tasks/DATA/DATA-029.md) | P1 | 2 | Dry-run preview showing 5 sample records before inserting |
| [DATA-030](../tasks/DATA/DATA-030.md) | P1 | 2 | Validation report after run (counts, failures, skipped) |
| [DATA-031](../tasks/DATA/DATA-031.md) | P1 | 2 | Save and reuse seeder recipes as doctype records |
| [DATA-032](../tasks/DATA/DATA-032.md) | P1 | 2 | Import/export recipes as JSON |
| [DATA-033](../tasks/DATA/DATA-033.md) | P1 | 2 | Throttling and chunked commits for large volumes |
| [DATA-034](../tasks/DATA/DATA-034.md) | P2 | 11 | Custom provider plugin API (other apps register generators) |
| [DATA-035](../tasks/DATA/DATA-035.md) | P2 | 11 | Faker locale extensions for more Arab countries (EG, SA, AE, JO, MA) |
| [DATA-036](../tasks/DATA/DATA-036.md) | P2 | 11 | Name/brand dictionary management for Arabic transliteration |
| [DATA-037](../tasks/DATA/DATA-037.md) | P2 | 11 | Referential-integrity checker for seeded data |
| [DATA-038](../tasks/DATA/DATA-038.md) | P2 | 11 | Performance dataset generator (100k+ docs) for load testing |
| [DATA-039](../tasks/DATA/DATA-039.md) | P2 | 11 | Anonymizer: replace real data with realistic fake data (opt-in, per field) |
| [DATA-040](../tasks/DATA/DATA-040.md) | P2 | 11 | Snapshot/restore of a seeded database state |
| [DATA-041](../tasks/DATA/DATA-041.md) | P2 | 11 | Scheduled re-seeding on demo/staging sites |
| [DATA-042](../tasks/DATA/DATA-042.md) | P2 | 11 | Demo-site reset button (wipe seeded data, re-seed scenario) |
| [DATA-043](../tasks/DATA/DATA-043.md) | P2 | 11 | Seeder CLI: `bench --site x admin-utils seed --recipe retail-small` |
| [DATA-044](../tasks/DATA/DATA-044.md) | P2 | 11 | Cross-version seeding tests (v15/v16 field differences) |
| [DATA-045](../tasks/DATA/DATA-045.md) | P2 | 11 | Data quality report (duplicates, nulls, outliers) of the seeded set |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [DATA-046](../tasks/DATA/DATA-046.md) | P1 | 2 | Preset generators: Egyptian/Gulf names, governorates, phone and national-id-like formats (non-valid) |
| [DATA-047](../tasks/DATA/DATA-047.md) | P1 | 2 | Product catalog generator with categories, variants, units and price tiers |
| [DATA-048](../tasks/DATA/DATA-048.md) | P1 | 2 | Customer segment generator (retail, wholesale, VIP) with credit limits |
| [DATA-049](../tasks/DATA/DATA-049.md) | P1 | 2 | Supplier and purchasing cycle generator |
| [DATA-050](../tasks/DATA/DATA-050.md) | P1 | 2 | POS session and receipt generator |
| [DATA-051](../tasks/DATA/DATA-051.md) | P1 | 2 | Project, task and timesheet generator |
| [DATA-052](../tasks/DATA/DATA-052.md) | P1 | 2 | Manufacturing BOM/work order generator |
| [DATA-053](../tasks/DATA/DATA-053.md) | P1 | 2 | Asset and maintenance generator |
| [DATA-054](../tasks/DATA/DATA-054.md) | P1 | 2 | CRM lead, opportunity and quotation generator with funnel realism |
| [DATA-055](../tasks/DATA/DATA-055.md) | P1 | 2 | Support ticket and SLA generator |
| [DATA-056](../tasks/DATA/DATA-056.md) | P1 | 2 | Realistic seasonality presets (Ramadan peaks, back-to-school, year-end) |
| [DATA-057](../tasks/DATA/DATA-057.md) | P1 | 2 | Realistic holiday/weekend calendars (Friday/Saturday weekend option) |
| [DATA-058](../tasks/DATA/DATA-058.md) | P2 | 11 | Cohort generator for retention/aging report testing |
| [DATA-059](../tasks/DATA/DATA-059.md) | P2 | 11 | Error-injection mode (create deliberate bad data for validation testing) |
| [DATA-060](../tasks/DATA/DATA-060.md) | P2 | 11 | Historical backfill generator (3 years of transactions) |
| [DATA-061](../tasks/DATA/DATA-061.md) | P2 | 11 | Seed-to-file export (fixtures/CSV) for reuse in other environments |
| [DATA-062](../tasks/DATA/DATA-062.md) | P2 | 11 | Seed progress ETA and resource usage guard |
| [DATA-063](../tasks/DATA/DATA-063.md) | P2 | 11 | Distribution editors (normal, Pareto, uniform) per numeric field |
| [DATA-064](../tasks/DATA/DATA-064.md) | P2 | 11 | Relationship ratios (orders per customer, lines per order) editor |
| [DATA-065](../tasks/DATA/DATA-065.md) | P2 | 11 | Seeded-record watermark field to prevent mixing with real data |

## Tests

- determinism with fixed seed, dependency ordering, all docstatus variants, batch delete cleans everything, Arabic provider output validation.
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
