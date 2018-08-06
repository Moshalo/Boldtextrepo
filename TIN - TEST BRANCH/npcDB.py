from dialogDB import dialogDB as DDB
from ItemDB import ItemDB as IDB

class npc():
    def __init__(self, name, xc, yc, qe, quest, dialog):
        self.name = name
        self.xc = xc
        self.yc = yc
        self.qe = qe
        self.quest = quest
        self.dialog = dialog

class Quest():
    def __init__(self, name, type, item, ph, quantity, itemgiven, desc, enddesc, gr, ir, ps, ls):
        self.name = name
        self.type = type
        self.item = item
        self.ph = ph
        self.quantity = quantity
        self.itemgiven = itemgiven
        self.desc = desc
        self.enddesc = enddesc
        self.gr = gr
        self.ir = ir
        self.ps = ps
        self.ls = ls

class questDB():
    sahandimerchantquest1 = Quest("For Family", 'item', IDB.carvedpistol, 0, 1, 0, """
    -------------------------------------------------
                       For Family
    In the woods to the east there is a Lone bandit and
    I need you to kill him and take his pistol for me,
    it's a family heirloom that's been passed down for
    generations in my family. There will be a bit of gold
    involved, interested?
    -------------------------------------------------
    """, """
    -------------------------------------------------
                       For Family
    You pulled through! Did he even put up a good fight?
    Well anyways, here's the gold I promised, and I also
    found this steel shortsword, I figure you need it more
    than I do. Thank you stranger.
    -------------------------------------------------    
    """, 20, IDB.simplemap, 0, 1)
    rdudequest = Quest("Iron sword quest", 'item', IDB.ironsword, 0, 1, 0, """
    dis nibba just need a sword.., """, """
    he thank
    """, 10, IDB.coal, 0, 1)

class npcDB():
    QDB = questDB()
    sahandimerchant = npc("Sa'Handi Merchant", 5, 5, False, QDB.sahandimerchantquest1, [DDB.sahandi1, DDB.sahandi2, DDB.sahandi3])
    randomdudetest = npc("Random Test Dude", 4, 4, False, QDB.rdudequest, [DDB.rdude1, DDB.rdude2])

    allnpcs = [sahandimerchant, randomdudetest]


class ItemQuest():
    def __init__(self, name, npc, item, quantity, given, desc):
        self.name = name
        self.npc = npc
        self.item = item
        self.quantity = quantity
        self.given = given
        self.desc = desc

