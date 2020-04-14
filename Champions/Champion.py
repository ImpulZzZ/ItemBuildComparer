import Item

class Champion:

    def __init__(self, name):

        # happens if an empty entry was submitted
        if name == "":
            print("Empty String given")
            return

        self.items = []

        base_stats = []
        self.name = name
        self.build_name = ""
        self.cooldown_reduction = 0.0
        self.flat_magic_penetration = 0
        self.ap = 0
        self.bonus_attack_speed = 0

        self.level = 1
        self.max_level = 18

        self.item_amount = 0
        self.max_item_amount = 6

        # Here the base-stats are read out of a data.txt
        basestats = open("DATA/Champions.txt", "r").readlines()
        champion_name_length = len(name)
        counter = 0
        for x in basestats:

            if x.startswith(name) and (
                    basestats[counter][champion_name_length] != " " or basestats[counter][champion_name_length] != "&"):
                break
            else:
                # happens when the given champion name was not found
                if counter == len(basestats) - 1:
                    print("Champion not found")
                    return
                else:
                    counter = counter + 1

        # runs through the line and gets the stats out of it
        number = str("")
        base_stat_counter = 0
        length_of_line = len(basestats[counter])
        i = 0
        while not basestats[counter][i].isdigit() and i < length_of_line - 1:
            i = i + 1
            while basestats[counter][i].isdigit() or basestats[counter][i] == '.':
                number = number + basestats[counter][i]
                i = i + 1

            # when we have a number, append it on the base_stat-list and reset the string afterwards
            if number != "":
                base_stats.append(float(number))
                base_stat_counter = base_stat_counter + 1
            number = ""

        # initiates the base stats of the champion
        self.base_hp = base_stats[0]
        self.base_hp_per_level = base_stats[1]
        self.base_hpreg = base_stats[2]
        self.base_hpreg_per_level = base_stats[3]
        self.base_mp = base_stats[4]
        self.base_mp_per_level = base_stats[5]
        self.base_mpreg = base_stats[6]
        self.base_mpreg_per_level = base_stats[7]
        self.base_ad = base_stats[8]
        self.base_ad_per_level = base_stats[9]
        self.base_attack_speed = base_stats[10]
        self.base_attack_speed_per_level = base_stats[11]
        self.base_armor = base_stats[12]
        self.base_armor_per_level = base_stats[13]
        self.base_mr = base_stats[14]
        self.base_mr_per_level = base_stats[15]
        self.base_movespeed = base_stats[16]
        self.base_range = base_stats[17]

        self.hp = base_stats[0]
        self.hpreg = base_stats[2]
        self.mp = base_stats[4]
        self.mpreg = base_stats[6]
        self.ad = base_stats[8]
        self.attack_speed = base_stats[10]
        self.armor = base_stats[12]
        self.mr = base_stats[14]
        self.movespeed = base_stats[16]
        self.range = base_stats[17]

    def buy_item(self, item_name):
        if self.item_amount == self.max_item_amount:
            return

        self.item_amount = self.item_amount + 1

        item = eval('Item.' + item_name + '()')

        self.ap = self.ap + item.ability_power
        self.cooldown_reduction = self.cooldown_reduction + item.cooldown_reduction
        self.mp = self.mp + item.mana
        self.armor = self.armor + item.armor
        self.hp = self.hp + item.hp
        self.movespeed = self.movespeed + item.flat_movement_speed
        self.flat_magic_penetration = self.flat_magic_penetration + item.flat_magic_penetration

        # todo: Attackspeed and Movementspeed calculation
        self.attack_speed = self.base_attack_speed + (1 + (self.bonus_attack_speed / 100))
        self.bonus_attack_speed = self.bonus_attack_speed + item.attack_speed
        self.movespeed = self.movespeed + (self.movespeed * item.movement_speed)

        self.items.append(item_name)

    def sell_item(self, item_name):
        if self.item_amount == 0:
            print("Error: This Champion has no items to sell!")
            return

        self.item_amount = self.item_amount - 1

        item = eval('Item.' + item_name + '()')

        self.ap = self.ap - item.ability_power
        self.cooldown_reduction = self.cooldown_reduction - item.cooldown_reduction
        self.mp = self.mp - item.mana
        self.armor = self.armor - item.armor
        self.hp = self.hp - item.hp
        self.movespeed = self.movespeed - item.flat_movement_speed
        self.flat_magic_penetration = self.flat_magic_penetration - item.flat_magic_penetration

        # todo: Attackspeed and Movementspeed calculation
        self.attack_speed = self.attack_speed / (1 + item.attack_speed)
        self.movespeed = self.movespeed + (self.movespeed / (1 + item.movement_speed))

        self.items.remove(item_name)

    def give_build_name(self, build_name):
        self.build_name = build_name

    def sell_all_items(self):
        for item in self.items:
            self.sell_item(item)

