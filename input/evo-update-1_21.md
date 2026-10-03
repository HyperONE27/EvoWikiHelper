---
title: "1.21 Patch Notes"
short_title: "1.21"
author: "HyperONE"
date: "2026-10-04"
blog-image: "/assets/img/blog/blog-update-1_21.webp"
tags: "Update, Extension, New Model, Balance"
---

# SC: Evo Complete Extension Update 1.21
***

Hello, everyone,

Patch 1.21 contains incremental balance adjustments across all three Brood War races. It is also the last major balance update I will be involved in for the foreseeable future.

If you haven't seen the announcement on Discord: I'm stepping away indefinitely from SC: Evo Complete development for personal reasons. I'd like to come back at some point, but I don't know when. In the meantime, multiplayer balance will stay locked until my return or until someone else can be found to take up the reins, and I won't be updating the wiki, organizing or funding tournaments, making maps, or writing blog posts like this one. Everything else, including art, Core, and Campaign, carries on without me.

I'm grateful to everyone who tested patches, argued with my reasoning, and showed up to events over these last couple of years. That includes the people who disagreed with me, because a lot of what's in these notes is better for someone pushing back. Writing these has been some of the work I'm proudest of, and I'm sorry to be putting it down for now.

This isn't a clean exit, though. SC: Evo Complete's ladder is moving to Vespene.gg (details in the section below), and its gameplay data will show me how these changes play out. I'll keep tabs on it and release a minor update later to address any issues that come up. After that, I'll step back for real until I can return.

***
### Thank You For Your Support!
***

{{donations}}

{{toc}}

***
### Vespene Ladder
***

We're excited to announce that the SC: Evo Complete Ranked Ladder is re-launching in collaboration with [Vespene.gg](https://vespene.gg), and **Season 1** is about to begin.

[Pending images]

Vespene.gg and its companion desktop app achieve much of what we were aiming for with the Evo Arcade Ladder and the Evo Discord Bot Ladder, with big improvements to matchmaking, map bans, and match reporting, plus several quality-of-life features, all in one much easier package.

