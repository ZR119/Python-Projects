#Ivan
#Pokemon

#init
import random
global pokemon_level
pokemon_level = 0
global pokemon_name
pokemon_name = "Gastly"
global day
day = 1


def stage_1():
    print((r"                            _\n"))
    print((r"                         .\"' `..._\n"))
    print((r"                        '         `.\n"))
    print((r"                      .'      ___..'\n"))
    print((r"                _   .\"       '   .__,-.,\"\", ,----.\n"))
    print((r"     ,.-\"\"''-..\" :  :        `--'        ' :      :\n"))
    print((r"   .'            :_,'                    `._`\"--. ;\n"))
    print((r"   :              _,.--'\"'\"\"`--._           `.  `\"\n"))
    print((r"  j             ,'               `-.      ,._.'  ,\"\".\n"))
    print((r"  :           ,'                   ,-.   .   __  `..'\n"))
    print((r"  `--.    .'.'                   ,'   `. :_,\"  `.\n"))
    print((r",.   ;   .   \\                 ,'      |         `.\n"))
    print(("' :  :    |    `.             ,'        |\\         `.  _\n"))
    print((r"`.   ._  |      \\         _.'          | .      ___ `\" :\n"))
    print((r"       : '     . \\      ,'  .          ' |     :   `...'\n"))
    print((r"      ,'  \\       `.   .             ,'  |     '  __\n"))
    print((r"     .    `.       |    \\          .'    '    .  (  `.\n"))
    print((r"   .'      \\`.___,'      `-.____.-'     '     :   `-.'\n"))
    print((r"    .   ,\". \\ ..___              _     /      :    .\n"))
    print((r"    :   . :  \\|/\\  `\"'--------+\"|,'  ,'       `-..' :\n"))
    print((r"     `-\" .'   `: `\"-.._______,.\\|  .'               '\n"))
    print((r"         `--. _ `._             _,'        ,\"\"-.__,'\n"))
    print((r"             \" :   `\"--.....--\"'     __   .\n"))
    print((r"             ,-'                 ,.-\"  `-'\n"))
    print((r"            :   ,..             .    ,\"\".\n"))
    print((r"           .'   .  :   __..._   `\"-. :   :\n"))
    print((r"           `.._  : ' ,'      `\"--..' `--\"\n"))
    print((r"               `-' `\" mh\n"))

def stage_2():
    print((r"              -._                                   _.\n"))
    print((r"               \\ `-.._                           _,' |\n"))
    print((r"                \\     `-._    _,.--------.._  _.\"    '\n"))
    print((r"                 \\        `--'              ``.     /\n"))
    print((r"                  \\                                j    __\n"))
    print(("__         __       \\                               |.-\"' /\n"))
    print((r"`.`-.`-.__`.`'\"----\"\\                              |    /\n"))
    print((r"   `.       `.       '        ._                       /\n"))
    print((r"   `..        \\               | `.               /|   /\n"))
    print((r"     `.        `.             |   `._          .' |  /\n"))
    print((r"       `.  .-----`            |      `.       /   ' '\"\"''\n"))
    print((r"         `. `.            .    ._      `_    /  ,'    .'\n"))
    print((r"           `. `.           `._   `'\"\"'\"'     \"\"' ,  ,'\n"))
    print((r"             `. `.          `.`.              ,-/ ,'       _..\n"))
    print((r"               `. `.          \\|,---..  ,--\"./ / ,--------\".  \\\n"))
    print((r"                 `._           `.     `/ , .`.',:           \\  \\\n"))
    print((r"                    `._          `..\".,./ ' _.' :            \\  `.\n"))
    print((r"                  ,-'\" `-._              _.\"     .   |.-\"`.   \\  |\n"))
    print((r"                 .         `-..........-'        |   `..   \\   |_'\n"))
    print((r"                 |           `\".                 `.._   .  '  ,'\n"))
    print((r"                 |         |   |                     `\"'    .'\n"))
    print((r"                 |   /\\    |'  '\n"))
    print((r"                 '  /  \\   ||   .\n"))
    print((r"                '   \\  '   |'   ;\n"))
    print((r"                 \\  '  \\   `...'\n"))
    print((r"                  `\"\"   `,' mh\n"))

def stage_3():
    print((r"                |`._         |\\\n"))
    print((r"                `   `.  .    | `.    |`.\n"))
    print((r"                 .    `.|`-. |   `-..'  \\           _,.-'\n"))
    print((r"                 '      `-. `.           \\ /|   _,-'   /\n"))
    print((r"             .--..'        `._`           ` |.-'      /\n"))
    print((r"              \\   |                                  /\n"))
    print((r"           ,..'   '                                 /\n"))
    print((r"           `.                                      /\n"))
    print((r"           _`.---                                 /\n"))
    print((r"       _,-'               `.                 ,-  /\"-._\n"))
    print((r"     ,\"                   | `.             ,'|   `    `.\n"))
    print((r"   .'                     |   `.         .'  |    .     `.\n"))
    print((r" ,'                       '   ()`.     ,'()  '    |       `.\n"))
    print(("'-.                    |`.  `.....-'    -----' _   |         .\n"))
    print((r"/ ,   ________..'     '  `-._              _.'/   |         :\n"))
    print((r"` '-\"\" _,.--\"'         \\   | `\"+--......-+' //   j `\"--.. , '\n"))
    print((r"   `.'\"    .'           `. |   |     |   / //    .       ` '\n"))
    print((r"     `.   /               `'   |    j   /,.'     '\n"))
    print((r"       \\ /                  `-.|_   |_.-'       /\\\n"))
    print((r"        /                        `\"\"          .'  \\\n"))
    print((r"       j                                           .\n"))
    print((r"       |                                 _,        |\n"))
    print((r"       |             ,^._            _.-\"          '\n"))
    print((r"       |          _.'    `'\"\"`----`\"'   `._       '\n"))
    print((r"       j__     _,'                         `-.'-.\"`\n"))
    print((r"         ',-.,' mh\n"))

def rest():
    print(pokemon_name)
    print("your pokemons level is ",(pokemon_level))
    if pokemon_name == "Gastly":
        stage_1()
    elif pokemon_name == "Haunter":
        stage_2()
    else:
        stage_3()


def train():
    global pokemon_level
    pokemon_level = pokemon_level + 1
    print("Your pokemon went on a run")


def evolve():
    global pokemon_level
    global pokemon_name
    if pokemon_level >= 10:
        print("your Pokemon has evolved into Haunter!")
        pokemon_name = "Haunter"
    elif pokemon_level >= 20:
        print("your pokemon has evolved into Gengar!")
        pokemon_name = "Gengar"

def gym_battle():
    global pokemon_level
    outcome = random.randint(1,2)
    if outcome == 1:
        print("you won!")
        pokemon_level = pokemon_level + 2
    elif outcome == 2:
        print("You Lose")




while True:
    print("choose an activity for today: " + str(day))
    print(""""1.train
          2.rest (display info)
          3.gym battle
          4.quit""""")
    activity = int(input("Activity for the day: "))
    if activity == 1:
        train()
        evolve()
    elif activity == 2:
        rest()
    elif activity == 3:
        gym_battle()
    elif activity == 4:
        break






