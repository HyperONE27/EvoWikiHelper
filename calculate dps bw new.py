from enum import IntEnum
from dataclasses import dataclass
from typing import List, Tuple, Union
import math


class DamageType(IntEnum):
    """Enum for damage types in the game."""
    CONCUSSIVE = 0
    EXPLOSIVE = 1
    NORMAL = 2


class TargetType(IntEnum):
    """Enum for target types."""
    BASE = 0
    LIGHT = 1
    ARMORED = 2
    SHIELDS = 3


class DisplayMode(IntEnum):
    """Enum for display modes."""
    BASIC = 0
    WIKI = 1


@dataclass
class DamageData:
    """Container for damage calculations."""
    damage: float = 0.0
    damage_per_upgrade: float = 0.0
    dps: float = 0.0
    dps_per_upgrade: float = 0.0


class DPSCalculator:
    """Calculator for DPS in Starcraft: Brood War."""
    
    # Damage multipliers for each damage type against each target type
    DAMAGE_MULTIPLIERS = {
        DamageType.CONCUSSIVE: {
            TargetType.BASE: 1.0,
            TargetType.LIGHT: 1.0,
            TargetType.ARMORED: -0.5,
            TargetType.SHIELDS: 0.5
        },
        DamageType.EXPLOSIVE: {
            TargetType.BASE: 1.0,
            TargetType.LIGHT: -1/6,
            TargetType.ARMORED: 1/3,
            TargetType.SHIELDS: 0.0
        },
        DamageType.NORMAL: {
            TargetType.BASE: 1.0,
            TargetType.LIGHT: 0.0,
            TargetType.ARMORED: 0.0,
            TargetType.SHIELDS: 0.0
        }
    }
    
    def __init__(self, unit_name: str, base_damage: float, upgrade_damage: float, cooldown: float, damage_type: DamageType, attacks: int = 1):
        """
        Initialize DPS calculator.
        
        Args:
            unit_name: Name of the unit
            base_damage: Damage per hit vs. tagless unit
            upgrade_damage: Increase in damage per hit per upgrade level
            cooldown: Attack period in seconds (on Faster speed)
            damage_type: Type of damage (concussive, explosive, or normal)
            attacks: Number of attacks
        """
        self.unit_name = unit_name
        self.base_damage = base_damage
        self.upgrade_damage = upgrade_damage
        self.cooldown = cooldown
        self.damage_type = damage_type
        self.attacks = attacks
        self.damage_data = self._calculate_damage()
    
    def _calculate_damage(self) -> List[DamageData]:
        """Calculate damage and DPS for all target types."""
        damage_data = []
        multipliers = self.DAMAGE_MULTIPLIERS[self.damage_type]
        
        for target_type in TargetType:
            multiplier = multipliers[target_type]
            
            damage = self.base_damage * multiplier * self.attacks
            damage_per_upgrade = self.upgrade_damage * multiplier * self.attacks
            dps = damage / self.cooldown
            dps_per_upgrade = damage_per_upgrade / self.cooldown
            
            damage_data.append(DamageData(
                damage=damage,
                damage_per_upgrade=damage_per_upgrade,
                dps=dps,
                dps_per_upgrade=dps_per_upgrade
            ))
        
        return damage_data
    
    @staticmethod
    def _round_away_from_zero(value: float, decimals: int) -> float:
        """Round a value away from zero when the last digit is 5."""
        factor = 10 ** decimals
        if value >= 0:
            return math.floor(value * factor + 0.5) / factor
        else:
            return math.ceil(value * factor - 0.5) / factor
    
    @staticmethod
    def _format_damage_value(value: float) -> str:
        """
        Format damage values (exact values).
        
        - Values under +/-0.01 display as "0"
        - Maximum 2 decimal places
        - Round away from zero when last digit is 5
        - Remove unnecessary trailing zeros and decimal points
        """
        if abs(value) < 0.01:
            return "0"
        
        # Round to 2 decimal places, away from zero when ending in 5
        rounded = DPSCalculator._round_away_from_zero(value, 2)
        
        # Check if it's effectively an integer after rounding
        if abs(rounded - round(rounded)) < 1e-9:
            return str(int(round(rounded)))
        
        # Format with up to 2 decimal places, removing trailing zeros
        if abs(rounded * 10 - round(rounded * 10)) < 1e-9:
            # Has only 1 decimal place
            return f"{rounded:.1f}"
        else:
            # Has 2 decimal places
            return f"{rounded:.2f}"
    
    @staticmethod
    def _format_dps_value(value: float) -> str:
        """
        Format DPS values (inexact values).
        
        - Values under +/-0.01 display as "0"
        - Maximum 2 decimal places
        - Round away from zero when last digit is 5
        - Keep trailing zeros unless the result is clean with 1 decimal
        """
        if abs(value) < 0.01:
            return "0"
        
        # Round to 2 decimal places, away from zero when ending in 5
        rounded = DPSCalculator._round_away_from_zero(value, 2)
        
        # Check if it's effectively an integer after rounding
        if abs(rounded - round(rounded)) < 1e-9:
            return str(int(round(rounded)))
        
        # Check if it has only 1 significant decimal place
        if abs(rounded * 10 - round(rounded * 10)) < 1e-9:
            return f"{rounded:.1f}"
        
        # Otherwise, show 2 decimal places
        return f"{rounded:.2f}"
    
    @staticmethod
    def _format_value_with_sign(value: Union[int, float, str]) -> str:
        """Add sign prefix for positive numbers."""
        if isinstance(value, str):
            # Already formatted
            if value.startswith('-'):
                return value
            elif value == "0":
                return "+0"
            else:
                return f"+{value}"
        else:
            # Numeric value
            if value > 0:
                return f"+{value}"
            elif value == 0:
                return "+0"
            else:
                return str(value)
    
    def _format_damage_string(self, base_value: float, upgrade_value: float, 
                            show_attacks: bool = True) -> str:
        """Format damage string with base and upgrade values."""
        base_str = self._format_damage_value(base_value)
        upgrade_str = self._format_damage_value(upgrade_value)
        damage_str = f"{base_str} ({self._format_value_with_sign(upgrade_str)})"
        
        if show_attacks and self.attacks > 1:
            damage_str += f" (x{self.attacks})"
        return damage_str
    
    def display_basic(self) -> None:
        """Display unit stats in basic format."""
        base_data = self.damage_data[TargetType.BASE]
        
        print(f"Unit name: {self.unit_name}")
        print(f"Unit damage: {self._format_damage_string(self.base_damage, self.upgrade_damage)}")
        
        base_dps_str = self._format_dps_value(base_data.dps)
        base_dps_upgrade_str = self._format_dps_value(base_data.dps_per_upgrade)
        print(f"Unit DPS: {base_dps_str} ({self._format_value_with_sign(base_dps_upgrade_str)})")
        print(f"Unit cooldown: {self.cooldown}")
        
        if self.damage_type != DamageType.NORMAL:
            self._display_bonus_stats()
        print()
    
    def _display_bonus_stats(self) -> None:
        """Display bonus damage stats for non-normal damage types."""
        light_data = self.damage_data[TargetType.LIGHT]
        armor_data = self.damage_data[TargetType.ARMORED]
        shield_data = self.damage_data[TargetType.SHIELDS]
        
        # Format damage values
        light_dmg = self._format_damage_value(light_data.damage)
        light_upg = self._format_damage_value(light_data.damage_per_upgrade)
        armor_dmg = self._format_damage_value(armor_data.damage)
        armor_upg = self._format_damage_value(armor_data.damage_per_upgrade)
        shield_dmg = self._format_damage_value(shield_data.damage)
        shield_upg = self._format_damage_value(shield_data.damage_per_upgrade)
        
        # Format DPS values
        light_dps = self._format_dps_value(light_data.dps)
        light_dps_upg = self._format_dps_value(light_data.dps_per_upgrade)
        armor_dps = self._format_dps_value(armor_data.dps)
        armor_dps_upg = self._format_dps_value(armor_data.dps_per_upgrade)
        shield_dps = self._format_dps_value(shield_data.dps)
        shield_dps_upg = self._format_dps_value(shield_data.dps_per_upgrade)
        
        bonus_damage = (
            f"{self._format_value_with_sign(light_dmg)} "
            f"({self._format_value_with_sign(light_upg)}) vs Light | "
            f"{self._format_value_with_sign(armor_dmg)} "
            f"({self._format_value_with_sign(armor_upg)}) vs Armored | "
            f"{self._format_value_with_sign(shield_dmg)} "
            f"({self._format_value_with_sign(shield_upg)}) vs Shields"
        )
        
        bonus_dps = (
            f"{self._format_value_with_sign(light_dps)} "
            f"({self._format_value_with_sign(light_dps_upg)}) vs Light | "
            f"{self._format_value_with_sign(armor_dps)} "
            f"({self._format_value_with_sign(armor_dps_upg)}) vs Armored | "
            f"{self._format_value_with_sign(shield_dps)} "
            f"({self._format_value_with_sign(shield_dps_upg)}) vs Shields"
        )
        
        print(f"Unit bonus: {bonus_damage}")
        print(f"Unit bonus DPS: {bonus_dps}")
    
    def display_wiki(self) -> None:
        """Display unit stats in wiki format."""
        base_data = self.damage_data[TargetType.BASE]
        
        print(f"Unit name: {self.unit_name}")
        
        # Format damage line
        damage_line = f"|attack1_damage={self._format_damage_string(self.base_damage, self.upgrade_damage, show_attacks=(self.attacks > 1))}"
        print(damage_line)
        
        base_dps_str = self._format_dps_value(base_data.dps)
        base_dps_upgrade_str = self._format_dps_value(base_data.dps_per_upgrade)
        print(f"|attack1_dps={base_dps_str} ({self._format_value_with_sign(base_dps_upgrade_str)})")
        print(f"|attack1_cooldown={self.cooldown}")
        
        if self.damage_type != DamageType.NORMAL:
            self._display_wiki_bonus_stats()
        print()
    
    def _display_wiki_bonus_stats(self) -> None:
        """Display bonus stats in wiki format."""
        light_data = self.damage_data[TargetType.LIGHT]
        armor_data = self.damage_data[TargetType.ARMORED]
        shield_data = self.damage_data[TargetType.SHIELDS]
        
        # Format damage values
        light_dmg = self._format_damage_value(light_data.damage)
        light_upg = self._format_damage_value(light_data.damage_per_upgrade)
        armor_dmg = self._format_damage_value(armor_data.damage)
        armor_upg = self._format_damage_value(armor_data.damage_per_upgrade)
        shield_dmg = self._format_damage_value(shield_data.damage)
        shield_upg = self._format_damage_value(shield_data.damage_per_upgrade)
        
        # Format DPS values
        light_dps = self._format_dps_value(light_data.dps)
        light_dps_upg = self._format_dps_value(light_data.dps_per_upgrade)
        armor_dps = self._format_dps_value(armor_data.dps)
        armor_dps_upg = self._format_dps_value(armor_data.dps_per_upgrade)
        shield_dps = self._format_dps_value(shield_data.dps)
        shield_dps_upg = self._format_dps_value(shield_data.dps_per_upgrade)
        
        bonus_damage = (
            f"{self._format_value_with_sign(light_dmg)} "
            f"({self._format_value_with_sign(light_upg)}) "
            f"vs [[User:SCEvo/Attributes#Light|Light]]<br>"
            f"{self._format_value_with_sign(armor_dmg)} "
            f"({self._format_value_with_sign(armor_upg)}) "
            f"vs [[User:SCEvo/Attributes#Armored|Armored]]<br>"
            f"{self._format_value_with_sign(shield_dmg)} "
            f"({self._format_value_with_sign(shield_upg)}) "
            f"vs [[User:SCEvo/Attributes#Shields|Shields]]"
        )
        
        bonus_dps = (
            f"{self._format_value_with_sign(light_dps)} "
            f"({self._format_value_with_sign(light_dps_upg)}) "
            f"vs [[User:SCEvo/Attributes#Light|Light]]<br>"
            f"{self._format_value_with_sign(armor_dps)} "
            f"({self._format_value_with_sign(armor_dps_upg)}) "
            f"vs [[User:SCEvo/Attributes#Armored|Armored]]<br>"
            f"{self._format_value_with_sign(shield_dps)} "
            f"({self._format_value_with_sign(shield_dps_upg)}) "
            f"vs [[User:SCEvo/Attributes#Shields|Shields]]"
        )
        
        print(f"|attack1_bonus={bonus_damage}")
        print(f"|attack1_bonus_dps={bonus_dps}")
    
    def display(self, mode: DisplayMode = DisplayMode.WIKI) -> None:
        """Display unit stats in the specified format."""
        if mode == DisplayMode.BASIC: 
            self.display_basic()
        else:
            self.display_wiki()


