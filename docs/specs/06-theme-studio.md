---
code: THEM
title: "Theme Studio"
number: 06
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/theme/
frontend_path: frontend/src/features/theme/
tasks: docs/tasks/THEM/INDEX.md
---

# Spec 06 — Theme Studio (`THEM`)

## Purpose

Theme Studio: see feature groups below.

## Placement

- Python package: `admin_utils/theme/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/theme/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Theme Studio Settings`; on/off flag `enable_theme` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/theme/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 14 |
| P1 | 58 |
| P2 | 38 |

Waves: wave 3 (72), wave 6 (1), wave 11 (37)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [THEM-001](../tasks/THEM/THEM-001.md) | P0 | 3 | Theme doctype storing design tokens (colors, radius, spacing, fonts, shadows) |
| [THEM-002](../tasks/THEM/THEM-002.md) | P0 | 3 | Token editor with live preview of desk-like components |
| [THEM-003](../tasks/THEM/THEM-003.md) | P0 | 3 | Color palette generator (50–950 scale from one base color) |
| [THEM-004](../tasks/THEM/THEM-004.md) | P0 | 3 | Contrast checker (WCAG AA/AAA) with warnings |
| [THEM-005](../tasks/THEM/THEM-005.md) | P0 | 3 | Light and dark variants per theme |
| [THEM-006](../tasks/THEM/THEM-006.md) | P0 | 3 | Compile tokens to CSS variables and serve as a static file |
| [THEM-007](../tasks/THEM/THEM-007.md) | P0 | 3 | Apply theme to the app's SPA instantly |
| [THEM-008](../tasks/THEM/THEM-008.md) | P0 | 3 | Apply theme to desk via supported mechanisms only (no core overrides) |
| [THEM-009](../tasks/THEM/THEM-009.md) | P0 | 3 | Activate/deactivate/revert theme with one click |
| [THEM-010](../tasks/THEM/THEM-010.md) | P1 | 3 | Typography settings (font family, sizes, weights, Arabic font pairing) |
| [THEM-011](../tasks/THEM/THEM-011.md) | P1 | 3 | Google Fonts/local fonts upload with licensing note |
| [THEM-012](../tasks/THEM/THEM-012.md) | P1 | 3 | Spacing, radius, border and shadow scales |
| [THEM-013](../tasks/THEM/THEM-013.md) | P1 | 3 | Component preview gallery (buttons, inputs, tables, badges, alerts, modals) |
| [THEM-014](../tasks/THEM/THEM-014.md) | P1 | 3 | Per-role or per-user theme assignment |
| [THEM-015](../tasks/THEM/THEM-015.md) | P1 | 3 | Per-company theme assignment |
| [THEM-016](../tasks/THEM/THEM-016.md) | P1 | 3 | Login page designer (logo, background, text, layout) |
| [THEM-017](../tasks/THEM/THEM-017.md) | P1 | 3 | Navbar/sidebar styling presets |
| [THEM-018](../tasks/THEM/THEM-018.md) | P1 | 3 | Print format and PDF styling tokens |
| [THEM-019](../tasks/THEM/THEM-019.md) | P1 | 3 | Email template styling tokens |
| [THEM-020](../tasks/THEM/THEM-020.md) | P1 | 3 | Website theme tokens (portal pages) |
| [THEM-021](../tasks/THEM/THEM-021.md) | P1 | 3 | Import/export theme as JSON |
| [THEM-022](../tasks/THEM/THEM-022.md) | P1 | 3 | Theme presets gallery (corporate, minimal, high-contrast, brand-based) |
| [THEM-023](../tasks/THEM/THEM-023.md) | P1 | 3 | Brand kit import (logo, palette, fonts from one JSON) |
| [THEM-024](../tasks/THEM/THEM-024.md) | P1 | 3 | Theme versioning and rollback |
| [THEM-025](../tasks/THEM/THEM-025.md) | P1 | 3 | Validation to prevent unreadable combinations |
| [THEM-026](../tasks/THEM/THEM-026.md) | P2 | 11 | Theme scheduling (seasonal/event themes) |
| [THEM-027](../tasks/THEM/THEM-027.md) | P2 | 11 | Density modes (compact/comfortable) |
| [THEM-028](../tasks/THEM/THEM-028.md) | P2 | 11 | High-contrast and reduced-motion accessibility presets |
| [THEM-029](../tasks/THEM/THEM-029.md) | P2 | 11 | Icon set selection |
| [THEM-030](../tasks/THEM/THEM-030.md) | P2 | 11 | Chart color palette editor |
| [THEM-031](../tasks/THEM/THEM-031.md) | P2 | 11 | Screenshot-based visual regression baselines per theme |
| [THEM-032](../tasks/THEM/THEM-032.md) | P2 | 11 | Theme diff between versions |
| [THEM-033](../tasks/THEM/THEM-033.md) | P2 | 11 | Theme usage analytics |
| [THEM-034](../tasks/THEM/THEM-034.md) | P2 | 11 | Shareable theme packages across sites |
| [THEM-035](../tasks/THEM/THEM-035.md) | P2 | 11 | CSS-injection safety scanner (blocks external URLs/scripts in custom CSS) |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [THEM-036](../tasks/THEM/THEM-036.md) | P1 | 3 | Semantic token layer (primary, success, warning, danger, surface, text) mapped to raw palette |
| [THEM-037](../tasks/THEM/THEM-037.md) | P1 | 3 | Button, input, table, card, modal style variants editor |
| [THEM-038](../tasks/THEM/THEM-038.md) | P1 | 3 | Focus ring and selection color controls |
| [THEM-039](../tasks/THEM/THEM-039.md) | P1 | 3 | Status badge palette for document states |
| [THEM-040](../tasks/THEM/THEM-040.md) | P1 | 3 | Theme linting (missing tokens, duplicate values, unreadable pairs) |
| [THEM-041](../tasks/THEM/THEM-041.md) | P2 | 11 | Gradient and background pattern library (safe, local assets) |
| [THEM-042](../tasks/THEM/THEM-042.md) | P2 | 11 | Animation/transition duration tokens and reduced-motion respect |
| [THEM-043](../tasks/THEM/THEM-043.md) | P2 | 11 | Responsive breakpoints editor |
| [THEM-044](../tasks/THEM/THEM-044.md) | P2 | 11 | Theme inheritance (child theme overrides parent tokens) |
| [THEM-045](../tasks/THEM/THEM-045.md) | P2 | 11 | Dark-mode auto-generation from light tokens with manual tweaks |
| [THEM-046](../tasks/THEM/THEM-046.md) | P2 | 11 | Theme preview on real screens (list, form, report) using seeded data |
| [THEM-047](../tasks/THEM/THEM-047.md) | P2 | 11 | Theme performance check (CSS size, unused variables) |
| [THEM-048](../tasks/THEM/THEM-048.md) | P2 | 11 | Export design tokens to Figma/Style Dictionary JSON |
| [THEM-049](../tasks/THEM/THEM-049.md) | P2 | 11 | Import tokens from Tailwind config |
| [THEM-050](../tasks/THEM/THEM-050.md) | P2 | 11 | Branding checklist (logo variants, favicon, splash, email header) |

