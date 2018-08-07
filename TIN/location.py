from enemyDB import enemyDB as EDB


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
        self.description = description

class dynlDB:
    p12 = dynl(12, townDB.ttown, [], [], [], "The outskirts of Test Town..")
    p42 = dynl(42, None, [], [], [EDB.fban, EDB.fban, EDB.fban], "A bandit camp lies ahead... type 'attack camp' if you want to fight")
    pointsofinterest = [p12]

