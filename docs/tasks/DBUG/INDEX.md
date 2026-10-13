# DBUG — Error Debugger & Triage: tasks

Spec: [`37-error-debugger.md`](../../specs/37-error-debugger.md) · 70 tasks · done 0


## Triage & grouping

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [DBUG-001](DBUG-001.md) | P0 | 2 | todo | Error inbox listing grouped errors with count, first seen, last seen, affected users and status |
| [DBUG-002](DBUG-002.md) | P0 | 2 | todo | Fingerprinting that groups errors by exception type and normalized stack, ignoring volatile values |
| [DBUG-003](DBUG-003.md) | P0 | 2 | todo | Error detail page: message, exception chain, stack trace, request context (masked), environment and version info |
| [DBUG-004](DBUG-004.md) | P0 | 2 | todo | Status workflow (new, investigating, known issue, fixed, ignored) with owner and due date |
| [DBUG-005](DBUG-005.md) | P1 | 2 | todo | Classification: expected validation message, permission denial, data integrity, timeout, resource, integration, code defect |
| [DBUG-006](DBUG-006.md) | P1 | 2 | todo | Severity scoring from frequency, user impact, module criticality and trend |
| [DBUG-007](DBUG-007.md) | P1 | 2 | todo | Assignment rules (route by app, module or doctype to an owner) |
| [DBUG-008](DBUG-008.md) | P1 | 2 | todo | Reopen automatically when a "fixed" error returns after a later version |
| [DBUG-009](DBUG-009.md) | P1 | 2 | todo | Merge and split groups manually when fingerprinting is wrong |
| [DBUG-010](DBUG-010.md) | P1 | 2 | todo | Bulk actions (assign, ignore, resolve) with an undo window |
| [DBUG-011](DBUG-011.md) | P1 | 2 | todo | Ignore rules with reason and expiry |
| [DBUG-012](DBUG-012.md) | P1 | 2 | todo | Saved views (my errors, production-only, last release, security-related) |
| [DBUG-013](DBUG-013.md) | P2 | 11 | todo | Related errors suggestion (similar fingerprint, shared cause) |
| [DBUG-014](DBUG-014.md) | P2 | 11 | todo | Error budgets per module with breach alerts |
| [DBUG-015](DBUG-015.md) | P2 | 11 | todo | Weekly triage digest with new, rising and stale items |

## Understanding the error

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [DBUG-016](DBUG-016.md) | P0 | 2 | todo | Stack trace analyzer highlighting the first application frame and the likely responsible app |
| [DBUG-017](DBUG-017.md) | P0 | 2 | todo | Request context panel (user, role, doctype, method, route, form values with sensitive fields masked, browser, IP) |
| [DBUG-018](DBUG-018.md) | P1 | 2 | todo | "What changed before this" panel (recent change sets, config edits, permission applies, app updates, patches, backups, restarts) |
| [DBUG-019](DBUG-019.md) | P1 | 2 | todo | First-seen correlation with releases and change markers |
| [DBUG-020](DBUG-020.md) | P1 | 2 | todo | Affected-records view (which documents, users, companies hit the error) |
| [DBUG-021](DBUG-021.md) | P1 | 2 | todo | Breakdown charts (by app, doctype, user, browser, version, hour) |
| [DBUG-022](DBUG-022.md) | P1 | 2 | todo | Plain-language explanations for common Frappe errors (link validation, mandatory fields, naming conflicts, permission errors, deadlocks, timeouts, integrity errors) in EN/AR |
| [DBUG-023](DBUG-023.md) | P1 | 2 | todo | Known-issues catalog with symptoms, causes and fixes, searchable and extensible by admins |
| [DBUG-024](DBUG-024.md) | P1 | 2 | todo | Permission error debugger linked to the permission explainer (PERM-027) showing the exact rule that denied access |
| [DBUG-025](DBUG-025.md) | P1 | 2 | todo | Validation error helper showing which field and which rule failed, with a link to the doctype definition |
| [DBUG-026](DBUG-026.md) | P1 | 2 | todo | Database error helper (lock wait, deadlock, duplicate entry, data too long, missing column after migration) with next steps |
| [DBUG-027](DBUG-027.md) | P1 | 2 | todo | Timeout and gateway error helper correlating 502/504 with worker, queue and database state at the same time |
| [DBUG-028](DBUG-028.md) | P1 | 2 | todo | Memory and resource error helper correlating with MNTR metrics |
| [DBUG-029](DBUG-029.md) | P1 | 2 | todo | Source viewer that shows code around a frame from installed apps, read-only, with the file path |
| [DBUG-030](DBUG-030.md) | P2 | 11 | todo | Git blame and recent commit hints for the failing line when the app has a repository available |
| [DBUG-031](DBUG-031.md) | P2 | 11 | todo | Dependency and version suspect list (library recently upgraded) |
| [DBUG-032](DBUG-032.md) | P2 | 11 | todo | Client-side error capture from the app SPA and selected desk pages (opt-in, masked) with source-map support |
| [DBUG-033](DBUG-033.md) | P2 | 11 | todo | Browser and device breakdown for client errors |
| [DBUG-034](DBUG-034.md) | P2 | 11 | todo | Assistive explanation of a trace in plain language with human review (AIAS-006 extension) |