### Visual design studio

| ID | P | Wave | Task |
|---|---|---|---|
| [THEM-051](../tasks/THEM/THEM-051.md) | P0 | 3 | WYSIWYG theme studio: click any element in a live preview of real screens and edit its style directly |
| [THEM-052](../tasks/THEM/THEM-052.md) | P0 | 3 | Split-screen live preview of list, form, report, dashboard, workspace and login pages using seeded data |
| [THEM-053](../tasks/THEM/THEM-053.md) | P0 | 3 | "Start from brand" wizard: upload a logo, extract a palette, generate a complete theme with accessible color pairs |
| [THEM-054](../tasks/THEM/THEM-054.md) | P0 | 3 | Simple mode (five controls: primary color, font, density, corner style, light/dark) and Advanced mode (all tokens) |
| [THEM-055](../tasks/THEM/THEM-055.md) | P1 | 3 | Element inspector showing which token controls the element under the cursor |
| [THEM-056](../tasks/THEM/THEM-056.md) | P1 | 3 | Undo/redo history with named checkpoints inside the studio |
| [THEM-057](../tasks/THEM/THEM-057.md) | P1 | 3 | Before/after toggle and comparison slider |
| [THEM-058](../tasks/THEM/THEM-058.md) | P1 | 3 | Device and viewport previews (desktop, tablet, phone) with an RTL toggle |
| [THEM-059](../tasks/THEM/THEM-059.md) | P1 | 3 | Preview as different roles (what a Junior sees versus an Auditor) to check navigation styling |
| [THEM-060](../tasks/THEM/THEM-060.md) | P1 | 3 | State previews: hover, focus, active, disabled, error, loading and empty |
| [THEM-061](../tasks/THEM/THEM-061.md) | P1 | 3 | Light and dark mode side-by-side preview |
| [THEM-062](../tasks/THEM/THEM-062.md) | P1 | 3 | Theme recipes: modern, classic, compact data-heavy, friendly, high-contrast, print-like |
| [THEM-063](../tasks/THEM/THEM-063.md) | P1 | 3 | Palette inspiration generator with lock controls (keep primary, vary the rest) |
| [THEM-064](../tasks/THEM/THEM-064.md) | P1 | 3 | Color picker with harmony rules (analogous, complementary, triadic) and named colors |
| [THEM-065](../tasks/THEM/THEM-065.md) | P1 | 3 | Gradient, shadow and elevation editors with visual handles |
| [THEM-066](../tasks/THEM/THEM-066.md) | P1 | 3 | Typography scale editor with live specimen in English and Arabic |
| [THEM-067](../tasks/THEM/THEM-067.md) | P1 | 3 | Arabic typography tuning: line height, letter spacing, weight pairing, numeral style |
| [THEM-068](../tasks/THEM/THEM-068.md) | P2 | 11 | Micro-interaction presets (subtle, standard, none) |
| [THEM-069](../tasks/THEM/THEM-069.md) | P2 | 11 | Empty-state illustration style packs using local assets only |
| [THEM-070](../tasks/THEM/THEM-070.md) | P2 | 11 | Icon stroke and style packs |

