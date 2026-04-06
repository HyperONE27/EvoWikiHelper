the first block of text is my patch list, I need to turn it into a list formatted like the second oneMar 22Check available skillsCheck available skillsHere's the patch list reformatted to match the wiki markup style from the second document:
* Versus
** Terran
*** [[Vulture]] attack period: 1.36 → 1.32 [1.9 → 1.8438]
*** [[Spider Mine|Spider Mines]] research time: 57.1 → 50 [80 → 70]
*** [[Dropship]] build cost: 100/50 → 100/25
*** [[Dropship]] build time: 25 → 22.9 [35 → 32]
*** [[Dropship]] HP: 180 → 150
*** [[Valkyrie]] attack period: 2.68 → 2.54 [3.75 → 3.5625]
** Zerg
*** [[Sunken Colony]] attack period: 1.34 → 1.25 [1.875 → 1.75]
*** [[Hydralisk Den]] build time: 28.6 → 25 [40 → 35]
*** [[Muscular Augments]] research cost: 100/100 → 125/125
*** [[Grooved Spines]] research cost: 100/100 → 125/125
*** [[Lurker]] attack range: 7 → 8
*** [[Lurker]] attack damage: 25 → 20 + 5 vs Light
*** [[Lurker]] attack damage increase per upgrade: +3 → +2
*** [[Spire]] build cost: 200/150 → 150/150
*** [[Spire]] build time: 71.4 → 66 [100 → 92.4]
*** [[Mutalisk]] attack range: 4.5 → 5
*** [[Mutalisk]] movement acceleration: 5.86 → 8.75 [4.1875 → 6.25]
*** [[Mutalisk]] radius: 0.6875 → 0.5
*** [[Mutalisk]] separation radius: 0.4 → 0.5
*** [[Parasite]] cannot target Frenzied units
*** [[Spawn Broodling]] cannot target Frenzied units
*** [[Spawn Broodling]] cast range: 10 → 9
*** [[Ultralisk]] radius: 0.875 → 0.75
*** [[Ultralisk]] model size: 0.8125 → 0.75
*** [[Defiler]] build time: 35.7 → 32.1 [50 → 45]
** Protoss
*** [[Pylon]] HP: 300 → 250
*** [[Pylon]] Plasma Shields: 300 → 250
*** [[Shield Battery]] build time: 25 → 21.4 [35 → 30]
*** [[Dragoon]] movement speed: 4.11 → 4.13 [2.9375 → 2.9531]
*** [[Gravitic Drive]] research cost: 125/125 → 150/150
*** [[Gravitic Drive]] research time: 71.4 → 78.6 [100 → 110]
*** [[Reaver|Reavers]] are no longer Massive
**** Scarabs remain Massive
*** [[Reaver]] build time: 39.2 → 35.7 [55 → 50]
*** The behavior of Scarabs re-tracking Adepts / Stalkers / Dark Templar after Psionic Transfer / Blink / Shadow Stride is no longer restricted to teleportations completing inside the original weapon range of the attacking Reaver and now will re-track the target at any range so long as the teleport completed in vision of the player owning the Reaver
**** This behavior is no longer cancelled if the Reaver that fired the Scarab is destroyed
**** This behavior is cancelled if the Reaver is lifted by the Phoenix's Graviton Beam
**** This behavior is still cancelled if the Reaver is picked up by a transport, or if the player owning the Reaver loses vision of the target
**** Scarabs will continue to track non-teleporting targets as usual, even without vision
*** [[Scarab]] build time: 4.69 → 4.38 [6.5625 → 6.125]
*** [[Scarab]] damage research cost: 125/125 → 150/150
*** [[Psionic Storm]] research time: 71.4 → 78.6 [100 → 110]
*** [[Hallucination]] no longer requires an upgrade
*** Hallucinations now follow BW rules instead of SC2 rules
*** [[Maelstrom]] research cost: 150/150 → 100/100
*** [[Mind Control]] can no longer target allied units
*** [[Scout]] build cost: 200/100 → 175/100
*** [[Scout]] build time: 34.3 → 32.1 [48 → 45]
*** [[Scout]] HP: 150 → 100
*** [[Scout]] movement speed: 4.46 → 4.55 [3.1875 → 3.25]
**** [[Gravitic Thrusters]] movement speed increase: 0.79 → 0.7 [0.5625 → 0.5]
*** [[Scout]] movement acceleration: 4.2 → 4.46 [3 → 3.1875]
*** [[Scout]] movement lateral acceleration: 4.2 → 2.8 [3 → 2]
*** [[Scout]] anti-air attack period: 0.98 → 0.89 [1.375 → 1.25]
*** [[Scout]] anti-ground attack damage bonus: +2 vs Light → +3 vs Light
*** [[Scout]] anti-ground attack damage point: 0.07 → 0.12 [0.1 → 0.167]
*** [[Corsair]] turning rate: 1400 → 2100 [999.8437 → 1499.9414]
*** [[Corsair]] stationary turning rate: 1050 → 2100 [749.8828 → 1499.9414]
*** [[Arbiter]] build cost: 100/300 → 100/350
*** [[Stasis Field]] research time: 71.4 → 64.3 [100 → 90]
A few things I handled:

