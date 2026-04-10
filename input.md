Version: Patch 1.18.2

Link: https://scevo.net/posts/evo-update-1_18_2.html

Date: 2026-04-09

Contents to turn to A + B:

***
## Terran Changes
***

{{unit "wraith"}}
- Increased anti-ground attack damage: 14 -> {{buff}}15{{/buff}}
- Decreased separation radius while moving: 0.5 -> {{buff}}0.1{{/buff}}
{{/unit}}

The Wraith currently serves a central role in the early-game against StarCraft II Terran and is largely unseen against the other two StarCraft II factions. Due to the absence of Reactors for Brood War Terran production, as well as the relative lack of unit variety producible without the Academy, Machine Shop, and Control Tower, Cloak Wraiths are critical for securing air and map control against StarCraft II Terran, giving Brood War Terran the necessary safety to freely choose their mid-game tech.

We think that there is room in all matchups to see more Wraith play. As such, we are buffing the Wraith's damage output slightly and giving it the same stacking mechanic that the Mutalisk received in Patch 1.18.1. The damage increase breaks several notable thresholds: SCVs and Combat Shields Marines that have activated Stimpack now die in 3 attacks instead of 4, and Cyclones fall in 9 attacks instead of 10 — enough for three Wraiths to kill a Cyclone in 3 volleys instead of 4. These buffs not only augment the performance of the Wraith in Factory-expand 1-1-1 openers against StarCraft II Terran, but also improve the viability of multi-Starport Wraith openers in all matchups and, by extension, create room for broader Sky Terran strategies.

Due to technical and performance limitations, the Wraith is likely to be the last unit that will receive dynamic separation radius.

***
## Zerg Changes
***

{{unit "zergling"}}
- Decreased Unburrow period: 0.71 -> {{buff}}0.36{{/buff}} [1 -> {{buff}}0.5{{/buff}}]
- Decreased Unburrow random delay: 0.36 -> {{buff}}0.08{{/buff}} [0.5 -> {{buff}}0.1125{{/buff}}]
{{/unit}}

{{unit "hydralisk"}}
- Decreased Unburrow period: 0.71 -> {{buff}}0.36{{/buff}} [1 -> {{buff}}0.5{{/buff}}]
- Decreased Unburrow random delay: 0.36 -> {{buff}}0.08{{/buff}} [0.5 -> {{buff}}0.1125{{/buff}}]
{{/unit}}

This set of changes matches these values with those of the StarCraft II Zergling and Hydralisk.

***
{{unit "guardian"}}
- Increased attack damage increase per upgrade: +2 -> {{buff}}+3{{/buff}}
{{/unit}}

{{unit "devourer"}}
- Decreased attack period: 3.11 -> {{buff}}2.54{{/buff}} [4.35 -> {{buff}}3.5625{{/buff}}]
{{/unit}}

In Patch 1.18.1, we reduced the damage dealt by each of the Guardian's attacks. Our justification was that due to Guardians now outranging the StarCraft II Ghost's Steady Targeting ability and being on par with the Thor's 250mm Punisher Cannons, we expect them to be quite a disruptive unit. We also think — while we do not expect players to directly target Ghosts with Guardians — that Guardians might incidentally hit Ghosts quite often, more so than players expect. Nevertheless, we do not think fully upgraded Guardians need to be weak in their anti-ground role, so we are reverting the decrease in damage increase per upgrade.

We also think that the Devourer could use further buffs. Although the Devourer was originally designed as a support unit and should remain one, the Devourer simply cannot justify its cost against the StarCraft II races given its current combat performance and complete lack of utility aside from its anti-air role — even the StarCraft II Corruptor can use Caustic Spray on structures. We think that we can both improve its direct cost-efficiency and augment its support-debuffer capabilities with an additional decrease in attack period.

***
## Protoss Changes
***

{{unit "darkarchon"}}
- Decreased Feedback cast range: 10.5 -> {{nerf}}10{{/nerf}}
{{/unit}}

This change was previously intended to enable the Dark Archon to win duels against the StarCraft II Ghost and High Templar. However, considering the Carrier adjustments this patch, we think that giving enemy spellcasters — especially counter-spellcasters such as the Ghost and High Templar — more room to operate around the Dark Archon would be prudent.