def calculate_dps_bw(unit_name: str, base: float, upgrade: float, cooldown: float, dmg_type: int, attacks: int, display_mode: int = 1) -> None:
    """
    Legacy function for backward compatibility.
    
    Args:
        unit_name: Name of the unit
        base: Damage per hit vs. tagless unit
        upgrade: Increase in damage per hit per upgrade level
        cooldown: Attack period (on Faster), in seconds
        dmg_type: 0 for concussive, 1 for explosive, 2 for normal
        attacks: Number of attacks
        display_mode: 0 for basic, 1 for detailed
    """
    calculator = DPSCalculator(
        unit_name=unit_name,
        base_damage=base,
        upgrade_damage=upgrade,
        cooldown=cooldown,
        damage_type=DamageType(dmg_type),
        attacks=attacks
    )
    calculator.display(DisplayMode(display_mode))


def main():
    """Run DPS calculations for various units."""
    units = [
        ("Marine", 6, 1, 0.67, 2, 1),
        ("MarineBonus", 6, 1, 0.67 / 1.75, 2, 1),
        ("Wraith", 15, 1.5, 0.94, 1, 1),
        ("Valkyrie", 4.5, 0.75, 2.54, 1, 8),
        ("Battlecruiser", 34, 3, 1.25, 2, 1),
        ("Hydralisk", 7.5, 0.75, 0.67, 1, 1),
        ("Scout", 7, 1, 1.12, 2, 2),
        ("ScoutBonus", 2, 0, 1.12, 2, 2),
        ("Vulture", 10, 1, 1.32, 0, 1)
    ]
    
    for unit_params in units:
        calculator = DPSCalculator(*unit_params)
        calculator.display(DisplayMode.WIKI)


if __name__ == "__main__":
    main()

# Patch 1.18 and 1.18.1
# Come back to: Vulture, Valkyrie, Hydralisk, Mutalisk, Scout