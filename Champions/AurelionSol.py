from Champions.Champion import Champion
import Spell


class AurelionSol(Champion):

    def __init__(self):
        Champion.__init__(self, "AurelionSol")

    def p_damage_per_hit(self, ap, skillrank_of_w):
        skill_level_of_w = skillrank_of_w - 1
        base_damage = [12, 14, 16, 18, 20, 23, 26, 32, 38, 44, 50, 60, 70, 80, 90, 100, 110, 120]
        w_rank_damage = [5, 10, 15, 20, 25]
        ap_scaling = 0.25
        amount = base_damage[self.level - 1] + w_rank_damage[skill_level_of_w] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 0)

    def q_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [70, 110, 150, 190, 230]
        base_stun_duration = [0.55, 0.6, 0.65, 0.7, 0.75]
        ap_scaling = 0.65
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, base_stun_duration[skill_level])

    def w_damage_per_hit(self, ap, skillrank):
        amount = self.p_damage_per_hit(ap, skillrank).amount
        amount = amount + (amount * 0.4)
        return Spell.Spell(1, amount, 0, 0)

    def r_damage(self, ap, skillrank):
        skill_level = skillrank - 1
        base_damage = [150, 250, 350]
        ap_scaling = 0.70
        amount = base_damage[skill_level] + (ap * ap_scaling)
        return Spell.Spell(1, amount, 0, 2)
