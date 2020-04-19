from Champions.Champion import Champion
import Spell


class Ahri(Champion):

    def __init__(self):
        Champion.__init__(self, "Ahri")

    def q_first_damage(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [40, 65, 90, 115, 140]
        scaling = 0.35
        amount = base_damage[skill_level] * scaling
        return Spell(2, amount, 0, 0)

    def q_first_damage_amplified_by_charm(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [40, 65, 90, 115, 140]
        scaling = 0.35
        amount = base_damage[skill_level] * scaling
        # charmed target takes 20% more dmg
        amount = amount + (amount * 0.20)
        return Spell(2, amount, 0, 0)

    def q_second_damage(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [40, 65, 90, 115, 140]
        scaling = 0.35
        amount = base_damage[skill_level] * scaling
        return Spell(1, amount, 0, 0)

    def w_one_target_damage(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [40, 65, 90, 115, 140]
        base_damage_reduced = [12, 19.5, 27, 34.5, 42]
        scaling = 0.30
        scaling_reduced = 0.09
        amount = base_damage[skill_level] * scaling
        amount = amount + (2 * (base_damage_reduced[skill_level]) * scaling_reduced)
        return Spell(2, amount, 0, 0)

    def w_one_target_damage_amplified_by_charm(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [40, 65, 90, 115, 140]
        base_damage_reduced = [12, 19.5, 27, 34.5, 42]
        scaling = 0.30
        scaling_reduced = 0.09
        amount = base_damage[skill_level] * scaling
        amount = amount + (2 * (base_damage_reduced[skill_level]) * scaling_reduced)
        # charmed target takes 20% more dmg
        amount = amount + (amount * 0.20)
        return Spell(2, amount, 0, 0)

    def e_damage(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [60, 90, 120, 150, 180]
        charm_duration = [1.4, 1.55, 1.7, 1.85, 2]
        scaling = 0.40
        amount = base_damage[skill_level] * scaling
        return Spell(2, amount, charm_duration[skill_level], 0)

    def r_one_target_damage(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [180, 270, 360]
        scaling = 1.05
        amount = base_damage[skill_level] * scaling
        return Spell(2, amount, 0, 0)

    def r_one_target_damage_amplified_by_charm(self, ap, skillpoints):
        skill_level = skillpoints - 1
        base_damage = [180, 270, 360]
        scaling = 1.05
        amount = base_damage[skill_level] * scaling
        return Spell(2, amount, 0, 0)
