from ItemDB import ItemDB as IDB
from npcDB import npcDB as NDB


class Quest():
    def __init__(self, name, type, item, quantity, itemgiven, desc, ps, ls, ir):
        self.name = name
        self.type = type
        self.item = item
        self.quantity = quantity
        self.itemgiven = itemgiven
        self.desc = desc
        self.ps = ps
        self.ls = ls
        self.ir = ir
class ItemQuest():
    def __init__(self, name, npc, item, quantity, given, desc):
        self.name = name
        self.npc = npc
        self.item = item
        self.quantity = quantity
        self.given = given
        self.desc = desc
class questDB():
    testitemquest = Quest("Test Give Item Quest", 'item', IDB.centhorn, 2, 0, """
    -------------------------------------------------
                  Test Give Item Quest
    I need you to find me two centaur horns. Thank you
    for your help!    
    -------------------------------------------------
    """, 0, 1, [IDB.simplemap])

