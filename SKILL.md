# SC Evo Patch Notes → Wiki Markup

You convert raw SC Evo patch notes into MediaWiki markup for the Team Koprulu wiki. The input arrives in `input.md` and may be in any format — markdown lists, plain text, tables, etc. You produce one or both output modes depending on what is requested.

Before processing, read `entities.json` to know which units, abilities, and upgrades exist and their canonical wiki slugs.

---

## Extraction

From the input, extract:

1. **Patch metadata**: version number, date, and URL. These will appear somewhere in the input text — look for patterns like version numbers (`1.18.1`), dates (`29 August 2024`), and URLs.
2. **Balance changes**: every discrete stat or behavior change, tagged with:
   - **Race**: Terran, Zerg, or Protoss
   - **Entity name**: the unit, ability, or upgrade being changed
   - **Entity type**: determined by the *property being changed* (see routing rules below)
   - **Property**: what stat is changing
   - **Old value / New value**: the real-time values only (strip any bracketed game-speed conversions like `[80 → 70]`)

### Stripping Rules

Remove from input before processing:
- Color tags: `%red%`, `%green%`, `%yellow%`, `%%`, `BUFF`, `NERF`, `ADJUST`
- Bracketed game-speed values: anything matching `[number → number]`
- Commentary paragraphs, editorial notes, horizontal rules (`---`), bold emphasis on individual entries
- Section decorators like "These changes were previously proposed..."

### Preservation Rules

Keep:
- Sub-bullet structure (clarifications, exceptions, caveats under a parent entry)
- Exact numeric precision from the real-time values
- Race ordering from the input

---

## Entity Type Routing

The **property being changed** determines the entity type and wiki link path:

### Unit / Building → `[[User:SCEvo/{slug}|{display}]]`

Properties: build time, build cost, HP, Plasma Shields, movement speed, movement acceleration, movement lateral acceleration, attack period, attack damage, attack damage increase per upgrade, attack range, attack damage bonus, attack damage point, radius, model size, separation radius, turning rate, stationary turning rate, morph cost

### Upgrade → `[[User:SCEvo/SCUpgrade/{slug}|{display}]]`

Properties: research cost, research time, movement speed increase, attack range increase

### Ability → `[[User:SCEvo/SCAbility/{slug}|{display}]]`

Properties: Energy cost, cast range, behavioral targeting changes (e.g., "cannot target X", "can no longer target X")

### Ambiguous Names

Many names exist as both an upgrade and an ability in `entities.json` (e.g., Lockdown, Restoration, Psionic Storm). When you encounter one:

- `research cost` or `research time` → **SCUpgrade**
- `Energy cost`, `cast range`, or behavioral change → **SCAbility**
- The same name CAN correctly appear twice in one patch, once as each type. This is not a duplicate.

### Slug Rules

- Look up the canonical slug in `entities.json`. Use it exactly.
- If the input uses a plural ("Reavers", "Scarabs"), the **slug** is still the canonical singular form, but the **display name** preserves the input form: `[[User:SCEvo/Reaver|Reavers]]`
- If an entity is NOT in `entities.json`, use best-guess routing by property, use the input name as the slug, and add a comment `<!-- NEW ENTITY: {name} -->` after the line so it can be flagged for review.

---

## Output Mode A: Patch Changelog

A full list of all changes from one patch, grouped by race.

### Format

```
* Versus
** {Race}
*** [[User:SCEvo/{path}|{display}]] {property}: {old} → {new}
*** [[User:SCEvo/{path}|{display}]] {behavioral description}
**** {sub-bullet clarification}
```

### Rules

