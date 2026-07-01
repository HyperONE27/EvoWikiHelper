---
title: "1.20 Patch Notes"
short_title: "1.20"
author: "HyperONE"
date: "2026-06-27"
blog-image: "/assets/img/blog/blog-update-1_20.webp"
tags: "Update, Extension"
---

# SC: Evo Complete Extension Update 1.20
***

Hello, everyone,

This update concludes the 1.20 PTR cycle, bringing substantial reworks to Terran production, adjustments across all races, and refinements based on three rounds of playtesting, replay data, and player feedback.

***
### Thank You For Your Support!
***

{{donations}}

{{toc}}

***
### A Word on StarCraft II Patch 5.0.16 and the 8-Worker Start
***

After careful consideration, the SC: Evo Complete multiplayer development team has decided not to follow the transition from a 12-worker start to an 8-worker start introduced in Patch 5.0.16, nor implement any of the balance or quality of life changes from that update, aside from purely cosmetic/audiovisual bug fixes. As of this post's publishing, all of these changes have been reverted.

We do not believe that Patch 5.0.16 accomplishes its stated goal of increasing overall strategic diversity across all three StarCraft II races. We also do not believe that an 8-worker start is feasible, given the existing variety of overspecialized worker harassment units and openers, without either comprehensively redesigning unit and structure specifications, or replacing StarCraft II's existing "Worker Pairing" economic model with more dynamic and forgiving alternatives, such as a Brood War-like economy or a Triple Harvest economy. The Patch 5.0.16 PTR demonstrated tremendous racial imbalance, which we think was insufficiently addressed by the minimal changes between the 5.0.16 PTR and 5.0.16 live versions. This would only be compounded by the aforementioned overspecialization of StarCraft II worker harassment units, which proved to be problematic for the early game last time SC: Evo Complete experimented with lower worker count starts in 2024.

SC: Evo Complete is meant to faithfully represent both the Brood War and StarCraft II games, and the most natural way to keep the StarCraft II factions—and by extension, SC: Evo Complete itself—accessible to incoming StarCraft II veterans is to maintain them exactly as they are in the current live version. However, given the lack of competent design and care put into the latest balance patch by Blizzard, we can no longer simply follow along with the official direction. Among the remaining possibilities, we think that freezing the specs of the StarCraft II races as they are in Patch 5.0.15 is the most intuitive and defensible, and we will maintain them here for the foreseeable future.

***
## New Models
***

It's been a while since we had a chance to add new models but rest assured we're working hard to get all of them in the game as soon as possible. This time however we've finally completed our work on the new models to replace the *less than ideal* Hatchery/Lair/Hive Models, as well as a brand new set of textures for the Queen to give her that authentic BW Feel.

These new models were brought to you thanks to Robert and Yohiner, they knocked these out of the park and we're incredibly excited about the upcoming batch of models.

{{compare animate="true"}}
| label    | before                                                | after                                                 |
|----------|-------------------------------------------------------|-------------------------------------------------------|
| hatchery | /assets/video/Hatchery_Star2.webm                     | /assets/video/Hatchery_Classic.webm                   |
| lair     | /assets/video/Lair_Star2.webm                         | /assets/video/Lair_Classic.webm                       |
| hive     | /assets/video/Hive_Star2.webm                         | /assets/video/Hive_Classic.webm                       |
| queen    | /assets/video/Queen_Star2.webm                        | /assets/video/Queen_Classic.webm                      |
{{/compare}}

> Due to technical difficulties the amount of new models for Patch 1.20 has been reduced.

*-Kat*

***
### A Brief Note
***

Please note that all speed- and time-related values are given as **Faster Speed [Normal Speed]**.

This list aggregates changes from all three 1.20 PTR phases, with some additional adjustments. These changes are marked using {{badge new}} and {{badge reverted}}.

***
## General Changes
***

- Concussive weapon damage ratio vs Shields: 75% -> {{buff}}87.5%{{/buff}}
- Explosive weapon damage ratio vs Shields: 75% -> {{buff}}87.5%{{/buff}}
- {{new}}Concussive weapon damage ratio vs Shields: 87.5% -> {{buff}}100%{{/buff}}{{/new}}
- {{new}}Explosive weapon damage ratio vs Shields: 87.5% -> {{buff}}100%{{/buff}}{{/new}}
<br>

At the start of the 1.20 PTR cycle, we nerfed the Hydralisk's attack period to discourage safely massing it against StarCraft II Terran, and raised the Concussive and Explosive weapon damage ratio vs Shields at the same time to keep the unit strong against StarCraft II Protoss. Partway through the cycle, playtesting showed the attack period nerf needed to go further, so we doubled down on it. Now, as we move to live, we are increasing the Shields damage ratio again to compensate.

