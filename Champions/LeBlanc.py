from Champions.Champion import Champion
import Spell


class LeBlanc(Champion):

    def __init__(self):
        Champion.__init__(self, "LeBlanc")

    def q_first_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [60, 85, 110, 135, 160]
        ap_scaling = 0.45
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 3)