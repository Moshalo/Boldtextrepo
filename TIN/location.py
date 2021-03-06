from enemyDB import enemyDB as EDB
from ItemDB import ItemDB as I

class biome():
    def __init__(self, type, mra, wl, temp, description):
        self.type = type
        self.mra = mra
        self.wl = wl
        self.temp = temp
        self.description = description

class biomeDB():
    northwoods = biome("Northern Woodlands", [], 7, 40, "Pine and spruce trees as far as the eye can see. Also pretty chilly.")
    northplains = biome("Northern Plains", [], 1, 38, "Lightly frosted plainlands, little wildlife to be seen.")
    northbeaches = biome("Northern beach", [], 0, 35, "A chilly beach with the clean but cold northern air blowing strong")
    northmountains = biome("Northern Mountains", [], 0, 18, "Frozen stacks of rock and snow, the winds billowing through the pass like an ancient chant...")


class town():
    def __init__(self, name, pos, xpos, ypos, bank, bankamount, blacksmith, gunsmith, generalstore, known):
        self.name = name
        self.pos = pos
        self.xpos = xpos
        self.ypos = ypos
        self.bank = bank
        self.bankamount = bankamount
        self.blacksmith = blacksmith
        self.gunsmith = gunsmith
        self.generalstore = generalstore
        self.known = known

class camp():
    def __init__(self, name, pos, enemies, endloot, known, description):
        self.name = name
        self.pos = pos
        self.enemies = enemies
        self.endloot = endloot
        self.known = known
        self.description = description

class campDB():
    bcamp1 = camp("Bandit Camp", 42, [], [], False, "a small campsite with bandits around the campfire..")

class townDB():
    narja = town("Narja", 12, 16, 7, True, {I.goldpiece: 0}, [], [], [I.wolfpelt, I.bread, I.bread], True)
    lorasu = town("Lorasu", 76, 20, 11, True, {I.goldpiece: 0}, [], [], [I.wolfpelt, I.bread, I.bread], False)
    mourngarth = town("Mourngarth", 169, 18, 15, True, {I.goldpiece: 0}, [], [], [I.wolfpelt, I.bread, I.bread], False)

class ferryl():
    def __init__(self, pos, returnpos, cost):
        self.pos = pos
        self.returnpos = returnpos
        self.cost = cost

class dynl():
    def __init__(self, pos, town, locations, npcs, enemies, items, description, foundlootdesc, encbf, preencdesc, danger, postcombdesc):
        self.pos = pos
        self.town = town
        self.locations = locations
        self.npcs = npcs
        self.enemies = enemies
        self.items = items
        self.biome = biome
        self.description = description
        self.foundlootdesc = foundlootdesc
        self.encbf = encbf
        self.preencdesc = preencdesc
        self.danger = danger
        self.postcombdesc = postcombdesc

class dynlDB:
    p12 = dynl(12, townDB.narja, [], [], [], [], "The outskirts of the town of Narja..", '', False, '', False, '')
    p13 = dynl(13, None, [], [], [], [], 'You see a town in the distance to the west.', '', False, '', False, '')
    p25 = dynl(25, None, [], [], [], [], 'You see a town in the distance to the northeast', '', False, '', False, '')
    p26 = dynl(26, None, [], [], [], [], 'You see a town in the distance to the north', '', False, '', False, '')
    p27 = dynl(27, None, [], [], [EDB.sqmugger], [I.simplemap], 'You see a town in the distance to the northwest', 'You searched a small chest the mugger left behind and found your map!', False, 'You approach the smoke you saw in the distance, it is coming from a campfire and the mugger that attacked you is sitting at the fire drinking, he must pay!', True, 'You kill the mugger, and he had your gold purse. You search him for anything else you can find and your map isnt on him. You should search the area to see if it is around!')
    p42 = dynl(42, None, [], [], [EDB.fban, EDB.fban, EDB.fban], [], "A bandit camp lies ahead... type 'attack camp' if you want to fight", '', False, 'You notice a bandit camp up ahead. There are multiple enemies and it would be hard to take them all on at once without being very strong and skilled. Maybe you should think twice about approaching..', True, '')
    p76 = dynl(76, townDB.lorasu, [], [], [], [], "The outskirts of the town of Lorasu..", '', False, '', False, '')
    p169 = dynl(169, townDB.mourngarth, [], [], [], [], "To outskirts of the town of Mourngarth...", '', False, '', False, '')
    pointsofinterest = [p13, p25, p26, p27, p42]
    townsl = [p12, p76, p169]
    #BORDERS
    southcompwall = [320, 321, 322, 324, 325, 326, 327, 328, 329, 330]
    southcompgate = [323]
    #NORTH
    northbeachesl = [5, 6, 7, 12, 13, 14, 15, 16 ,17 ,19, 23, 24, 25, 32, 37, 38, 39, 47, 52, 62, 68, 78, 86, 104, 105, 106, 79, 63, 48, 35, 36, 51, 67, 85, 107, 137, 138]
    northwoodsl = [42, 43, 44, 45, 56, 57, 58, 59, 60, 71, 72, 73, 74, 75, 76, 98, 99, 119, 120]
    northmountainsl = [64, 65, 66, 81, 82, 83, 84, 100, 101, 102, 130]
    #MIDLAND
    midbeachesl = [107, 139, 163, 189, 164, 165, 166, 167, 190, 191, 216, 217, 218, 219, 220, 221, 242, 266, 294, 138,
                   161, 185, 207, 231, 250, 274, 302]
    tempforestl = [111, 112, 113, 114, 115, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 152, 154, 155, 156, 157,
                   168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 192, 193, 194, 195, 196, 197,
                   198, 199, 200, 201, 202, 203, 222, 223, 224, 225, 226, 227]
    jungle = [267, 278, 269, 270, 271, 272, 273, 295, 296, 297, 298, 299, 300, 301]