The original rationale for decreasing the Concussive and Explosive weapon damage ratios vs Shields from their Brood War value of 100% was the concerning effectiveness of units with these weapons against StarCraft II Protoss, particularly the Vulture and Hydralisk. This was compounded by the Hydralisk's historically shorter attack period, the Concussive weapon damage ratio vs Armored units sitting at 37.5% rather than its original 25%, and the generally lower level of game knowledge and familiarity players had with SC: Evo Complete at the time.

Both of those conditions have since changed: the Concussive weapon damage ratio vs Armored targets has been reduced to its original 25%, and this patch substantially increases the Hydralisk's attack period. With both mitigating factors in place, we think we can proceed with a full reversion of the Concussive and Explosive weapon damage ratio vs Shields to its original value of 100%.

This change is aimed primarily at the Hydralisk in the StarCraft II Protoss matchup, which currently feels more like a unit Zerg is obligated to use than one that poses a real threat on its own. It allows Hydralisks to deal an additional 2.5 damage per hit against Plasma Shields, reducing their HTK count against Zealots by 1 and improving their TTK against Archons, even with their slower attack period this patch. Sunken Colonies also become more effective against Protoss as a result.

***
## Terran Changes
***

{{unit "scv"}}
- {{reverted}}Decreased attack period: 1.1 -> {{buff}}1.07{{/buff}} [1.54 -> {{buff}}1.5{{/buff}}]{{/reverted}}
{{/unit}}

***
{{unit "barracks"}}
- Decreased build cost: 150/0 -> {{buff}}125/0{{/buff}}
- Decreased build time: 50 -> {{buff}}48.2{{/buff}} [70 -> {{buff}}67.5{{/buff}}]
{{/unit}}

{{unit "factory"}}
- Decreased build cost: 150/100 -> {{buff}}125/75{{/buff}}
- Increased build time: 39.3 -> {{nerf}}41.1{{/nerf}} [55 -> {{nerf}}57.5{{/nerf}}]
{{/unit}}

{{unit "machineshop"}}
- Increased build cost: 50/25 -> {{nerf}}50/50{{/nerf}}
{{/unit}}

{{unit "starport"}}
- Decreased build cost: 150/100 -> {{buff}}125/75{{/buff}}
{{/unit}}

{{unit "controltower"}}
- Increased build cost: 50/25 -> {{nerf}}50/50{{/nerf}}
{{/unit}}

Based on the supply count of Brood War Terran in the early game, even adjusting for the supply density of certain units, it has become evident lately that Brood War Terran production throughput is simply too low. This is especially apparent in games where Terran is defending against 200/200 Roach timings.

The changes to Barracks, Factory, Starport, Machine Shop, and Control Tower build costs bring them into alignment with StarCraft II Terran production structures:
- Two BW Barracks now cost 250/0, whereas one SC2 Barracks + Reactor costs 200/50
- Two BW Factories/Starports now cost 250/150, whereas one SC2 Factory/Starport + Reactor costs 200/150
- One BW Factory/Starport + Machine Shop/Control Tower now cost 175/125, whereas one SC2 Factory/Starport + Tech Lab costs 200/125
<br>
We have also moved the Barracks build time closer to that of its StarCraft II counterpart and lengthened the build time of the Factory by the same amount.

***
{{unit "marine"}}
- Increased build time: 16.1 -> {{nerf}}17.9{{/nerf}} [22.5 -> {{nerf}}25{{/nerf}}]
{{/unit}}

{{unit "medic"}}
- Increased build time: 16.1 -> {{nerf}}17.9{{/nerf}} [22.5 -> {{nerf}}25{{/nerf}}]
{{/unit}}

{{unit "firebat"}}
- Increased build time: 16.1 -> {{nerf}}17.9{{/nerf}} [22.5 -> {{nerf}}25{{/nerf}}]
- Decreased attack period: 0.98 -> {{buff}}0.94{{/buff}} [1.375 -> {{buff}}1.3125{{/buff}}]
{{/unit}}

{{unit "vulture"}}
- Increased build time: 19.3 -> {{nerf}}21.4{{/nerf}} [27 -> {{nerf}}30{{/nerf}}]
- Decreased attack period: 1.32 -> {{buff}}1.25{{/buff}} [1.8437 -> {{buff}}1.75{{/buff}}]
{{/unit}}

{{unit "goliath"}}
- Increased build time: 22.1 -> {{nerf}}25{{/nerf}} [31 -> {{nerf}}35{{/nerf}}]
- Decreased Hellfire Missile Pack attack period: 1.03 -> {{buff}}0.94{{/buff}} [1.4375 -> {{buff}}1.3125{{/buff}}]
{{/unit}}

