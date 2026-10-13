# DATA — Data Seeder: tasks

Spec: [`09-data-seeder.md`](../../specs/09-data-seeder.md) · 65 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [DATA-001](DATA-001.md) | P0 | 2 | todo | Seeder UI: choose doctype(s), count, locale (en/ar), seed value |
| [DATA-002](DATA-002.md) | P0 | 2 | todo | Field-aware generator by fieldtype (Data, Int, Float, Currency, Date, Select, Link, Table, ...) |
| [DATA-003](DATA-003.md) | P0 | 2 | todo | Link-field resolution (pick existing records or auto-create dependencies) |
| [DATA-004](DATA-004.md) | P0 | 2 | todo | Dependency graph ordering (create masters before transactions) |
| [DATA-005](DATA-005.md) | P0 | 2 | todo | Child table row generation with min/max rows |
| [DATA-006](DATA-006.md) | P0 | 2 | todo | Respect mandatory, unique, read-only and validation rules |
| [DATA-007](DATA-007.md) | P0 | 2 | todo | Run as background job with progress and per-record error capture |
| [DATA-008](DATA-008.md) | P0 | 2 | todo | "Seed batch" tagging so all seeded records can be listed and deleted |
| [DATA-009](DATA-009.md) | P0 | 2 | todo | One-click delete of a seed batch (respecting links/docstatus) |
| [DATA-010](DATA-010.md) | P0 | 2 | todo | Production guard (blocked unless environment allows, typed confirmation) |
| [DATA-011](DATA-011.md) | P0 | 2 | todo | Arabic data provider: names, addresses, companies, items, phone formats |
| [DATA-012](DATA-012.md) | P0 | 2 | todo | English data provider via Faker with locale options |
| [DATA-013](DATA-013.md) | P1 | 2 | todo | Deterministic seeding with a seed value for reproducible datasets |
| [DATA-014](DATA-014.md) | P1 | 2 | todo | Per-field generator override (fixed value, list, range, regex, formula) |
| [DATA-015](DATA-015.md) | P1 | 2 | todo | Dataset profiles (small/medium/large) with sensible ratios |
| [DATA-016](DATA-016.md) | P1 | 2 | todo | Scenario packs: retail store, wholesale distributor, clinic, school, restaurant, contractor |
| [DATA-017](DATA-017.md) | P1 | 2 | todo | Realistic date distribution (business days, seasonality, growth trend) |
| [DATA-018](DATA-018.md) | P1 | 2 | todo | Realistic numeric distributions (price tiers, quantity curves) |
| [DATA-019](DATA-019.md) | P1 | 2 | todo | Transaction cycle simulation (quote → order → delivery → invoice → payment) |
| [DATA-020](DATA-020.md) | P1 | 2 | todo | Stock simulation (receipts, issues, transfers) with valid balances |
| [DATA-021](DATA-021.md) | P1 | 2 | todo | Accounting-valid seeding (balanced GL, correct accounts, fiscal year) |
| [DATA-022](DATA-022.md) | P1 | 2 | todo | HR simulation (employees, attendance, leave, payroll) |
| [DATA-023](DATA-023.md) | P1 | 2 | todo | User and role seeding for permission tests (links PERM) |
| [DATA-024](DATA-024.md) | P1 | 2 | todo | Submit/cancel simulation to produce all docstatus variants |
| [DATA-025](DATA-025.md) | P1 | 2 | todo | Workflow-aware seeding (distribute documents across states) |
| [DATA-026](DATA-026.md) | P1 | 2 | todo | Attachment/image placeholder generation |
| [DATA-027](DATA-027.md) | P1 | 2 | todo | Arabic/English mixed dataset option |
| [DATA-028](DATA-028.md) | P1 | 2 | todo | Email/phone/tax-id generators that cannot hit real addresses (safe domains/reserved ranges) |
| [DATA-029](DATA-029.md) | P1 | 2 | todo | Dry-run preview showing 5 sample records before inserting |
| [DATA-030](DATA-030.md) | P1 | 2 | todo | Validation report after run (counts, failures, skipped) |
| [DATA-031](DATA-031.md) | P1 | 2 | todo | Save and reuse seeder recipes as doctype records |
| [DATA-032](DATA-032.md) | P1 | 2 | todo | Import/export recipes as JSON |
| [DATA-033](DATA-033.md) | P1 | 2 | todo | Throttling and chunked commits for large volumes |
| [DATA-034](DATA-034.md) | P2 | 11 | todo | Custom provider plugin API (other apps register generators) |
| [DATA-035](DATA-035.md) | P2 | 11 | todo | Faker locale extensions for more Arab countries (EG, SA, AE, JO, MA) |
| [DATA-036](DATA-036.md) | P2 | 11 | todo | Name/brand dictionary management for Arabic transliteration |
| [DATA-037](DATA-037.md) | P2 | 11 | todo | Referential-integrity checker for seeded data |
| [DATA-038](DATA-038.md) | P2 | 11 | todo | Performance dataset generator (100k+ docs) for load testing |
| [DATA-039](DATA-039.md) | P2 | 11 | todo | Anonymizer: replace real data with realistic fake data (opt-in, per field) |
| [DATA-040](DATA-040.md) | P2 | 11 | todo | Snapshot/restore of a seeded database state |
| [DATA-041](DATA-041.md) | P2 | 11 | todo | Scheduled re-seeding on demo/staging sites |
| [DATA-042](DATA-042.md) | P2 | 11 | todo | Demo-site reset button (wipe seeded data, re-seed scenario) |
| [DATA-043](DATA-043.md) | P2 | 11 | todo | Seeder CLI: `bench --site x admin-utils seed --recipe retail-small` |
| [DATA-044](DATA-044.md) | P2 | 11 | todo | Cross-version seeding tests (v15/v16 field differences) |
| [DATA-045](DATA-045.md) | P2 | 11 | todo | Data quality report (duplicates, nulls, outliers) of the seeded set |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [DATA-046](DATA-046.md) | P1 | 2 | todo | Preset generators: Egyptian/Gulf names, governorates, phone and national-id-like formats (non-valid) |
| [DATA-047](DATA-047.md) | P1 | 2 | todo | Product catalog generator with categories, variants, units and price tiers |
| [DATA-048](DATA-048.md) | P1 | 2 | todo | Customer segment generator (retail, wholesale, VIP) with credit limits |
| [DATA-049](DATA-049.md) | P1 | 2 | todo | Supplier and purchasing cycle generator |
| [DATA-050](DATA-050.md) | P1 | 2 | todo | POS session and receipt generator |
| [DATA-051](DATA-051.md) | P1 | 2 | todo | Project, task and timesheet generator |
| [DATA-052](DATA-052.md) | P1 | 2 | todo | Manufacturing BOM/work order generator |
| [DATA-053](DATA-053.md) | P1 | 2 | todo | Asset and maintenance generator |
| [DATA-054](DATA-054.md) | P1 | 2 | todo | CRM lead, opportunity and quotation generator with funnel realism |
| [DATA-055](DATA-055.md) | P1 | 2 | todo | Support ticket and SLA generator |
| [DATA-056](DATA-056.md) | P1 | 2 | todo | Realistic seasonality presets (Ramadan peaks, back-to-school, year-end) |
| [DATA-057](DATA-057.md) | P1 | 2 | todo | Realistic holiday/weekend calendars (Friday/Saturday weekend option) |
| [DATA-058](DATA-058.md) | P2 | 11 | todo | Cohort generator for retention/aging report testing |
| [DATA-059](DATA-059.md) | P2 | 11 | todo | Error-injection mode (create deliberate bad data for validation testing) |
| [DATA-060](DATA-060.md) | P2 | 11 | todo | Historical backfill generator (3 years of transactions) |
| [DATA-061](DATA-061.md) | P2 | 11 | todo | Seed-to-file export (fixtures/CSV) for reuse in other environments |
| [DATA-062](DATA-062.md) | P2 | 11 | todo | Seed progress ETA and resource usage guard |
| [DATA-063](DATA-063.md) | P2 | 11 | todo | Distribution editors (normal, Pareto, uniform) per numeric field |
| [DATA-064](DATA-064.md) | P2 | 11 | todo | Relationship ratios (orders per customer, lines per order) editor |
| [DATA-065](DATA-065.md) | P2 | 11 | todo | Seeded-record watermark field to prevent mixing with real data |
