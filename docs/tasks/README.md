# Tasks

One file per feature: `docs/tasks/<CODE>/<CODE-NNN>.md`. The front matter is the single source of truth for status; `INDEX.md` files, `tasks.json` and `tasks.csv` are generated (`python scripts/tasks.py reindex`).

## Status lifecycle

`todo` -> `ready` (Definition of Ready met) -> `in-progress` -> `in-review` -> `done`; `blocked` at any point (write why in Notes).

## CLI

```
python scripts/tasks.py stats
python scripts/tasks.py list [--module PERM] [--wave 1] [--priority P0] [--status todo]
python scripts/tasks.py show PERM-016
python scripts/tasks.py next [--module PERM] [--wave 1]
python scripts/tasks.py set-status PERM-016 in-progress
python scripts/tasks.py set-wave PERM-016 2
python scripts/tasks.py validate
python scripts/tasks.py reindex
```

`next` returns the lowest-wave, highest-priority task that is `todo`/`ready` and whose `references` are all `done`.

## Adding a task

Copy `_TEMPLATE.md`, use the next free ID in the module, then `reindex`.