With production costs aligned, we are slowing the production of basic Terran units across the board, including the Marine, Medic, Firebat, Vulture, Goliath, and Wraith. The build times of units requiring a Machine Shop or a Control Tower are unaffected.

The Firebat, the Vulture, and the Goliath have received attack period reversions to Core. Particularly in the case of the Goliath, the previous anti-air attack period nerf did not create the intended effects in the Goliath-Tempest interaction and also made the Goliath unable to deal with Mutalisks efficiently.

***
{{unit "wraith"}}
- Increased build time: 27.1 -> {{nerf}}30{{/nerf}} [38 -> {{nerf}}42{{/nerf}}]
- Stacking is now {{adjust}}toggled on/off with a manual ability instead of automatically on movement{{/adjust}}
  - Stacking mode is toggled on a per-unit basis
  - Stacking mode is ON by default
  - Separation radius while stacking mode is enabled: 0.1 (unchanged)
  - Separation radius while stacking mode is disabled: 0.625 (unchanged)
  - (Note: Separation radius only affects flying units while they are in motion, so both stacking and non-stacking Wraiths will fully spread out when stationary)
{{/unit}}

In Patch 1.18.1, we implemented a mechanic allowing the Wraith and the Mutalisk to shrink their separation radii automatically when moving, allowing them to move in tight formations and enabling Brood War-style stacking controls. Players immediately noticed that this stacking enabled them to extract more value from Wraiths and Mutalisks/ However, since the stacking occurs automatically on movement and cannot be disabled, and since stacked air units clump so densely, players cannot easily reactively split specific units out of the formation. 

During the 1.20 PTR cycle, we tried to solve this problem and give players more control over air unit stacking by implementing a separation radius toggle. Since then, many viewers have expressed that they believe this toggle is contrived and out-of-place in StarCraft, especially for a standard melee-adjacent project like SC: Evo Complete. While we recognize that this toggle is slightly unusual, we think that allowing stacking mode to be toggled is a more accurate reflection of the fact that air units in Brood War could also be stacked and unstacked at will. Implementing the stacking behavior exactly as it was in Brood War — where it only activates when a non-Wraith/Mutalisk unit is included in the control group — while technically possible, would require many trigger-based checks that would harm game performance. StarCraft II and SC: Evo Complete are also no strangers to importing Brood War mechanics in a form that is easier to use, such as with the previously automatic Wraith/Mutalisk stacking, Hold Fire Lurkers, and worker-only paths to replacing workers bugging through mineral lines. Ultimately, we do not see this change as being out of line with what we have done in this mod before.

Overall, we expect this toggle to give Wraiths and Mutalisks more longevity into the late game as more splash damage units are available to deal with them.

***
{{unit "spidermine"}}
- Decreased HP: 25 -> {{nerf}}20{{/nerf}}
{{/unit}}

This change reverts the HP of the Spider Mine to its Core value, allowing it to be one-shot by Immortals. The HTK counts of most other ground units against the Spider Mine are not meaningfully affected.

***
{{unit "dropship"}}
- Increased build cost: 100/25 -> {{nerf}}100/50{{/nerf}}
- Increased movement acceleration: 1.93 -> {{buff}}2.45{{/buff}} [1.375 -> {{buff}}1.75{{/buff}}]
- Increased movement deceleration: 1.93 -> {{buff}}2.45{{/buff}} [1.375 -> {{buff}}1.75{{/buff}}]
{{/unit}}

Previously, we decreased the build cost of the Dropship from 100/50 to 100/25 to encourage players to use it more. However, upon further examination, it was not the build cost, the build time, or even the Control Tower tech prerequisite that discouraged players from using it. It is simply that the opportunity cost of not making Science Vessels once having invested resources into the Starport is too great, and if a player begins construction of both a Science Facility and a Control Tower simultaneously, there is not enough spare time on the Starport to squeeze in a Dropship. Later in the game, with more static defenses and air units, Dropships also become less effective.

In the few scenarios where producing Dropships does seem sensible, 100/25 seems obviously too cheap. Rather than try to encourage players to use Dropships with a disproportionately low build cost, we are reverting this value to 100/50. As an incremental buff to help make the unit feel more worthwhile for its build cost, we are matching its movement acceleration and deceleration with that of the Shuttle.

***
{{unit "ghost"}}
- Decreased HP: 60 -> {{nerf}}55{{/nerf}}
{{/unit}}

This change lowers the minimum amount of Energy on the Ghost for the StarCraft II High Templar to kill it in a single cast of Feedback from 120 to 110. The particular value of 55 prevents the StarCraft II Siege Tank from one-shotting the Ghost, even with Vehicle Weapons Level 3 research.

