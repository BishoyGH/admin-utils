# Wave 00 — Foundation

**Indicative duration:** 3–4 weeks  
**Scope:** CORE shell, guard, audit, jobs, compat layer, i18n/RTL; CI matrix v15/v16; agent harness; QAUT-001/002; TRCE-001 trace-id propagation

**Tasks:** 54  ·  `python scripts/tasks.py list --wave 0`

## Entry criteria

- Repository scaffold from `setup.sh` exists; CI skeleton present.

## Modules and tasks

| Module | Tasks | IDs |
|---|---|---|
| [CORE](../tasks/CORE/INDEX.md) | 51 | 001–038, 046–058 |
| [QAUT](../tasks/QAUT/INDEX.md) | 2 | 001–002 |
| [TRCE](../tasks/TRCE/INDEX.md) | 1 | 001 |

## Exit criteria

- All P0/P1 tasks of the wave are done per the Definition of Done (`docs/checklists/definition-of-done.md`).
- No open high/critical security findings; flaky-test rate within agreed limit.
