from Champions.Champion import Champion
import Spell

class Annie(Champion):
    def __init__(self):
        Champion.__init__(self, "Annie")

    def p_stun(self, level):
        if level < 6:
            return Spell.Spell(0, 0, 1.25, 0)
        if level < 11:
            return Spell.Spell(0, 0, 1.5, 0)
        else:
            return Spell.Spell(0, 0, 1.75, 0)

    def q_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [80, 115, 150, 185, 220]
        ap_scaling = 0.80
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)

    def w_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [70, 115, 160, 205, 250]
        ap_scaling = 0.85
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)

    def e_dmg_per_getting_autoattacked(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [20, 30, 40, 50, 60]
        ap_scaling = 0.20
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)

    def r_initial_dmg(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [150, 275, 400]
        ap_scaling = 0.65
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)