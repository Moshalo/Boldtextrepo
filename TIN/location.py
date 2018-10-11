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
    narja = town("Narja", 12, 16, 7, True, 60000, [], [], [I.wolfpelt, I.bread, I.bread], True)

class dynl():
    def __init__(self, pos, town, locations, npcs, enemies, items, description, foundlootdesc):
        self.pos = pos
        self.town = town
        self.locations = locations
        self.npcs = npcs
        self.enemies = enemies
        self.items = items
        self.biome = biome
        self.description = description
        self.foundlootdesc = foundlootdesc

class dynlDB:
    p12 = dynl(12, townDB.narja, [], [], [], [], "The outskirts of the town of Narja..", '')
    p13 = dynl(13, None, [], [], [], [], 'You see a town in the distance to the west.', '')
    p25 = dynl(25, None, [], [], [], [], 'You see a town in the distance to the northeast', '')
    p26 = dynl(26, None, [], [], [], [], 'You see a town in the distance to the north', '')
    p27 = dynl(27, None, [], [], [EDB.sqmugger], [I.simplemap], 'You see a town in the distance to the northwest', 'You searched a small chest the mugger left behind and found your map!')
    p42 = dynl(42, None, [], [], [EDB.fban, EDB.fban, EDB.fban], [], "A bandit camp lies ahead... type 'attack camp' if you want to fight", '')
    pointsofinterest = [p13, p25, p26, p27, p42]
    townsl = [p12]
    #BORDERS
    southcompwall = [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330]
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
