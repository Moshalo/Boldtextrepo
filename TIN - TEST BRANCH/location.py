class town():
    def __init__(self, name, pos, bank, bankamount, blacksmith, gunsmith, generalstore):
        self.name = name
        self.pos = pos
        self.bank = bank
        self.bankamount = bankamount
        self.blacksmith = blacksmith
        self.gunsmith = gunsmith
        self.generalstore = generalstore

class townDB():
    ttown = town("Test Town", 12, True, 60000, [], [], [])

class dynl():
    def __init__(self, pos, town, locations, npcs):
        self.pos = pos
        self.town = town
        self.locations = locations
        self.npcs = npcs

class dynlDB:
    p12 = dynl(12, townDB.ttown, [], [])

    pointsofinterest = [p12]

