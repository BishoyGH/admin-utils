# BNCH — Run Bench Commands From UI: tasks

Spec: [`03-bench-commands.md`](../../specs/03-bench-commands.md) · 55 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [BNCH-001](BNCH-001.md) | P0 | 4 | todo | Allowlist registry of permitted commands with argv templates |
| [BNCH-002](BNCH-002.md) | P0 | 4 | todo | Per-command schema for arguments (type, range, regex) and validation |
| [BNCH-003](BNCH-003.md) | P0 | 4 | todo | Execution via `subprocess` with `shell=False`, timeout, and resource limits |
| [BNCH-004](BNCH-004.md) | P0 | 4 | todo | Run as background job with live stdout/stderr streaming |
| [BNCH-005](BNCH-005.md) | P0 | 4 | todo | Role gate: `Admin Utils Bench Operator` only |
| [BNCH-006](BNCH-006.md) | P0 | 4 | todo | Full audit log of command, args, user, exit code, duration |
| [BNCH-007](BNCH-007.md) | P0 | 4 | todo | Typed confirmation for destructive commands |
| [BNCH-008](BNCH-008.md) | P0 | 4 | todo | Global kill switch to disable the module entirely |
| [BNCH-009](BNCH-009.md) | P0 | 4 | todo | `migrate` with pre-migrate backup option |
| [BNCH-010](BNCH-010.md) | P0 | 4 | todo | `clear-cache`, `clear-website-cache` |
| [BNCH-011](BNCH-011.md) | P0 | 4 | todo | `build` / `build --app` (where applicable) |
| [BNCH-012](BNCH-012.md) | P0 | 4 | todo | `backup` (with/without files, compress) |
| [BNCH-013](BNCH-013.md) | P1 | 4 | todo | `restart` via supervisor/systemd helper (configurable) |
| [BNCH-014](BNCH-014.md) | P1 | 4 | todo | `doctor`, `show-config`, `list-apps` read-only info commands |
| [BNCH-015](BNCH-015.md) | P1 | 4 | todo | `set-config` using key allowlist (links CONF module) |
| [BNCH-016](BNCH-016.md) | P1 | 4 | todo | `reload-doctype`, `reload-doc` |
| [BNCH-017](BNCH-017.md) | P1 | 4 | todo | `execute` limited to allowlisted dotted paths only |
| [BNCH-018](BNCH-018.md) | P1 | 4 | todo | `export-fixtures`, `export-csv` |
| [BNCH-019](BNCH-019.md) | P1 | 4 | todo | `scheduler enable/disable/status` |
| [BNCH-020](BNCH-020.md) | P1 | 4 | todo | `set-maintenance-mode on/off` |
| [BNCH-021](BNCH-021.md) | P1 | 4 | todo | Command presets ("Safe update", "Cache reset", "Nightly maintenance") |
| [BNCH-022](BNCH-022.md) | P1 | 4 | todo | Multi-step runbooks (backup → migrate → clear cache → restart) with stop-on-failure |
| [BNCH-023](BNCH-023.md) | P1 | 4 | todo | Dry-run/explain mode showing the exact argv to be executed |
| [BNCH-024](BNCH-024.md) | P1 | 4 | todo | Output search, copy, download, and ANSI color rendering |
| [BNCH-025](BNCH-025.md) | P1 | 4 | todo | Concurrency lock (one mutating command at a time per site) |
| [BNCH-026](BNCH-026.md) | P1 | 4 | todo | Cancel running command safely (SIGTERM → SIGKILL) |
| [BNCH-027](BNCH-027.md) | P1 | 4 | todo | Command history with re-run and compare |
| [BNCH-028](BNCH-028.md) | P2 | 4 | todo | Scheduled commands (cron-like) with notifications |
| [BNCH-029](BNCH-029.md) | P2 | 4 | todo | Pre-flight checks (disk space, pending backups, maintenance state) |
| [BNCH-030](BNCH-030.md) | P2 | 4 | todo | Post-run health checks and auto-notify on failure |
| [BNCH-031](BNCH-031.md) | P2 | 4 | todo | Approval step for production (second admin must approve) |
| [BNCH-032](BNCH-032.md) | P2 | 4 | todo | Notify via email/Telegram/Slack webhook on completion |
| [BNCH-033](BNCH-033.md) | P2 | 4 | todo | Custom command registration API for other apps (still allowlisted) |
| [BNCH-034](BNCH-034.md) | P2 | 4 | todo | Per-environment command policies (dev allows more than prod) |
| [BNCH-035](BNCH-035.md) | P2 | 4 | todo | Run summary report PDF for change management |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [BNCH-036](BNCH-036.md) | P1 | 9 | todo | Command catalog UI with risk labels (read-only, mutating, destructive) |
| [BNCH-037](BNCH-037.md) | P1 | 9 | todo | Per-command help with examples and expected side effects |
| [BNCH-038](BNCH-038.md) | P1 | 9 | todo | Environment-aware defaults (e.g. skip build on prod unless asked) |
| [BNCH-039](BNCH-039.md) | P1 | 9 | todo | Restart plan preview (which processes, expected downtime) |
| [BNCH-040](BNCH-040.md) | P1 | 9 | todo | Maintenance banner auto-enable during risky runbooks |
| [BNCH-041](BNCH-041.md) | P1 | 9 | todo | Runbook designer (ordered steps, conditions, retries, timeouts) |
| [BNCH-042](BNCH-042.md) | P1 | 9 | todo | Runbook variables and parameter prompts at run time |
| [BNCH-043](BNCH-043.md) | P1 | 9 | todo | Runbook dry-run executing only read-only steps |
| [BNCH-044](BNCH-044.md) | P1 | 9 | todo | Step-level logs and resume-from-failed-step |
| [BNCH-045](BNCH-045.md) | P1 | 9 | todo | Auto-rollback hooks (restore backup if migrate fails, opt-in) |
| [BNCH-046](BNCH-046.md) | P1 | 9 | todo | Command output redaction of secrets and tokens |
| [BNCH-047](BNCH-047.md) | P2 | 11 | todo | Bench/site selector when several sites exist, with per-site allowlists |
| [BNCH-048](BNCH-048.md) | P2 | 11 | todo | Run history analytics (failure rate, avg duration) |
| [BNCH-049](BNCH-049.md) | P2 | 11 | todo | Compare outputs of consecutive `migrate` runs (patches applied) |
| [BNCH-050](BNCH-050.md) | P2 | 11 | todo | Disk-space-aware gating for backup/build |
| [BNCH-051](BNCH-051.md) | P2 | 11 | todo | Calendar of scheduled operations with conflict detection |
| [BNCH-052](BNCH-052.md) | P2 | 11 | todo | Hook points for pre/post command custom checks (allowlisted functions) |
| [BNCH-053](BNCH-053.md) | P2 | 11 | todo | Export runbook as shell script for operators who prefer terminal (non-executing) |
| [BNCH-054](BNCH-054.md) | P2 | 11 | todo | Signed runbooks (hash verified before run) |
| [BNCH-055](BNCH-055.md) | P2 | 11 | todo | Two-person rule for runbooks marked "critical" |
