class Champion:

    def __init__(self, name):
        base_stats = []
        self.name = name
        self.ap = 0
        self.level = 18

        self.item_amount = 0
        self.max_item_amount = 6

        # Here the abilities are saved with their Base-Dmg and Scaling
        data = open("DATA/" + name + ".txt", "r").readlines()
        self.passive = data[0]
        self.passive_scaling = data[1]
        self.q = data[2]
        self.q_scaling = data[3]
        self.w = data[4]
        self.w_scaling = data[5]
        self.e = data[6]
        self.e_scaling = data[7]
        self.r = data[8]
        self.r_scaling = data[9]

        # Here the base-stats are read out of a data.txt
        basestats = open("DATA/Champions.txt", "r").readlines()
        champion_name_length = len(name)
        counter = 0
        for x in basestats:
            if x.startswith(name) and (basestats[counter][champion_name_length] != " " or basestats[counter][champion_name_length] != "&"):
                break
            else:
                counter = counter + 1

        # runs through the line and gets the stats out of it
        number = str("")
        base_stat_counter = 0
        length_of_line = len(basestats[counter])
        i = 0
        while not basestats[counter][i].isdigit() and i < length_of_line-1:
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
        self.hp = base_stats[0]
        self.hp_per_level = base_stats[1]
        self.hpreg = base_stats[2]
        self.hpreg_per_level = base_stats[3]
        self.mp = base_stats[4]
        self.mp_per_level = base_stats[5]
        self.mpreg = base_stats[6]
        self.mpreg_per_level = base_stats[7]
        self.ad = base_stats[8]
        self.ad_per_level = base_stats[9]
        self.atks = base_stats[10]
        self.atks_per_level = base_stats[11]
        self.armor = base_stats[12]
        self.armor_per_level = base_stats[13]
        self.mr = base_stats[14]
        self.mr_per_level = base_stats[15]
        self.movespeed = base_stats[16]
        self.range = base_stats[17]
















