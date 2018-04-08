from random import randint, randrange
import random
from os import system
import sys
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style
from item import *
from location import *
from enemy import *
from quest import *
from unit import *
from dialog import *
from ItemDB import ItemDB as I
from crecipe import Recipe as Rec
from crecipe import RecipeDB as RDB
from enemyDB import enemyDB as E
from dialogDB import dialogDB as D
from npcDB import npcDB as NDB
from quest import questDB as QDB
from randomencounter import *
from weapon import weapon as w
from armor import armor as a
from misc import misc as m
import pickle
class Main():
    def __init__(self):
        #Character
        system("title Time is now v0.4")
        self.name = ""
        self.health = 100
        self.maxhealth = 100
        self.xcoord = 5
        self.ycoord = 4
        self.biome = "Forest"
        self.rs = None
        self.ms= None
        self.hs = None
        self.cs = None
        self.ps = None
        self.fs = None
        self.location = None
        self.npc = None
        self.damage = 0
        self.gundamage = 0
        self.shot = 0
        self.reloading = 0
        self.defence = 0
        self.status = 'normal'
        self.fighting = None
        self.battling = None
        self.playerhit = ""
        self.enemyhit = ""
        self.cdid = 99
        self.devenabled = 1
        self.ammo = 0
        #CharacterStats(WIP)
        self.statswords = 1
        self.statblock = 1
        self.statdodge = 1
        #CharacterSkills(WIP)
        self.skillblacksmith = 1
        self.skillgunsmith = 1
        self.skillfishing = 1
        self.skillleatherwork = 1
        self.skillbuilding = 1
        self.skillcommanding = 1
        self.skillmining = 1
        self.skillforaging = 1
        self.skillhunting = 1
        self.skillcooking = 1
        self.skillalch = 1
        #CharacterMaterials
        self.matiron = 9999
        self.matcopper = 9999
        self.mattin = 9999
        self.matsteel = 9999
        self.matwood = 9999
        #QUESTS
        self.questlog = []
        self.compquests = []
        self.test = []
        #Crafting Recipes known
        self.alchrec = [RDB.smallhpr, RDB.nhpr, RDB.spoison]
        self.bsrec = [RDB.ironsword]
        self.gsrec = []
        self.consrec = []
        self.asrec = []
        self.cookrec = []
        #Admin Item USED FOR TOWNS TO SHOW AN EMPTY INVENTORY
        self.aitem = item("34y6y734577562735723", "admin", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', Style.DIM, 666)
        #Inventory
        self.gold = 0
        #Towns
        self.devtown = town("DEV", 9999, 9999, 1, 10000,  [I.bread], [I.bread], [I.bread])
        self.norag = town("Norag", 16, -11, 1, 0, [self.aitem], [], [self.aitem])
        self.gabesh = town("Gabesh", 6, 12, 0, 0, [], [], [])
        self.yoeran = town("Yoeran", 4, 16, 1, 0, [self.aitem], [self.aitem], [self.aitem])
        self.litau = town("Litau", 30, -55, 1, 0, [self.aitem], [], [])
        self.uash = town(colored(Style.BRIGHT + "Uash", 'white'), 33, -4, 0, 0, [self.aitem], [self.aitem], [self.aitem])
        self.shreeda = town("Shreeda", 11, 27, 1, 0, [], [], [self.aitem])
        self.towns = [self.devtown, self.norag, self.gabesh, self.yoeran, self.litau, self.uash, self.shreeda]
        #Townstuffs/
        self.inventory = [I.ironsword, I.clothcap, I.leathertunic, I.clothpants, I.ruggedshoes]
        self.stackinv = {
            IDB.aethdust: 0,
            IDB.centhorn: 0,
            IDB.wolfpelt: 0,
            IDB.bottlewater: 2,
            IDB.salt: 2,
            IDB.potatoweed: 0,
            IDB.wberries: 4,
            IDB.coal: 3,
            IDB.ironore: 0,
            IDB.ironingot: 1,
            IDB.woodrod: 1
        }
        #self.inventory = [I.bread, I.ironsword, I.ironlsword, I.leathertunic, I.steelsword, I.steellsword, I.leathcolbp, I.bsteelsword, I.bsteellsword, I.disasterblade, I.sfsword,
                         #I.bladeofeternity, I.aetherialhelm, I.aetherialcp, I.aetheriallp, I.aetherialwraps, I.gsofkings, I.mkwarhammer]
        # Developer item kits (REMOVE IN FINAL RELEASE)
        self.dkit1 = [I.ironsword, I.clothcap, I.leathertunic, I.clothpants, I.ruggedshoes]
        self.dkit2 = [I.bread, I.ironsword, I.ironlsword, I.leathertunic, I.steelsword, I.steellsword, I.leathcolbp, I.bsteelsword, I.bsteellsword, I.disasterblade, I.sfsword,
                         I.bladeofeternity, I.aetherialhelm, I.aetherialcp, I.aetheriallp, I.aetherialwraps, I.gsofkings, I.mkwarhammer]
        self.dkit3 = [I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp]
    def help(self):
        system("cls")
        print("""
        -----------------------------------------
                        Commands
        - "north": Walk north a bit
        - "south": Walk south a bit
        - "east": Walk east a bit
        - "west": Walk west a bit
        - "equip": Equip an item. Case sensitive.
        - "inventory": Displays your current
        inventory.
        - "status": Displays information about
        your character.
        - "questlog": Displays your current quests
        - "changelog": Displays a list of changes
        for the current version.
        -----------------------------------------
        """)
        if self.devenabled == 1:
            print("""
            -----------------------------------------
                          Dev Commands
            - "dev1": Get into combat
            -----------------------------------------
            """)
    def drop(self):
        y = randint(0, 100)
        print(y)
        if self.status == 'questcombat':
            if self.fighting.qi is not None:
                self.inventory.append(self.fighting.qi)
                print("%s added to inventory" % self.fighting.qi.name)
                self.status = 'normal'
        else:
            if y >= 25:
                if self.fighting.dp != []:
                    x = random.choice(self.fighting.dp)
                    print("It dropped a/an %s" % x.name)
                    if x in IDB.stackablelist:
                        self.stackinv[x] += 1
                    else:
                        self.inventory.append(x)
    def renc(self):
        x = random.randint(1, 5)
        for y in self.reclist:
            if x == y.id:
                z = random.randint(1, 100)
                if z <= y.chance:
                    print (y.desc)
                    if y.enctype == "enemy":
                        self.status = 'combat'
                        self.fighting = random.choice(y.enemy)
                        self.fightform()
                    break
                else:
                    self.renc()
                    break
    def consume(self):
        self.cinventory()
        x = input("What would you like to consume?")
        for z in self.inventory:
            if x == z.name:
                self.inventory.remove(z)
                self.health += z.hh
                if self.health > self.maxhealth:
                    self.health = self.maxhealth
                print("You consumed the %s" % z.name)
                break
    def changelog(self):
        system("cls")
        print("""
        -----------------------------------------
                    Changelog v0.4A
        - New Item system fully Integrated X
        - New Enemy system fully Integrated X
        - New quest system FULLY Integrated with
        5 starter quests
        - Lots, lots and lots of new Items
        - Plenty of new enemies
        - All UI simplified and colorized
        -----------------------------------------
        """)
    def cinventory(self):
        system("cls")
        cprint("█████████████████████████████████████████", 'green')
        cprint(Style.BRIGHT + "               Inventory                 ", 'green')
        for x in self.inventory:
            cprint("- " + x.style + x.name, x.color)
        if self.gold > 0:
            cprint(Style.BRIGHT + "Gold: %d" % self.gold, 'yellow')
        if self.ammo > 0:
            print(Style.BRIGHT + "Ammo: %d" % self.ammo)
        cprint("█████████████████████████████████████████", 'green')
        cprint(Style.BRIGHT + "               Stackables                 ", 'white')
        for i in self.stackinv:
            if self.stackinv[i] > 0:
                cprint(i.style + i.name, i.color, end="")
                print(" (x" + str(self.stackinv[i]) + ")")
        cprint("█████████████████████████████████████████", 'green')
    def questlog(self):
        system("cls")
        cprint("█████████████████████████████████████████", 'yellow')
        cprint(Style.BRIGHT + "               Questlog                 ", 'yellow')
        for x in self.questlog:
            cprint("- " + x.name)
        cprint("█████████████████████████████████████████", 'yellow')
    def compquests(self):
        system("cls")
        cprint("█████████████████████████████████████████", 'blue')
        cprint(Style.BRIGHT + "               Completed Quests                 ", 'blue')
        for x in self.compquests:
            cprint("- " + x.name)
        cprint("█████████████████████████████████████████", 'blue')
    def towndisp(self):
        if self.location.bank > 0:
            w = "Bank"
        else:
            w = "There is no Bank here."
        if self.location.blacksmith != []:
            x = "Blacksmith" 
        else:
            x = "There is no Blacksmith here."
        if self.location.gunsmith != []:
            y = "Gunsmith"
        else:
            y = "There is no Gunsmith here."
        if self.location.generalstore != []:
            z = "General Store"
        else:
            z = "There is no General store here."
        print("""
        >█████████████████████████████████████<
        You are in: %s
        >█████████████████████████████████████<
         Where would you like to go?:
         %s
         %s
         %s
         %s
         Leave
        >█████████████████████████████████████<
        """ % (self.location.name, w, x, y, z))
        goto = input("> ")
        if goto == "General store":
            self.clear()
            self.genstoredisp()
        elif goto == "general store":
            self.clear()
            self.genstoredisp()
        elif goto == "General Store":
            self.clear()
            self.genstoredisp()
        elif goto == "Bank":
            self.clear()
            self.bankdisp()
        elif goto == "Gunsmith":
            self.clear()
            self.gunsmithdisp()
        elif goto == "Blacksmith":
            self.clear()
            self.blacksmithdisp()
        elif goto == "Leave":
            self.ycoord -= 1
            system("cls")
            print("You have left %s." % self.location.name)
            self.location = None
        else:
            print("Unknown option")
            system("pause")
            self.clear()
    def smeltcraft(self):
        self.clear()
        print("-------------------------------")
        print("            Smelting           ")
        print("1. Smelt")
        print("2. Check Recipes")
        print("3. Leave Crafting")
        print("-------------------------------")
        choice = input("What would you like to do?(#): ")
        if choice == '1':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in RDB.allrecipes:
                if a.type == "ingot":
                    print("- " + a.name)
            print("-------------------------------")
            whatpot = input("What would you like to smith?: ")
            for b in RDB.allrecipes:
                if b.type == "ingot":
                    if whatpot == b.name:
                        made = True
                        for i in b.ing:
                            if b.ing[i] > self.stackinv[i]:
                                made = False
                                print("You do not have the required materials...")
                                break
                        if made == True:
                            for i in b.ing:
                                self.stackinv[i] -= b.ing[i]
                            self.inventory.append(b.ic)
                            print("You created a %s" % b.ic.name)
        if choice == '2':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in RDB.allrecipes:
                if a.type == "ingot":
                    print("- " + a.name)
            print("-------------------------------")
            whatrec = input("What recipe do you want to check?: ")
            for b in RDB.allrecipes:
                if b.type == "ingot":
                    if whatrec == b.name:
                        print("This recipe requires...")
                        for i in b.ing:
                            print(i.name + " x" + str(b.ing[i]))
                        leave = input("Press any key to continue..")
                        self.alchcraft()
        if choice == '3':
            return 0
    def genstoredisp(self):
        system("cls")
        print("-----------------------------------")
        print("        %s General store           " % self.location.name)
        print("-----------------------------------")
        for x in self.location.generalstore:
            if x == self.aitem:
                continue
            else:
                print("{0} - {1} gold".format(x.name, x.bp))
        print("-----------------------------------")
        choice = input("(buy, sell, leave)> ")
        if choice == "buy":
            system("cls")
            print("-----------------------------------")
            print("        %s General store           " % self.location.name)
            print("-----------------------------------")
            for x in self.location.generalstore:
                print(x.name)
            print("-----------------------------------")
            buy = input("What would you like to buy?: ")
            for x in self.location.generalstore:
                if buy == x.name:
                    if x.bp > self.gold:
                        u = x.bp - self.gold
                        print("You need %d more gold to afford that." % u)
                        system("pause")
                        system("cls")
                        self.genstoredisp()
                    else:
                        print("You bought %s for %d gold." % (x.name, x.bp))
                        self.location.generalstore.remove(x)
                        self.inventory.append(x)
                        self.gold -= x.bp
                        system("pause")
                        system("cls")
                        self.genstoredisp()
                        break
            else:
                print("The General store does not have that item.")
                system("pause")
                system("cls")
                self.genstoredisp()
        elif choice == "sell":
            system("cls")
            print("-----------------------------------")
            print("        Your inventory             ")
            print("-----------------------------------")
            for x in self.inventory:
                print(x.name)
            print("-----------------------------------")
            sell = input("What would you like to sell?: ")
            for x in self.inventory:
                if sell == x.name:
                    if x in self.location.generalstore:
                        self.inventory.remove(x)
                        self.location.generalstore.append(x)
                        self.gold += x.sp
                        print("You sold a %s to the General store." % x.name)
                        system("pause")
                        system("cls")
                        self.genstoredisp()
                        break
                    else:
                        self.inventory.remove(x)
                        self.location.generalstore.append(x)
                        self.gold += (x.sp)
                        print("You sold a %s to the General store." % x.name)
                        self.genstoredisp()
                        break
            else:
                print("You do not have a %s" % sell)
                system("pause")
                system("cls")
                self.genstoredisp()
        elif choice == "leave":
            print("You leave the general store.")
            system("pause")
            self.clear()
            self.towndisp()
    def blacksmithdisp(self):
        system("cls")
        print("-----------------------------------")
        print("          %s Blacksmith            " % self.location.name)
        print("-----------------------------------")
        for x in self.location.blacksmith:
            if x == self.aitem:
                continue
            else:
                print("{0} - {1} gold".format(x.name, x.bp))
        print("-----------------------------------")
        choice = input("(buy, sell, craft, leave)> ")
        if choice == "buy":
            system("cls")
            print("-----------------------------------")
            print("          %s Blacksmith            " % self.location.name)
            print("-----------------------------------")
            for x in self.location.blacksmith:
                print(x.name)
            print("-----------------------------------")
            buy = input("What would you like to buy?: ")
            for x in self.location.blacksmith:
                if buy == x.name:
                    if x.bp > self.gold:
                        u = x.bp - self.gold
                        print("You need %d more gold to afford that." % u)
                        system("pause")
                        system("cls")
                        self.blacksmithdisp()
                    else:
                        print("You bought %s for %d gold." % (x.name, x.buyprice))
                        self.location.blacksmith.remove(x)
                        self.inventory.append(x)
                        self.gold -= x.bp
                        system("pause")
                        system("cls")
                        self.blacksmithdisp()
                else:
                    print("The blacksmith does not have that item.")
                    system("pause")
                    system("cls")
                    self.blacksmithdisp()
        elif choice == "sell":
            system("cls")
            print("-----------------------------------")
            print("        Your inventory             ")
            print("-----------------------------------")
            for x in self.inventory:
                print(x.name)
            print("-----------------------------------")
            sell = input("What would you like to sell?: ")
            for x in self.inventory:
                if sell == x.name:
                    if x in self.location.blacksmith:
                        self.inventory.remove(x)
                        self.location.blacksmith.append(x)
                        self.gold += x.sp
                        print("You sold a %s to the blacksmith." % x.name)
                        system("pause")
                        system("cls")
                        self.blacksmithdisp()
                        break
                    else:
                        self.inventory.remove(x)
                        self.location.blacksmith.append(x)
                        self.gold += (x.sp)
                        print("You sold a %s to the blacksmith." % x.name)
                        self.blacksmithdisp()
                        break
            else:
                print("You do not have a %s" % sell)
                system("pause")
                system("cls")
                self.blacksmithdisp()
        elif choice == "craft":
            print("(WIP)")
        elif choice == "leave":
            print("You leave the blacksmith.")
            system("pause")
            self.clear()
            self.towndisp()
    def gunsmithdisp(self):
        system("cls")
        print("-----------------------------------")
        print("           %s Gunsmith             " % self.location.name)
        print("-----------------------------------")
        for x in self.location.gunsmith:
            print("{0} - {1} gold".format(x.name, x.bp))
        print("-----------------------------------")
        choice = input("(buy, sell, leave)> ")
        if choice == "buy":
            system("cls")
            print("-----------------------------------")
            print("           %s Gunsmith             " % self.location.name)
            print("-----------------------------------")
            for x in self.location.gunsmith:
                print(x.name)
            print("-----------------------------------")
            buy = input("What would you like to buy?: ")
            for x in self.location.gunsmith:
                if buy == x.name:
                    if x.bp > self.gold:
                        u = x.bp - self.gold
                        print("You need %d more gold to afford that." % u)
                        system("pause")
                        system("cls")
                        self.gunsmithdisp()
                    else:
                        print("You bought %s for %d gold." % (x.name, x.bp))
                        self.location.gunsmith.remove(x)
                        self.inventory.append(x)
                        self.gold -= x.bp
                        system("pause")
                        system("cls")
                        self.gunsmithdisp()
                else:
                    print("The gunsmith does not have that item.")
                    system("pause")
                    system("cls")
                    self.gunsmithdisp()
        elif choice == "sell":
            system("cls")
            print("-----------------------------------")
            print("        Your inventory             ")
            print("-----------------------------------")
            for x in self.inventory:
                print(x.name)
            print("-----------------------------------")
            sell = input("What would you like to sell?: ")
            for x in self.inventory:
                if sell == x.name:
                    if x in self.location.gunsmith:
                        self.inventory.remove(x)
                        self.location.gunsmith.append(x)
                        self.gold += x.sp
                        print("You sold a %s to the gunsmith." % x.name)
                        system("pause")
                        system("cls")
                        self.gunsmithdisp()
                        break
                    else:
                        self.inventory.remove(x)
                        self.location.generalstore.append(x)
                        self.gold += (x.sp)
                        print("You sold a %s to the gunsmith." % x.name)
                        self.gunsmithdisp()
                        break
            else:
                print("You do not have a %s" % sell)
                system("pause")
                system("cls")
                self.gunsmithdisp()
        elif choice == "leave":
            print("You leave the gunsmith.")
            system("pause")
            self.clear()
            self.towndisp()
    def givenpc(self):
        self.cinventory()
        x = input("What would you like to give this npc?: ")
        for y in self.inventory:
            if x == y.name:
                if self.npc.quest.ph == 1:
                    if y.name == self.npc.quest.item.name:
                        self.inventory.remove(y)
                        self.npc.quest.itemgiven += 1
                        if self.npc.quest.itemgiven == self.npc.quest.quantity:
                            system("cls")
                            print(self.npc.quest.enddesc)
                            system("pause")
                            if self.npc.quest.gr > 0:
                                print("%d gold received" % self.npc.quest.gr)
                                self.gold += self.npc.quest.gr
                            if self.npc.quest.ir is not None:
                                self.inventory.append(self.npc.quest.ir)
                                print("%s received, added to inventory" % self.npc.quest.ir.name)
                            print("%s added to completed quests." % self.npc.quest.name)
                            self.questlog.remove(self.npc.quest)
                            self.compquests.append(self.npc.quest)
                    else:
                        print("%s does not want that." % self.npc.name)
                        system("pause")
                        system("cls")
                        self.npcmenu()
                else:
                    print("You cannot give this to %s without accepting the quest first." % self.npc.name)
    def bankdisp(self):
        self.clear()
        print("-----------------------------------")
        print("               Bank                ")
        print("-----------------------------------")
        print("You have %d gold on you." % self.gold)
        print("You have %d stored in this bank." % self.location.bankamount)
        print("-----------------------------------")
        choice = input("(deposit, withdraw, leave)> ")
        if choice == "deposit":
            if self.gold > 0:
                deposit = int(input("How much would you like to deposit?: "))
                if deposit > self.gold:
                    print("You don't have %d gold to deposit." % deposit)
                    system("pause")
                    self.clear()
                    self.bankdisp()
                else:
                    self.gold -= deposit
                    self.location.bankamount += deposit
                    print("You deposited %d gold into the bank." % deposit)
                    system("pause")
                    self.clear()
                    self.bankdisp()
            else:
                print("You have no gold to deposit.")
                system("pause")
                self.clear()
                self.bankdisp()
        elif choice == "withdraw":
            if self.location.bankamount <= 0:
                print("You have no gold deposited here.")
                system("pause")
                self.clear()
                self.bankdisp()
            else:
                withdraw = int(input("How much would you like to withdraw?: "))
                if withdraw > self.location.bankamount:
                    print("You do not have %d gold deposited here. Withdraw less." % withdraw)
                    system("pause")
                    self.clear()
                    self.bankdisp()
                else:
                    self.location.bankamount -= withdraw
                    self.gold += withdraw
                    print("You withdrew %d gold from the bank." % withdraw)
                    system("pause")
                    self.clear()
                    self.bankdisp()
        else:
            print("You leave the bank.")
            system("pause")
            self.clear()
            self.towndisp()
    def npcmenu(self):
        if not self.npc.qe:
            print("""
            ---------------------------------------
                              %s
            1. Speak
            2. Give
            """ % self.npc.name)
            x = input("What would you like to do?: ")
        else:
            print("""
            ---------------------------------------
                              %s
            1. Speak
            2. Give
            3. Quest
            """ % self.npc.name)
            x = input("What would you like to do?: ")
        if x == "Speak":
            y = 0
            for z in self.npc.dialog:
                system("cls")
                print("----------------------------------------------")
                print("                       %s                     " % self.npc.name)
                print("%s" % self.npc.dialog[y].dialog)
                print("----------------------------------------------")
                input("Press a key to continue.")
                y += 1
            self.npc.qe = True
            system("cls")
            self.npcmenu()
        elif x == "Quest":
            if not self.npc.qe:
                print("You have to speak to this person before you can possibly recieve a quest from them.")
                system("pause")
                system("cls")
                self.npcmenu()
            else:
                self.npc.quest.ph = 1
                print(self.npc.quest.desc)
                self.questlog.append(self.npc.quest)
                print("%s added to questlog" % self.npc.quest.name)
        elif x == "Give":
            self.givenpc()
    def cquests(self):
        system("cls")
        print("-----------------------------------------")
        print("               Quest Log                 ")
        for y in self.questlog:
            print(y.name)
        print("-----------------------------------------")
    def gonorth(self):
        self.ycoord += 1
        print("You travel north a bit.")
        for x in self.towns:
            if self.xcoord == x.x:
                if self.ycoord == x.y:
                    print("You have reached %s" % x.name)
                    self.location = x
                    system("pause")
                    self.clear()
                    self.towndisp()
        for y in NDB.allnpcs:
            if self.xcoord == y.xc:
                if self.ycoord == y.yc:
                    self.npc = y
                    print("You come across a person named %s" % y.name)
                    input("Press a key to continue.")
                    system('cls')
                    self.npcmenu()
    def goeast(self):
        self.xcoord += 1
        print("You travel east a bit.")
        for x in self.towns:
            if self.xcoord == x.x:
                if self.ycoord == x.y:
                    print("You have reached %s" % x.name)
                    self.location = x
                    system("pause")
                    self.clear()
                    self.towndisp()
        for y in NDB.allnpcs:
            if self.xcoord == y.xc:
                if self.ycoord == y.yc:
                    self.npc = y
                    print("You come across a person named %s" % y.name)
                    input("Press a key to continue.")
                    system('cls')
                    self.npcmenu()

        for y in E.qenemylist:
            if self.xcoord == y.xc:
                if self.ycoord == y.yc:
                    if y.quest in self.questlog:
                        self.status = 'questcombat'
                        self.fighting = y
                        self.fightdisp()
                        self.fightform()
    def gosouth(self):
        self.ycoord -= 1
        print("You travel south a bit.")
        for x in self.towns:
            if self.xcoord == x.x:
                if self.ycoord == x.y:
                    print("You have reached %s" % x.name)
                    self.location = x
                    system("pause")
                    self.clear()
                    self.towndisp()
    def gowest(self):
        self.xcoord -= 1
        print("You travel west a bit.")
        for x in self.towns:
            if self.xcoord == x.x:
                if self.ycoord == x.y:
                    print("You have reached %s" % x.name)
                    self.location = x
                    system("pause")
                    self.clear()
                    self.towndisp()
        for y in NDB.allnpcs:
            if self.xcoord == y.xc:
                if self.ycoord == y.yc:
                    self.npc = y
                    print("You come across a person named %s" % y.name)
                    input("Press a key to continue.")
                    system('cls')
                    self.npcmenu()
    def bscraft(self):
        self.clear()
        print("-------------------------------")
        print("          Blacksmithing        ")
        print("1. Craft")
        print("2. Check Recipes")
        print("3. Leave Crafting")
        print("-------------------------------")
        choice = input("What would you like to do?(#): ")
        if choice == '1':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in self.bsrec:
                print("- " + a.name)
            print("-------------------------------")
            whatpot = input("What would you like to smith?: ")
            for b in self.bsrec:
                if whatpot == b.name:
                    made = True
                    for i in b.ing:
                        if b.ing[i] > self.stackinv[i]:
                            made = False
                            print("You do not have the required materials...")
                            break
                    if made == True:
                        for i in b.ing:
                            self.stackinv[i] -= b.ing[i]
                        self.inventory.append(b.ic)
                        print("You created a %s" % b.ic.name)
        if choice == '2':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in self.gsrec:
                print("- " + a.name)
            print("-------------------------------")
            whatrec = input("What recipe do you want to check?: ")
            for b in self.gsrec:
                if whatrec == b.name:
                    print("This recipe requires...")
                    for i in b.ing:
                        print(i.name + " x" + str(b.ing[i]))
                    leave = input("Press any key to continue..")
                    self.alchcraft()
        if choice == '3':
            return 0
    def gscraft(self):
        self.clear()
        print("-------------------------------")
        print("           Gunsmithing         ")
        print("1. Craft")
        print("2. Check Recipes")
        print("3. Leave Crafting")
        print("-------------------------------")
        choice = input("What would you like to do?(#): ")
        if choice == '1':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in self.gsrec:
                print("- " + a.name)
            print("-------------------------------")
            whatpot = input("What would you like to smith?: ")
            for b in self.gsrec:
                if whatpot == b.name:
                    made = True
                    for i in b.ing:
                        if b.ing[i] > self.stackinv[i]:
                            made = False
                            print("You do not have the required materials...")
                            break
                    if made == True:
                        for i in b.ing:
                            self.stackinv[i] -= b.ing[i]
                        self.inventory.append(b.ic)
                        print("You created a %s" % b.ic.name)
        if choice == '2':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in self.gsrec:
                print("- " + a.name)
            print("-------------------------------")
            whatrec = input("What recipe do you want to check?: ")
            for b in self.gsrec:
                if whatrec == b.name:
                    print("This recipe requires...")
                    for i in b.ing:
                        print(i.name + " x" + str(b.ing[i]))
                    leave = input("Press any key to continue..")
                    self.alchcraft()
        if choice == '3':
            return 0
    def alchcraft(self):
        self.clear()
        print("-------------------------------")
        print("            Alchemy            ")
        print("1. Craft")
        print("2. Check Recipes")
        print("3. Leave Crafting")
        print("-------------------------------")
        choice = input("What would you like to do?(#): ")
        if choice == '1':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in self.alchrec:
                print("- " + a.name)
            print("-------------------------------")
            whatpot = input("What potion would you like to craft?: ")
            for b in RDB.allrecipes:
                if whatpot == b.name:
                    made = True
                    for i in b.ing:
                        if b.ing[i] > self.stackinv[i]:
                            made = False
                            print("You do not have the required ingredients...")
                            break
                    if made == True:
                        for i in b.ing:
                            self.stackinv[i] -= b.ing[i]
                        self.inventory.append(b.ic)
                        print("You created a %s" % b.ic.name)
        if choice == '2':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in self.alchrec:
                print("- " + a.name)
            print("-------------------------------")
            whatrec = input("What recipe do you want to check?: ")
            for b in self.alchrec:
                if whatrec == b.name:
                    print("This recipe requires...")
                    for i in b.ing:
                        print(i.name + " x" + str(b.ing[i]))
                    leave = input("Press any key to continue..")
                    self.alchcraft()
        if choice == '3':
            return 0
    def createrandomitem(self):
        x = item("","", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None, 0)
    def equip(self):
        self.cinventory()
        equip = input("What would you like to equip?: ")
        for x in self.inventory:
            if equip == x.name:
                if x.type == "mwep":
                    if self.ms != None:
                        self.inventory.append(self.ms)
                        cprint("Removed the " + self.ms.style + self.ms.name, self.ms.color)
                        self.damage = 0
                    self.inventory.remove(x)
                    self.ms = x
                    cprint("Equipped the " + self.ms.style + self.ms.name, self.ms.color)
                    self.damage = self.ms.damage
                    break
                if x.type == "rwep":
                    if self.rs != None:
                        self.inventory.append(self.rs)
                        cprint("Removed the " + self.rs.style + self.rs.name, self.rs.color)
                        self.gundamage = 0
                    self.inventory.remove(x)
                    self.rs = x
                    cprint("Equipped the " + self.rs.style + self.rs.name, self.rs.color)
                    self.gundamage = self.rs.damage
                    break
                if x.type == "helm":
                    if self.hs != None:
                        self.inventory.append(self.hs)
                        cprint("Removed the " + self.hs.style + self.hs.name, self.hs.color)
                        self.defence -= self.hs.defence
                        self.maxhealth -= self.hs.health
                    self.inventory.remove(x)
                    self.hs = x
                    cprint("Equipped the " + self.hs.style + self.hs.name, self.hs.color)
                    self.defence += x.defence
                    self.maxhealth += x.health
                    break
                if x.type == "chest":
                    if self.cs != None:
                        self.inventory.append(self.cs)
                        cprint("Removed the " + self.cs.style + self.cs.name, self.cs.color)
                        self.defence -= self.cs.defence
                        self.maxhealth -= self.cs.health
                    self.inventory.remove(x)
                    self.cs = x
                    cprint("Equipped the " + self.cs.style + self.cs.name, self.cs.color)
                    self.defence += x.defence
                    self.maxhealth += x.health
                    break
                if x.type == "legs":
                    if self.ps != None:
                        self.inventory.append(self.ps)
                        cprint("Removed the " + self.ps.style + self.ps.name, self.ps.color)
                        self.defence -= self.ps.defence
                        self.maxhealth -= self.ps.health
                    self.inventory.remove(x)
                    self.ps = x
                    cprint("Equipped the " + self.ps.style + self.ps.name, self.ps.color)
                    self.defence += x.defence
                    self.maxhealth += x.health
                    break
                if x.type == "foot":
                    if self.fs != None:
                        self.inventory.append(self.fs)
                        cprint("Removed the " + self.fs.style + self.fs.name, self.fs.color)
                        self.defence -= self.fs.defence
                        self.maxhealth -= self.fs.health
                    self.inventory.remove(x)
                    self.fs = x
                    self.defence += x.defence
                    self.maxhealth += x.health
                    cprint("Equipped the " + self.fs.style + self.fs.name, self.fs.color)
                    break
    def dev2(self):
        self.status = 'combat'
        self.fighting = self.bban
        self.fightdisp()
        self.fightform()
    def status(self):
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("               Character                 ")
        print("Health: %d" % self.health)
        print("Gold: %d" % self.gold)
        print("Range Damage: %s" % self.gundamage)
        print("Damage: %d" % self.damage)
        print("Defence: %d" % self.defence)
        for x in self.inventory:
            if x.type == 'map':
                print("X Coordinate - %d" % self.xcoord)
                print("Y Coordinate - %d" % self.ycoord)
                break
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("               Equipment                 ")
        if self.rs != None:
            cprint(self.rs.style + "Gun: %s" % self.rs.name, self.rs.color)
        else:
            print("Gun: Empty Slot")
        if self.ms != None:
            cprint(self.ms.style + "Weapon: %s" % self.ms.name, self.ms.color)
        else:
            print("Weapon: Empty Slot")
        if self.hs != None:
            cprint(self.hs.style + "Head: %s" % self.hs.name, self.hs.color)
        else:
            print("Head: Empty Slot")
        if self.cs != None:
            cprint(self.cs.style + "Torso: %s" % self.cs.name, self.cs.color)
        else:
            print("Torso: Empty Slot")
        if self.ps != None:
            cprint(self.ps.style + "Legs: %s" % self.ps.name, self.ps.color)
        else:
            print("Legs: Empty Slot")
        if self.fs != None:
            cprint(self.fs.style + "Feet: %s" % self.fs.name, self.fs.color)
        else:
            print("Feet: Empty Slot")
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    def dev1(self):
        self.status = 'combat'
        fight = random.randint(999, 1002)
        for x in self.enemylist:
            if fight == x.id:
                self.fighting = x
        self.fightform()
    def enabledev(self):
        self.devenabled = 1
    def disabledev(self):
        self.devenabled = 0
    def battleplayerturn(self):
        system("cls")
        self.battledisp()
        pbchoice = input("> ")
        if pbchoice == 2:
            if self.yardsaway == 10:
                cc = input("You are only 10 yards away from the enemy company. Would you like to melee charge instead?(Y/N): ")
                if cc == "Y":
                    print("NRY")
                else:
                    print("Choose a different action.")
                    system("pause")
                    system("cls")
                    self.battleplayerturn()
            else:
                self.yardsaway -= 10
                print("Your company advances 10 yards.")
                system("pause")
                self.battlenemyturn()
        elif pbchoice == 1:
            if self.yardsaway > self.cr:
                print("Your company fires, but is out of range to hit any enemies.")
            else:
                return 0
    def battleenemyturn(self):
        print("NRY")
        system("pause")
        self.battleplayerturn()
    def battledisp(self):
        if self.aa == 0:
            self.aas = "They have the accuracy advantage"
        else:
            self.aas = "You have the accuracy advantage"
        if self.battling != None:
            print("""
            =======
            Battle
            =======
            Your company is %d yards away
            from the enemy.
            -------------------------------
            %s
            -------------------------------
            What would you like to do? (Choose a number)
            1. Fire
            2. Advance ten yards
            3. Fall back ten yards
            4. Retreat
            5. Battle Info
            -------------------------------

            """ % (self.yardsaway, self.aas))
    def battleform(self):
        return 0
    def combatplayerturn(self):
        if self.damage < self.fighting.defence:
            fhit = randint(1, (self.health + 5))
            print("You cannot harm the %s. You flee, but the %s hits you for %d while you ran!" % (self.fighting.name, self.fighting.name, fhit))
            self.health -= fhit
        else:
            phit = randint(0, 10 + (self.damage - self.fighting.defence))
            if phit == 0:
                self.playerhit = ("Your hit was deflected by " + self.fighting.name + "'s armor!")
                system("cls")
                self.combatenemyturn()
            elif phit >= self.fighting.health:
                print("You killed the %s!" % self.fighting.name)
                self.drop()
                self.playerhit = ""
                self.enemyhit = ""
                self.fighting.health = self.fighting.health
                self.fighting = None
                self.status = 'normal'
            else:
                self.playerhit = ("You hit the %s for %d" % (self.fighting.name, phit))
                self.fighting.health -= phit
                system("cls")
                self.combatenemyturn()
    def combatenemyturn(self):
        if self.shot == 1:
            if self.reloading > 0:
                self.reloading -= 1
            else:
                self.shot = 0
        if (self.defence - self.fighting.damage > 50):
            print("The %s is too scared to fight you, and runs away." % self.fighting.name)
            self.fighting = None
            self.status = 'normal'
        elif (self.fighting.damage - self.defence) <= 0:
            if self.health == 1:
                self.enemyhit = ("The %s is not powerful enough to deliver a finishing blow. Keep fighting!" % self.fighting.name)
            else:
                self.health -= 1
                self.enemyhit = ("The %s hit you for 1" % self.fighting.name)
            if self.fighting != None:
                system("cls")
                self.fightdisp()
                self.fightform()
        else:
            if self.fighting.hasgun == 0:
                ehit = randint(0, 10 + (self.fighting.damage - self.defence))
                if ehit <= 2:
                    self.enemyhit = ("The %s missed!" % self.fighting.name)
                    system("cls")
                    self.fightdisp()
                    self.fightform()
                elif ehit >= self.health:
                    system("cls")
                    print("The %s killed you! Exiting." % self.fighting.name)
                    self.fighting = None
                    system("pause")
                    system('exit')
                    self.health = 0
                    self.health = 0
                else:
                    z = randint(0, (self.defence * 2) + 1)
                    if z <= self.defence / 2:
                        self.enemyhit = ("The %s hit but your armor deflected it." % self.fighting.name)
                    else:
                        self.enemyhit = ("The %s hit you for %d." % (self.fighting.name, ehit))
                        self.health -= ehit
            else:
                eshoot = randint(0, 100)
                if eshoot >= 75:
                    cosh = randint(0, 100)
                    if cosh >= 50:
                        ehit = randint(1, self.fighting.damage * 5)
                        if ehit >= self.health:
                            print("The %s shot, and killed you. Exiting." % self.fighting.name)
                            system("pause")
                            system("exit")
                            self.health = 0
                        else:
                            self.enemyhit = "The %s shot you, and did %d damage." % (self.fighting.name, ehit)
                            self.health -= ehit
                    else:
                        self.enemyhit = "The %s shot at you, but missed!" % self.fighting.name
                else:
                    ehit = randint(0, 10 + (self.fighting.damage - self.defence))
                    if ehit == 0:
                        self.enemyhit = ("The %s missed!" % self.fighting.name)
                        system("cls")
                        self.fightdisp()
                        self.fightform()
                    elif ehit >= self.health:
                        system("cls")
                        print("The %s killed you! Exiting." % self.fighting.name)
                        system("pause")
                        self.health = 0
                        self.health = 0
                    else:
                        z = randint(0, (self.defence * 2) + 1)
                        if z > self.defence / 2:
                            self.enemyhit = ("The %s hit but your armor deflected it." % self.fighting.name)
                        else:
                            self.enemyhit = ("The %s hit you for %d." % (self.fighting.name, ehit))
                            self.health -= ehit
            if self.fighting != None:
                system("cls")
                self.fightdisp()
                self.fightform()
    def save(self):
        save = input("What would you like to name the save?(This will overwrite): ")
        pickle.dump([self.stackinv, self.maxhealth, self.inventory, self.norag, self.gabesh, self.yoeran, self.litau, self.uash, self.shreeda, self.questlog, self.compquests, self.name, self.health, self.xcoord, self.ycoord, self.rs, self.ms, self.hs, self.cs, self.ps, self.fs, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.gold, self.devenabled], open("{0}.tin".format(save), "wb"))
    def devsave(self):
        pickle.dump([self.eitemslist, self.inventory, self.norag, self.gabesh, self.yoeran, self.litau, self.uash, self.shreeda, self.sq1, self.sq2, self.questlog, self.compquests, self.name, self.health, self.xcoord, self.ycoord, self.gslot, self.mslot, self.headslot, self.chestslot, self.legslot, self.footslot, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.devenabled], open("devsave.tin", "wb"))
    def devload(self):
        self.eitemslist, self.inventory, self.norag, self.gabesh, self.yoeran, self.litau, self.uash, self.shreeda, self.sq1, self.sq2, self.questlog, self.compquests, self.name, self.health, self.xcoord, self.ycoord, self.gslot, self.mslot, self.headslot, self.chestslot, self.legslot, self.footslot, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.devenabled = pickle.load(open("devsave.tin", "rb"))
    def loadt(self):
        load = input("What file would you like to load(Doesn't exist = Crash): ")
        self.stackinv, self.maxhealth, self.inventory, self.norag, self.gabesh, self.yoeran, self.litau, self.uash, self.shreeda, self.questlog, self.compquests, self.name, self.health, self.xcoord, self.ycoord, self.rs, self.ms, self.hs, self.cs, self.ps, self.fs, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.gold, self.devenabled = pickle.load(open("{0}.tin".format(load), "rb"))
    def dev4(self):
        self.fighting = self.wban
        self.status = 'combat'
        self.fightdisp()
        self.fightform()
    def playershoot(self):
        if self.reloading == 0:
            self.shot = 1
            self.reloading = 3
            self.ammo -= 1
            x = randint(0, self.gslot.accuracy)
            if x > (self.gslot.accuracy / 2):
                y = randint(self.gslot.damage / 2, self.gslot.damage)
                self.fighting.health -= y
                self.playerhit = "You shot and hit the %s for %d" % (self.fighting.name, y)
                if self.fighting.health <= 0:
                    print("You killed the %s!" % self.fighting.name)
                    self.fighting.health = randint(40, self.fighting.maxhealth)
                    self.fighting = None
                    self.status = 'normal'
                else:
                    self.combatenemyturn()
            else:
                self.playerhit = "You shot, and missed!"
                self.combatenemyturn()
        else:
            self.playerhit = "You cannot shoot, you are currently reloading."
            self.combatenemyturn()
    def dev3(self):
        self.mslot = self.ironsword
        self.damage = self.ironsword.damage
        self.inventory = []
        self.headslot = self.clothcap
        self.chestslot = self.leathertunic
        self.legslot = self.clothpants
        self.footslot = self.ruggedshoes
        print("Tutorial Quest #1 Completed! Added it to the completed quests log. Next quest Added.")
        self.questlog.remove(self.sq1)
        self.questlog.append(self.sq2)
        system("cls")
        print(self.sq2.desc)
        system("pause")
        self.fighting = self.fban
        self.fightdisp()
        self.fightform()
    def bossdisp(self):
        if self.fighting != None:
            cprint("█████████████████████████████████████████", 'red')
            cprint(self.fighting.style + self.fighting.name, self.fighting.color)
            print("%s's Health: %d" % (self.fighting.name, self.fighting.health))
            print("Your Health: %d" % self.health)
            cprint("> %s" % self.playerhit, 'green')
            cprint("> %s" % self.enemyhit, 'red')
            cprint("█████████████████████████████████████████", 'red')
    def bossfight(self):
        if self.rs != None:
            cc = input("Type 'a' to attack or 's' to shoot:")
        else:
            cc = input("Type 'a' to attack, c to consume a potion or food, f to flee:")
        if cc == 'a':
            self.combatplayerturn()
        elif cc == 'c':
            self.cinventory()
            x = input("What would you like to consume?")
            for z in self.inventory:
                if x == z.name:
                    self.inventory.remove(z)
                    self.health += z.hh
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    print("You consumed the %s" % z.name)
                    break
            self.fightdisp()
            self.fightform()
        elif cc == 's':
            if self.rs == None:
                self.playerhit = "You cannot shoot without a gun."
                self.fightdisp()
                self.fightform()
            else:
                self.playershoot()
        else:
            system("cls")
            print("Unknown command.")
            self.fightdisp()
            self.fightform()
    def bossfightplayer(self):
        return 0
    def bossfightboss(self):
        return 0
    def fightdisp(self):
        if self.fighting != None:
            cprint("█████████████████████████████████████████", 'red')
            print("                Combat")
            print("%s's Health: %d" % (self.fighting.name, self.fighting.health))
            print("Your Health: %d" % self.health)
            cprint("> %s" % self.playerhit, 'green')
            cprint("> %s" % self.enemyhit, 'red')
            cprint("█████████████████████████████████████████", 'red')







            #print("""
            #-----------------------------------------
            #                Combat
            #%s's Health: %d
            #Your health: %d
            #> %s
            #> %s
           # -----------------------------------------
            #""" % (self.fighting.name, self.fighting.health, self.health, self.playerhit, self.enemyhit))
    def fightform(self):
        if self.rs != None:
            cc = input("Type 'a' to attack or 's' to shoot:")
        else:
            cc = input("Type 'a' to attack, c to consume a potion or food, f to flee:")
        if cc == 'a':
            self.combatplayerturn()
        elif cc == 'c':
            self.cinventory()
            x = input("What would you like to consume?")
            for z in self.inventory:
                if x == z.name:
                    self.inventory.remove(z)
                    self.health += z.hh
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    print("You consumed the %s" % z.name)
                    break
            self.fightdisp()
            self.fightform()
        elif cc == 's':
            if self.rs == None:
                self.playerhit = "You cannot shoot without a gun."
                self.fightdisp()
                self.fightform()
            else:
                self.playershoot()
        else:
            system("cls")
            print("Unknown command.")
            self.fightdisp()
            self.fightform()
    def map(self):
        for x in self.inventory:
            if x.type == 'map':
                print("""
                ------------------------------------------
                Major Locations:
                ---------------------------
                Norag - X16, Y-11
                Gabesh - X6, Y12
                Yoeran - X4, Y16
                Litau - X30, Y-55
                Uash - X33, Y-4
                Shreeda - X11, Y27
                ------------------------------------------             
                """)
    def talkto(self):
        for y in NDB.allnpcs:
            if self.xcoord == y.xc:
                if self.ycoord == y.yc:
                    self.npc = y
                    print("You approach %s" % y.name)
                    input("Press a key to continue.")
                    system('cls')
                    self.npcmenu()
                else:
                    print("There is no one here for you to talk to.")
            else:
                print("There is no one here for you to talk to.")
    def clear(self):
        system("cls")
    def devmenu(self):
        print("""
        --------------------------------------
        Dev Menu
        1. Kits
        2. Get Item
        3. Fight an enemy
        4. Go to developer town
        5. Set custom health
        6. Alchemy Menu
        7. Blacksmithing Menu
        8. Smelting Menu helloooooo
        --------------------------------------
        """)
        choice = input("Type the number: ")
        if choice == '1':
            kitc = input("Which kit would you like?(1 is starter items, 2 is high end items, 3 is large health pots): ")
            if kitc == '1':
                for x in self.dkit1:
                    self.inventory.append(x)
            elif kitc == '2':
                for y in self.dkit2:
                    self.inventory.append(y)
            elif kitc == '3':
                for z in self.dkit3:
                    self.inventory.append(z)
        elif choice == '2':
            self.clear()
            self.dev7()
        elif choice == '3':
            self.clear()
            self.dev8()
        elif choice == '4':
            self.devt()
        elif choice == '5':
            self.clear()
            self.dev11()
        elif choice == '6':
            self.alchcraft()
        elif choice == '7':
            self.bscraft()
        elif choice == '8':
            self.smeltcraft()
    def dev6(self):
        self.health = 20000
        cprint(self.clothcap.name, self.clothcap.color)
    def dev7(self):
        itemtg = input("What item to get?: ")
        for x in I.itemlist:
            if itemtg == x.name:
                if x in IDB.stackablelist:
                    self.stackinv[x] += 1
                else:
                    self.inventory.append(x)
    def dev8(self):
        x = input("What do you want to fight? ")
        for z in E.enemylist:
            if x == z.name:
                self.fighting = enemy(z.name, z.minhealth, randint(z.minhealth, z.maxhealth), z.maxhealth, z.damage, z.defence, z.hasgun, z.dp, z.id)
                break
        self.status = 'combat'
        self.fightdisp()
        self.fightform()
    def dev10(self):
        self.fighting = E.mugger
        self.status = 'combat'
        self.fightdisp()
        self.fightform()
    def dev11(self):
        health = int(input("What would you want your health set at?: "))
        self.health = health
    def dev12(self):
        print(self.maxhealth)
    def dev13(self):
        self.fighting = E.morkool
        self.bossdisp()
    def dev9(self):
        x = int(input("What would you like to set your defence to?: "))
        self.defence = x
    def showc(self):
        print("X: %d, Y: %d" % (self.xcoord, self.ycoord))
    def readtest(self):
        file = open("config.txt", "r")
        print (file.read(10))
    def devt(self):
        print("You magically teleported to developer town")
        system("pause")
        self.clear()
        self.location = self.devtown
        self.towndisp()
Commands = {
  'readtest': Main.readtest,
  'help': Main.help,
  'inventory': Main.cinventory,
  'north': Main.gonorth,
  'east': Main.goeast,
  'south': Main.gosouth,
  'west': Main.gowest,
  'equip': Main.equip,
  'status': Main.status,
  'clear': Main.clear,
  'dev1': Main.dev1,
  'devt': Main.devt,
  'dev2': Main.dev2,
  'dev3': Main.dev3,
  'changelog': Main.changelog,
  '20657': Main.enabledev,
  'ddev': Main.disabledev,
  'save': Main.save,
  'loadt': Main.loadt,
  'testload': Main.loadt,
  'dev4': Main.dev4,
  'speak': Main.talkto,
  'dev5': Main.drop,
  'dev6': Main.dev6,
  'devsave': Main.devsave,
  'devload': Main.devload,
  'dev7': Main.dev7,
  'dev8': Main.dev8,
  'dev9': Main.dev9,
  'dev10': Main.dev10,
  'dev11': Main.dev11,
  'dev12': Main.dev12,
  'dev13': Main.dev13,
  'eat': Main.consume,
  'drink': Main.consume,
  'showc': Main.showc,
  'questlog': Main.questlog,
  'completed quests': Main.compquests,
  '0': Main.devmenu,
  'map': Main.map,
  }

p = Main()
print ("""
----------------------------------------
          The Time is Now v0.4
1. New game
2. Load game
3. About
----------------------------------------
""")
menuchoice = input("Type the number: ")
if menuchoice == "1":
    p.name = input("What is your name? ")
    print("%s wakes up in the middle of a forest. Try to get to civilization" % p.name)
    print("(type help to get a list of actions)")
    if p.name == "Developer":
        p.defence = 30
    else:
        p.defence = 0
elif menuchoice == "2":
    p.loadt()
elif menuchoice == "3":
    print("""
    --------------------------------------------
                        About
    'The Time is Now' is built off of a
    very simple base for a text adventure
    found on www.balau82.wordpress.com. All
    credit for the base code goes to Francesco
    Balducci. The base has been heavily modified
    and converted to work with Python 3, all
    other credit goes to Shane Fales
    --------------------------------------------
    """)
elif menuchoice == "6":
    p.devload()
else:
    print("Wrong command typed")
while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print("Command not found")
