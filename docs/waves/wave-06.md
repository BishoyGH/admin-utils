# Wave 06 — Code export & promotion

**Indicative duration:** 6–8 weeks  
**Scope:** BLDR, MIGR P0/P1; TSTD generators; GOVN deployment controls; shipping themes/onboarding/courses inside generated apps

**Tasks:** 85  ·  `python scripts/tasks.py list --wave 6`

## Entry criteria

- Everything in earlier waves that this wave depends on is done and CI is green on v15 and v16.

## Modules and tasks

| Module | Tasks | IDs |
|---|---|---|
| [THEM](../tasks/THEM/INDEX.md) | 1 | 100 |
| [ONBD](../tasks/ONBD/INDEX.md) | 1 | 094 |
| [BLDR](../tasks/BLDR/INDEX.md) | 53 | 001–017, 021–048, 051–058 |
| [MIGR](../tasks/MIGR/INDEX.md) | 16 | 001–016 |
| [GOVN](../tasks/GOVN/INDEX.md) | 3 | 005–007 |
| [TSTD](../tasks/TSTD/INDEX.md) | 10 | 001, 004–009, 012, 019, 024 |
| [TRAIN](../tasks/TRAIN/INDEX.md) | 1 | 079 |

## Exit criteria

- All P0/P1 tasks of the wave are done per the Definition of Done (`docs/checklists/definition-of-done.md`).
- No open high/critical security findings; flaky-test rate within agreed limit.
