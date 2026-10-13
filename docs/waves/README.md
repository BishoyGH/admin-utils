# Waves

Wave assignment is stored per task (`wave:` in front matter) and was derived from the roadmap; change it with `python scripts/tasks.py set-wave ID N`.

| Wave | Focus | Duration | Tasks |
|---|---|---|---|
| [0](wave-00.md) | Foundation | 3–4 weeks | 54 |
| [1](wave-01.md) | Permissions & governance core | 5–6 weeks | 89 |
| [2](wave-02.md) | Data, monitoring, logs & test studio | 8–9 weeks | 176 |
| [3](wave-03.md) | Flagship: experience & training | 10–12 weeks | 216 |
| [4](wave-04.md) | Privileged core | 6–8 weeks | 103 |
| [5](wave-05.md) | Builders | 8–10 weeks | 130 |
| [6](wave-06.md) | Code export & promotion | 6–8 weeks | 85 |
| [7](wave-07.md) | Views & localization | 8–10 weeks | 95 |
| [8](wave-08.md) | Automation & integrations | 6–8 weeks | 75 |
| [9](wave-09.md) | Scale & intelligence | 7–9 weeks | 112 |
| [10](wave-10.md) | Hardening & GA | 6–8 weeks | 0 |
| [11](wave-11.md) | Continuous | ongoing | 680 |

## How waves were derived

- P2 tasks -> wave 11 (continuous), except the three "ship inside generated apps" tasks (THEM-100, ONBD-094, TRAIN-079) -> wave 6.
- Ranges named in the roadmap (e.g. BNCH-001…035, CONF-001…017) -> their wave; module-level assignments for the rest (see roadmap).
- Interpretation choices to review: DATA P0/P1 and MNTR P0 -> wave 2 ("core"); MNTR P1 and other unlisted P1 -> wave 9 ("remaining P1"); GOVN-005…007 (calendar, emergency path, checklists) -> wave 6 as "deployment controls".
- Release train: public alpha after wave 2; flagship preview after wave 3; beta after wave 6; release candidate after wave 9; 1.0 after wave 10. Privileged modules ship behind flags off by default.
