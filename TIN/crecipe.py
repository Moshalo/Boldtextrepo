from ItemDB import ItemDB as IDB


class Recipe():
    def __init__(self, name, type, k, ic, ing, lvl, exp, r):
        self.name = name
        self.type = type
        self.k = k
        self.ic = ic
        self.ing = ing
        self.lvl = lvl
        self.exp = exp
        self.r = r
class RecipeDB():
    #ALCHEMY
    smallhpr = Recipe("Small Health Potion", "potion", 0, IDB.lowhp, {
        IDB.bottlewater: 1,
        IDB.wberries: 2,
        IDB.salt: 1
    }, 0, 5, True)
    nhpr = Recipe("Health Potion", "potion", 0, IDB.hp, {
        IDB.bottlewater: 1,
        IDB.wberries: 2,
        IDB.potatoweed: 1,
        IDB.salt: 2
    }, 5, 20, True)
    lhpr = Recipe("Large Health Potion", "potion", 0, IDB.largehp, {
        IDB.bottlewater: 1,
        IDB.potatoweed: 2,
        IDB.wberries: 4,
        IDB.salt: 6
    }, 15, 55, True)
    hhpr = Recipe("Huge Health Potion", "potion", 0, IDB.hugehp, {
        IDB.bottlewater: 1,
        IDB.aethdust: 2,
        IDB.potatoweed: 1,
        IDB.salt: 1
    }, 0, 5, True)
    spoison = Recipe("Simple Poison", "potion", 0, IDB.poison, {
        IDB.bottlewater: 1,
        IDB.centhorn: 1
    }, 0, 5, True)
    #SMELTING(Not actually a skill)
    ironingot = Recipe("Iron Ingot", "ingot", 0, IDB.ironingot, {
        IDB.coal: 1,
        IDB.ironore: 2,
    }, 0, 0, True)
    #BLACKSMITHING
    ironsword = Recipe("Iron Shortsword", "weapon", 0, IDB.ironsword, {
        IDB.coal: 2,
        IDB.ironingot: 1,
        IDB.woodrod: 1
    }, 1, 15, True)
    ironlsword = Recipe("Iron Longsword", "weapon", 0, IDB.ironlsword, {
        IDB.coal: 3,
        IDB.ironingot: 2,
        IDB.woodrod: 2
    }, 3, 30, True)

    #GUNSMITHING
    #ARMORSMITHING
    #COOKING
    #CONSTRUCTION
    allrecipes = [smallhpr, nhpr, spoison, ironingot, ironsword]