### Token system & accessibility

| ID | P | Wave | Task |
|---|---|---|---|
| [THEM-071](../tasks/THEM/THEM-071.md) | P0 | 3 | Automatic contrast repair: nudge a failing color to the nearest accessible value and show the change |
| [THEM-072](../tasks/THEM/THEM-072.md) | P1 | 3 | Color-blindness simulation previews (protanopia, deuteranopia, tritanopia) |
| [THEM-073](../tasks/THEM/THEM-073.md) | P1 | 3 | Status color semantics check (success, warning, danger distinguishable without color alone) |
| [THEM-074](../tasks/THEM/THEM-074.md) | P1 | 3 | Minimum font-size and touch-target checks |
| [THEM-075](../tasks/THEM/THEM-075.md) | P1 | 3 | Theme scorecard (accessibility, consistency, readability, performance) |
| [THEM-076](../tasks/THEM/THEM-076.md) | P1 | 3 | Token usage map showing unused and overused tokens |
| [THEM-077](../tasks/THEM/THEM-077.md) | P1 | 3 | Semantic layer editor with token dependency graph |
| [THEM-078](../tasks/THEM/THEM-078.md) | P1 | 3 | Component-level overrides with scope control (only tables, only buttons) |
| [THEM-079](../tasks/THEM/THEM-079.md) | P2 | 11 | Fluid type and spacing scale generator |
| [THEM-080](../tasks/THEM/THEM-080.md) | P2 | 11 | Screen-versus-print color parity checker |

### Scoping & governance

| ID | P | Wave | Task |
|---|---|---|---|
| [THEM-081](../tasks/THEM/THEM-081.md) | P1 | 3 | Theme assignment rules by role, company, department, user group, language and device |
| [THEM-082](../tasks/THEM/THEM-082.md) | P1 | 3 | Rule priority and conflict preview ("which theme will this user see") |
| [THEM-083](../tasks/THEM/THEM-083.md) | P1 | 3 | Personal tweaks within admin-defined limits (density, dark mode, font size) |
| [THEM-084](../tasks/THEM/THEM-084.md) | P1 | 3 | Approval workflow before a theme is activated (links GOVN) |
| [THEM-085](../tasks/THEM/THEM-085.md) | P1 | 3 | Staged rollout to a test group first, with instant rollback |
| [THEM-086](../tasks/THEM/THEM-086.md) | P1 | 3 | Theme lock during freeze periods |
| [THEM-087](../tasks/THEM/THEM-087.md) | P2 | 11 | A/B theme experiments with usability metrics |
| [THEM-088](../tasks/THEM/THEM-088.md) | P2 | 11 | Seasonal and event schedules with automatic revert |
| [THEM-089](../tasks/THEM/THEM-089.md) | P2 | 11 | Per-environment visual cue (staging and production look different) |
| [THEM-090](../tasks/THEM/THEM-090.md) | P2 | 11 | Theme change audit with before/after screenshots |