- Top level: `* Versus`
- Race headers: `** Terran`, `** Zerg`, `** Protoss`
- Entries: `***`
- Sub-bullets: `****`
- Arrow: always `→` (never `->` or `-->`)
- Cost format: `minerals/gas` (e.g., `100/50 → 100/25`)
- Each `***` entry has exactly one wiki link for the entity being changed (unless it's a prose-only note with no specific entity, like "Hallucinations now follow BW rules instead of SC2 rules")

---

## Upgrade / Ability Ownership (Mode B)

When grouping changes into per-entity tables for Mode B, an upgrade or ability change belongs to the unit listed in its `belongs_to` field in `entities.json` — NOT to the structure that researches it. For example:

- `Grooved Spines` and `Muscular Augments` have `belongs_to: ["Hydralisk"]` → their changes go in the **Hydralisk** table, not Hydralisk Den.
- `Charon Boosters` belongs to Goliath → goes in the Goliath table, not Armory.
- `Stimpack` belongs to Marine and Firebat → put it in both tables.

The structure (Hydralisk Den, Armory, etc.) only gets its own entries for changes to the structure itself (build time, build cost, HP).

If an upgrade has no `belongs_to` field, route by best judgment and flag with `<!-- AMBIGUOUS OWNERSHIP: {name} -->`.

---

## Output Mode B: Per-Unit Patch History

For a specific unit/ability/upgrade's wiki page. Shows what changed for that entity in a given patch, wrapped in a collapsible wikitable with a citation.

### Format

```
{| class="wikitable collapsible collapsed"
! Patch {version}<ref>{{Cite web|url={url}|title=SCEvo Update {version} Notes|author=Team Koprulu|publisher=Team Koprulu|date={date}}}</ref>
|-
|
* {Change description in prose form.}
* {Another change.}
|}
```

### Prose Rules

For each change to the target entity, write one `*` bullet in natural prose:

| Condition | Wording |
|-----------|---------|
| Numeric value goes up | "{Property} increased from {old} to {new}." |
| Numeric value goes down | "{Property} reduced from {old} to {new}." |
| Ambiguous direction (complex values, mixed changes) | "{Property} adjusted from {old} to {new}." |
| Behavioral / qualitative change | Direct prose. e.g., "Can no longer target allied units." |

- Sentence case. End each bullet with a period.
- Use the property name in natural English (e.g., "Build time" not "build time:", "Anti-air attack period" not "anti-air attack period:")
- Sub-bullets from Mode A that belong to this entity become additional `*` entries or are folded into the parent's prose if they're short clarifications.

### Metadata

The version, date, and URL are extracted from the input. If any are missing, add a comment `<!-- MISSING: version/date/url -->` inside the wikitable header.

---

## Examples

### Mode A Examples

**Input:**
```
- %red% NERF %% Goliath anti-air attack period: 0.94 → 1.03 [1.3125 → 1.4375]
```
**Output:**
```
*** [[User:SCEvo/Goliath|Goliath]] anti-air attack period: 0.94 → 1.03
```

---

**Input:**
```
- %red% NERF %% Restoration research time: 42.9 → 57.1 [60 → 80]
- %red% NERF %% Restoration Energy cost: 50 → 75
```
**Output:**
```
*** [[User:SCEvo/SCUpgrade/Restoration|Restoration]] research time: 42.9 → 57.1
*** [[User:SCEvo/SCAbility/Restoration|Restoration]] Energy cost: 50 → 75
```

---

**Input:**
```
- Reavers are no longer Massive
  - Scarabs remain Massive
```
**Output:**
```
*** [[User:SCEvo/Reaver|Reavers]] are no longer Massive
**** Scarabs remain Massive
```

---

**Input:**
```
- %green% BUFF %% Charon Boosters attack range increase: +2 → +2.5
```
**Output:**
```
*** [[User:SCEvo/SCUpgrade/Charon Boosters|Charon Boosters]] attack range increase: +2 → +2.5
```

---

**Input:**
```
- Mind Control can no longer target allied units
```
**Output:**
```
*** [[User:SCEvo/SCAbility/Mind Control|Mind Control]] can no longer target allied units
```

---

**Input:**
```
- Hallucination no longer requires an upgrade
```
**Output:**
```
*** [[User:SCEvo/SCUpgrade/Hallucination|Hallucination]] no longer requires an upgrade
```

---

**Input:**
```
- %red% NERF %% Science Vessel build cost: 100/200 → 100/225
```
**Output:**
```
*** [[User:SCEvo/Science Vessel|Science Vessel]] build cost: 100/200 → 100/225
```

### Mode B Example

Given the Scout changes from a patch with version `1.17`, date `22 March 2025`, URL `https://teamkoprulu.github.io/Koprulu-Blog/post-evo-1_17/`:

**Output:**
```
{| class="wikitable collapsible collapsed"
! Patch 1.17 <ref>{{Cite web|url=https://teamkoprulu.github.io/Koprulu-Blog/post-evo-1_17/|author=Team Koprulu|publisher=Team Koprulu|date=22 March 2025}}</ref>
|-
|
* Build cost reduced from 200/100 to 175/100.
* Build time reduced from 34.3 seconds to 32.1 seconds.
* HP reduced from 150 to 100.
* Movement speed increased from 4.46 to 4.55.
* Movement acceleration increased from 4.2 to 4.46.
* Movement lateral acceleration reduced from 4.2 to 2.8.
* Anti-air attack period reduced from 0.98 to 0.89.
* Anti-ground attack damage bonus adjusted from +2 vs Light to +3 vs Light.
* Anti-ground attack damage point increased from 0.07 to 0.12.
|}
```
