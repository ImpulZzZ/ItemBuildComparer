class Item:
    def __init__(self):
        self.unique = 0
        self.ability_power = 0
        self.cooldown_reduction = 0
        self.mana = 0
        self.armor = 45
        self.hp = 0
        self.movement_speed = 0
        self.soft_cc = 0
        self.flat_magic_penetration = 0
        self.attack_speed = 0.0
        self.magic_penetration = 0
        self.flat_movement_speed = 0

class Rabadons_Deathcap(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 120

    def unique_passive(ap):
        ability_power_boost = 0.40 * ap
        return ability_power_boost

class Voidstaff(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 70
        self.unique_percentual_magic_penetration = 0.4
        self.unique = 1

class Seraphs_Embrace(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 50
        self.cooldown_reduction = 0.1
        self.mana = 1400
        self.unique_passive_cooldown_reduction = 0.1
        self.unique = 1

    def unique_passive(mana):
        ability_power_boost = 0.03 * mana
        return ability_power_boost

class Zhonyas_Hourglass(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 75
        self.armor = 45
        self.cooldown_reduction = 0.1

class Twin_Shadows(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 70
        self.cooldown_reduction = 0.1
        self.movement_speed = 0.07
        self.soft_cc = 1

class Rod_of_Ages(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 60
        self.hp = 300
        self.mana = 300

class Rod_of_Ages_full_stacked(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 100
        self.cooldown_reduction = 500
        self.movement_speed = 400

class Rylais_Crystal_Scepter(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 90
        self.hp = 300
        self.soft_cc = 1

class Sorcerers_Shoes(Item):
    def __init__(self):
        super().__init__()
        self.magic_penetration = 18
        self.flat_movement_speed = 45

class Spellbinder(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 120
        self.movement_speed = 0.10

class Spellbinder_full_stacked(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 200
        self.movement_speed = 0.60
        self.unique = 1

class Nashors_Tooth(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 80
        self.attack_speed = 0.50
        self.unique_cooldown_reduction = 0.20
        self.unique = 1

    def unique_passive_damage_per_hit(ap):
        damage = (0.15 * ap) + 15
        return damage


class Morellonomicon(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 70
        self.hp = 300
        self.unique_flat_magic_penetration = 15
        self.unique = 1

class Liandrys_Torment(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 75
        self.hp = 300
        self.unique = 1

    def unique_passive_damage_of_enemy_max_hp_as_magic_damage(enemy_hp):
        damage = 0.045 * enemy_hp
        return damage

class Liandrys_Torment_against_cced_enemy(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 75
        self.hp = 300
        self.unique = 1

    def unique_passive_damage_of_enemy_max_hp_as_magic_damage(enemy_hp):
        damage = 0.075 * enemy_hp
        return damage

class Liandrys_Torment_fully_stacked(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 75
        self.hp = 300
        self.unique_damage_increase = 0.10
        self.unique = 1

    def unique_passive_damage_of_enemy_max_hp_as_magic_damage(enemy_hp):
        damage = 0.045 * enemy_hp
        return damage

class Liandrys_Torment_fully_stacked_against_cced_enemy(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 75
        self.hp = 300
        self.unique_damage_increase = 0.10
        self.unique = 1

    def unique_passive_damage_of_enemy_max_hp_as_magic_damage(enemy_hp):
        damage = 0.075 * enemy_hp
        return damage


class Lichbane(Item):
    def __init__(self):
        super().__init__()
        self.ability_power = 80
        self.cooldown_reduction = 0.10
        self.movement_speed = 0.07
        self.mana = 250
        self.unique = 1

    def unique_passive_damage_per_autoattack(self, ap, base_ad):
        damage_per_autoattack_base_ad = 0.75 * base_ad
        damage_per_autoattack_ap = 0.50 * ap
        return damage_per_autoattack_base_ad + damage_per_autoattack_ap


class Ludens_Echo(Item):

    def __init__(self):
        super().__init__()
        self.ability_power = 90
        self.cooldown_reduction = 0.10
        self.mana = 600
        self.unique = 1

    def unique_passive_one_target(self, ap):
        magic_damage_base = 100
        magic_damage_ap_scaling = 0.10
        return magic_damage_base + (magic_damage_ap_scaling * ap)

    def unique_passive_four_targets(self, ap):
        magic_damage_base = 100
        magic_damage_ap_scaling = 0.10
        return (magic_damage_base + (magic_damage_ap_scaling * ap)) * 4

class Hextech_Protobelt_01(Item):

    def __init__(self):
        super().__init__()
        self.ability_power = 60
        self.cooldown_reduction = 0.10
        self.hp = 300
        self.unique = 1

    def unique_passive_damage(self, ap, level):
        return 75 + (4.1667 * level) + (0.25 * ap)

class Hextech_Gunblade(Item):

    def __init__(self):
        super().__init__()
        self.ability_power = 80
        self.attack_damage = 40
        self.unique = 1

    def unique_passive_damage(self, ap, level):
        return 175 + (4.333 * level) + (0.30 * ap)

class Hextech_GLP_800(Item):

    def __init__(self):
        super().__init__()
        self.ability_power = 80
        self.cooldown_reduction = 0.10
        self.mana = 600
        self.unique_cooldown_reduction = 0.10
        self.unique = 1

    def unique_passive_damage(self, ap, level):
        return 100 + (5.5556 * level) + (0.20 * ap)

class Banshees_Veil(Item):

    def __init__(self):
        super().__init__()
        self.ability_power = 75
        self.cooldown_reduction = 0.10
        self.magic_resist = 60
        self.unique = 1

class Archangels_Staff(Item):

    def __init__(self):
        super().__init__()
        self.ability_power = 50
        self.cooldown_reduction = 0.10
        self.mana = 650
        self.unique_cooldown_reduction = 0.10
        self.unique = 1

    def unique_passive(mana):
        ability_power_boost = 0.01 * mana
        return ability_power_boost


