# TRNS — Scoped Translation System: tasks

Spec: [`05-translations.md`](../../specs/05-translations.md) · 45 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [TRNS-001](TRNS-001.md) | P0 | 7 | todo | `Scoped Translation` doctype (source text, translated text, language, scope type, scope target) |
| [TRNS-002](TRNS-002.md) | P0 | 7 | todo | Scope types: global, module, doctype, report, page, workspace, custom app |
| [TRNS-003](TRNS-003.md) | P0 | 7 | todo | Resolution order: doctype → module → global → core fallback |
| [TRNS-004](TRNS-004.md) | P0 | 7 | todo | Context-aware lookup used by the app SPA and generated views |
| [TRNS-005](TRNS-005.md) | P0 | 7 | todo | Translation editor grid with inline editing and search |
| [TRNS-006](TRNS-006.md) | P0 | 7 | todo | Filter by language, scope, status (missing/translated/reviewed) |
| [TRNS-007](TRNS-007.md) | P0 | 7 | todo | Source string extractor for a doctype (labels, descriptions, options, buttons) |
| [TRNS-008](TRNS-008.md) | P0 | 7 | todo | Cache with explicit invalidation on save |
| [TRNS-009](TRNS-009.md) | P1 | 7 | todo | Missing-translation finder per module/doctype |
| [TRNS-010](TRNS-010.md) | P1 | 7 | todo | Coverage dashboard (% translated per language/scope) |
| [TRNS-011](TRNS-011.md) | P1 | 7 | todo | Import/export CSV/PO/JSON per scope |
| [TRNS-012](TRNS-012.md) | P1 | 7 | todo | Bulk find/replace across translations with preview |
| [TRNS-013](TRNS-013.md) | P1 | 7 | todo | Translation memory (suggest previous translations of similar strings) |
| [TRNS-014](TRNS-014.md) | P1 | 7 | todo | Glossary of enforced terms (e.g., "Customer" → "عميل") with violation checks |
| [TRNS-015](TRNS-015.md) | P1 | 7 | todo | Placeholder/variable integrity check (`{0}`, `%s`) between source and target |
| [TRNS-016](TRNS-016.md) | P1 | 7 | todo | RTL/LTR mixed-text sanity check |
| [TRNS-017](TRNS-017.md) | P1 | 7 | todo | Review workflow (draft → reviewed → approved) |
| [TRNS-018](TRNS-018.md) | P1 | 7 | todo | Per-translator assignment and progress tracking |
| [TRNS-019](TRNS-019.md) | P1 | 7 | todo | Preview translated doctype form/list in context |
| [TRNS-020](TRNS-020.md) | P1 | 7 | todo | Translate custom fields, property setters and workflow states/actions |
| [TRNS-021](TRNS-021.md) | P1 | 7 | todo | Translate print formats, email templates and notifications |
| [TRNS-022](TRNS-022.md) | P1 | 7 | todo | Translate select options and link titles |
| [TRNS-023](TRNS-023.md) | P2 | 11 | todo | Optional machine-translation provider hook (off by default, review required) |
| [TRNS-024](TRNS-024.md) | P2 | 11 | todo | Version history and revert per translation |
| [TRNS-025](TRNS-025.md) | P2 | 11 | todo | Conflict detection when core translation updates after upgrade |
| [TRNS-026](TRNS-026.md) | P2 | 11 | todo | Pluralization and gender forms support |
| [TRNS-027](TRNS-027.md) | P2 | 11 | todo | Arabic-specific helpers (diacritics normalization, numerals choice) |
| [TRNS-028](TRNS-028.md) | P2 | 11 | todo | Translation unit tests generated from glossary |
| [TRNS-029](TRNS-029.md) | P2 | 11 | todo | Export a scope as an installable translation fixture for other sites |
| [TRNS-030](TRNS-030.md) | P2 | 11 | todo | Audit of who changed which translation |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [TRNS-031](TRNS-031.md) | P1 | 7 | todo | Translation scopes inheritance diagram |
| [TRNS-032](TRNS-032.md) | P1 | 7 | todo | Auto-detect strings needing translation from a newly installed app |
| [TRNS-033](TRNS-033.md) | P1 | 7 | todo | Context hints for translators (screenshot + field path) |
| [TRNS-034](TRNS-034.md) | P1 | 7 | todo | Length/overflow warnings for button and column labels |
| [TRNS-035](TRNS-035.md) | P1 | 7 | todo | Side-by-side view: English, Arabic, current override |
| [TRNS-036](TRNS-036.md) | P1 | 7 | todo | Bulk status change and reviewer assignment |
| [TRNS-037](TRNS-037.md) | P1 | 7 | todo | Search by partial source or translation text with regex option |
| [TRNS-038](TRNS-038.md) | P1 | 7 | todo | Translate DocType names, field labels and section titles at module scope |
| [TRNS-039](TRNS-039.md) | P2 | 11 | todo | Translation of user-generated select options (custom lists) |
| [TRNS-040](TRNS-040.md) | P2 | 11 | todo | Number/date/currency format overrides per scope |
| [TRNS-041](TRNS-041.md) | P2 | 11 | todo | Translator comments and discussion threads |
| [TRNS-042](TRNS-042.md) | P2 | 11 | todo | Quality checks (double spaces, punctuation, trailing characters) |
| [TRNS-043](TRNS-043.md) | P2 | 11 | todo | Release notes of translation changes between versions |
| [TRNS-044](TRNS-044.md) | P2 | 11 | todo | Fallback chain configuration (ar-EG → ar → en) |
| [TRNS-045](TRNS-045.md) | P2 | 11 | todo | Per-user preferred language override honored by the SPA |
