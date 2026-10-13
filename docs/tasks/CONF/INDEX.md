# CONF — Site Config JSON Editor: tasks

Spec: [`04-site-config.md`](../../specs/04-site-config.md) · 35 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [CONF-001](CONF-001.md) | P0 | 4 | todo | Read `site_config.json` (and `common_site_config.json` read-only) with secrets masked |
| [CONF-002](CONF-002.md) | P0 | 4 | todo | Structured form editor generated from a known-keys schema |
| [CONF-003](CONF-003.md) | P0 | 4 | todo | Raw JSON editor with schema validation and error hints |
| [CONF-004](CONF-004.md) | P0 | 4 | todo | Automatic timestamped backup before every write |
| [CONF-005](CONF-005.md) | P0 | 4 | todo | Diff preview before save |
| [CONF-006](CONF-006.md) | P0 | 4 | todo | Restore any previous config backup |
| [CONF-007](CONF-007.md) | P0 | 4 | todo | Key allowlist for editing; denylist for critical keys (db credentials, encryption_key) |
| [CONF-008](CONF-008.md) | P0 | 4 | todo | Atomic write (temp file + rename) and permission preservation |
| [CONF-009](CONF-009.md) | P0 | 4 | todo | Role gate `Admin Utils Config Editor` + audit log |
| [CONF-010](CONF-010.md) | P1 | 4 | todo | Known keys catalog with descriptions (maintenance_mode, developer_mode, host_name, mail settings, etc.) |
| [CONF-011](CONF-011.md) | P1 | 4 | todo | Type-aware inputs (bool, int, list, object) |
| [CONF-012](CONF-012.md) | P1 | 4 | todo | Reveal-secret action with re-authentication and audit entry |
| [CONF-013](CONF-013.md) | P1 | 4 | todo | Config templates (production hardening, dev-friendly) |
| [CONF-014](CONF-014.md) | P1 | 4 | todo | Validate hostnames, URLs, emails, ports |
| [CONF-015](CONF-015.md) | P1 | 4 | todo | Highlight keys that require restart/migrate/build after change |
| [CONF-016](CONF-016.md) | P1 | 4 | todo | Config comparison between two sites (if multi-site) |
| [CONF-017](CONF-017.md) | P1 | 4 | todo | Config lint: warns about insecure values (developer_mode on prod, weak settings) |
| [CONF-018](CONF-018.md) | P2 | 11 | todo | Config change history timeline with who/why |
| [CONF-019](CONF-019.md) | P2 | 11 | todo | Change reason required field |
| [CONF-020](CONF-020.md) | P2 | 11 | todo | Scheduled temporary config changes (auto-revert) |
| [CONF-021](CONF-021.md) | P2 | 11 | todo | Export/import config (secrets excluded by default) |
| [CONF-022](CONF-022.md) | P2 | 11 | todo | Drift detection (config changed outside the UI) |
| [CONF-023](CONF-023.md) | P2 | 11 | todo | Safe-mode lock to make config read-only |
| [CONF-024](CONF-024.md) | P2 | 11 | todo | Show effective config (site + common + environment overrides) |
| [CONF-025](CONF-025.md) | P2 | 11 | todo | Environment variable reference viewer (read-only) |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [CONF-026](CONF-026.md) | P1 | 9 | todo | Key-level permissions (some keys editable by senior admins only) |
| [CONF-027](CONF-027.md) | P1 | 9 | todo | Validation rules per key (ranges, enums, dependencies between keys) |
| [CONF-028](CONF-028.md) | P1 | 9 | todo | "Requires restart" tracker and pending-restart banner |
| [CONF-029](CONF-029.md) | P1 | 9 | todo | Config snapshot tagging ("before upgrade", "known good") |
| [CONF-030](CONF-030.md) | P2 | 11 | todo | Safe-edit sandbox: validate on a temp copy before writing |
| [CONF-031](CONF-031.md) | P2 | 11 | todo | Config inheritance viewer (common vs site) |
| [CONF-032](CONF-032.md) | P2 | 11 | todo | Alert on risky key changes (Slack/email) |
| [CONF-033](CONF-033.md) | P2 | 11 | todo | Config policy as code (YAML) enforced and drift-reported |
| [CONF-034](CONF-034.md) | P2 | 11 | todo | Rotation helper for generated secrets with staged rollout notes |
| [CONF-035](CONF-035.md) | P2 | 11 | todo | Key usage finder (which app reads which key, best effort static scan) |