***
{{unit "sciencevessel"}}
- Irradiate damage {{nerf}}no longer stacks{{/nerf}}
- Decreased Defensive Matrix Energy cost: 100 -> {{buff}}75{{/buff}}
- Decreased Defensive Matrix barrier HP: 300 -> {{nerf}}250{{/nerf}}
{{/unit}}

The Science Vessel's power curve suffers from two extremes. Early on, even after Irradiate research is complete, the Science Vessel seems rather impotent against StarCraft II Zerg; many are required to reach the critical mass of Irradiate casts needed to hold off late-game Zerg armies. After amassing enough Science Vessels alongside a maxed-out Mech army, however, the Terran player quickly becomes nearly impossible to break; Ultralisks and Corruptors, the best available tools, melt to stacked Irradiate damage. While these traits could be considered characteristic of the original Science Vessel, we would like to feature smoother power curves in SC: Evo Complete and maintain fair potential for comebacks and counterplay.

To ease the transition into Science Vessels, we are reducing the Energy cost of Defensive Matrix to 75 and reverting its barrier HP to 250. We think the lower Energy cost better serves the ability's role as a transitional tool, creating more opportunities to leverage an ability often overshadowed by Irradiate and EMP Shockwave. To address the late-game entrenchment problem, Irradiate damage no longer stacks.

***
## Zerg Changes
***

{{unit "drone"}}
- Decreased attack period: 1.1 -> {{buff}}1.07{{/buff}} [1.54 -> {{buff}}1.5{{/buff}}]
{{/unit}}

***
{{unit "spawningpool"}}
- {{reverted}}Increased build time: 53.6 -> {{nerf}}57.1{{/nerf}} [75 -> {{nerf}}80{{/nerf}}]{{/reverted}}
{{/unit}}

{{unit "sunkencolony"}}
- Increased morph time: 14.3 -> {{nerf}}17.9{{/nerf}} [20 -> {{nerf}}25{{/nerf}}]
  - Increased total morph time: 28.6 -> {{nerf}}32.1{{/nerf}} [40 -> {{nerf}}45{{/nerf}}]
- Increased attack period: 1.25 -> {{nerf}}1.34{{/nerf}} [1.75 -> {{nerf}}1.875{{/nerf}}]
{{/unit}}

{{unit "zergling"}}
- Increased movement speed: 4.33 -> {{buff}}4.38{{/buff}} [3.0973 -> {{buff}}3.125{{/buff}}]
- {{reverted}}Decreased attack period: 0.421 -> {{buff}}0.414{{/buff}} [0.59 -> {{buff}}0.58{{/buff}}]{{/reverted}}
- {{reverted}}Decreased attack period: 0.414 -> {{buff}}0.407{{/buff}} [0.58 -> {{buff}}0.57{{/buff}}]{{/reverted}}
- {{reverted}}Decreased Metabolic Boost research time: 71.4 -> {{buff}}67.9{{/buff}} [100 -> {{buff}}95{{/buff}}]{{/reverted}}
{{/unit}}

{{unit "hydralisk"}}
- {{reverted}}Increased attack period: 0.69 -> {{nerf}}0.70{{/nerf}} [0.9687 -> {{nerf}}0.9843{{/nerf}}]{{/reverted}}
- Increased attack period: 0.69 -> {{nerf}}0.73{{/nerf}} [0.9687 -> {{nerf}}1.0156{{/nerf}}]
- Decreased Muscular Augments research cost: 125/125 -> {{buff}}100/100{{/buff}}
{{/unit}}

During the 1.20 PTR cycle, we tried to discourage players from blindly massing Hydralisks and Sunken Colonies without scouting by shifting some of their power onto the Zergling. +1 Carapace Hydralisk into Lurker play had become strong enough against StarCraft II Terran that there was little reason to explore alternative strategies. It was even possible on certain maps to use mass Hydralisks with barely any other support at all. Blind Sunken Colonies were similarly too strong and too forgiving to use in every matchup, even posing problems offensively against StarCraft II Zerg. To shift some of this power toward the Zergling, which rarely sees play outside of the early game and the late game after Adrenal Glands research completes, we gave it a faster attack period in exchange for delaying the completion time of the Spawning Pool. Our intention was to shift the emphasis of Zerg play in this matchup towards Zerglings, Lurkers, and Mutalisks.

After further playtesting and internal experimentation, we concluded that we could not justify the Zergling buff. Zerglings proved to be plenty strong as-is, and their current underutilization seems to be more of a stylistic preference than a real weakness; +1 Carapace Zerglings are already strong against Bio play. Brood War Zerg has enough strong tools to defend StarCraft II Terran aggression that we are comfortable nerfing the matchup without further compensation, so the Zergling attack period buff and the Spawning Pool and Metabolic Boost adjustments have been reverted.

