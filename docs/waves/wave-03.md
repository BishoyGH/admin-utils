# Wave 03 — Flagship: experience & training

**Indicative duration:** 10–12 weeks  
**Scope:** THEM, GUID, ONBD, TRAIN P0/P1; KNOW-001…007; MOBL-001…003

**Tasks:** 216  ·  `python scripts/tasks.py list --wave 3`

## Entry criteria

- Everything in earlier waves that this wave depends on is done and CI is green on v15 and v16.
- Depends: GUID needs CORE shell and THEM tokens; ONBD needs GUID; TRAIN needs ONBD, GUID, DATA scenarios and sandbox isolation.

## Modules and tasks

| Module | Tasks | IDs |
|---|---|---|
| [THEM](../tasks/THEM/INDEX.md) | 72 | 001–025, 036–040, 051–067, 071–078, 081–086, 091–097, 103–106 |
| [ONBD](../tasks/ONBD/INDEX.md) | 61 | 001–017, 026–029, 036–051, 055–065, 069–075, 080–085 |
| [MOBL](../tasks/MOBL/INDEX.md) | 3 | 001–003 |
| [KNOW](../tasks/KNOW/INDEX.md) | 7 | 001–007 |
| [TRAIN](../tasks/TRAIN/INDEX.md) | 49 | 001–016, 021–027, 031–038, 043–051, 061–065, 071–074 |
| [GUID](../tasks/GUID/INDEX.md) | 24 | 001–024 |

## Exit criteria

- All P0/P1 tasks of the wave are done per the Definition of Done (`docs/checklists/definition-of-done.md`).
- No open high/critical security findings; flaky-test rate within agreed limit.
- Flagship criteria on pilot sites: first real task under 15 min with guidance; 10-step onboarding flow built in under 20 min with no code; 90% of guided steps still match after a Frappe minor upgrade (rest auto-flagged); 100% of shipped flows/lessons have reviewed AR + EN; AA-accessible branded theme from a logo in under 5 min.
