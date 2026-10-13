# Wave 02 — Data, monitoring, logs & test studio

**Indicative duration:** 8–9 weeks  
**Scope:** DATA, MNTR P0, LOGS P0/P1, DBUG P0/P1, NTFY-001…010, TSTD-001…014, INSI-001…004

**Tasks:** 176  ·  `python scripts/tasks.py list --wave 2`

## Entry criteria

- Everything in earlier waves that this wave depends on is done and CI is green on v15 and v16.

## Modules and tasks

| Module | Tasks | IDs |
|---|---|---|
| [DATA](../tasks/DATA/INDEX.md) | 45 | 001–033, 046–057 |
| [MNTR](../tasks/MNTR/INDEX.md) | 10 | 001–010 |
| [NTFY](../tasks/NTFY/INDEX.md) | 10 | 001–010 |
| [INSI](../tasks/INSI/INDEX.md) | 4 | 001–004 |
| [TSTD](../tasks/TSTD/INDEX.md) | 6 | 002–003, 010–011, 013–014 |
| [LOGS](../tasks/LOGS/INDEX.md) | 55 | 001–019, 024–035, 043–051, 055–062, 067–071, 080–081 |
| [DBUG](../tasks/DBUG/INDEX.md) | 46 | 001–012, 016–029, 035–046, 051–055, 059–061 |

## Exit criteria

- All P0/P1 tasks of the wave are done per the Definition of Done (`docs/checklists/definition-of-done.md`).
- No open high/critical security findings; flaky-test rate within agreed limit.
