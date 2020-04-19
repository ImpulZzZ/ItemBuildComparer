from appJar import gui

import Champions.Champion
import Champions.Ahri
import Champions.Akali
import Champions.Anivia
import Champions.Annie
import Champions.AurelionSol


def give_stats_gui(champions):
    app = gui("Item Build Comparing Tool", "800x800")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(14)
    app.addLabel("info", champions[0].ap)
    app.go()


def itemization_gui(champions, recursion_depth):
    # the current champion is chosen
    champion = champions[recursion_depth - 1]

    # if the champion did not get a buildname, its buildname is it's standard name
    if champion.build_name == "":
        champion.give_build_name(champion.name)

    # the event-handler that reads out the chosen items and goes to the next page
    def finish(button):
        item_counter = 0
        for item in all_items_for_auto_entry:
            if app.getCheckBox(item):
                if item_counter < champion.max_item_amount:
                    champion.buy_item(item)
                    item_counter = item_counter + 1
                # if more than 6 items want to be put on a champion, it throws an error
                else:
                    error_msg = "You tried to give " + champion.build_name + " more than " + str(
                        champion.max_item_amount) + \
                                " items! Try again!"
                    app.errorBox("Error", error_msg)
                    champion.sell_all_items()
                    return

        # the current gui is closed
        app.stop()
        # responsible, that every chosen championbuild has its own process for giving items.
        # when all builds are done, the next page is shown
        if recursion_depth > 0:
            itemization_gui(champions, recursion_depth - 1)
        else:
            give_stats_gui(champions)

    all_items_for_auto_entry = ['Archangels_Staff', 'Banshees_Veil', 'Hextech_GLP_800', 'Hextech_Gunblade',
                                'Hextech_Protobelt_01', 'Liandrys_Torment', 'Liandrys_Torment_against_cced_enemy',
                                'Liandrys_Torment_fully_stacked', 'Liandrys_Torment_fully_stacked_against_cced_enemy',
                                'Lichbane', 'Ludens_Echo', 'Morellonomicon', 'Nashors_Tooth', 'Rabadons_Deathcap',
                                'Rod_of_Ages', 'Rod_of_Ages_full_stacked', 'Rylais_Crystal_Scepter', 'Seraphs_Embrace',
                                'Sorcerers_Shoes', 'Spellbinder', 'Spellbinder_full_stacked', 'Twin_Shadows',
                                'Voidstaff', 'Zhonyas_Hourglass']

    app = gui("Item Build Comparing Tool", "800x800")
    app.setFont(12)
    app.addLabel(champion.build_name, champion.build_name)
    app.setLabelBg(champion.build_name, "blue")

    # add a checkbox for every item
    for item in all_items_for_auto_entry:
        app.addCheckBox(item)

    # if a champion has no buildname, his buildname will be his standard name
    if champion.build_name == "":
        champion.build_name = champion.name

    button_message = "Finish " + str(champion.build_name)
    app.addButton(button_message, finish, row=1, column=1)
    app.go()


def renaming_gui(champions):
    # The Event-Handler, when the continue button is pressed
    def next_page(button):
        # reads out all entries and gives the builds their names
        counter = 1
        for champion in champions:
            connected_entry = "buildname" + str(counter)
            # take the given input and rename a build
            new_name = app.getEntry(connected_entry)
            champions[int(counter) - 1].give_build_name(new_name)
            counter = counter + 1

        # the current gui is closed and the itemization_gui is created
        app.stop()
        itemization_gui(champions, len(champions) - 1)

    # Initialization of the gui
    app = gui("Item Build Comparing Tool", "800x800")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(14)

    # here the entrys are created, where the user types in the names for his build
    counter = 1
    for champion in champions:
        entry_name = "buildname" + str(counter)
        entry_message = "Give your " + str(counter) + ": " + champion.name + " itembuild a name"
        new_name = app.addEntry(entry_name)
        app.setEntryDefault(entry_name, entry_message)
        champion.build_name = new_name
        counter = counter + 1

    app.addButton("Continue", next_page)
    app.go()


