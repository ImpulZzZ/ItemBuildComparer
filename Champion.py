class Champion:

    def __init__(self, name):
        self.base_stats = [16]
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
            if x.startswith(name) and basestats[counter][champion_name_length] != " ":
                break
            else:
                counter = counter + 1

        print(basestats[counter])

        # runs through the line and gets the stats out of it
        base_stat_counter = 0
        length_of_line = len(basestats[1])
        i = 0
        while not basestats[1][i].isdigit() and i < length_of_line-1:
            i = i + 1
            while basestats[1][i].isdigit():
                i = i + 1
                base_stat_counter = base_stat_counter + 1