## Reproduce & fix

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [DBUG-035](DBUG-035.md) | P1 | 2 | todo | Reproduction bundle export (sanitized request context, relevant records anonymized, versions, steps) for a developer |
| [DBUG-036](DBUG-036.md) | P1 | 2 | todo | Sandbox reproduction: recreate the situation on a training or test site using seeded data |
| [DBUG-037](DBUG-037.md) | P1 | 2 | todo | Safe replay of an allowlisted failed request against a test site (never against production) |
| [DBUG-038](DBUG-038.md) | P1 | 2 | todo | Failed background job debugger: arguments (masked), queue history, retries, worker logs, one-click retry on a test site |
| [DBUG-039](DBUG-039.md) | P1 | 2 | todo | Failed email debugger (queue entry, SMTP response, recipient validation, template render check) |
| [DBUG-040](DBUG-040.md) | P1 | 2 | todo | Failed webhook and integration debugger with request, response, signature check and replay on a test endpoint |
| [DBUG-041](DBUG-041.md) | P1 | 2 | todo | Failed patch and migration debugger (which patch, which statement, state of the schema, safe recovery guidance) |
| [DBUG-042](DBUG-042.md) | P1 | 2 | todo | Failed import debugger (row-level reasons, corrected file generator) |
| [DBUG-043](DBUG-043.md) | P1 | 2 | todo | Failed print/PDF debugger (template errors, missing fields, rendering engine output) |
| [DBUG-044](DBUG-044.md) | P1 | 2 | todo | Scheduler and cron debugger (job never ran, ran twice, overlapped, stuck) |
| [DBUG-045](DBUG-045.md) | P1 | 2 | todo | Workflow and approval debugger (why a transition is unavailable, which condition failed) |
| [DBUG-046](DBUG-046.md) | P1 | 2 | todo | Server Script and Client Script error attribution (which script, which line, last edited by) |
| [DBUG-047](DBUG-047.md) | P2 | 11 | todo | Generate a regression test from an error case (links TSTD) |
| [DBUG-048](DBUG-048.md) | P2 | 11 | todo | Fix verification: after a fix is deployed, watch the fingerprint and confirm silence for a defined window |
| [DBUG-049](DBUG-049.md) | P2 | 11 | todo | Hotfix helper that packages a fix as a change set through BLDR and MIGR |
| [DBUG-050](DBUG-050.md) | P2 | 11 | todo | Rollback suggestion when an error appears right after a specific change set |

## Debug sessions

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [DBUG-051](DBUG-051.md) | P0 | 2 | todo | Time-boxed debug session for one user or one doctype that raises log verbosity and captures extra context, expiring automatically |
| [DBUG-052](DBUG-052.md) | P1 | 2 | todo | Verbose logging toggles for allowlisted loggers with auto-revert and audit |
| [DBUG-053](DBUG-053.md) | P1 | 2 | todo | Capture-on-error snapshots (request, user, settings) stored with masking and short retention |
| [DBUG-054](DBUG-054.md) | P1 | 2 | todo | "Ask the user to reproduce" flow: the user clicks a Record my session button, the admin receives a masked trace bundle |
| [DBUG-055](DBUG-055.md) | P1 | 2 | todo | Developer-mode awareness (clear warnings when developer mode or debug settings are on in production) |
| [DBUG-056](DBUG-056.md) | P2 | 11 | todo | Console for read-only diagnostic queries over an allowlist of safe diagnostics (never arbitrary code execution) |
| [DBUG-057](DBUG-057.md) | P2 | 11 | todo | Variable inspector for captured frames with sensitive-name masking and size limits (opt-in, off by default) |
| [DBUG-058](DBUG-058.md) | P2 | 11 | todo | Session recording of server-side events for one user flow (document events, hooks fired, permission checks) |

## Collaboration & reporting

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [DBUG-059](DBUG-059.md) | P1 | 2 | todo | Comments, mentions and attachments on an error group |
| [DBUG-060](DBUG-060.md) | P1 | 2 | todo | Create an issue draft for an external tracker (GitHub, GitLab or similar) with masked context, sent only after review |
| [DBUG-061](DBUG-061.md) | P1 | 2 | todo | Link errors to change requests (GOVN) and releases |
| [DBUG-062](DBUG-062.md) | P2 | 11 | todo | Incident declaration from an error group, linked to MNTR incidents |
| [DBUG-063](DBUG-063.md) | P2 | 11 | todo | Post-mortem generator (timeline, impact, cause, fix, follow-ups) |
| [DBUG-064](DBUG-064.md) | P2 | 11 | todo | MTTR and recurrence metrics by module and owner |
| [DBUG-065](DBUG-065.md) | P2 | 11 | todo | Error-to-training loop: recurring user mistakes create suggested lessons (TRAIN, INSI) |
| [DBUG-066](DBUG-066.md) | P2 | 11 | todo | Exportable error report (PDF, Markdown) for support or vendors, masked |
| [DBUG-067](DBUG-067.md) | P2 | 11 | todo | Shareable read-only error link with expiry, scoped and audited |
| [DBUG-068](DBUG-068.md) | P2 | 11 | todo | Vendor support bundle (versions, config summary, recent errors, health checks) with masking |
| [DBUG-069](DBUG-069.md) | P2 | 11 | todo | Guided debugging walkthroughs for common problems (GUID flows) |
| [DBUG-070](DBUG-070.md) | P2 | 11 | todo | Debugging knowledge base that grows from resolved errors (KNOW) |