What remains from this effort: the Hydralisk's attack period has been nerfed substantially and the Sunken Colony has had both its attack period and morph time increased. We are reducing the research cost of Muscular Augments to 100/100 as a consolation change for the now weaker Hydralisk.

The increase to Zergling movement speed, when combined with the 20% creep movement speed bonus for all Brood War Zerg units, allows them to reach 5.25 [3.75] movement speed on creep, which is as fast as a Reaper. This will limit the amount of economic disruption that can be inflicted by a single scouting Reaper while maintaining Zerg's vulnerability to aggression from several Reapers.

***
{{unit "lurker"}}
- {{new}}Increased attack damage: 24 -> {{buff}}25{{/buff}}{{/new}}
{{/unit}}

We previously changed Lurker attack damage from 25 to 24 so that +1 Ground Carapace Roaches could survive an extra hit from +1 Missile Attacks Lurkers. With Hydralisks substantially weakened against StarCraft II Zerg, we are reverting this change to maintain the existing strength level of Hydralisk-Lurker armies against Roach-Ravager forces. This reversion does not meaningfully affect HTKs against other ground units, such as StarCraft II Marines and Zerglings.

***
{{unit "mutalisk"}}
- Stacking is now {{adjust}}toggled on/off with a manual ability instead of automatically on movement{{/adjust}}
  - Stacking mode is toggled on a per-unit basis
  - Stacking mode is ON by default
  - Separation radius while stacking mode is enabled: 0.1 (unchanged)
  - Separation radius while stacking mode is disabled: 0.5 (unchanged)
  - (Note: Separation radius only affects flying units while they are in motion, so both stacking and non-stacking Mutalisks will fully spread out when stationary)
{{/unit}}

In Patch 1.18.1, we implemented a mechanic allowing the Wraith and the Mutalisk to shrink their separation radii automatically when moving, allowing them to move in tight formations and enabling Brood War-style stacking controls. Players immediately noticed that this stacking enabled them to extract more value from Wraiths and Mutalisks/ However, since the stacking occurs automatically on movement and cannot be disabled, and since stacked air units clump so densely, players cannot easily reactively split specific units out of the formation. 

During the 1.20 PTR cycle, we tried to solve this problem and give players more control over air unit stacking by implementing a separation radius toggle. Since then, many viewers have expressed that they believe this toggle is contrived and out-of-place in StarCraft, especially for a standard melee-adjacent project like SC: Evo Complete. While we recognize that this toggle is slightly unusual, we think that allowing stacking mode to be toggled is a more accurate reflection of the fact that air units in Brood War could also be stacked and unstacked at will. Implementing the stacking behavior exactly as it was in Brood War — where it only activates when a non-Wraith/Mutalisk unit is included in the control group — while technically possible, would require many trigger-based checks that would harm game performance. StarCraft II and SC: Evo Complete are also no strangers to importing Brood War mechanics in a form that is easier to use, such as with the previously automatic Wraith/Mutalisk stacking, Hold Fire Lurkers, and worker-only paths to replacing workers bugging through mineral lines. Ultimately, we do not see this change as being out of line with what we have done in this mod before.

Overall, we expect this toggle to give Wraiths and Mutalisks more longevity into the late game as more splash damage units are available to deal with them.

***
{{unit "scourge"}}
- {{reverted}}Decreased HP: 30 -> {{nerf}}25{{/nerf}}{{/reverted}}
- {{reverted}}Increased HP: 25 -> {{buff}}30{{/buff}}{{/reverted}}
- Decreased movement speed: 5.25 -> {{nerf}}4.9{{/nerf}} [3.75 -> {{nerf}}3.5{{/nerf}}]
{{/unit}}

One of the greatest beneficiaries among the Brood War units in the transition to the StarCraft II engine was the Scourge. In Brood War, although it was tied for being the fastest air unit in the game, Scourge could be dodged by enemies who exploited the unit's poor targeting with careful control. In StarCraft II's engine, Scourge now path directly toward enemy air units and never overkill. Moreover, StarCraft II races are much more dependent on their air units than their Brood War counterparts, especially StarCraft II Terran, whose Medivac is the backbone of its longevity and harassment capabilities. Scourge are so effective in their anti-air role, especially for their Vespene gas and supply cost, that Bio forces have a difficult time moving out onto the map past the early mid game.

At the onset of the 1.20 PTR cycle, we had some vague suspicion that the Scourge could use a nerf, and simply reverted the Scourge to its Core HP of 25. However, after we realized our issue with the Scourge specifically had to do with faster, non-capital air units, especially the Medivac, we reworked the Scourge to keep its higher HP value but with a slightly reduced movement speed. This change allows Medivacs to escape more easily, and slightly aids skilled players in focus-firing Scourge with Marines.

