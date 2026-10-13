---
code: ONBD
title: "Onboarding Studio"
number: 07
status: draft
privileged: false
depends_on: [CORE, GUID]
code_path: admin_utils/onboarding/
frontend_path: frontend/src/features/onboarding/
tasks: docs/tasks/ONBD/INDEX.md
---

# Spec 07 — Onboarding Studio (`ONBD`)

## Purpose

Onboarding Studio: see feature groups below.

## Placement

- Python package: `admin_utils/onboarding/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/onboarding/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Onboarding Studio Settings`; on/off flag `enable_onboarding` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/onboarding/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 17 |
| P1 | 44 |
| P2 | 34 |

Waves: wave 3 (61), wave 6 (1), wave 11 (33)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`GUID`](35-guidance-engine.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [ONBD-001](../tasks/ONBD/ONBD-001.md) | P0 | 3 | Visual onboarding builder for Module Onboarding and steps |
| [ONBD-002](../tasks/ONBD/ONBD-002.md) | P0 | 3 | Step types: create entity, update settings, view list, report, video, custom route |
| [ONBD-003](../tasks/ONBD/ONBD-003.md) | P0 | 3 | Reorder steps by drag-and-drop |
| [ONBD-004](../tasks/ONBD/ONBD-004.md) | P0 | 3 | Step completion rules (manual, on-document-created, on-field-set) |
| [ONBD-005](../tasks/ONBD/ONBD-005.md) | P0 | 3 | Preview as end user |
| [ONBD-006](../tasks/ONBD/ONBD-006.md) | P0 | 3 | Assign onboarding to roles/users/modules |
| [ONBD-007](../tasks/ONBD/ONBD-007.md) | P0 | 3 | Progress tracking per user with percentage |
| [ONBD-008](../tasks/ONBD/ONBD-008.md) | P1 | 3 | Templates (new company, first sales invoice, inventory setup, HR setup) |
| [ONBD-009](../tasks/ONBD/ONBD-009.md) | P1 | 3 | Rich-text step descriptions with images |
| [ONBD-010](../tasks/ONBD/ONBD-010.md) | P1 | 3 | Video embed (allowlisted hosts only) |
| [ONBD-011](../tasks/ONBD/ONBD-011.md) | P1 | 3 | Arabic/English step content with RTL preview |
| [ONBD-012](../tasks/ONBD/ONBD-012.md) | P1 | 3 | Step dependency (locked until previous done) |
| [ONBD-013](../tasks/ONBD/ONBD-013.md) | P1 | 3 | Reset and re-run onboarding for a user |
| [ONBD-014](../tasks/ONBD/ONBD-014.md) | P1 | 3 | Export/import onboarding as JSON |
| [ONBD-015](../tasks/ONBD/ONBD-015.md) | P1 | 3 | Version history and restore |
| [ONBD-016](../tasks/ONBD/ONBD-016.md) | P1 | 3 | Validation of target routes/doctypes (broken step detection) |
| [ONBD-017](../tasks/ONBD/ONBD-017.md) | P1 | 3 | Auto-link onboarding to workspace blocks |
| [ONBD-018](../tasks/ONBD/ONBD-018.md) | P2 | 11 | Completion analytics (drop-off per step) |
| [ONBD-019](../tasks/ONBD/ONBD-019.md) | P2 | 11 | Reminder notifications for unfinished steps |
| [ONBD-020](../tasks/ONBD/ONBD-020.md) | P2 | 11 | Checklist-style onboarding for new hires (HR flavor) |
| [ONBD-021](../tasks/ONBD/ONBD-021.md) | P2 | 11 | Interactive tour overlays (highlight UI elements) within the app SPA |
| [ONBD-022](../tasks/ONBD/ONBD-022.md) | P2 | 11 | Feedback collection per step ("Was this helpful?") |
| [ONBD-023](../tasks/ONBD/ONBD-023.md) | P2 | 11 | Conditional steps by role or company |
| [ONBD-024](../tasks/ONBD/ONBD-024.md) | P2 | 11 | Completion certificates/badges |
| [ONBD-025](../tasks/ONBD/ONBD-025.md) | P2 | 11 | Onboarding diff on app upgrade |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [ONBD-026](../tasks/ONBD/ONBD-026.md) | P1 | 3 | Step action recorder (capture a click path to create a step) |
| [ONBD-027](../tasks/ONBD/ONBD-027.md) | P1 | 3 | Estimated time per step and total |
| [ONBD-028](../tasks/ONBD/ONBD-028.md) | P1 | 3 | Required vs optional steps |
| [ONBD-029](../tasks/ONBD/ONBD-029.md) | P1 | 3 | Branching paths by answers |
| [ONBD-030](../tasks/ONBD/ONBD-030.md) | P2 | 11 | Tooltips and hotspots anchored to existing app elements |
| [ONBD-031](../tasks/ONBD/ONBD-031.md) | P2 | 11 | Role-specific welcome screens |
| [ONBD-032](../tasks/ONBD/ONBD-032.md) | P2 | 11 | Gamified progress (streaks, milestones) off by default |
| [ONBD-033](../tasks/ONBD/ONBD-033.md) | P2 | 11 | Knowledge-check quizzes at the end of a flow |
| [ONBD-034](../tasks/ONBD/ONBD-034.md) | P2 | 11 | Admin dashboard of team onboarding status |
| [ONBD-035](../tasks/ONBD/ONBD-035.md) | P2 | 11 | Link steps to seeded sandbox data for practice |

### Authoring (zero-code, point-and-click)

| ID | P | Wave | Task |
|---|---|---|---|
| [ONBD-036](../tasks/ONBD/ONBD-036.md) | P0 | 3 | Onboarding studio: build a flow by clicking through the real app while the recorder captures steps |
| [ONBD-037](../tasks/ONBD/ONBD-037.md) | P0 | 3 | Single-panel step editor: title, instruction, target element, expected action and success check |
| [ONBD-038](../tasks/ONBD/ONBD-038.md) | P0 | 3 | Visual element picker: point at a UI element in a live preview to anchor a step |
| [ONBD-039](../tasks/ONBD/ONBD-039.md) | P0 | 3 | Resilient anchors (multiple selector strategies, role and text fallbacks) so steps survive UI changes |
| [ONBD-040](../tasks/ONBD/ONBD-040.md) | P0 | 3 | Auto-generate a draft flow from any DocType or workflow (create, fill key fields, save, submit) |
| [ONBD-041](../tasks/ONBD/ONBD-041.md) | P1 | 3 | Step type library: explain, click here, fill this, choose, wait for, watch, read, quiz |
| [ONBD-042](../tasks/ONBD/ONBD-042.md) | P1 | 3 | Flow branding (icon, cover image, colors from the active theme) |
| [ONBD-043](../tasks/ONBD/ONBD-043.md) | P1 | 3 | Rich step content: text, images, short clips, callouts, "why this matters", common mistakes |
| [ONBD-044](../tasks/ONBD/ONBD-044.md) | P1 | 3 | Per-step "Show me" animated demonstration and optional "Do it for me" in the sandbox |
| [ONBD-045](../tasks/ONBD/ONBD-045.md) | P1 | 3 | Escalating hints (hint 1, hint 2, show answer) |
| [ONBD-046](../tasks/ONBD/ONBD-046.md) | P1 | 3 | Success checks: field value, document created, status changed, route visited, allowlisted custom check |
| [ONBD-047](../tasks/ONBD/ONBD-047.md) | P1 | 3 | Validation of flows against the current UI (broken anchors, missing permissions, missing data) |
| [ONBD-048](../tasks/ONBD/ONBD-048.md) | P1 | 3 | Flow linter (too long, missing hints, unclear goals, missing Arabic translation) |
| [ONBD-049](../tasks/ONBD/ONBD-049.md) | P1 | 3 | Preview mode that plays the flow as a learner without saving progress |
| [ONBD-050](../tasks/ONBD/ONBD-050.md) | P1 | 3 | Draft, review and publish lifecycle with reviewer comments |
| [ONBD-051](../tasks/ONBD/ONBD-051.md) | P1 | 3 | Flow versioning with learner migration rules (restart, continue, map steps) |
| [ONBD-052](../tasks/ONBD/ONBD-052.md) | P2 | 11 | Authoring templates for common tasks (create a customer, post an invoice, run a report, approve a leave) |
| [ONBD-053](../tasks/ONBD/ONBD-053.md) | P2 | 11 | Co-authoring with comments and suggestions |
| [ONBD-054](../tasks/ONBD/ONBD-054.md) | P2 | 11 | Import flow content from Markdown, a slide outline or an SOP document |

### Learner experience

| ID | P | Wave | Task |
|---|---|---|---|
| [ONBD-055](../tasks/ONBD/ONBD-055.md) | P0 | 3 | Floating "Learning" launcher showing recommended next steps for the current user |
| [ONBD-056](../tasks/ONBD/ONBD-056.md) | P0 | 3 | Guided overlay with spotlight, arrow and step card that never blocks required controls |
| [ONBD-057](../tasks/ONBD/ONBD-057.md) | P0 | 3 | Pause, resume, skip, back and "restart this step" at any time |
| [ONBD-058](../tasks/ONBD/ONBD-058.md) | P0 | 3 | Plain-language, short step text with a reading-level check for authors |
| [ONBD-059](../tasks/ONBD/ONBD-059.md) | P1 | 3 | Progress ring and checklist with estimated time remaining |
| [ONBD-060](../tasks/ONBD/ONBD-060.md) | P1 | 3 | "Stuck?" button offering a hint, a colleague to ask, or the related help article |
| [ONBD-061](../tasks/ONBD/ONBD-061.md) | P1 | 3 | Fully keyboard and screen-reader operable guidance |
| [ONBD-062](../tasks/ONBD/ONBD-062.md) | P1 | 3 | Language switch mid-flow (English/Arabic) with RTL-correct overlays |
| [ONBD-063](../tasks/ONBD/ONBD-063.md) | P1 | 3 | Practice mode in a sandbox with seeded data and automatic reset |
| [ONBD-064](../tasks/ONBD/ONBD-064.md) | P1 | 3 | Everything created during practice is tagged and cleaned up |
| [ONBD-065](../tasks/ONBD/ONBD-065.md) | P1 | 3 | Professional, configurable encouragement (can be turned off) |
| [ONBD-066](../tasks/ONBD/ONBD-066.md) | P2 | 11 | Bite-size mode (two-minute micro-lessons) and deep-dive mode |
| [ONBD-067](../tasks/ONBD/ONBD-067.md) | P2 | 11 | Resume on another device with synced progress |
| [ONBD-068](../tasks/ONBD/ONBD-068.md) | P2 | 11 | Offline-readable cheat sheet export of any flow |

### Adaptive & role-based

| ID | P | Wave | Task |
|---|---|---|---|
| [ONBD-069](../tasks/ONBD/ONBD-069.md) | P0 | 3 | Role-based paths assigned automatically from ladder level and module access (links PERM) |
| [ONBD-070](../tasks/ONBD/ONBD-070.md) | P1 | 3 | Skill detection that skips steps the user has already done for real |
| [ONBD-071](../tasks/ONBD/ONBD-071.md) | P1 | 3 | Contextual triggers: first time opening a doctype, first use of a feature, first error on a form |
| [ONBD-072](../tasks/ONBD/ONBD-072.md) | P1 | 3 | Assign flows to users, roles, departments or companies with due dates |
| [ONBD-073](../tasks/ONBD/ONBD-073.md) | P1 | 3 | Manager view of team progress with gentle nudges |
| [ONBD-074](../tasks/ONBD/ONBD-074.md) | P1 | 3 | New-joiner journeys (day 1, week 1, month 1) combining accounts, tools and processes |
| [ONBD-075](../tasks/ONBD/ONBD-075.md) | P1 | 3 | Role-change journeys (promotion from junior to senior triggers training on the new capabilities) |
| [ONBD-076](../tasks/ONBD/ONBD-076.md) | P2 | 11 | Prerequisites and unlock rules between flows |
| [ONBD-077](../tasks/ONBD/ONBD-077.md) | P2 | 11 | Recommendations from the user's recent errors and unused features |
| [ONBD-078](../tasks/ONBD/ONBD-078.md) | P2 | 11 | Period-based flows (month-end close, stock count, year-end) |
| [ONBD-079](../tasks/ONBD/ONBD-079.md) | P2 | 11 | "What changed in this update" flows generated from change sets |

### Analytics & management

| ID | P | Wave | Task |
|---|---|---|---|
| [ONBD-080](../tasks/ONBD/ONBD-080.md) | P1 | 3 | Completion, drop-off and time-per-step analytics per flow |
| [ONBD-081](../tasks/ONBD/ONBD-081.md) | P1 | 3 | Step difficulty heatmap (where learners fail or ask for hints) |
| [ONBD-082](../tasks/ONBD/ONBD-082.md) | P1 | 3 | Anchor health dashboard (steps that stopped matching the UI) |
| [ONBD-083](../tasks/ONBD/ONBD-083.md) | P1 | 3 | Learner feedback on each step with a summary |
| [ONBD-084](../tasks/ONBD/ONBD-084.md) | P1 | 3 | Content ownership, review dates and stale-flow alerts |
| [ONBD-085](../tasks/ONBD/ONBD-085.md) | P1 | 3 | Language coverage report |
| [ONBD-086](../tasks/ONBD/ONBD-086.md) | P2 | 11 | A/B test of two flow versions |
| [ONBD-087](../tasks/ONBD/ONBD-087.md) | P2 | 11 | Time-to-productivity metrics for new users by role |
| [ONBD-088](../tasks/ONBD/ONBD-088.md) | P2 | 11 | Progress export (CSV, PDF) with privacy controls |
| [ONBD-089](../tasks/ONBD/ONBD-089.md) | P2 | 11 | Spaced reminders of key steps after completion |
| [ONBD-090](../tasks/ONBD/ONBD-090.md) | P2 | 11 | Cohort comparison before and after a training change |
| [ONBD-091](../tasks/ONBD/ONBD-091.md) | P2 | 11 | Admin "training health" score |
| [ONBD-092](../tasks/ONBD/ONBD-092.md) | P2 | 11 | Demo mode of a flow using a static recording for people without accounts |
| [ONBD-093](../tasks/ONBD/ONBD-093.md) | P2 | 11 | Embed a flow in a workspace block, an email or a share link for invited users |
| [ONBD-094](../tasks/ONBD/ONBD-094.md) | P2 | 6 | Ship onboarding flows inside generated apps (BLDR export) |
| [ONBD-095](../tasks/ONBD/ONBD-095.md) | P2 | 11 | Marketplace-ready flow packs with metadata and licensing |

## Tests

- v15/v16 schema compat fixtures, broken-link detection.
- nightly Playwright playback of every flow on v15 and v16 in LTR and RTL; anchor-resilience tests that mutate the DOM; sandbox-isolation tests proving no email, webhook or payment leaves the training environment; task-verification tests with known-good and known-bad end states; keyboard-only and screen-reader walkthroughs; reading-level checks on shipped content.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Guided flows break when the UI changes: resilient anchors, anchor health dashboard, nightly playback

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
