---
code: TRAIN
title: "Training Academy"
number: 34
status: draft
privileged: false
depends_on: [CORE, ONBD, GUID, DATA, PERM, GOVN]
code_path: admin_utils/training/
frontend_path: frontend/src/features/training/
tasks: docs/tasks/TRAIN/INDEX.md
---

# Spec 34 — Training Academy (`TRAIN`)

## Purpose

the most intuitive way to learn Frappe and ERPNext inside the product itself: role-based learning paths, a safe practice sandbox, automatic task verification, assessments and certification, with tools for trainers and measurable impact.

## Placement

- Python package: `admin_utils/training/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/training/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Training Academy Settings`; on/off flag `enable_training` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/training/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 9 |
| P1 | 40 |
| P2 | 31 |

Waves: wave 3 (49), wave 6 (1), wave 11 (30)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`ONBD`](07-onboarding-studio.md) must provide what this module consumes before dependent tasks start
- [`GUID`](35-guidance-engine.md) must provide what this module consumes before dependent tasks start
- [`DATA`](09-data-seeder.md) must provide what this module consumes before dependent tasks start
- [`PERM`](01-permissions-manager.md) must provide what this module consumes before dependent tasks start
- [`GOVN`](26-governance.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Learning paths & curricula

| ID | P | Wave | Task |
|---|---|---|---|
| [TRAIN-001](../tasks/TRAIN/TRAIN-001.md) | P0 | 3 | Course builder: courses, lessons and activities with learning objectives per lesson |
| [TRAIN-002](../tasks/TRAIN/TRAIN-002.md) | P0 | 3 | Learning paths per role aligned with the permission ladder (base, viewer, junior, self-support, senior, auditor) |
| [TRAIN-003](../tasks/TRAIN/TRAIN-003.md) | P0 | 3 | Lesson types: guided walkthrough, practice task, reading, video, quiz, scenario, checklist |
| [TRAIN-004](../tasks/TRAIN/TRAIN-004.md) | P0 | 3 | Practice sandbox with seeded scenario data and one-click reset |
| [TRAIN-005](../tasks/TRAIN/TRAIN-005.md) | P0 | 3 | Learner dashboard (my path, due items, achievements, next best action) |
| [TRAIN-006](../tasks/TRAIN/TRAIN-006.md) | P1 | 3 | Starter curricula: Frappe basics, Sales, Purchasing, Stock, Accounting, HR, Projects, Administration |
| [TRAIN-007](../tasks/TRAIN/TRAIN-007.md) | P1 | 3 | Prerequisites, unlock rules and optional advanced tracks |
| [TRAIN-008](../tasks/TRAIN/TRAIN-008.md) | P1 | 3 | Competency tags per lesson |
| [TRAIN-009](../tasks/TRAIN/TRAIN-009.md) | P1 | 3 | Competency matrix per role (what a Junior must be able to do) with tracking |
| [TRAIN-010](../tasks/TRAIN/TRAIN-010.md) | P1 | 3 | Scenario labs ("a customer disputes an invoice: find it and issue a credit note") |
| [TRAIN-011](../tasks/TRAIN/TRAIN-011.md) | P1 | 3 | Task verification engine that checks the sandbox state for correctness, not just clicks |
| [TRAIN-012](../tasks/TRAIN/TRAIN-012.md) | P1 | 3 | Automatic feedback explaining what went wrong and why |
| [TRAIN-013](../tasks/TRAIN/TRAIN-013.md) | P1 | 3 | Guided, assisted and unassisted (test) modes of the same task |
| [TRAIN-014](../tasks/TRAIN/TRAIN-014.md) | P1 | 3 | Glossary of Frappe terms (DocType, Workflow, Naming Series, Link field) with in-context definitions in EN/AR |
| [TRAIN-015](../tasks/TRAIN/TRAIN-015.md) | P1 | 3 | Concept explainers with visuals (document lifecycle, draft → submitted → cancelled, linked documents) |
| [TRAIN-016](../tasks/TRAIN/TRAIN-016.md) | P1 | 3 | Permission experience lessons: learners try each ladder level in the sandbox and see what it can and cannot do |
| [TRAIN-017](../tasks/TRAIN/TRAIN-017.md) | P2 | 11 | Drills for shortcuts, navigation and filters |
| [TRAIN-018](../tasks/TRAIN/TRAIN-018.md) | P2 | 11 | Spaced-repetition review of key concepts |
| [TRAIN-019](../tasks/TRAIN/TRAIN-019.md) | P2 | 11 | Case-study library of real-world processes |
| [TRAIN-020](../tasks/TRAIN/TRAIN-020.md) | P2 | 11 | Moderated peer tips |

### Sandbox & environments

| ID | P | Wave | Task |
|---|---|---|---|
| [TRAIN-021](../tasks/TRAIN/TRAIN-021.md) | P0 | 3 | Sandbox provisioning as a dedicated training company or throwaway site using DATA scenarios |
| [TRAIN-022](../tasks/TRAIN/TRAIN-022.md) | P0 | 3 | Sandbox isolation (no emails, webhooks, payments or notifications leave the training environment) |
| [TRAIN-023](../tasks/TRAIN/TRAIN-023.md) | P1 | 3 | Per-learner data namespace or snapshot restore |
| [TRAIN-024](../tasks/TRAIN/TRAIN-024.md) | P1 | 3 | Industry scenario packs (retail, wholesale, clinic, school, restaurant, contractor, NGO) |
| [TRAIN-025](../tasks/TRAIN/TRAIN-025.md) | P1 | 3 | Arabic and English training datasets with realistic names, items and amounts |
| [TRAIN-026](../tasks/TRAIN/TRAIN-026.md) | P1 | 3 | Reset to a known state between exercises and sessions |
| [TRAIN-027](../tasks/TRAIN/TRAIN-027.md) | P1 | 3 | Training date helper (set a "training today" for aging and period exercises) |
| [TRAIN-028](../tasks/TRAIN/TRAIN-028.md) | P2 | 11 | Fault-injection scenarios (wrong tax template, duplicate customer) for troubleshooting practice |
| [TRAIN-029](../tasks/TRAIN/TRAIN-029.md) | P2 | 11 | Multi-user simulation (trainer plays approver while learner plays requester) |
| [TRAIN-030](../tasks/TRAIN/TRAIN-030.md) | P2 | 11 | Sandbox resource limits and automatic cleanup |

### Assessment & certification

| ID | P | Wave | Task |
|---|---|---|---|
| [TRAIN-031](../tasks/TRAIN/TRAIN-031.md) | P0 | 3 | Quiz engine: single and multiple choice, ordering, matching, fill-in and "click where you would..." hotspots |
| [TRAIN-032](../tasks/TRAIN/TRAIN-032.md) | P1 | 3 | Practical assessments verified automatically in the sandbox |
| [TRAIN-033](../tasks/TRAIN/TRAIN-033.md) | P1 | 3 | Question banks with tags, difficulty and randomization |
| [TRAIN-034](../tasks/TRAIN/TRAIN-034.md) | P1 | 3 | Pass marks, attempts, cooldowns and remediation paths |
| [TRAIN-035](../tasks/TRAIN/TRAIN-035.md) | P1 | 3 | Certificates and badges per path with verification codes (EN/AR, themed through THEM) |
| [TRAIN-036](../tasks/TRAIN/TRAIN-036.md) | P1 | 3 | Manager or trainer sign-off for on-the-job competencies |
| [TRAIN-037](../tasks/TRAIN/TRAIN-037.md) | P1 | 3 | Link certification to permission levels (for example the Senior role is requested only after the "Submit & Reports" certification), through a GOVN-approved workflow |
| [TRAIN-038](../tasks/TRAIN/TRAIN-038.md) | P1 | 3 | Recertification schedules and expiry |
| [TRAIN-039](../tasks/TRAIN/TRAIN-039.md) | P2 | 11 | Question analysis (too easy, too hard, ambiguous) |
| [TRAIN-040](../tasks/TRAIN/TRAIN-040.md) | P2 | 11 | Lightweight exam controls (time limits, focus-loss notes), off by default |
| [TRAIN-041](../tasks/TRAIN/TRAIN-041.md) | P2 | 11 | Accessibility accommodations (extra time, alternative formats) |
| [TRAIN-042](../tasks/TRAIN/TRAIN-042.md) | P2 | 11 | Transcript and certificate export for HR records |

### Trainer & admin tools

| ID | P | Wave | Task |
|---|---|---|---|
| [TRAIN-043](../tasks/TRAIN/TRAIN-043.md) | P0 | 3 | Trainer console: assign courses, monitor progress, view each learner's sandbox attempt |
| [TRAIN-044](../tasks/TRAIN/TRAIN-044.md) | P1 | 3 | Cohorts and classes with schedules, attendance and materials |
| [TRAIN-045](../tasks/TRAIN/TRAIN-045.md) | P1 | 3 | Live-session mode: the trainer broadcasts a guided flow and learners follow step by step |
| [TRAIN-046](../tasks/TRAIN/TRAIN-046.md) | P1 | 3 | Learner help queue ("raise hand") with trainer responses |
| [TRAIN-047](../tasks/TRAIN/TRAIN-047.md) | P1 | 3 | Authoring workspace with templates, review and publishing |
| [TRAIN-048](../tasks/TRAIN/TRAIN-048.md) | P1 | 3 | Reusable content blocks (glossary entries, callouts, scenario setups) |
| [TRAIN-049](../tasks/TRAIN/TRAIN-049.md) | P1 | 3 | Course import/export (JSON, Markdown) and sharing between sites |
| [TRAIN-050](../tasks/TRAIN/TRAIN-050.md) | P1 | 3 | Translation workflow EN/AR with side-by-side editor |
| [TRAIN-051](../tasks/TRAIN/TRAIN-051.md) | P1 | 3 | Course catalog with search, tags and difficulty |
| [TRAIN-052](../tasks/TRAIN/TRAIN-052.md) | P2 | 11 | Training calendar and reminders |
| [TRAIN-053](../tasks/TRAIN/TRAIN-053.md) | P2 | 11 | Facilitator guides generated from a course |
| [TRAIN-054](../tasks/TRAIN/TRAIN-054.md) | P2 | 11 | Printable workbooks and handouts (theme-aware) |
| [TRAIN-055](../tasks/TRAIN/TRAIN-055.md) | P2 | 11 | Training effort and budget tracking |
| [TRAIN-056](../tasks/TRAIN/TRAIN-056.md) | P2 | 11 | Post-session surveys with trends |
| [TRAIN-057](../tasks/TRAIN/TRAIN-057.md) | P2 | 11 | Train-the-trainer path |
| [TRAIN-058](../tasks/TRAIN/TRAIN-058.md) | P2 | 11 | Content review cycle with owners and expiry dates |
| [TRAIN-059](../tasks/TRAIN/TRAIN-059.md) | P2 | 11 | Course versioning with learner migration |
| [TRAIN-060](../tasks/TRAIN/TRAIN-060.md) | P2 | 11 | Marketplace-ready course packs |

### Analytics & impact

| ID | P | Wave | Task |
|---|---|---|---|
| [TRAIN-061](../tasks/TRAIN/TRAIN-061.md) | P1 | 3 | Training dashboard (enrollment, completion, scores, time spent) |
| [TRAIN-062](../tasks/TRAIN/TRAIN-062.md) | P1 | 3 | Skill-gap report per team and role |
| [TRAIN-063](../tasks/TRAIN/TRAIN-063.md) | P1 | 3 | Training-versus-error correlation (do trained users make fewer entry errors?) with INSI |
| [TRAIN-064](../tasks/TRAIN/TRAIN-064.md) | P1 | 3 | Time-to-productivity tracking for new hires |
| [TRAIN-065](../tasks/TRAIN/TRAIN-065.md) | P1 | 3 | Per-lesson engagement and drop-off |
| [TRAIN-066](../tasks/TRAIN/TRAIN-066.md) | P2 | 11 | Impact view combining training effort with error and support reductions |
| [TRAIN-067](../tasks/TRAIN/TRAIN-067.md) | P2 | 11 | Compliance training tracker (mandatory courses, deadlines, overdue) |
| [TRAIN-068](../tasks/TRAIN/TRAIN-068.md) | P2 | 11 | Rule-based, explainable "who needs help" detection |
| [TRAIN-069](../tasks/TRAIN/TRAIN-069.md) | P2 | 11 | Opt-in, team-based leaderboards with privacy controls |
| [TRAIN-070](../tasks/TRAIN/TRAIN-070.md) | P2 | 11 | Executive summary reports |

### Integration & experience

| ID | P | Wave | Task |
|---|---|---|---|
| [TRAIN-071](../tasks/TRAIN/TRAIN-071.md) | P1 | 3 | Learning drawer in the app shell plus a link entry from the Frappe desk |
| [TRAIN-072](../tasks/TRAIN/TRAIN-072.md) | P1 | 3 | Mobile-friendly learning with offline-readable content |
| [TRAIN-073](../tasks/TRAIN/TRAIN-073.md) | P1 | 3 | Assignment, due-date and achievement notifications through NTFY |
| [TRAIN-074](../tasks/TRAIN/TRAIN-074.md) | P1 | 3 | Single sign-on with the Frappe account, no separate login |
| [TRAIN-075](../tasks/TRAIN/TRAIN-075.md) | P2 | 11 | Optional content sync with Frappe LMS when installed |
| [TRAIN-076](../tasks/TRAIN/TRAIN-076.md) | P2 | 11 | SCORM/xAPI-style result export for external learning systems |
| [TRAIN-077](../tasks/TRAIN/TRAIN-077.md) | P2 | 11 | Webhook events for completions (to HR systems) |
| [TRAIN-078](../tasks/TRAIN/TRAIN-078.md) | P2 | 11 | Opt-in portal training pages for external customers |
| [TRAIN-079](../tasks/TRAIN/TRAIN-079.md) | P2 | 6 | Ship courses inside generated apps (BLDR) so training travels with customizations |
| [TRAIN-080](../tasks/TRAIN/TRAIN-080.md) | P2 | 11 | "Train on my customization": draft lessons from a change set, reviewed by a human (AIAS-assisted) |

## Tests

- nightly Playwright playback of every flow on v15 and v16 in LTR and RTL; anchor-resilience tests that mutate the DOM; sandbox-isolation tests proving no email, webhook or payment leaves the training environment; task-verification tests with known-good and known-bad end states; keyboard-only and screen-reader walkthroughs; reading-level checks on shipped content.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Training sandbox causes real-world side effects (email, webhooks, payments): dedicated company/site, outbound blocking, isolation tests
- Training content goes stale: owners, review dates, release-based "what changed" flows

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