Stripped the %green% BUFF %% / %red% NERF %% / %yellow% ADJUST %% tags since the target format doesn't use them
Converted section headers to ** Race and entries to *** / **** for sub-bullets
Wrapped unit/ability names in [[double brackets]] for wiki links, matching the pattern in doc 2 (you'll want to update those to match your exact wiki page paths like [[User:SCEvo/Scout|Scout]] if needed)
* Versus
** Terran
*** [[User:SCEvo/Marine|Marine]] build time: 17 → 16
*** [[User:SCEvo/Marine|Marine]] attack period: 0.69 → 0.67
*** [[User:SCEvo/SCAbility/Stimpack|Stimpack]] attack speed bonus for Marine: 100% → 75%
**** [[User:SCEvo/Marine|Marine]] attack period after Stimpack: 0.34 → 0.38
***pastedI guess I should have been more specific.
* units need to be hyperlinked as [[User:SCEvo/{unit}|{unit}]]
* abilities need to be hyperlinked as [[User:SCEvo/SCAbility/{ability}|{ability}]]
* upgrades need to be hyperlinked as [[User:SCEvo/SCUpgrade/{upgrade}|{upgrade}]]many abilities and upgrades also share names so you need to distinguish whether the document refers to an upgrade or an ability based on the property that is changed. also the wiki markup style should only use the 1.36 -> 1.32 section in 1.36 → 1.32 [1.9 → 1.8438]Mar 22Got it. Here's the reformatted list with proper hyperlinks and only the real-time values (dropping the bracketed game-speed values):
* Versus
** Terran
*** [[User:SCEvo/Vulture|Vulture]] attack period: 1.36 → 1.32
*** [[User:SCEvo/SCUpgrade/Spider Mines|Spider Mines]] research time: 57.1 → 50
*** [[User:SCEvo/Dropship|Dropship]] build cost: 100/50 → 100/25
*** [[User:SCEvo/Dropship|Dropship]] build time: 25 → 22.9
*** [[User:SCEvo/Dropship|Dropship]] HP: 180 → 150
*** [[User:SCEvo/Valkyrie|Valkyrie]] attack period: 2.68 → 2.54
** Zerg
*** [[User:SCEvo/Sunken Colony|Sunken Colony]] attack period: 1.34 → 1.25
*** [[User:SCEvo/Hydralisk Den|Hydralisk Den]] build time: 28.6 → 25
*** [[User:SCEvo/SCUpgrade/Muscular Augments|Muscular Augments]] research cost: 100/100 → 125/125
*** [[User:SCEvo/SCUpgrade/Grooved Spines|Grooved Spines]] research cost: 100/100 → 125/125
*** [[User:SCEvo/Lurker|Lurker]] attack range: 7 → 8
*** [[User:SCEvo/Lurker|Lurker]] attack damage: 25 → 20 + 5 vs Light
*** [[User:SCEvo/Lurker|Lurker]] attack damage increase per upgrade: +3 → +2
*** [[User:SCEvo/Spire|Spire]] build cost: 200/150 → 150/150
*** [[User:SCEvo/Spire|Spire]] build time: 71.4 → 66
*** [[User:SCEvo/Mutalisk|Mutalisk]] attack range: 4.5 → 5
*** [[User:SCEvo/Mutalisk|Mutalisk]] movement acceleration: 5.86 → 8.75
*** [[User:SCEvo/Mutalisk|Mutalisk]] radius: 0.6875 → 0.5
*** [[User:SCEvo/Mutalisk|Mutalisk]] separation radius: 0.4 → 0.5
*** [[User:SCEvo/SCAbility/Parasite|Parasite]] cannot target Frenzied units
*** [[User:SCEvo/SCAbility/Spawn Broodling|Spawn Broodling]] cannot target Frenzied units
*** [[User:SCEvo/SCAbility/Spawn Broodling|Spawn Broodling]] cast range: 10 → 9
*** [[User:SCEvo/Ultralisk|Ultralisk]] radius: 0.875 → 0.75
*** [[User:SCEvo/Ultralisk|Ultralisk]] model size: 0.8125 → 0.75
*** [[User:SCEvo/Defiler|Defiler]] build time: 35.7 → 32.1
** Protoss
*** [[User:SCEvo/Pylon|Pylon]] HP: 300 → 250
*** [[User:SCEvo/Pylon|Pylon]] Plasma Shields: 300 → 250
*** [[User:SCEvo/Shield Battery|Shield Battery]] build time: 25 → 21.4
*** [[User:SCEvo/Dragoon|Dragoon]] movement speed: 4.11 → 4.13
*** [[User:SCEvo/SCUpgrade/Gravitic Drive|Gravitic Drive]] research cost: 125/125 → 150/150
*** [[User:SCEvo/SCUpgrade/Gravitic Drive|Gravitic Drive]] research time: 71.4 → 78.6
*** [[User:SCEvo/Reaver|Reavers]] are no longer Massive
**** Scarabs remain Massive
*** [[User:SCEvo/Reaver|Reaver]] build time: 39.2 → 35.7
*** The behavior of [[User:SCEvo/Scarab|Scarabs]] re-tracking Adepts / Stalkers / Dark Templar after Psionic Transfer / Blink / Shadow Stride is no longer restricted to teleportations completing inside the original weapon range of the attacking [[User:SCEvo/Reaver|Reaver]] and now will re-track the target at any range so long as the teleport completed in vision of the player owning the [[User:SCEvo/Reaver|Reaver]]
**** This behavior is no longer cancelled if the [[User:SCEvo/Reaver|Reaver]] that fired the [[User:SCEvo/Scarab|Scarab]] is destroyed
**** This behavior is cancelled if the [[User:SCEvo/Reaver|Reaver]] is lifted by the Phoenix's Graviton Beam
**** This behavior is still cancelled if the [[User:SCEvo/Reaver|Reaver]] is picked up by a transport, or if the player owning the [[User:SCEvo/Reaver|Reaver]] loses vision of the target
**** [[User:SCEvo/Scarab|Scarabs]] will continue to track non-teleporting targets as usual, even without vision
*** [[User:SCEvo/Scarab|Scarab]] build time: 4.69 → 4.38
*** [[User:SCEvo/SCUpgrade/Scarab Damage|Scarab Damage]] research cost: 125/125 → 150/150
*** [[User:SCEvo/SCUpgrade/Psionic Storm|Psionic Storm]] research time: 71.4 → 78.6
*** [[User:SCEvo/SCUpgrade/Hallucination|Hallucination]] no longer requires an upgrade
*** Hallucinations now follow BW rules instead of SC2 rules
*** [[User:SCEvo/SCUpgrade/Maelstrom|Maelstrom]] research cost: 150/150 → 100/100
*** [[User:SCEvo/SCAbility/Mind Control|Mind Control]] can no longer target allied units
*** [[User:SCEvo/Scout|Scout]] build cost: 200/100 → 175/100
*** [[User:SCEvo/Scout|Scout]] build time: 34.3 → 32.1
*** [[User:SCEvo/Scout|Scout]] HP: 150 → 100
*** [[User:SCEvo/Scout|Scout]] movement speed: 4.46 → 4.55
**** [[User:SCEvo/SCUpgrade/Gravitic Thrusters|Gravitic Thrusters]] movement speed increase: 0.79 → 0.7
*** [[User:SCEvo/Scout|Scout]] movement acceleration: 4.2 → 4.46
*** [[User:SCEvo/Scout|Scout]] movement lateral acceleration: 4.2 → 2.8
*** [[User:SCEvo/Scout|Scout]] anti-air attack period: 0.98 → 0.89
*** [[User:SCEvo/Scout|Scout]] anti-ground attack damage bonus: +2 vs Light → +3 vs Light
*** [[User:SCEvo/Scout|Scout]] anti-ground attack damage point: 0.07 → 0.12
*** [[User:SCEvo/Corsair|Corsair]] turning rate: 1400 → 2100
*** [[User:SCEvo/Corsair|Corsair]] stationary turning rate: 1050 → 2100
*** [[User:SCEvo/Arbiter|Arbiter]] build cost: 100/300 → 100/350
*** [[User:SCEvo/SCUpgrade/Stasis Field|Stasis Field]] research time: 71.4 → 64.3
A few judgment calls worth flagging:

Spider Mines — treated as SCUpgrade since the changed property is research time (matches the pattern in the reference doc)
Hallucination — the "no longer requires an upgrade" line refers to the upgrade being removed, so I kept it as SCUpgrade but left it as prose since there's no stat value to display
Psionic Storm / Maelstrom / Stasis Field — research cost/time changes → SCUpgrade; cast behavior changes → SCAbility
Spawn Broodling — used singular to match the ability name convention in the reference doc (Spawn Broodlings appears to be the ability page name in some patches, let me know if you want it pluralized)
here's another batch, fix it up in the same format# Patch 1.18.1 Proposal - Revision #6

## Terran Changes
---
- %red% NERF %% Barracks build time: 46.4 → 50 [65 → 70]
- %red% NERF %% Restoration research time: 42.9 → 57.1 [60 → 80]
- %red% NERF %% Restoration Energy cost: 50 → 75
- %red% NERF %% Optic Flare research time: 42.9 → 64.3 [60 → 90]
- %green% BUFF %% Optic Flare Energy cost: 75 → 50
- %green% BUFF %% Lockdown research cost: 150/150 → 125/125
- %red% NERF %% Goliath anti-air attack period: 0.94 → 1.03 [1.3125 → 1.4375]
- %green% BUFF %% Charon Boosters attack range increase: +2 → +2.5
- %red% NERF %% Science Vessel build cost: 100/200 → 100/225
- %red% NERF %% Science Vessel build time: 34.3 → 39.3 [48 → 55]
- %green% BUFF %% EMP Shockwave research cost: 150/150 → 125/125

These changes were previously proposed and I am keeping them as-is.

---
- **%red% NERF %% SCV attack period: 1.07 → 1.1 [1.5 → 1.54]**

Parallel to Drone attack period buffs when 12 Pool Drone pull was all the rage.

## Zerg Changes
---
- %red% NERF %% Spore Colony attack damage: 20 → 15
- %green% BUFF %% Spore Colony attack period: 0.67 → 0.61 [0.9375 → 0.8608]
- %red% NERF %% Pneumatized Carapace movement speed increase: 2.25 → 2.16 [1.6055 → 1.543]
- %red% NERF %% Ventral Sacs research cost: 150/150 → 200/200
- %red% NERF %% Ventral Sacs research time: 64.3 → 71.4 [90 → 100]
- %red% NERF %% Hydralisk attack period: 0.67 → 0.69 [0.9375 → 0.9688]
- %green% BUFF %% Grooved Spines research cost: 125/125 → 75/75
- %red% NERF %% Spire build cost: 150/150 → 200/150
- %red% NERF %% Spire build time: 66 → 71.4 [92.4 → 100]
- %red% NERF %% Mutalisk attack damage: 10 → 9
- %red% NERF %% Mutalisk attack period: 1.21 → 1.25 [1.6875 → 1.75]
- %red% NERF %% Guardian attack damage: 25 → 20
- %red% NERF %% Guardian attack damage increase per upgrade: +3 → +2
- %green% BUFF %% Guardian attack period: 1.34 → 1.25 [1.875 → 1.75]
- %green% BUFF %% Guardian attack range: 10 → 11
- %red% NERF %% Devourer morph cost: 50/50 → 100/50
- %green% BUFF %% Devourer attack range: 7 → 8
- %green% BUFF %% Ultralisk build cost: 175/175 → 200/150
- %red% NERF %% Anabolic Synthesis research cost: 125/125 → 150/150
- %red% NERF %% Chitinous Plating research cost: 125/125 → 150/150

These changes were previously proposed and I am keeping them as-is.Show more7:27 PM* Versus
** Terran
*** [[User:SCEvo/Barracks|Barracks]] build time: 46.4 → 50
*** [[User:SCEvo/SCUpgrade/Restoration|Restoration]] research time: 42.9 → 57.1
*** [[User:SCEvo/SCAbility/Restoration|Restoration]] Energy cost: 50 → 75
*** [[User:SCEvo/SCUpgrade/Optic Flare|Optic Flare]] research time: 42.9 → 64.3
*** [[User:SCEvo/SCAbility/Optic Flare|Optic Flare]] Energy cost: 75 → 50
*** [[User:SCEvo/SCUpgrade/Lockdown|Lockdown]] research cost: 150/150 → 125/125
*** [[User:SCEvo/Goliath|Goliath]] anti-air attack period: 0.94 → 1.03
*** [[User:SCEvo/SCUpgrade/Charon Boosters|Charon Boosters]] attack range increase: +2 → +2.5
*** [[User:SCEvo/Science Vessel|Science Vessel]] build cost: 100/200 → 100/225
*** [[User:SCEvo/Science Vessel|Science Vessel]] build time: 34.3 → 39.3
*** [[User:SCEvo/SCUpgrade/EMP Shockwave|EMP Shockwave]] research cost: 150/150 → 125/125
*** [[User:SCEvo/SCV|SCV]] attack period: 1.07 → 1.1
** Zerg
*** [[User:SCEvo/Spore Colony|Spore Colony]] attack damage: 20 → 15
*** [[User:SCEvo/Spore Colony|Spore Colony]] attack period: 0.67 → 0.61
*** [[User:SCEvo/SCUpgrade/Pneumatized Carapace|Pneumatized Carapace]] movement speed increase: 2.25 → 2.16
*** [[User:SCEvo/SCUpgrade/Ventral Sacs|Ventral Sacs]] research cost: 150/150 → 200/200
*** [[User:SCEvo/SCUpgrade/Ventral Sacs|Ventral Sacs]] research time: 64.3 → 71.4
*** [[User:SCEvo/Hydralisk|Hydralisk]] attack period: 0.67 → 0.69
*** [[User:SCEvo/SCUpgrade/Grooved Spines|Grooved Spines]] research cost: 125/125 → 75/75
*** [[User:SCEvo/Spire|Spire]] build cost: 150/150 → 200/150
*** [[User:SCEvo/Spire|Spire]] build time: 66 → 71.4
*** [[User:SCEvo/Mutalisk|Mutalisk]] attack damage: 10 → 9
*** [[User:SCEvo/Mutalisk|Mutalisk]] attack period: 1.21 → 1.25
*** [[User:SCEvo/Guardian|Guardian]] attack damage: 25 → 20
*** [[User:SCEvo/Guardian|Guardian]] attack damage increase per upgrade: +3 → +2
*** [[User:SCEvo/Guardian|Guardian]] attack period: 1.34 → 1.25
*** [[User:SCEvo/Guardian|Guardian]] attack range: 10 → 11
*** [[User:SCEvo/Devourer|Devourer]] morph cost: 50/50 → 100/50
*** [[User:SCEvo/Devourer|Devourer]] attack range: 7 → 8
*** [[User:SCEvo/Ultralisk|Ultralisk]] build cost: 175/175 → 200/150
*** [[User:SCEvo/SCUpgrade/Anabolic Synthesis|Anabolic Synthesis]] research cost: 125/125 → 150/150
*** [[User:SCEvo/SCUpgrade/Chitinous Plating|Chitinous Plating]] research cost: 125/125 → 150/150
One judgment call: Restoration and Optic Flare each appear twice — once for a research time change (SCUpgrade) and once for an Energy cost change (SCAbility). I split them accordingly. I also folded the bolded SCV line in with the rest of the Terran changes since the bold was just authorial emphasis in your draft, not a structural distinction.if I wanted to create a skill file to give to any model to do this task, what would I need? I imagine I would need instructions + context + a data dump? mind you, the information could be presented in a variety of forms, not merely the particular one I gave you7:28 PM2 / 2For a skill file to handle this reliably, you'd need three things:
1. Instructions
The transformation rules:

Strip color tags (%red%, %green%, %yellow%, %%)
Strip bracketed game-speed values [x → y]
Convert section headers to ** Race wiki structure
Convert entries to *** / **** for sub-bullets
Use → not ->
Distinguish upgrade vs. ability vs. unit by what property is changing:

research cost/time → SCUpgrade
Energy cost, cast range, effect duration, etc. → SCAbility
HP, build time, attack period, movement speed, etc. → unit page


Link format: units as [[User:SCEvo/{Name}|{Name}]], abilities as [[User:SCEvo/SCAbility/{Name}|{Name}]], upgrades as [[User:SCEvo/SCUpgrade/{Name}|{Name}]]
Preserve sub-bullet structure for entries that have clarifying child notes

2. Disambiguation context
This is the hard part. Many names are ambiguous — Lockdown, Restoration, Optic Flare, Psionic Storm, Maelstrom, Stasis Field, etc. all have both an SCUpgrade and an SCAbility page. The model needs a lookup table mapping each name to whether it lives under unit/SCAbility/SCUpgrade, or flagging it as ambiguous (resolve by property changed). You'd also want the canonical URL-safe name for each entry since some differ from display names (e.g. Spawn_Broodling vs Spawn Broodlings, U-238_Shells with the underscore).
3. Examples
A small set of before/after pairs covering the main cases: a plain unit stat, a split upgrade/ability pair (like Restoration appearing twice), a sub-bullet entry, and a multi-word ability with a non-obvious URL slug. You don't need many — maybe 6-8 — but they need to cover the edge cases rather than the easy ones.
The data dump you mentioned would slot into #2: a structured list of every unit, ability, and upgrade name with its canonical page path. Without that, the model is guessing on slugs and ambiguous names, which is where errors will cluster. That list doesn't need to be exhaustive up front — you could seed it with just the names that are ambiguous or have non-obvious slugs, and let the model handle obvious cases by convention.
The input format variation you mentioned is genuinely low-risk given clear enough instructions — the structural signals (race headers, stat changes with →, sub-bullets) are stable across formats even if the surrounding syntax differs. The main thing instructions need to handle is "what counts as a sub-bullet vs. a new top-level entry," which your current format signals via indentation.==Patch Changes==
{| class="wikitable collapsible collapsed"
! Patch 1.11 <ref>{{Cite web|https://teamkoprulu.github.io/Koprulu-Blog/post-evo-1_11/|author=Team Koprulu|publisher=Team Koprulu|date=8 November 2024}}</ref>
|-
|
* Dual Photon Blasters attack period increased from 1.21 seconds to 1.34 sepastedthink I could automate this too?7:29 PMYes, but it's a different automation target than the patch notes conversion. This is essentially the inverse problem — you're extracting per-unit change history from a chronological patch log rather than converting a patch list into wiki markup.
The pipeline would look like:
Input: the full patch history document (in whatever form — your raw patch notes, the wiki markup from doc 3, etc.)
Step 1 — Extraction: For each patch, extract every change and tag it with (patch, race, entity, property, old_value, new_value). This is the structured intermediate representation. A model can do this reliably from your existing patch note format since the entries are already fairly regular.
Step 2 — Filtering: Group by entity, pull only the rows where entity matches the target unit/ability/upgrade.
Step 3 — Rendering: Convert each row to the wiki prose format ("X increased/decreased from A to B") and wrap in the wikitable collapsible template with the correct patch citation.
The main judgment calls the model needs to handle:

"increased" vs "decreased" (derivable from old/new values, except for things like damage that can go up or down in complex ways like 10 → 4 (x4) where the framing requires domain knowledge)
Which citation URL/metadata to attach to each patch (you'd want a static lookup table for this — patch number → URL, author, date)
Whether a property belongs on the unit page vs. a sub-page (e.g. Gravitic Thrusters changes appearing on the Scout page)

The trickiest part is the citation table — that's pure reference data you'd need to maintain separately and feed in. Everything else is mechanical enough that a model with clear instructions and a few examples could handle it in one pass.
Worth noting: the extraction step (Step 1) is also the most reusable piece. Once you have a clean structured representation of the full patch history, you can generate both the chronological patch wiki pages and the per-unit history pages from the same source, which is probably the right long-term architecture.can a skills file on its own, if sufficiently detailed and tie with maybe a light validation script for the LLM to check against, constitute an LLM automation pipeline7:44 PMYes, essentially. What you're describing is the minimal viable version of an LLM pipeline — a well-structured prompt (the skill file) plus a lightweight correctness check (the validation script). The validation script is doing the work that orchestration frameworks like LangChain or DSPy would handle with more ceremony.
The skill file covers:

Task decomposition (what steps to follow)
Format specification (what the output must look like)
Disambiguation rules (the lookup table, the upgrade/ability distinction)
Examples (the few-shot demonstrations)

The validation script covers:

Structural checks (every *** line has a properly formed wikilink, arrows are → not ->, no bracketed values remain, etc.)
Completeness checks (number of input entries roughly matches output entries)
Lookup table checks (every linked page slug exists in your known list)

What you don't get without more infrastructure:

Retry logic on validation failure (though you can just feed the validation output back to the model as a second pass, which is often enough)
Parallelism across large batches
Persistent state across runs

But for your use case — patch notes that come in discrete batches, maybe a few dozen entries at a time — a skill file plus a ~50-line Python validation script is genuinely the right amount of machinery. Adding an orchestration layer would be solving a scaling problem you don't have.
The one thing that would meaningfully improve reliability beyond those two pieces is a canonical entity list as a flat file the validation script checks against. Not because the model will hallucinate page slugs often, but because when it does, the error is silent without that check — the wiki just produces a red link instead of breaking in a detectable way.so...maybe a markdown file + a json file + a script7:44 PMExactly. The three artifacts map cleanly:
SKILL.md
The prompt/instructions — transformation rules, link format conventions, upgrade/ability disambiguation logic, input format variations the model should handle, and a handful of examples covering the edge cases (ambiguous names, sub-bullets, complex value representations like 4 (x4)).
entities.json
The canonical lookup table. Something like:
json{
  "Lockdown": { "type": "ambiguous", "unit": null, "upgrade": "Lockdown", "ability": "Lockdown" },
  "Restoration": { "type": "ambiguous", "upgrade": "Restoration", "ability": "Restoration" },
  "Spider Mines": { "type": "upgrade", "slug": "Spider_Mines" },
  "Sunken Colony": { "type": "unit", "slug": "Sunken Colony" }
}
This is also the artifact that grows incrementally as you add new patches — every new unit, ability, or upgrade that appears for the first time gets an entry.
validate.py
Checks the output against entities.json and enforces structural rules. Probably three classes of check:

Hard errors that mean the output is wrong: malformed wikilinks, -> instead of →, bracketed values surviving, unknown slug not in entities.json
Warnings that need human review: entry count mismatch between input and output, an ambiguous entity resolved the same way twice in a row (possible sign the model stopped thinking about it)
Info for your own records: which entities were newly encountered and need adding to the json

The script output then either gates the result or gets fed back to the model as a correction prompt, depending on how much you want to automate the retry loop.
The nice property of this setup is that each file has a clear owner — the skill file is edited when the task logic changes, the json is edited when new content is added, and the script is edited when you discover a new failure mode. They don't bleed into each other.