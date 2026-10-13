# Wave 11 — Continuous

**Indicative duration:** ongoing  
**Scope:** all P2 items, ordered by usage analytics and risk; quarterly Frappe compatibility sweeps

**Tasks:** 680  ·  `python scripts/tasks.py list --wave 11`

## Entry criteria

- Everything in earlier waves that this wave depends on is done and CI is green on v15 and v16.

## Modules and tasks

| Module | Tasks | IDs |
|---|---|---|
| [CORE](../tasks/CORE/INDEX.md) | 14 | 039–045, 059–065 |
| [PERM](../tasks/PERM/INDEX.md) | 34 | 050–070, 093–105 |
| [REPT](../tasks/REPT/INDEX.md) | 27 | 029–045, 061–070 |
| [BNCH](../tasks/BNCH/INDEX.md) | 9 | 047–055 |
| [CONF](../tasks/CONF/INDEX.md) | 14 | 018–025, 030–035 |
| [TRNS](../tasks/TRNS/INDEX.md) | 15 | 023–030, 039–045 |
| [THEM](../tasks/THEM/INDEX.md) | 37 | 026–035, 041–050, 068–070, 079–080, 087–090, 098–099, 101–102, 107–110 |
| [ONBD](../tasks/ONBD/INDEX.md) | 33 | 018–025, 030–035, 052–054, 066–068, 076–079, 086–093, 095 |
| [WKSP](../tasks/WKSP/INDEX.md) | 18 | 025–035, 044–050 |
| [DATA](../tasks/DATA/INDEX.md) | 20 | 034–045, 058–065 |
| [MNTR](../tasks/MNTR/INDEX.md) | 27 | 031–040, 051–060, 064–070 |
| [F2B](../tasks/F2B/INDEX.md) | 15 | 022–030, 035–040 |
| [VIEW](../tasks/VIEW/INDEX.md) | 27 | 022–025, 036–040, 045–050, 060–065, 069–071, 074, 079–080 |
| [EXTR](../tasks/EXTR/INDEX.md) | 28 | 028–040, 051–065 |
| [SECU](../tasks/SECU/INDEX.md) | 10 | 021–030 |
| [AUTO](../tasks/AUTO/INDEX.md) | 13 | 018–030 |
| [FORM](../tasks/FORM/INDEX.md) | 9 | 017–025 |
| [PRNT](../tasks/PRNT/INDEX.md) | 10 | 016–025 |
| [IMEX](../tasks/IMEX/INDEX.md) | 6 | 015–020 |
| [DASH](../tasks/DASH/INDEX.md) | 10 | 011–020 |
| [APIX](../tasks/APIX/INDEX.md) | 9 | 012–020 |
| [QAUT](../tasks/QAUT/INDEX.md) | 5 | 011–015 |
| [BLDR](../tasks/BLDR/INDEX.md) | 17 | 018–020, 049–050, 059–070 |
| [MIGR](../tasks/MIGR/INDEX.md) | 14 | 017–030 |
| [GOVN](../tasks/GOVN/INDEX.md) | 14 | 017–030 |
| [BKUP](../tasks/BKUP/INDEX.md) | 15 | 016–030 |
| [INSI](../tasks/INSI/INDEX.md) | 17 | 009–025 |
| [TSTD](../tasks/TSTD/INDEX.md) | 9 | 015–018, 020–023, 025 |
| [PERF](../tasks/PERF/INDEX.md) | 19 | 012–030 |
| [MSIT](../tasks/MSIT/INDEX.md) | 15 | 011–025 |
| [AIAS](../tasks/AIAS/INDEX.md) | 20 | 011–030 |
| [KNOW](../tasks/KNOW/INDEX.md) | 13 | 008–020 |
| [TRAIN](../tasks/TRAIN/INDEX.md) | 30 | 017–020, 028–030, 039–042, 052–060, 066–070, 075–078, 080 |
| [GUID](../tasks/GUID/INDEX.md) | 26 | 025–050 |
| [LOGS](../tasks/LOGS/INDEX.md) | 35 | 020–023, 036–042, 052–054, 063–066, 072–079, 082–090 |
| [DBUG](../tasks/DBUG/INDEX.md) | 24 | 013–015, 030–034, 047–050, 056–058, 062–070 |
| [TRCE](../tasks/TRCE/INDEX.md) | 22 | 019–040 |

## Exit criteria

- Continuous: P2 pulled in by usage data, risk and review capacity.
- No open high/critical security findings; flaky-test rate within agreed limit.
