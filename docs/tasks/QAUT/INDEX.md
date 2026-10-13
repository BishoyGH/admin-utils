# QAUT — Built-in Self-Test & Diagnostics: tasks

Spec: [`23-self-test.md`](../../specs/23-self-test.md) · 15 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [QAUT-001](QAUT-001.md) | P0 | 0 | todo | In-app "Self-test" page running safe diagnostics for every enabled module |
| [QAUT-002](QAUT-002.md) | P0 | 0 | todo | Environment compatibility report (Frappe version, DB, Python, Node, required apps) |
| [QAUT-003](QAUT-003.md) | P1 | 9 | todo | Permission smoke test per ladder level using temporary test users (cleaned up after) |
| [QAUT-004](QAUT-004.md) | P1 | 9 | todo | Guard coverage checker (every endpoint protected and flagged) |
| [QAUT-005](QAUT-005.md) | P1 | 9 | todo | Audit coverage checker (every mutating action logs) |
| [QAUT-006](QAUT-006.md) | P1 | 9 | todo | Secrets masking self-check |
| [QAUT-007](QAUT-007.md) | P1 | 9 | todo | Job system health test (enqueue → run → result) |
| [QAUT-008](QAUT-008.md) | P1 | 9 | todo | Realtime channel test |
| [QAUT-009](QAUT-009.md) | P1 | 9 | todo | Config backup/restore round-trip test on a temp file |
| [QAUT-010](QAUT-010.md) | P1 | 9 | todo | Seeder round-trip test (seed small batch, verify, delete) |
| [QAUT-011](QAUT-011.md) | P2 | 11 | todo | Diagnostics bundle export (sanitized) for support |
| [QAUT-012](QAUT-012.md) | P2 | 11 | todo | Post-upgrade verification suite triggered by `after_migrate` |
| [QAUT-013](QAUT-013.md) | P2 | 11 | todo | Scheduled self-test with alert on regression |
| [QAUT-014](QAUT-014.md) | P2 | 11 | todo | Contract checks against core doctype schemas used by the app |
| [QAUT-015](QAUT-015.md) | P2 | 11 | todo | Accessibility self-audit (axe) runnable from admin UI on key pages |