***
{{unit "guardian"}}
- {{new}}Increased attack damage: 20 -> {{buff}}25{{/buff}}{{/new}}
- {{new}}Decreased attack range: 11 -> {{nerf}}10{{/nerf}}{{/new}}
{{/unit}}

***
{{unit "infestedterran"}}
- Increased build cost: 75/25 -> {{nerf}}100/50{{/nerf}}
- Increased build time: 13.6 -> {{nerf}}17.9{{/nerf}} [19 -> {{nerf}}25{{/nerf}}]
- Increased attack damage: 307.5 -> {{buff}}375{{/buff}}
  - Increased damage vs Armored: 410 -> {{buff}}500{{/buff}}
{{/unit}}

Last year, numerous units received exotic or gratuitous buffs or reworks for no reason other than to encourage their use. One of these units was the Infested Terran, whose utility is limited not by its strength as a unit, but by how difficult it is to acquire. In the rare event that Infested Terrans see a couple games of use in the future, we think reverting the build cost and damage stats of this unit to their original values will produce the best player and spectator experience and create a feel reminiscent of the original game.

With some regard for how difficult it is to use, we have kept a moderate build time buff relative to the original 25 seconds. Astute readers may recognize 17.9 [25] seconds as equalling that of the Marine.

***
{{unit "ultralisk"}}
- Increased attack period: 0.60 -> {{nerf}}0.63{{/nerf}} [0.8437 -> {{nerf}}0.875{{/nerf}}]
{{/unit}}

We have noticed that the sheer speed of the Ultralisk allows it to disengage from combat and rotate around enemy defenses more quickly than its StarCraft II counterpart, perhaps to a degree that the StarCraft II races find difficult to contend with. However, we also do not want to simply remove the traits that distinguish the two Ultralisks if we can help it, so we are starting by nerfing the Ultralisk's weapon, which is one of its most buffed attributes relative to its Core value, and adjusting as needed.

***
## Protoss Changes
***

{{unit "gateway"}}
- {{reverted}}Decreased build cost: 150/0 -> {{buff}}125/0{{/buff}}{{/reverted}}
- {{reverted}}Increased build time: 46.4 -> {{nerf}}48.2{{/nerf}} [65 -> {{nerf}}67.5{{/nerf}}]{{/reverted}}
{{/unit}}

{{unit "zealot"}}
- Increased HP: 100 -> {{buff}}110{{/buff}}
- Decreased Plasma Shields: 60 -> {{nerf}}50{{/nerf}}
- Decreased Leg Enhancements research time: 71.4 -> {{buff}}64.3{{/buff}} [100 -> {{buff}}90{{/buff}}]
{{/unit}}

{{unit "dragoon"}}
- {{reverted}}Decreased attack period: 1.34 -> {{buff}}1.25{{/buff}} [1.875 -> {{buff}}1.75{{/buff}}]{{/reverted}}
- {{reverted}}Increased attack period: 1.25 -> {{nerf}}1.34{{/nerf}} [1.75 -> {{nerf}}1.875{{/nerf}}]{{/reverted}}
- {{reverted}}Increased Singularity Charge research time: 107.1 -> {{nerf}}125{{/nerf}} [150 -> {{nerf}}175{{/nerf}}]{{/reverted}}
- {{reverted}}Decreased Singularity Charge research time: 125 -> {{buff}}107.1{{/buff}} [175 -> {{buff}}150{{/buff}}]{{/reverted}}
- Increased HP: 100 -> {{buff}}110{{/buff}}
- Decreased Plasma Shields: 80 -> {{nerf}}70{{/nerf}}
{{/unit}}

{{unit "hightemplar"}}
- {{reverted}}Increased build time: 27.1 -> {{nerf}}32.1{{/nerf}} [38 -> {{nerf}}45{{/nerf}}]{{/reverted}}
{{/unit}}

{{unit "darktemplar"}}
- {{reverted}}Increased build time: 25 -> {{nerf}}32.1{{/nerf}} [35 -> {{nerf}}45{{/nerf}}]{{/reverted}}
- {{reverted}}Decreased build time: 32.1 -> {{buff}}27.1{{/buff}} [45 -> {{buff}}38{{/buff}}]{{/reverted}}
{{/unit}}

In the 1.20 PTR cycle, we attempted to rework Gateways to be cheaper, equalizing unit production throughput on a supply basis with other races. However, since Gateways only have one production speed throughout the entire game, unlike their StarCraft II counterparts which become faster as they transform into Warp Gates, any production throughput buffs have tremendous impact on early game balance. The adjustments we made to counteract this were clearly insufficient, and it has become clear to us that we simply cannot make Zealots and Dragoons produce any faster. An attempt to re-balance the Dragoon around its faster Core attack period relative to the live version failed for similar reasons. Therefore, we are reverting the Dragoon attack period buff and the build cost/time changes for the Gateway and all units produced from it, so that these units remain the same as they are in Patch 1.19.1.

