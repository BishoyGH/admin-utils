---
code: GUID
title: "In-App Guidance Engine"
number: 35
status: draft
privileged: false
depends_on: [CORE, THEM]
code_path: admin_utils/guidance/
frontend_path: frontend/src/features/guidance/
tasks: docs/tasks/GUID/INDEX.md
---

# Spec 35 — In-App Guidance Engine (`GUID`)

## Purpose

the runtime that makes guidance feel native: tours, hints and contextual help that appear at the right moment, in the user's language, and never get in the way.

## Placement

- Python package: `admin_utils/guidance/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/guidance/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `In-App Guidance Engine Settings`; on/off flag `enable_guidance` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/guidance/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 5 |
| P1 | 19 |
| P2 | 26 |

Waves: wave 3 (24), wave 11 (26)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`THEM`](06-theme-studio.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [GUID-001](../tasks/GUID/GUID-001.md) | P0 | 3 | Overlay runtime with spotlight, step cards, arrows and correct focus management |
| [GUID-002](../tasks/GUID/GUID-002.md) | P0 | 3 | Works inside the app SPA and on selected Frappe desk pages through a supported, non-invasive loader |
| [GUID-003](../tasks/GUID/GUID-003.md) | P0 | 3 | Element targeting by role, label, text and data attributes with fallbacks |
| [GUID-004](../tasks/GUID/GUID-004.md) | P0 | 3 | Anchor self-healing suggestions when the UI changes |
| [GUID-005](../tasks/GUID/GUID-005.md) | P0 | 3 | Event-driven progression (click, input, route change, document event, realtime event) |
| [GUID-006](../tasks/GUID/GUID-006.md) | P1 | 3 | Tooltips and hotspots that are persistent, dismissible or once-per-user |
| [GUID-007](../tasks/GUID/GUID-007.md) | P1 | 3 | Beacons that highlight new or recommended features |
| [GUID-008](../tasks/GUID/GUID-008.md) | P1 | 3 | "This page" help panel with relevant lessons, articles and glossary terms |
| [GUID-009](../tasks/GUID/GUID-009.md) | P1 | 3 | Field-level help showing meaning, example, common mistakes and who normally fills it |
| [GUID-010](../tasks/GUID/GUID-010.md) | P1 | 3 | Form walkthrough generated from doctype metadata (required fields first) |
| [GUID-011](../tasks/GUID/GUID-011.md) | P1 | 3 | Plain-language validation coaching with fix actions |
| [GUID-012](../tasks/GUID/GUID-012.md) | P1 | 3 | "Why can't I do this?" explanations tied to the permission explainer (PERM-027) |
| [GUID-013](../tasks/GUID/GUID-013.md) | P1 | 3 | Role-aware guidance (never teach actions the user cannot perform) |
| [GUID-014](../tasks/GUID/GUID-014.md) | P1 | 3 | Announcement banners and what's-new dialogs with targeting and scheduling |
| [GUID-015](../tasks/GUID/GUID-015.md) | P1 | 3 | Setup checklist widgets for workspaces |
| [GUID-016](../tasks/GUID/GUID-016.md) | P1 | 3 | Empty-state guidance ("no invoices yet, create your first") |
| [GUID-017](../tasks/GUID/GUID-017.md) | P1 | 3 | Keyboard shortcut coach (suggests shortcuts after repeated mouse actions) |
| [GUID-018](../tasks/GUID/GUID-018.md) | P1 | 3 | Task search: type "how to cancel an invoice" and start the matching guided flow |
| [GUID-019](../tasks/GUID/GUID-019.md) | P1 | 3 | Targeting rules by role, company, doctype, first-time use, language and device |
| [GUID-020](../tasks/GUID/GUID-020.md) | P1 | 3 | Frequency caps and fatigue controls so guidance never nags |
| [GUID-021](../tasks/GUID/GUID-021.md) | P1 | 3 | Do-not-disturb and dismiss-forever options with an admin override for critical notices |
| [GUID-022](../tasks/GUID/GUID-022.md) | P1 | 3 | Guidance analytics (views, completions, dismissals) |
| [GUID-023](../tasks/GUID/GUID-023.md) | P1 | 3 | Author preview and test mode on real pages without publishing |
| [GUID-024](../tasks/GUID/GUID-024.md) | P1 | 3 | Safety rule: guidance never auto-clicks, submits or changes data without explicit learner action, except sandbox "do it for me" |
| [GUID-025](../tasks/GUID/GUID-025.md) | P2 | 11 | Action recorder that turns recorded actions into editable steps, with personal-data redaction |
| [GUID-026](../tasks/GUID/GUID-026.md) | P2 | 11 | Animated cursor demonstration ("watch me do it") |
| [GUID-027](../tasks/GUID/GUID-027.md) | P2 | 11 | Narration support with captions (EN/AR) |
| [GUID-028](../tasks/GUID/GUID-028.md) | P2 | 11 | Picture-in-picture video lessons that stay visible while the user works |
| [GUID-029](../tasks/GUID/GUID-029.md) | P2 | 11 | Side-panel helper that answers task questions using approved content only (read-only, links AIAS-017) |
| [GUID-030](../tasks/GUID/GUID-030.md) | P2 | 11 | Context-triggered micro-surveys ("was this form easy to fill?") |
| [GUID-031](../tasks/GUID/GUID-031.md) | P2 | 11 | Guidance for customizations generated from BLDR change sets |
| [GUID-032](../tasks/GUID/GUID-032.md) | P2 | 11 | Flow compatibility tags for v15 and v16 UI differences |
| [GUID-033](../tasks/GUID/GUID-033.md) | P2 | 11 | All guidance elements themed through THEM tokens |
| [GUID-034](../tasks/GUID/GUID-034.md) | P2 | 11 | RTL-correct arrows, spotlights and step cards |
| [GUID-035](../tasks/GUID/GUID-035.md) | P2 | 11 | Accessibility: reduced motion, high contrast, screen-reader announcements |
| [GUID-036](../tasks/GUID/GUID-036.md) | P2 | 11 | Performance budget: runtime lazy-loaded and under 30 KB gzipped until activated |
| [GUID-037](../tasks/GUID/GUID-037.md) | P2 | 11 | Guidance as code: export and import as JSON in app repositories |
| [GUID-038](../tasks/GUID/GUID-038.md) | P2 | 11 | Multi-page flow state that survives reloads and navigation |
| [GUID-039](../tasks/GUID/GUID-039.md) | P2 | 11 | Interrupt handling (session timeout, errors) with graceful resume |
| [GUID-040](../tasks/GUID/GUID-040.md) | P2 | 11 | Guidance for ERPNext modules and custom apps through per-app, per-version anchor packs |
| [GUID-041](../tasks/GUID/GUID-041.md) | P2 | 11 | Shipped anchor packs for common ERPNext screens, versioned per release |
| [GUID-042](../tasks/GUID/GUID-042.md) | P2 | 11 | Post-upgrade detection of UI changes with a list of affected flows |
| [GUID-043](../tasks/GUID/GUID-043.md) | P2 | 11 | Author overlay that reveals all anchors on a page for debugging |
| [GUID-044](../tasks/GUID/GUID-044.md) | P2 | 11 | Conflict resolver when two flows target the same element |
| [GUID-045](../tasks/GUID/GUID-045.md) | P2 | 11 | "Tour of this site" generated from installed apps and workspaces |
| [GUID-046](../tasks/GUID/GUID-046.md) | P2 | 11 | Role-switch preview ("see guidance as a Junior") |
| [GUID-047](../tasks/GUID/GUID-047.md) | P2 | 11 | Nightly Playwright runner that plays every flow to catch broken steps |
| [GUID-048](../tasks/GUID/GUID-048.md) | P2 | 11 | Privacy-preserving, opt-in telemetry aggregates |
| [GUID-049](../tasks/GUID/GUID-049.md) | P2 | 11 | Admin kill switch that disables all guidance instantly |
| [GUID-050](../tasks/GUID/GUID-050.md) | P2 | 11 | Guidance catalog browser (search all tours, tips and checklists) |

## Tests

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