def create_first_gui():
    champions = []
    all_champions_for_auto_entry = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios",
                                    "Ashe",
                                    "AurelionSol", "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille",
                                    "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "DrMundo", "Draven", "Ekko",
                                    "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank",
                                    "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia",
                                    "Ivern", "Janna", "JarvanIV", "Jax", "Jayce", "Jinx", "Kai'Sa", "Kalista", "Karma",
                                    "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred",
                                    "Kled", "Kled&Skaarl", "Kog'Maw", "LeBlanc", "LeeSin", "Leona", "Lissandra",
                                    "Lucian",
                                    "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "MasterYi", "MegaGnar",
                                    "MissFortune",
                                    "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee",
                                    "Nocturne",
                                    "Nunu&Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana",
                                    "Quinn",
                                    "Rakan", "Rammus", "Rek'Sai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze",
                                    "Sejuani",
                                    "Senna", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner",
                                    "Sona",
                                    "Soraka", "Swain", "Sylas", "Syndra", "TahmKench", "Taliyah", "Talon", "Taric",
                                    "Teemo",
                                    "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr",
                                    "Urgot",
                                    "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear",
                                    "Warwick",
                                    "Wukong", "Xayah", "Xerath", "XinZhao", "Yasuo", "Yorick", "Yuumi", "Zac", "Zed",
                                    "Ziggs",
                                    "Zilean", "Zoe", "Zyra"]

    ap_champions_for_auto_entry = ["Ahri", "Akali", "Anivia", "Annie", "AurelionSol", "Azir", "Brand",
                                   "Cassiopeia", "Diana", "Ekko", "Fizz", "Galio", "Heimerdinger",
                                   "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Lux", "Malzahar", "Neeko",
                                   "Orianna", "Ryze", "Sylas", "Syndra", "TwistedFate", "Veigar", "Vel'Koz",
                                   "Viktor", "Vladimir", "Xerath", "Ziggs", "Zilean", "Zoe"]

    # here are the event-handling functions for every button in this gui
    def press(button):
        # whenever a champion is added, he gets a label and a Champion.x instance
        if button == "Add Champion":
            entry = app.getEntry("Champion")
            instancing_code = "Champions." + entry + "." + entry + "()"
            champion = eval(instancing_code)

            # Tests if a Champion was found with the given name
            try:
                test = champion.base_ad
            except AttributeError:
                app.errorBox("Error",
                             "You maybe typed out a Champion wrong!\nThe format should be like:\nAhri\nCho'Gath\nMissFortune")
                return

            # every champ is added to the list of champions which is used in every gui instance
            champions.append(champion)
            # here the label is created
            label_name = champion.name + str(len(champions))
            app.addLabel(label_name, champion.name)
            app.setLabelBg(label_name, "green")

        # the reset button restarts the application
        if button == "Reset":
            champions.clear()
            app.stop()
            create_first_gui()

        # here the user can see a little introduction
        if button == "Instructions":
            app.infoBox("Instructions", "Step 1: Type in a champion name in the textbox\n\n"
                                        "Step 2: Click 'Add champion'\n"
                                        "Your champs you add will be stored and shown below.\n"
                                        "If you did a mistake, you can reset the program\n\n"
                                        "Step 3: If you added the champions you want, click on 'Continue'\n\n"
                                        "Step 4: In the next window you give your Champs a name that you can differate them\n\n"
                                        "If you don't want a specific name, you can click 'Continue' without giving names\n\n"
                                        "Step 5: Work in Progress, but here you later can give your champions items, levels etc.")

        # event-handler for continue-button
        if button == "Continue":
            if len(champions) > 0:
                app.stop()
                renaming_gui(champions)
            else:
                app.errorBox("NoChampionsError", "You first have to select at least one champion")

    # Initialization of the gui
    app = gui("Item Build Comparing Tool", "800x800")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(14)
    app.addAutoEntry("Champion", ap_champions_for_auto_entry, row=0, column=0)
    app.setEntryDefault("Champion", "Type in a Champion")
    app.addButton("Add Champion", press, row=0, column=1, colspan=1)
    app.addButton("Continue", press, row=1, column=0, colspan=1)
    app.addButton("Reset", press, row=1, column=1, colspan=1)
    app.addButton("Instructions", press, row=2, column=1, colspan=1)
    app.addLabel("Selected Champions:", row=2, column=0, colspan=1)
    app.setLabelBg("Selected Champions:", "green")
    app.go()


def main():
    create_first_gui()


if __name__ == '__main__':
    main()