**How to play:** Head to [Vespene.gg](https://vespene.gg), download the companion app, and link your Battle.net account. Pick your race and the servers you want to play on, and the app will find you a valid opponent. Once you're matched, each player bans a map from the pool and the app walks you through hosting and joining. The one thing the app can't do is create the lobby, so you'll still host that yourself. After the game, the app uploads the replay, reports the result, and gives you a summary of how the match went and where you can improve, including a build order review.

**Prize pool:** Season 1 has a prize pool that anyone can contribute to, and the development team will be adding funds throughout the season. At the end of the season, it will be split among the top 10 players, with additional prizes for the top Diamond/Platinum ranked players and the most active player overall.

{{countdown date="2026-12-31T00:00:00" label="Season 1 ends in"}}

***
### New Models
***

Art work has been slower than we'd like leading up to this release, but two long-awaited models are ready, with more in the pipeline.

{{player animate="true"}}
| title    | src                                   | description |
|----------|---------------------------------------|-------------|
| fleetbeacon | /assets/video/1_21_FleetBeacon.webm    | After a long wait, we've finished the Fleet Beacon model, created by AltJunior and sponsored by AcresDeCruz. The crystal ball materials were an interesting challenge, but we managed a faithful recreation of the original. |
| queen       | /assets/video/1_21_Queen.webm    | Ever since our last texture update to the Queen, we have wanted to complete its model remake by adding the missing skirt piece. Thanks to DaveSpectre, we've finally done it. |
{{/player}}


***
### A Brief Note
***

Please note that all speed- and time-related values are given as **Faster Speed [Normal Speed]**.

***
## Terran Changes
***

{{unit "scv"}}
- Increased attack period: 1.1 -> {{nerf}}1.14{{/nerf}} [1.54 -> {{nerf}}1.6{{/nerf}}]
- Decreased attack range: 0.1562 -> {{nerf}}0.1{{/nerf}}
{{/unit}}

These changes further discourage the use of SCVs in proxy Barracks and all-in strategies. Not only will SCVs attack more slowly, mitigating their HP advantage, but their first-attack advantage against Zerglings and enemy SC2 workers has been eliminated by reducing their attack range.

***
{{unit "marine"}}
- Decreased Stimpack attack speed bonus: 75% -> {{nerf}}72%{{/nerf}}
  - Increased attack period with Stimpack active: 0.38 -> {{nerf}}0.39{{/nerf}} [0.5357 -> {{nerf}}0.5451{{/nerf}}]
{{/unit}}

This is a marginal change to give SC2 Zerg, and to a lesser extent, SC2 Terran Bio and SC2 Protoss Warp Gate armies, slightly more leeway against BW Terran Bio forces.

***
{{unit "vulture"}}
- {{adjust}}Now decelerates when approaching a target{{/adjust}}
- Increased attack damage point: 0 -> {{adjust}}0.0875{{/adjust}} [0 -> {{adjust}}0.0625{{/adjust}}]
- Increased attack Backswing: 0 -> {{adjust}}1.225{{/adjust}} [0 -> {{adjust}}0.875{{/adjust}}]
- Decreased movement acceleration: 12.95 -> {{nerf}}8.75{{/nerf}} [9.25 -> {{nerf}}6.25{{/nerf}}]
- Decreased movement deceleration: 21 -> {{nerf}}4.2{{/nerf}} [15 -> {{nerf}}3{{/nerf}}]
- Decreased movement turning rate: 2800 -> {{nerf}}1008{{/nerf}} [2000 -> {{nerf}}720{{/nerf}}]
- Decreased stationary turning rate: 2800 -> {{nerf}}2100{{/nerf}} [2000 -> {{nerf}}1500{{/nerf}}]
- Vultures {{adjust}}no longer hesitate when the mine placement position is occupied{{/adjust}}; they will instead place a mine directly underneath themselves
{{/unit}}

Vulture moving shots have been reworked. Previously, the Vulture temporarily switched to a strafing weapon, similar to the Interceptor's strafing attack, while attacking in order to preserve its movement speed. However, the random strafing positions could cause the Vulture to move erratically. This has now been replaced with a trigger-based solution using the new "Moving Shot" behavior.

{{clip src="/assets/video/1_21_VultureShot.webm"}}

This allows the Vulture to properly retain its momentum while attacking, while also providing more natural acceleration and deceleration during combat. Skilled players can expect to extract more value out of good kiting control with Vultures.

Special thanks to **Solstice245** for developing this feature.

***
{{unit "valkyrie"}}
- {{adjust}}Valkyries now fire at their target before validating it{{/adjust}} {{badge core}}
{{/unit}}

This replicates the Brood War behavior of Valkyries firing an additional volley after their main target dies.

***
## Zerg Changes
***

{{unit "spawningpool"}}
- Decreased build time: 53.6 -> {{buff}}50{{/buff}} [75 -> {{buff}}70{{/buff}}]
{{/unit}}

{{unit "zergling"}}
- Increased Metabolic Boost research time: 71.4 -> {{nerf}}75{{/nerf}} [100 -> {{nerf}}105{{/nerf}}]
{{/unit}}

{{unit "hydraliskden"}}
- Increased build time: 25 -> {{nerf}}28.6{{/nerf}} [35 -> {{nerf}}40{{/nerf}}]
{{/unit}}

The build time of the Spawning Pool has been sped up, and an equal amount of time was added to the Metabolic Boost research and Hydralisk Den build times. This slightly improves the early availability of Zerglings for offense and defense without affecting Metabolic Boost and Hydralisk timings.

***
{{unit "hydralisk"}}
- Decreased attack period: 0.72 -> {{buff}}0.71{{/buff}} [1.0078 -> {{buff}}1{{/buff}}]
{{/unit}}

{{unit "lurker"}}
- Decreased morph time: 15 -> {{buff}}12.14{{/buff}} [21 -> {{buff}}17{{/buff}}]
- Adjusted attack damage: 25 -> {{adjust}}20 (+5 vs Light){{/adjust}}
- Burrowed Lurkers now {{adjust}}ignore collision{{/adjust}}
{{/unit}}

{{clip src="/assets/video/1_21_LurkerStacking.webm"}}

We previously felt that the overall well-roundedness of Lurkers against all enemy types has had certain negative consequences for the metagame, such as discouraging SC2 Terran mech play and overly enabling Lurker busts. Reverting their damage against non-Light targets helps address this, but requires compensation elsewhere.

One such form of compensation: Lurkers are now capable of Burrow stacking, allowing several Lurkers to better coordinate their attack volleys. This is especially important against weaker enemies, such as Marines. As part of our goal to implement more Brood War-style mechanics in SC: Evo Complete, we had been looking for an opportunity to introduce Burrow stacking, and now seems like a good time. Combined with a slightly faster morph time, we expect that BW Zerg will have an easier time defending against SC2 Terran aggression.

To somewhat fill in the gap in general combat power now vacated by the Lurker, we are also giving a slight attack period buff to the Hydralisk.

***
{{unit "mutalisk"}}
- Increased attack damage: 9 -> {{buff}}10{{/buff}}
{{/unit}}

When we gave the Mutalisk its current attack range of 5, we lowered its damage to 9 so it wouldn't be too strong. Since then, opponents seem to have figured out how to answer 5 range and stacking, and Mutalisk harassment no longer threatens enough to control the pacing of the early-mid game. We are increasing its attack damage back to 10 to restore some of that pressure.

***
{{unit "queen"}}
- Parasite {{buff}}can now target Frenzied units{{/buff}}
- Spawn Broodling {{buff}}can now target Frenzied units{{/buff}}
{{/unit}}

We previously stopped Parasite and Spawn Broodling from targeting Frenzied units to tone down the Queen in the late game against SC2 Zerg, since we felt BW Zerg players too often entered this phase with a runaway lead. Since then, the Hydralisk's attack period has become considerably slower, and this patch reduces Lurker damage against non-Light units such as Roaches, Ravagers, and SC2 Lurkers. As such, the early and mid-game leads feeding BW Zerg's late-game advantage have been reduced, and, especially, BW Hydralisk-Lurker armies will struggle to deal with SC2 Lurkers efficiently, even before Seismic Spines. Therefore, we are once again allowing Parasite and Spawn Broodling to target Frenzied units, so Queens can serve as a broad solution to late-game threats, such as the Lurker and the Ultralisk.

***
## Protoss Changes
***

{{unit "scout"}}
- Now {{buff}}has a stacking mode{{/buff}}
  - Stacking is {{adjust}}toggled on/off with a manual ability{{/adjust}}
    - Stacking mode is ON by default
    - Separation radius while in stacking mode: 0.75 -> {{buff}}0.1{{/buff}}
{{/unit}}

Ever since adding stacking mechanics to the Wraith and the Mutalisk, we have received many requests to add this to other air units. However, due to game performance limitations, it is not feasible for us to add this mechanic to all air units.

Since we think that the best candidates for the mechanic are fast air-to-ground units, we are adding it to the Scout.

***
{{unit "corsair"}}
- Decreased attack period: 0.36 -> {{buff}}0.33{{/buff}} [0.5 -> {{buff}}0.4687{{/buff}}]
{{/unit}}

Although we have been hesitant to buff the Corsair's combat performance due to concerns about scaling in large numbers, it seems clear that even the drastic mobility bonuses given to the unit in previous patches do not fully close the gap against certain enemies, such as SC2 Zerg Mutalisks. Therefore, we are simply reducing the Corsair's attack period to allow it to better hold its ground. At this time, we do not think a compensatory nerf elsewhere is necessary.