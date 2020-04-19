from Champions.Champion import Champion
import Spell


class Azir(Champion):

    def __init__(self):
        Champion.__init__(self, "Azir")

    def q_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [70, 90, 110, 130, 150]
        ap_scaling = 0.30
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 1)

    def w_damage(self, ap, amount_soldiers, target):
        base_damage = [60, 62, 64, 66, 68, 70, 72, 75, 80, 85, 90, 100, 110, 120, 130, 140, 150, 160]
        ap_scaling = 0.60
        amount = base_damage[self.level - 1] + (ap * ap_scaling)
        # Targets beyond the target take reduced dmg
        if target:
            if self.level < 6:
                amount = amount * 0.25
                return Spell.Spell(1, amount, 0, 0)
            if self.level < 11:
                amount = amount * 0.5
                return Spell.Spell(1, amount, 0, 0)
            if self.level < 16:
                amount = amount * 0.75
                return Spell.Spell(1, amount, 0, 0)
            else:
                return Spell.Spell(1, amount, 0, 0)

    def e_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [60, 90, 120, 150, 180]
        ap_scaling = 0.40
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)

    def r_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [175, 325, 475]
        ap_scaling = 0.60
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0.5, 0)
