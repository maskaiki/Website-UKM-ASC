# Rule: UKM ASC Website Design System & WordPress Deployment Standards

## 1. Visual Aesthetics & Design Tokens (White-First Editorial)
- **Concept**: Effica light-mode clean conversion structure + Gobo kinetic typography & cinematic easing.
- **Palette Tokens**:
  - `--bg`: `#FFFFFF` (Pure white canvas)
  - `--surface`: `#F7F7F5` (Warm alabaster for cards & subtle backgrounds)
  - `--ink`: `#0B0A0F` (Obsidian black for primary typography & giant hero ASC)
  - `--muted` / `--mono-muted`: `#67666C` / `#8E8D94` (Technical mono metadata & labels)
  - `--accent`: `#143B66` (Deep Qur'anic Sapphire — harmonizes with logo embroidery)
  - `--amber`: `#B8732A` (Warm gold — echoes jacket badge stitching)
  - `--border`: `rgba(11, 10, 15, 0.10)` (Subtle hairline divider)
- **Typography**:
  - Primary Sans: `Geist`, -apple-system, sans-serif
  - Monospace Meta: `Geist Mono`, ui-monospace, monospace
- **Easing Primitive**:
  - Gobo signature curve: `cubic-bezier(0.22, 0.31, 0, 1)`

## 2. Interactive Components Standard
- **Bracket Magnetic CTA**: Monospace buttons styled as `[ LABEL █ ]` with hovering bracket expansion and blinking cursor (`goboBlink`).
- **Hero Cutout Parallax**: Giant `ASC` type at `z-index: 1`, cutout photo at `z-index: 2` with subtle mouse parallax, text and CTA at `z-index: 3`.
- **Bidang Pembinaan**: Row-to-preview layout where hovering a row shifts text 14px and dynamically updates the sticky detail pane.
- **Program Kerja**: Real-time category filtering (`[ALL]`, `[PEMBINAAN]`, `[KOMPETISI]`, `[PENGABDIAN]`) with seamless `[GRID]` and `[LIST]` views.
- **Live WIB Clock**: Footer must include live Jakarta/Malang time with blinking colon.

## 3. WordPress Elementor & Asset Portability Guardrails
- **Elementor Canvas Mode**: Always insert code into an Elementor **HTML** widget set to Elementor Canvas (never Text Editor).
- **Asset Portability**:
  - Standalone compiled files (`index.standalone.html`) must use resilient image references: either absolute GitHub raw / Pages URLs, WordPress Media Library URLs, or fallback Data URIs so that pasting into Elementor does not trigger 404 broken images.
- **Cloudflare WAF**: Never attempt automated script or CLI bypass against `ormawa.um.ac.id`. Manual paste into Elementor is the sanctioned deployment path.
- **Python Build Escaping**: In `build.py`, all CSS curly braces within Python f-strings must be escaped as `{{` and `}}`.