### Brand & delivery

| ID | P | Wave | Task |
|---|---|---|---|
| [THEM-091](../tasks/THEM/THEM-091.md) | P1 | 3 | Brand kit manager (logos, variants, favicon, clear-space rules, usage notes) |
| [THEM-092](../tasks/THEM/THEM-092.md) | P1 | 3 | Asset upload validation (size, format, transparency, sanitized SVG) |
| [THEM-093](../tasks/THEM/THEM-093.md) | P1 | 3 | Brand editor for login, signup, password reset and error pages |
| [THEM-094](../tasks/THEM/THEM-094.md) | P1 | 3 | Email header, footer and button styling synced from the theme |
| [THEM-095](../tasks/THEM/THEM-095.md) | P1 | 3 | PDF and print brand sync (letterhead, watermark, footer) with PRNT |
| [THEM-096](../tasks/THEM/THEM-096.md) | P1 | 3 | Mobile/PWA theme (status bar color, splash, icons) with MOBL |
| [THEM-097](../tasks/THEM/THEM-097.md) | P1 | 3 | Theme package export (tokens plus assets) and validated import |
| [THEM-098](../tasks/THEM/THEM-098.md) | P2 | 11 | Token export to Style Dictionary, CSS variables, Tailwind preset and Figma tokens |
| [THEM-099](../tasks/THEM/THEM-099.md) | P2 | 11 | Palette import from Figma, Tailwind config or a brand PDF |
| [THEM-100](../tasks/THEM/THEM-100.md) | P2 | 6 | Ship the theme inside a generated app via BLDR as app assets |
| [THEM-101](../tasks/THEM/THEM-101.md) | P2 | 11 | Theme library shared across sites (MSIT) |
| [THEM-102](../tasks/THEM/THEM-102.md) | P2 | 11 | Marketplace listing format with preview thumbnails and licensing metadata |

### Training-oriented theming

| ID | P | Wave | Task |
|---|---|---|---|
| [THEM-103](../tasks/THEM/THEM-103.md) | P1 | 3 | Training-mode theme that softly outlines learnable regions and shows labels |
| [THEM-104](../tasks/THEM/THEM-104.md) | P1 | 3 | Sandbox ribbon/banner so learners always know they are in practice mode |
| [THEM-105](../tasks/THEM/THEM-105.md) | P1 | 3 | Role-colored navigation accents so learners recognize their ladder level |
| [THEM-106](../tasks/THEM/THEM-106.md) | P1 | 3 | Readability presets for training (larger text, simplified chrome) |
| [THEM-107](../tasks/THEM/THEM-107.md) | P2 | 11 | Spotlight and dim-overlay styling shared with guided tours |
| [THEM-108](../tasks/THEM/THEM-108.md) | P2 | 11 | Coach-mark, tooltip and badge style editor shared by GUID and TRAIN |
| [THEM-109](../tasks/THEM/THEM-109.md) | P2 | 11 | Progress and celebration visuals (badges, confetti) that respect reduced motion |
| [THEM-110](../tasks/THEM/THEM-110.md) | P2 | 11 | Printable training material theme (handouts, cheat sheets) |

## Tests

- token → CSS compile snapshots, contrast checker vectors, CSS-injection blocklist.
- contrast auto-repair test vectors; assignment-rule precedence matrix; rollback restores the exact prior tokens; theme package export/import round trip; screenshot baselines per theme in light, dark, LTR and RTL.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Frappe UI breaking changes: pin versions, visual diffs on upgrade PRs

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
