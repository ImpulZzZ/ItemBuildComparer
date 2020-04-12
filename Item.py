class Item:

class Rabadon(Item):
    def __init__(self):
        self.ability_power = 120
        self.ability_power_boost = 0.40
        # todo passive has be implemented in runtime: 40% ap

class Voidstaff(Item):
    def __init__(self):
        self.ability_power = 70
        self.unique_percentual_magic_penetration = 0.4
        self.unique = 1

class Seraphs_Embrace(Item):
    def __init__(self):
        self.ability_power = 50
        self.cooldown_reduction = 0.1
        self.mana = 1400
        self.unique_passive_cooldown_reduction = 0.1
        self.unique = 1
        # todo passive has be implemented in runtime: bonus ap fpr 3% of max mana

class Zhonyas_Hourglass(Item):
    def __init__(self):
        self.ability_power = 75
        self.armor = 45
        self.cooldown_reduction = 0.1

class Twin_Shadows(Item):
    def __init__(self):
        self.ability_power = 70
        self.cooldown_reduction = 0.1
        self.movement_speed = 0.07
        self.soft_cc = 1

class Rod_of_Ages(Item):
    def __init__(self):
        self.ability_power = 60
        self.hp = 300
        self.mana = 300

class Rod_of_Ages_full_stacked(Item):
    def __init__(self):
        self.ability_power = 100
        self.cooldown_reduction = 500
        self.movement_speed = 400

class Rylais_Crystal_Scepter(Item):
    def __init__(self):
        self.ability_power = 90
        self.hp = 300
        self.soft_cc = 1

class Sorcerers_Shoes(Item):
    def __init__(self):
        self.magic_penetration = 18
        self.flat_movement_speed = 45

class Spellbinder(Item):
    def __init__(self):
        self.ability_power = 120
        self.movement_speed = 0.10

class Spellbinder_full_stacked(Item):
    def __init__(self):
        self.ability_power = 200
        self.movement_speed = 0.60
        self.unique = 1

class Nashors_Tooth(Item):
    def __init__(self):
        self.ability_power = 80
        self.attack_speed = 0.50
        self.unique_cooldown_reduction = 0.20
        self.unique = 1
        #todo: self.unique_damage_per_hit = 15 + 15%ap magic damage

class Morellonomicon(Item):
    def __init__(self):
        self.ability_power = 70
        self.hp = 300
        self.unique_flat_magic_penetration = 15
        self.unique = 1

class Liandrys_Torment(Item):
    def __init__(self):
        self.ability_power = 75
        self.hp = 300
        self.unique_damage_of_enemy_max_hp_as_magic_damage = 0.045
        self.unique = 1

class Liandrys_Torment_against_cced_enemy(Item):
    def __init__(self):
        self.ability_power = 75
        self.hp = 300
        self.unique_damage_of_enemy_max_hp_as_magic_damage = 0.075
        self.unique = 1

class Liandrys_Torment_fully_stacked(Item):
    def __init__(self):
        self.ability_power = 75
        self.hp = 300
        self.unique_damage_of_enemy_max_hp_as_magic_damage = 0.045
        self.unique_damage_increase = 0.10
        self.unique = 1

class Liandrys_Torment_fully_stacked_against_cced_enemy(Item):
    def __init__(self):
        self.ability_power = 75
        self.hp = 300
        self.unique_damage_of_enemy_max_hp_as_magic_damage = 0.075
        self.unique_damage_increase = 0.10
        self.unique = 1

class Lichbane(Item):
    def __init__(self):
        self.ability_power = 80
        self.cooldown_reduction = 0.10
        self.movement_speed = 0.07
        self.mana = 250
        self.unique_damage_per_autoattack = 0
        self.unique = 1

    def unique_passive(self, ap, base_ad):
        damage_per_autoattack_base_ad = 0.75 * base_ad
        damage_per_autoattack_ap = 0.50 * ap
        self.unique_damage_per_autoattack = damage_per_autoattack_base_ad + damage_per_autoattack_ap


class Ludens_Echo(Item):

    def __init__(self):
        self.ability_power = 90
        self.cooldown_reduction = 0.10
        self.mana = 600
        self.unique = 1
        self.unique_magic_damage_one_target = 0

    def unique_passive(self, ap):
        magic_damage_base = 100
        magic_damage_ap_scaling = 0.10
        self.unique_magic_damage_one_target = magic_damage_base + (magic_damage_ap_scaling * ap)





