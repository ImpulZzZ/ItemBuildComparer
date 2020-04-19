from Champions.Champion import Champion
import Spell


class Akali(Champion):

    def __init__(self):
        Champion.__init__(self, "Akali")

    def p_one_attack_bonus_damage(self, ap, bonus_ad):
        level_damage = [39, 42, 45, 48, 51, 54, 57, 60, 69, 78, 87, 96, 105, 120, 135, 150, 165, 180]
        ap_scaling = 0.50
        bonus_ad_scaling = 0.60
        amount = level_damage[self.level - 1] + (bonus_ad * bonus_ad_scaling) + (ap * ap_scaling)
        return Spell.Spell(2, amount, 0, 0)

    def p_movement_speed_bonus(self):
        if self.level < 6:
            return 0.40
        if self.level < 11:
            return 0.50
        if self.level < 16:
            return 0.60
        else:
            return 0.70

    def q_damage(self, ap, ad, skillrank):
        skill_level = skillrank - 1
        base_damage = [25, 50, 75, 100, 125]
        ap_scaling = 0.60
        ad_scaling = 0.65
        amount = base_damage[skill_level] + (ad * ad_scaling) + (ap * ap_scaling)
        return Spell.Spell(2, amount, 0, 0.5)

    def w_movementspeed_bonus(self, skillrank):
        base_value = [0.30, 0.35, 0.40, 0.45, 0.50]
        return base_value[skillrank - 1]

    def e_first_damage(self, ad, ap, skillrank):
        skill_level = skillrank - 1
        base_value = [50, 85, 120, 155, 190]
        ap_scaling = 0.50
        ad_scaling = 0.35
        amount = base_value[skill_level] + (ad * ad_scaling) + (ap * ap_scaling)
        return Spell.Spell(2, amount, 0, 0)

    def e_second_damage(self, ad, ap, skillrank):
        skill_level = skillrank - 1
        base_value = [50, 85, 120, 155, 190]
        ap_scaling = 0.50
        ad_scaling = 0.35
        amount = base_value[skill_level] + (ad * ad_scaling) + (ap * ap_scaling)
        return Spell.Spell(2, amount, 0, 0)

    def r_first_damage(self, bonus_ad, skillrank):
        skill_level = skillrank - 1
        base_value = [125, 225, 325]
        bonus_ad_scaling = 0.50
        amount = base_value[skill_level] + (bonus_ad * bonus_ad_scaling)
        return Spell.Spell(2, amount, 0, 0)

    def r_second_damage_minimum(self, ap, skillrank):
        skill_level = skillrank - 1
        base_value = [75, 145, 215]
        ap_scaling = 0.30
        amount = base_value[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)

    def r_second_damage(self, ap, skillrank, enemy_missing_health):
        skill_level = skillrank - 1
        base_value = [75, 145, 215]
        ap_scaling = 0.30
        amount = base_value[skill_level] + (ap * ap_scaling)

        if enemy_missing_health < 7:
            amount = amount + 0
        if enemy_missing_health < 14:
            amount = amount + (amount * 0.20)
        if enemy_missing_health < 21:
            amount = amount + (amount * 0.40)
        if enemy_missing_health < 28:
            amount = amount + (amount * 0.60)
        if enemy_missing_health < 35:
            amount = amount + (amount * 0.80)
        if enemy_missing_health < 42:
            amount = amount + (amount * 1.0)
        if enemy_missing_health < 49:
            amount = amount + (amount * 1.2)
        if enemy_missing_health < 56:
            amount = amount + (amount * 1.4)
        if enemy_missing_health < 63:
            amount = amount + (amount * 1.6)
        if enemy_missing_health < 70:
            amount = amount + (amount * 1.8)
        else:
            amount = amount + (amount * 2.0)

        return Spell.Spell(1, amount, 0, 0)