Leg Enhancements research time has been decreased, allowing Zealots to come online in the mid game slightly sooner against StarCraft II Zerg and Protoss.

Zealot and Dragoon vitals have been reworked to allow them to survive one use of Disruption Nova, since it has become clear as of late that Brood War Protoss effectively has no frontal engagement tools due to many of their units being one-shot and outranged by Disruptors. The vitals redistribution of these units also happens to serve as a marginal buff against StarCraft II Zerglings.

***
{{unit "archon"}}
- Decreased attack period: 0.98 -> {{buff}}0.85{{/buff}} [1.375 -> {{buff}}1.1875{{/buff}}]
{{/unit}}

Gateway play still seems undertuned against StarCraft II Zerg, but there does not seem to be any room to further increase unit production throughput without adverse effects on the early game. This reset of the Archon's attack period to its Core value is a targeted buff for the StarCraft II Zerg matchup, allowing it to serve as a more capable frontliner against Zerglings and Hydralisks, especially in combination with Leg Enhancements Zealots.

***
{{unit "darkarchon"}}
- Increased Feedback cast range: 10 -> {{buff}}10.5{{/buff}}
- Decreased Mind Control research cost: 150/150 -> {{buff}}100/100{{/buff}}
- Decreased Mind Control Energy cost: 150 -> {{buff}}125{{/buff}}
{{/unit}}

The Dark Archon often feels like a unit that is either wholly inferior to the High Templar in cost-effectiveness or only produced for its synergy with High Templar. These adjustments aim to address this by allowing Dark Archons to better justify their resource and supply cost independently.

The Feedback range increase allows Dark Archons to outrange the Feedback ability of StarCraft II High Templar. This enables them to better protect other Brood War Protoss spellcasters, such as Arbiters, which are needed against Disruptors for their Stasis Field ability.

The Mind Control buffs are intended to rescue this ability from meme status and give it a legitimate niche. Even though Mind Control can affect any unit — not only removing that unit from the opponent's army but also handing control to the casting player — it was a difficult ability to use, since the Dark Archon costs 250/150 resources and 4 supply and is not as easy to produce, maneuver, or conceal from the enemy as the Queen. We hope that the reductions in Mind Control research and Energy costs can help give it a legitimate niche.

***
{{unit "shuttle"}}
- Decreased build cost: 200/0 -> {{buff}}175/0{{/buff}}
- Increased Plasma Shields: 70 -> {{buff}}80{{/buff}}
- Decreased Gravitic Drive research cost: 150/150 -> {{buff}}100/100{{/buff}}
{{/unit}}

{{unit "reaver"}}
- {{new}}{{buff}}Added Massive Attribute{{/buff}}{{/new}}
- Increased HP: 100 -> {{buff}}110{{/buff}}
- Decreased Plasma Shields: 80 -> {{nerf}}70{{/nerf}}
- Decreased sight range: 9 -> {{nerf}}8{{/nerf}}
- Decreased attack range: 10 -> {{nerf}}9{{/nerf}}
- Decreased movement speed: 1.4 -> {{nerf}}1.3125{{/nerf}} [1 -> {{nerf}}0.9375{{/nerf}}]
- {{reverted}}Increased Unload stun duration: 1.12 -> {{nerf}}1.25{{/nerf}} [1.5625 -> {{nerf}}1.75{{/nerf}}]{{/reverted}}
- {{reverted}}Decreased Unload stun duration: 1.25 -> {{buff}}1.12{{/buff}} [1.75 -> {{buff}}1.5625{{/buff}}]{{/reverted}}
{{/unit}}

{{unit "scarab"}}
- Decreased movement speed: 8.4 -> {{nerf}}7.88{{/nerf}} [6 -> {{nerf}}5.625{{/nerf}}]
- Increased Scarab inner radius: 0.1875 -> {{adjust}}0.3125{{/adjust}}
  - (Note: Inner radius affects collision behavior with structures)
- {{reverted}}Increased Scarab radius: 0.125 -> {{adjust}}0.1875{{/adjust}}{{/reverted}}
  - {{reverted}}(Note: Radius affects collision behavior with other units){{/reverted}}
{{/unit}}

Lately, Shuttle-Reaver play has all but disappeared from the meta-game, replaced by Gateway and Stargate-centric compositions. This has been a drastic shift from the earlier days of the mod, where Shuttle-Reaver into Dragoon-Reaver pushes were the norm. While we are glad to have achieved greater build variety over time, it is regrettable that, in establishing the direction of Brood War Protoss design and balance in previous patches, one of the most iconic aspects of Brood War Protoss gameplay has fallen to the wayside.

