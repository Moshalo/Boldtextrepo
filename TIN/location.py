from enemyDB import enemyDB as EDB


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
    def __init__(self, name, pos, bank, bankamount, blacksmith, gunsmith, generalstore):
        self.name = name
        self.pos = pos
        self.bank = bank
        self.bankamount = bankamount
        self.blacksmith = blacksmith
        self.gunsmith = gunsmith
        self.generalstore = generalstore

class camp():
    def __init__(self, name, pos, enemies, endloot, description):
        self.name = name
        self.pos = pos
        self.enemies = enemies
        self.endloot = endloot
        self.description = description

class campDB():
    bcamp1 = camp("Bandit Camp", 42, [], [], "A small campsite with bandits around the campfire..")

class townDB():
    ttown = town("Test Town", 12, True, 60000, [], [], [])

class dynl():
    def __init__(self, pos, town, locations, npcs, enemies, description):
        self.pos = pos
        self.town = town
        self.locations = locations
        self.npcs = npcs
        self.enemies = enemies
        self.biome = biome
        self.description = description

class dynlDB:
    p12 = dynl(12, townDB.ttown, [], [], [], "The outskirts of Test Town..")
    p42 = dynl(42, None, [], [], [EDB.fban, EDB.fban, EDB.fban], "A bandit camp lies ahead... type 'attack camp' if you want to fight")
    pointsofinterest = [p42]
    townsl = [p12]
    northbeachesl = [5, 6, 7, 12, 13, 14, 15, 16 ,17 ,19, 23, 24, 25, 32, 37, 38, 39, 47, 52, 62, 68, 78, 86, 104, 105, 106, 79, 63, 48, 35, 36, 51, 67, 85, 107, 137, 138]
    northwoodsl = [42, 43, 44, 45, 56, 57, 58, 59, 60, 71, 72, 73, 74, 75, 76, 98, 99, 119, 120]
    northmountainsl = [64, 65, 66, 81, 82, 83, 84, 100, 101, 102, 130]

