class Spell:

    def __init__(self, damage_type, damage_amount, hard_cc_in_sec, soft_cc_in_sec):
        # types: true = 1, magic = 2, physical = 3, undefined = 0
        self.type = damage_amount
        self.amount = damage_amount
        self.hard_cc_in_sec = hard_cc_in_sec
        self.soft_cc_in_sec = soft_cc_in_sec