***
{{unit "shuttle"}}
- Increased build cost: 175/0 -> {{nerf}}200/0{{/nerf}}
- Decreased Plasma Shields: 80 -> {{nerf}}70{{/nerf}}
{{/unit}}

{{unit "reaver"}}
- Decreased armor: 1 -> {{nerf}}0{{/nerf}}
- Decreased movement speed: 1.50 -> {{nerf}}1.4{{/nerf}} [1.0703 -> {{nerf}}1{{/nerf}}]
- Decreased attack period: 2.68 -> {{buff}}2.5{{/buff}} [3.75 -> {{buff}}3.5{{/buff}}]
- Increased attack range: 8 -> {{buff}}9{{/buff}}
{{/unit}}

The Reaver was one of the few Brood War units short-changed in attack range in SC: Evo Complete. Since units in StarCraft II generally have much longer range on average than Brood War units do, implementing the Reaver with its Core range of 8 made it feel less advantaged in terms of range than it did in Brood War.

We are following up on changes to the Reaver in Patch 1.18 to improve its combat consistency with additional changes. These reset the Reaver to its Core value for armor and decrease its movement speed incrementally towards Core. In exchange, the Reaver is receiving additional attack range and fires Scarabs more frequently. To compensate both these changes and the implications of faster Reaver and Scarab production speed introduced in Patch 1.18, we are reverting the Shuttle to its Core build cost and reducing its Plasma Shields points slightly.

***
{{unit "scout"}}
- Increased Dual Photon Blasters attack period: 0.89 -> {{nerf}}0.94{{/nerf}} [1.25 -> {{nerf}}1.3125{{/nerf}}]
{{/unit}}

In Patch 1.18, we buffed the Scout's Dual Photon Blasters attack period as part of a rework of the unit. This was born from a concern that a decreased HP pool might lead to the Scout being too weak in air-to-air combat, something in which the original Scout was quite strong. However, based on recent testing and gameplay, we think that not only is the current Scout's combat performance fine, but actually that it is a bit overtuned. This nerf reverts the attack period to its Core value.

***
{{unit "carrier"}}
- Interceptor weapon is {{buff}}now hitscan{{/buff}}
- Increased Interceptor attack period: 1.21 -> {{nerf}}1.58{{/nerf}} [1.6875 -> {{nerf}}2.2165{{/nerf}}]
- Increased Interceptor Plasma Shields regen rate when inside a Carrier: 42 -> {{buff}}∞{{/buff}} [30 -> {{buff}}∞{{/buff}}]
{{/unit}}

We are reverting the Interceptor's weapon behavior to hitscan. While a projectile-based weapon more closely aligns with its Brood War behavior, this change made the Carrier wildly inconsistent in combat. This was not merely due to the potential for overkill; the targeting behavior of Interceptors and fast attack period relative to other units with projectile-based weapons made it impossible to perform micro techniques, such as concaving, that would otherwise be used to mitigate it. Moreover, its performance against small targets, such as Zerglings, was downright abysmal.

Restoring the hitscan behavior while aligning the attack period to that of the Core value seems to be the appropriate move here. Relative to the StarCraft II Carrier, the Brood War Carrier now has a lower base damage output, but is slightly less affected by enemy armor, retains more base armor of its own, and possesses Interceptors which retreat on their own when low on vitals, rapidly regenerate, and return to combat. For now, we think that this is a healthy state for the new Carrier.

Notably, Carriers are now much stronger against smaller units, such as Zerglings, Marines, and even Vikings. However, they are much less effective against units they were not overkilling, such as Thors, Ultralisks, Corruptors, and Tempests. Overall, we think this is fine, as the Carrier being stronger across the board but also possessing more defined counters is a preferable design state.

***
## Bug Fixes and Other Changes
***
- Acid Spores visuals now scale in size based on the stack count of Acid Spores.
- Consume can now target player-owned Changelings.
- StarCraft II Queens can now target allied Brood War Hatcheries, Lairs, and Hives with the Spawn Larvae ability.
- StarCraft II Pylons now activate their Warp Conduit passive when near an allied Brood War Nexus.
- Fixed an issue where Chrono Boost could not be activated on player-owned Brood War structures.