Unlike the tech branches ending in the Fleet Beacon and Templar Archives, where a Protoss player can choose to end at the Stargate and the Citadel of Adun and play a hybrid composition in the mid-game, the Robotics Facility lacks the ability to produce a combat unit without the Robotics Support Bay, so this tech branch is inherently very all-or-nothing. Shuttle-Reaver requires such a significant initial investment that losing the Shuttle and Reaver early is often unrecoverable. These changes aim to make Shuttle-Reaver harassment safer, less committal, and more affordable, while reducing the likelihood that Reaver drops inflict game-ending damage. Reduced costs on Shuttle production and Gravitic Drive research, alongside a slight bump in Plasma Shields, should encourage players to leverage Gravitic Drive Shuttles more freely. Decreases to Scarab movement speed and the Reaver movement speed nerf further distinguish the value of Shuttled versus un-Shuttled Reavers.

We recently increased the Reaver's attack range from 9 to 10 to give Protoss a consistent tool against Seismic Spines Lurkers. While the increase accomplishes this goal, it also made the Reaver too strong against other ground units—in hindsight, trying to buff the Reaver this way would inevitably make it practically impervious to ground attacks. As such, we are reverting the Reaver's attack range from 10 to 9. A sight range reduction from 9 to 8 serves as a further discouragement against leaving Reavers unattended or unsupported.

Reaver vitals have been reworked to allow them to survive one use of Disruption Nova, since it has become clear as of late that Brood War Protoss effectively has no frontal engagement tools due to many of their units being one-shot and outranged by Disruptors. The vitals redistribution of the Reaver also happens to serve as a marginal buff against StarCraft II Zerglings.

The return of the Massive tag to the Reaver is another change aimed at the StarCraft II Protoss. With Robotics Support Bay tech being so expensive, allowing Reavers to be targets of the Phoenix's Graviton Beam was especially painful for Brood War Protoss, discouraging players from choosing this tech branch in a matchup where Brood War Protoss suffers from a lack of viable options. Their inability to shatter Force Fields added insult to injury, and Massive Scarabs alone did not seem to be as consistent in dealing with them.

The change to inner radius prevents the Scarab from passing between the corner of a main ramp and a Supply Depot or Pylon built on it.

***
{{unit "scout"}}
- {{reverted}}Decreased Plasma Shields: 100 -> {{nerf}}80{{/nerf}}{{/reverted}}
- {{reverted}}Increased Plasma Shields: 80 -> {{buff}}100{{/buff}}{{/reverted}}
- Increased Dual Photon Blasters attack damage: 6 -> {{buff}}7{{/buff}}
- Decreased Dual Photon Blasters attack damage bonus: +4 vs Light -> {{nerf}}+3 vs Light{{/nerf}}
- {{new}}Adjusted Dual Photon Blasters attack damage bonus: +3 vs Light -> {{buff}}+3 vs Light and Shields{{/buff}}{{/new}}
- Increased Dual Photon Blasters attack period: 1.12 -> {{nerf}}1.25{{/nerf}} [1.5625 -> {{nerf}}1.75{{/nerf}}]
{{/unit}}

The reduction in attack period reduces the effectiveness of the Scout against Light ground units slightly, allowing Marines and Hydralisks to fight better against them. The base damage of the Scout has been increased slightly to maintain its performance against non-Light targets, and an anti-Shield bonus equal in magnitude to the existing anti-Light bonus has been added to open up Brood War Protoss' options against StarCraft II Protoss beyond Robotics Support Bay and Citadel of Adun technology.

***
{{unit "carrier"}}
- Increased Interceptor launch period: 0.27 -> {{nerf}}0.33{{/nerf}} [0.375 -> {{nerf}}0.4665{{/nerf}}]
{{/unit}}

This change reverts the Interceptor's launch period to its Core value.

This does not affect the behavior of already-launched Interceptors, so players can still utilize Carriers to their maximum combat potential by pre-launching Interceptors before a fight and issuing move commands to them so the Interceptors do not retreat. (Brood War Interceptors cannot re-enter their parent Carriers if they are moving.)

***
{{unit "arbiter"}}
- Decreased build cost: 100/350 -> {{buff}}100/300{{/buff}}
- {{nerf}}Added Massive Attribute{{/nerf}}
- Decreased Recall Energy cost: 125 -> {{buff}}100{{/buff}}
{{/unit}}

We felt that the Arbiter's power does not reflect the tremendous investment required to produce it, so we have reduced its Vespene gas cost and made Recall cheaper to cast.

At the same time, the Massive tag has been added to give the Arbiter some additional counters.

***
## Bug Fixes and Other Changes
***
- Fixed an issue where Lurker's weapon damage zones would miss targets at the end of its range.
