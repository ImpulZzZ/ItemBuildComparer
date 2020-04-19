from Champions.Champion import Champion
import Spell


class Anivia(Champion):

    def __init__(self):
        Champion.__init__(self, "Anivia")

    def q_first_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [60, 85, 110, 135, 160]
        ap_scaling = 0.45
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 3)

    def q_second_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [60, 85, 110, 135, 160]
        stun_duration = [1.1, 1.2, 1.3, 1.4, 1.5]
        ap_scaling = 0.45
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, stun_duration[skill_level], 3)

    def e_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [50, 75, 100, 125, 150]
        ap_scaling = 0.50
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)

    def e_damage_doubled(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [50, 75, 100, 125, 150]
        ap_scaling = 0.50
        amount = base_damage[skill_level] + (ap * ap_scaling)
        amount = amount * 2
        return Spell.Spell(1, amount, 0, 0)

    def r_damage_per_second(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [40, 60, 80]
        # slow = [0.20, 0.30, 0.40]
        ap_scaling = 0.125
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 1)

    def r_damage_per_second_fully_charged(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [40, 60, 80]
        # slow = [0.60, 0.90, 1.20]
        ap_scaling = 0.125
        amount = base_damage[skill_level] + (ap * ap_scaling)
        amount = amount * 3
        return Spell.Spell(1, amount, 0, 1)
