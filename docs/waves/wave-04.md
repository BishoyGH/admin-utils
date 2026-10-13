# Wave 04 — Privileged core

**Indicative duration:** 6–8 weeks  
**Scope:** BNCH-001…035, CONF-001…017, BKUP-001…015, F2B-001…021, SECU-006…020; external security review

**Tasks:** 103  ·  `python scripts/tasks.py list --wave 4`

## Entry criteria

- Everything in earlier waves that this wave depends on is done and CI is green on v15 and v16.
- BLDR and BKUP depend on the allowlisted bench runner (BNCH-001…012), delivered here before wave 6.

## Modules and tasks

| Module | Tasks | IDs |
|---|---|---|
| [BNCH](../tasks/BNCH/INDEX.md) | 35 | 001–035 |
| [CONF](../tasks/CONF/INDEX.md) | 17 | 001–017 |
| [F2B](../tasks/F2B/INDEX.md) | 21 | 001–021 |
| [SECU](../tasks/SECU/INDEX.md) | 15 | 006–020 |
| [BKUP](../tasks/BKUP/INDEX.md) | 15 | 001–015 |

## Exit criteria

- All P0/P1 tasks of the wave are done per the Definition of Done (`docs/checklists/definition-of-done.md`).
- No open high/critical security findings; flaky-test rate within agreed limit.
- External security review completed.
