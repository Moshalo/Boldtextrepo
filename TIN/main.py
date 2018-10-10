from random import randint, randrange
import random
from os import system
import sys
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style
from item import *
from location import townDB as TDB
from location import dynlDB as dynlDB
from location import biomeDB as bDB
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
from scroll import ScrollDB as SDB
from armor import armor as a
import time
from misc import misc as m
import pickle
class Main():
    def __init__(self):
        #Character
        system("title Time is now v0.5.1")
        self.name = ""
        self.health = 100
        self.maxhealth = 100
        self.xpos = 16
        self.ypos = 8
        self.rs = None
        self.ms= None
        self.hs = None
        self.cs = I.clothshirt
        self.ps = I.clothpants
        self.fs = I.ruggedshoes
        self.location = None
        self.npc = None
        self.damage = 0
        self.gundamage = 0
        self.shot = 0
        self.reloading = 0
        self.defence = 5
        self.status = 'normal'
        self.fighting = None
        self.battling = None
        self.playerhit = ""
        self.enemyhit = ""
        self.cdid = 99
        self.devenabled = 1
        self.ammo = 0
        self.devdropvar = 0
        #CharacterStats(WIP)
        self.statswords = 1
        self.statblock = 1
        self.statdodge = 1
        #CharacterSkills(
        self.skillblacksmith = 1
        self.skillgunsmith = 1
        self.skillfishing = 1
        self.skillleatherwork = 1
        self.skillbuilding = 1
        self.skillmining = 1
        self.skillforaging = 1
        self.skillhunting = 1
        self.skillcooking = 1
        self.skillalch = 1
        #CharacterSkillsEXP
        self.xpblacksmith = 0
        self.xpblacksmithnext = 5
        self.xpgunsmith = 0
        self.xpgunsmithnext = 5
        self.xpfishing = 0
        self.xpfishingnext = 10
        self.xpleatherwork = 0
        self.xpleatherworknext = 5
        self.xpbuilding = 0
        self.xpbuildingnext = 50
        self.xpmining = 0
        self.xpminingnext = 10
        self.xpforaging = 0
        self.xpforagingnext = 10
        self.xphunting = 0
        self.xphuntingnext = 10
        self.xpcooking = 0
        self.xpcookingnext = 5
        self.xpalch = 0
        self.xpalchnext = 5
        #QUESTS
        self.questlog = []
        self.compquests = []
        self.test = []
        #Crafting Recipes known
        self.alchrec = [RDB.nhpr, RDB.spoison]
        self.bsrec = [RDB.ironsword]
        self.gsrec = []
        self.consrec = []
        self.asrec = []
        self.cookrec = []
        #Admin Item USED FOR TOWNS TO SHOW AN EMPTY INVENTORY
        self.aitem = item("34y6y734577562735723", "admin", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'white', Style.DIM, 666)
        #Inventory
        self.gold = 0
        #Townstuffs/
        self.inventory = [I.irondagger]
        self.wallet = {
            I.goldpiece: 10
        }
        self.stackinv = {
            I.aethdust: 0,
            I.centhorn: 0,
            I.wolfpelt: 0,
            I.bottlewater: 3,
            I.salt: 3,
            I.potatoweed: 0,
            I.wberries: 6,
            I.coal: 3,
            I.ironore: 0,
            I.ironingot: 1,
            I.woodrod: 1,
            I.sharpcanine: 0,
            I.broketooth: 0,
        }
        #self.inventory = [I.bread, I.ironsword, I.ironlsword, I.leathertunic, I.steelsword, I.steellsword, I.leathcolbp, I.bsteelsword, I.bsteellsword, I.disasterblade, I.sfsword,
                         #I.bladeofeternity, I.aetherialhelm, I.aetherialcp, I.aetheriallp, I.aetherialwraps, I.gsofkings, I.mkwarhammer]
        # Developer item kits (REMOVE IN FINAL RELEASE)
        self.dkit1 = [I.ironsword, I.clothcap, I.leathertunic, I.clothpants, I.ruggedshoes]
        self.dkit2 = [I.bread, I.ironsword, I.ironlsword, I.leathertunic, I.steelsword, I.steellsword, I.leathcolbp, I.bsteelsword, I.bsteellsword, I.disasterblade, I.sfsword,
                         I.bladeofeternity, I.aetherialhelm, I.aetherialcp, I.aetheriallp, I.aetherialwraps, I.gsofkings, I.mkwarhammer]
        self.dkit3 = [I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp, I.largehp]
        #WORLDSPACE(TESTING)
        # GRID X             0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43
        self.worldspace = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 7, 0, 8, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 13, 14, 15, 16, 17, 18, 19, 0, 20, 21, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 24, 0, 25, 26, 27, 28, 29, 30, 31, 32, 0, 33, 34, 0, 0, 35, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8DONE!!
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 0, 0, 0, 48, 49, 50, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 0, 0, 63, 64, 65, 66, 67, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 130, 131, 132, 133, 134, 135, 136, 137, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 162, 0, 0, 0, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 186, 187, 188, 0, 189, 0, 0, 0, 0, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 0, 208, 0, 0, 0, 0, 0, 0, 0],  # 16DONE
            [0, 0, 0, 0, 0, 0, 0, 209, 210, 211, 212, 0, 0, 0, 213, 214, 215, 0, 0, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 0, 232, 233, 0, 0, 0, 0, 0],  # 17DONE
            [0, 0, 0, 0, 0, 0, 0, 234, 235, 236, 0, 0, 0, 237, 238, 239, 240, 241, 0, 0, 0, 0, 0, 0, 0, 242, 243, 244, 245, 246, 247, 248, 249, 250, 0, 251, 252, 253, 0, 0, 0, 0, 0, 0],  # 18DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 0, 0, 266, 267, 268, 269, 270, 271, 272, 273, 274, 0, 275, 276, 277, 278, 0, 0, 0, 0, 0],  # 19DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 0, 294, 295, 296, 297, 298, 299, 300, 301, 302, 0, 0, 0, 303, 304, 0, 0, 0, 0, 0],  # 20DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 0, 0, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 0, 0, 0, 0, 0, 0, 0],  # 21DONE
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 0, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 0, 0, 0, 0, 0, 0, 0],  # 22
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 0, 0, 0, 0, 0, 0, 0],  # 23
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 0, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 0, 0, 0, 0, 0, 0, 0],  # 24
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 25
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0, 0, 30, 31, 32, 33, 34, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 26
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 0, 31, 32, 33, 34, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 27
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 11, 0, 0, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 0, 31, 32, 33, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 28
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 0, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 0, 31, 32, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 29
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 0, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 30
            [0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 0, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 0, 0, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 31
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 11, 12, 0, 14, 15, 16, 17, 18, 19, 20, 21, 0, 0, 24, 25, 0, 0, 0, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 32
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 14, 15, 16, 17, 18, 19, 20, 21, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 33
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 16, 17, 18, 19, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 34
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 16, 0, 18, 0, 0, 21, 22, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 35
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 21, 22, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 36
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 21, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 37
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 38
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 39
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 40
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 41
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 42
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]  # 43
        self.wolfdt = [
            {'item': I.wolfpelt, 'minqty': 1, 'maxqty': 2, 'dc': 100},
            {'item': I.sharpcanine, 'minqty': 1, 'maxqty': 5, 'dc': 85},
            {'item': I.broketooth, 'minqty': 1, 'maxqty': 10, 'dc': 90},
            {'item': I.disasterblade, 'minqty': 1, 'maxqty': 1, 'dc': 25}
        ]
    def clearinv(self):
        x = input("Do you really want to clear the inventory?(Y/N): ").upper()
        if x == "Y":
            self.inventory = []
        elif x == "N":
            print('Canceled inventory clear')
        else:
            x = input("You didn't type Y or N")
            self.clearinv()
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
        - "search": Search the area you're in
        - "examine": Examine an item from the inventory
        -----------------------------------------
                        Information
        - When you go in a certain direction
        (north, east, south, west) it's 1 'pace'.
        NPC's will refer to it as a pace, so just remember
        that.
        """)
        if self.devenabled == 1:
            print("""
            -----------------------------------------
                          Dev Commands
            - "dev1": Get into combat
            -----------------------------------------
            """)
    def search(self):
        for x in dynlDB.pointsofinterest:
            if x.pos == self.worldspace[self.ypos][self.xpos]:
                if x.items == []:
                    print("You found no items of interest in the area..")
                else:
                    print(x.foundlootdesc)
                    for y in x.items:
                        x.items.remove(y)
                        self.inventory.append(y)
                        print(y.name + " added to inventory.")
    def drop(self):
        if self.status == 'questcombat':
            if self.fighting.qi is not None:
                self.inventory.append(self.fighting.qi)
                print("%s added to inventory" % self.fighting.qi.name)
                self.status = 'normal'

        for d in self.fighting.dp:
            for key in d:
                if key == 'dc':
                    y = random.randint(0, 100)
                    if y <= d['dc']:
                        x = random.randint(d['minqty'], d['maxqty'])
                        print("Dropped " + str(x) + " " + d['item'].name + "(s)")
                        if d['item'] in self.stackinv:
                            self.stackinv[d['item']] += x
                        if d['item'] in self.wallet:
                            self.wallet[d['item']] += x
                        else:
                            a = 0
                            while a < x:
                                self.inventory.append(d['item'])
                                a += 1
    def dropt(self):
        y = randint(0, 100)
        print(y)
        if self.status == 'questcombat':
            if self.fighting.qi is not None:
                self.inventory.append(self.fighting.qi)
                print("%s added to inventory" % self.fighting.qi.name)
                self.status = 'normal'

        for d in self.fighting.dp:
            for key in d:
                if key == 'dc':
                    y = random.randint(0, 100)
                    if y <= d['dc']:
                        x = random.randint(d['minqty'], d['maxqty'])
                        print("Dropped " + str(x) + " " + d['item'].name + "(s)")
                        if d['item'] in self.stackinv:
                            self.stackinv[d['item']] += x
                        else:
                            a = 0
                            while a < x:
                                self.inventory.append(d['item'])
                                a += 1
    def examine(self):
        self.cinventory()
        ex = input("Which item would you like to examine?: ").upper()
        self.clear()
        self.clear()
        for x in self.inventory:
            if ex == x.name.upper():
                cprint("----------------------------------------------", 'green')
                cprint(x.style + x.name, x.color)
                cprint("----------------------------------", 'green')
                if x.type == 'mwep':
                    print("Damage: " + str(x.damage))
                if x.type != 'mwep':
                    print("Defence: " + str(x.defence))
                if x.type != 'mwep':
                    print("Health Boost: " + str(x.health))
                cprint("----------------------------------", 'green')
                cprint("----------------------------------------------", 'green')
                break
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
        x = input("What would you like to consume?: ").upper()
        for z in self.inventory:
            if x == z.name.upper():
                self.inventory.remove(z)
                self.health += z.hh
                if z.type != 'spotion':
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                print("You consumed the %s" % z.name)
                break
    def changelog(self):
        system("cls")
        print("""
        -----------------------------------------
                    Changelog v0.5.1A
        - Crafting system implemented
        - Main worldspace implemented with towns
        - Dynamic drop table loot system
        -----------------------------------------
        """)
    def cinventory(self):
        system("cls")
        cprint("█████████████████████████████████████████", 'green')
        cprint(Style.BRIGHT + "               Inventory                 ", 'white')
        for x in self.inventory:
            if x.type != 'scroll':
                cprint("- " + x.style + x.name, x.color)
            else:
                cprint("- " + x.name)
        if self.gold > 0:
            cprint(Style.BRIGHT + "Gold: %d" % self.gold, 'yellow')
        if self.ammo > 0:
            print(Style.BRIGHT + "Ammo: %d" % self.ammo)
        cprint("█████████████████████████████████████████", 'green')
        cprint(Style.BRIGHT + "               Money Pouch                 ", 'yellow')
        for i in self.wallet:
            if self.wallet[i] > 0:
                cprint(i.style + i.name, i.color, end="")
                print(" (x" + str(self.wallet[i]) + ")")
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
        goto = input("> ").upper()
        if goto == "GENERAL STORE":
            self.clear()
            self.genstoredisp()
        elif goto == "BANK":
            self.clear()
            self.bankdisp()
        elif goto == "GUNSMITH":
            self.clear()
            self.gunsmithdisp()
        elif goto == "BLACKSMITH":
            self.clear()
            self.blacksmithdisp()
        elif goto == "LEAVE":
            system("cls")
            print("You have left %s. Type 'town' to reenter." % self.location.name)
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
        choice = input("(buy, sell, leave)> ").upper()
        if choice == "BUY":
            system("cls")
            print("-----------------------------------")
            print("        %s General store           " % self.location.name)
            print("-----------------------------------")
            for x in self.location.generalstore:
                print(x.name)
            print("-----------------------------------")
            buy = input("What would you like to buy?: ").upper()
            for x in self.location.generalstore:
                if buy == x.name.upper():
                    if x.bp > self.wallet[I.goldpiece]:
                        u = x.bp - self.wallet[I.goldpiece]
                        print("You need %d more gold to afford that." % u)
                        system("pause")
                        system("cls")
                        self.genstoredisp()
                    else:
                        print("You bought %s for %d gold." % (x.name, x.bp))
                        if x in self.stackinv:
                            self.stackinv[x] += 1
                        else:
                            self.inventory.append(x)
                        self.location.generalstore.remove(x)
                        self.wallet[I.goldpiece] -= x.bp
                        system("pause")
                        system("cls")
                        self.genstoredisp()
                        break
        elif choice == "SELL":
            system("cls")
            print("-----------------------------------")
            print("        Your inventory             ")
            print("-----------------------------------")
            for x in self.inventory:
                print(x.name)
            print("-----------------------------------")
            sell = input("What would you like to sell?: ").upper()
            for x in self.inventory:
                if sell == x.name.upper():
                    if x in self.location.generalstore:
                        self.inventory.remove(x)
                        self.location.generalstore.append(x)
                        self.wallet[I.goldpiece] += x.sp
                        print("You sold a %s to the General store." % x.name)
                        system("pause")
                        system("cls")
                        self.genstoredisp()
                        break
                    else:
                        self.inventory.remove(x)
                        self.location.generalstore.append(x)
                        self.wallet[I.goldpiece] += (x.sp)
                        print("You sold a %s to the General store." % x.name)
                        self.genstoredisp()
                        break
            else:
                print("You do not have a %s" % sell)
                system("pause")
                system("cls")
                self.genstoredisp()
        elif choice == "LEAVE":
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
    def area(self):
        for x in dynlDB.northbeachesl:
            if x == self.worldspace[self.ypos][self.xpos]:
                print(bDB.northbeaches.description)
        for x in dynlDB.midbeachesl:
            if x == self.worldspace[self.ypos][self.xpos]:
                print(bDB.midbeaches.description)
        for x in dynlDB.northwoodsl:
            if x == self.worldspace[self.ypos][self.xpos]:
                print(bDB.northwoods.description)
        print("Biome type: ")
    def gonorth(self):
        if self.worldspace[(self.ypos - 1)][self.xpos] == 0:
            print("You cannot go through this water without a boat!")
        else:
            #print(str(self.worldspace[self.ypos][self.xpos]))
            self.ypos -= 1
            for x in dynlDB.townsl:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(Style.DIM + x.town.name + " is in the area. Type 'town' to enter..", 'green')
            for x in dynlDB.pointsofinterest:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(x.description, 'yellow')
                    if x.enemies != []:
                        print("Fight")
                        for z in x.enemies:
                            self.status = 'fighting'
                            self.fighting = enemy(z.name, z.minhealth, randint(z.minhealth, z.maxhealth), z.maxhealth, z.damage, z.defence, z.hasgun, z.dp, z.id)
                            self.fightdisp()
                            self.fightform()
            #print(str(self.worldspace[self.ypos][self.xpos]))
    def goeast(self):
        if self.worldspace[self.ypos][(self.xpos + 1)] == 0:
            print("You cannot go through this water without a boat!")
        else:
            #print(str(self.worldspace[self.ypos][self.xpos]))
            self.xpos += 1
            for x in dynlDB.townsl:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(Style.DIM + x.town.name + " is in the area. Type 'town' to enter..", 'green')
            for x in dynlDB.pointsofinterest:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(x.description, 'yellow')
                    if x.enemies != []:
                        print("Fight")
                        for z in x.enemies:
                            self.status = 'fighting'
                            self.fighting = enemy(z.name, z.minhealth, randint(z.minhealth, z.maxhealth), z.maxhealth, z.damage, z.defence, z.hasgun, z.dp, z.id)
                            self.fightdisp()
                            self.fightform()
            #print(str(self.worldspace[self.ypos][self.xpos]))
    def gosouth(self):
        if self.worldspace[self.ypos + 1][self.xpos] == 0:
            print("You cannot go through this water without a boat!")
        if self.worldspace[self.ypos + 1][self.xpos] in dynlDB.southcompwall:
            print("You see a giant wall before you with banners that you do not recognize. There is no way for you to get through.")
        else:
            #print(str(self.worldspace[self.ypos][self.xpos]))
            self.ypos += 1
            for x in dynlDB.townsl:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(Style.DIM + x.town.name + " is in the area. Type 'town' to enter..", 'green')
            for x in dynlDB.pointsofinterest:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(x.description, 'yellow')
                    if x.enemies != []:
                        print("Fight")
                        for z in x.enemies:
                            self.status = 'fighting'
                            self.fighting = enemy(z.name, z.minhealth, randint(z.minhealth, z.maxhealth), z.maxhealth, z.damage, z.defence, z.hasgun, z.dp, z.id)
                            self.fightdisp()
                            self.fightform()
            #print(str(self.worldspace[self.ypos][self.xpos]))
    def gowest(self):
        if self.worldspace[self.ypos][(self.xpos - 1)] == 0:
            print("You cannot go through this water without a boat!")
        else:
            #print(str(self.worldspace[self.ypos][self.xpos]))
            self.xpos -= 1
            for x in dynlDB.townsl:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(Style.DIM + x.town.name + " is in the area. Type 'town' to enter..", 'green')
            for x in dynlDB.pointsofinterest:
                if x.pos == self.worldspace[self.ypos][self.xpos]:
                    cprint(x.description, 'yellow')
                    if x.enemies != []:
                        print("Fight")
                        for z in x.enemies:
                            self.status = 'fighting'
                            self.fighting = enemy(z.name, z.minhealth, randint(z.minhealth, z.maxhealth), z.maxhealth, z.damage, z.defence, z.hasgun, z.dp, z.id)
                            self.fightdisp()
                            self.fightform()
            #print(str(self.worldspace[self.ypos][self.xpos]))
    def town(self):
        for x in dynlDB.townsl:
            if x.pos == self.worldspace[self.ypos][self.xpos]:
                input("You enter " + x.town.name + " and are welcomed through the gates...")
                self.clear()
                self.location = x.town
                self.towndisp()
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
            whatpot = input("What would you like to smith?: ").lower()
            for b in self.gsrec:
                if whatpot == b.name.lower():
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
            whatpot = input("What potion would you like to craft?: ").lower()
            for b in RDB.allrecipes:
                if whatpot == b.name.lower():
                    if self.skillalch >= b.lvl:
                        made = True
                    else:
                        made = False
                        print("You are not skilled enough in Alchemy to create that potion.")
                        print(b.ic.name + " requires level %s in Alchemy." % str(b.lvl))
                    for i in b.ing:
                        if b.ing[i] > self.stackinv[i]:
                            made = False
                            if self.skillalch >= b.lvl:
                                print("You do not have the required ingredients...")
                            break
                    if made == True:
                        for i in b.ing:
                            self.stackinv[i] -= b.ing[i]
                        self.inventory.append(b.ic)
                        print("You created a %s" % b.ic.name)
                        self.xpalch += b.exp
                        if self.xpalch >= self.xpalchnext:
                            self.xpalch -= self.xpalchnext
                            if self.xpalch < 0:
                                self.xpalch = 0
                            self.skillalch += 1
                            self.xpalchnext *= 1.5
                            print("You leveled up in Alchemy! You are now level " + str(self.skillalch) + ".")
        if choice == '2':
            self.clear()
            print("-------------------------------")
            print("         Known Recipes         ")
            for a in self.alchrec:
                print("- " + a.name)
            print("-------------------------------")
            whatrec = input("What recipe do you want to check?: ").lower()
            for b in self.alchrec:
                if whatrec == b.name.lower():
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
        equip = input("What would you like to equip?: ").upper()
        for x in self.inventory:
            if equip == x.name.upper():
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
    def read(self):
        system("cls")
        cprint("█████████████████████████████████████████", 'green')
        cprint(Style.BRIGHT + "              Recipe Scrolls                 ", 'green')
        for x in self.inventory:
            if x.type == 'scroll':
                cprint("- " + x.name2)
        cprint("█████████████████████████████████████████", 'green')
        read = input("Which scroll do you want to read?(This will consume the item): ").upper()
        for x in self.inventory:
            if x.type == 'scroll':
                if read == x.name2.upper():
                    if x.skill == 'alch':
                        if x.rt in self.alchrec:
                            print("You already know this recipe..")
                        else:
                            self.alchrec.append(x.rt)
                            print("You learned how to make " + x.name2 + ".")
                            self.inventory.remove(x)
    def dev2(self):
        print(dynlDB.p12.description)
        x = str(input("What would you like this description to be?: "))
        dynlDB.p12.description = ("'" + x + "'")
    def stats(self):
        self.clear()
        cprint("█████████████████████████████████████████", 'yellow')
        print("                   Stats                 ")
        print("Alchemy: " + str(self.skillalch) + " (EXP: " + str(self.xpalch) + "/" + str(self.xpalchnext) + ")")
        print("Blacksmithing: " + str(self.skillblacksmith) + " (EXP: " + str(self.xpblacksmith) + "/" + str(self.xpblacksmithnext) + ")")
        print("Building: " + str(self.skillbuilding) + " (EXP: " + str(self.xpbuilding) + "/" + str(self.xpbuildingnext) + ")")
        print("Cooking: " + str(self.skillcooking) + " (EXP: " + str(self.xpcooking) + "/" + str(self.xpcookingnext) + ")")
        print("Fishing: " + str(self.skillfishing) + " (EXP: " + str(self.xpfishing) + "/" + str(self.xpfishingnext) + ")")
        print("Foraging: " + str(self.skillforaging) + " (EXP: " + str(self.xpforaging) + "/" + str(self.xpforagingnext) + ")")
        print("Gunsmithing: " + str(self.skillgunsmith) + " (EXP: " + str(self.xpgunsmith) + "/" + str(self.xpgunsmithnext) + ")")
        print("Hunting: " + str(self.skillhunting) + " (EXP: " + str(self.xphunting) + "/" + str(self.xphuntingnext) + ")")
        print("Leatherworking: " + str(self.skillleatherwork) + " (EXP: " + str(self.xpleatherwork) + "/" + str(self.xpleatherworknext) + ")")
        print("Mining: " + str(self.skillmining) + " (EXP: " + str(self.xpmining) + "/" + str(self.xpminingnext) + ")")
        cprint("█████████████████████████████████████████", 'yellow')
    def status(self):
        self.clear()
        cprint("█████████████████████████████████████████", 'yellow')
        print("               Character                 ")
        if self.health > self.maxhealth:
            print("Health: " + str(self.maxhealth) + Fore.GREEN + "(" + str(self.health - self.maxhealth) + ")" + Style.RESET_ALL + "/" + str(self.maxhealth))
        else:
            print("Health: " + str(self.health) + "/" + str(self.maxhealth))
        print("Gold: %d" % self.gold)
        print("Range Damage: %s" % self.gundamage)
        print("Damage: %d" % self.damage)
        print("Defence: %d" % self.defence)
        for x in self.inventory:
            if x.type == 'map':
                print("X Coordinate - %d" % self.xpos)
                print("Y Coordinate - %d" % self.ypos)
                print("Area ID - %d" % self.worldspace[self.ypos][self.xpos])
                break
        cprint("█████████████████████████████████████████", 'yellow')
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
        cprint("█████████████████████████████████████████", 'yellow')
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
                for x in dynlDB.pointsofinterest:
                    if x.pos == self.worldspace[self.ypos][self.xpos]:
                        for y in x.enemies:
                            if self.fighting.name == y.name:
                                x.enemies.remove(y)
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
                x = random.randint(0, 5)
                self.health -= x
                self.enemyhit = ("The " + self.fighting.name + " hit you for " + str(x) + ".")
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
        pickle.dump([self.wallet, self.skillblacksmith, self.skillgunsmith, self.skillfishing, self.skillleatherwork, self.skillbuilding, self.skillmining, self.skillforaging, self.skillhunting, self.skillcooking, self.skillalch, self.xpblacksmith, self.xpblacksmithnext, self.xpbuilding, self.xpbuildingnext, self.xphunting, self.xphuntingnext, self.xpcooking, self.xpcookingnext, self.xpfishing, self.xpfishingnext, self.xpforaging, self.xpforagingnext,
                     self.xpmining, self.xpminingnext, self.xpalch, self.xpalchnext, self.xpgunsmith, self.xpgunsmithnext, self.xpforaging, self.xpforagingnext, self.xpleatherwork, self.xpleatherworknext, self.stackinv, self.maxhealth, self.inventory, self.questlog, self.compquests, self.name, self.health, self.xpos, self.ypos, self.rs, self.ms, self.hs, self.cs, self.ps, self.fs, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.gold, self.devenabled], open("{0}.tin".format(save), "wb"))
        #City and town data
        pickle.dump([TDB.narja.bankamount, TDB.narja.generalstore, TDB.narja.blacksmith, TDB.narja.gunsmith], open("{0}.tin".format(save + "cd"), "wb"))
        #POIData
        pickle.dump([dynlDB.p12.description, dynlDB.p27.description, dynlDB.p27.items, dynlDB.p27.enemies], open("{0}.tin".format(save + "poi"), "wb"))
    def devsave(self):
        pickle.dump([self.eitemslist, self.inventory, self.norag, self.gabesh, self.yoeran, self.litau, self.uash, self.shreeda, self.sq1, self.sq2, self.questlog, self.compquests, self.name, self.health, self.xcoord, self.ycoord, self.gslot, self.mslot, self.headslot, self.chestslot, self.legslot, self.footslot, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.devenabled], open("devsave.tin", "wb"))
    def devload(self):
        self.eitemslist, self.inventory, self.sq1, self.sq2, self.questlog, self.compquests, self.name, self.health, self.xpos, self.ypos, self.gslot, self.mslot, self.headslot, self.chestslot, self.legslot, self.footslot, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.devenabled, TDB.ttown = pickle.load(open("devsave.tin", "rb"))
    def loadt(self):
        load = input("What file would you like to load(Doesn't exist = Crash): ")
        self.wallet, self.skillblacksmith, self.skillgunsmith, self.skillfishing, self.skillleatherwork, self.skillbuilding, self.skillmining, self.skillforaging, self.skillhunting, self.skillcooking, self.skillalch, self.xpblacksmith, self.xpblacksmithnext, self.xpbuilding, self.xpbuildingnext, self.xphunting, self.xphuntingnext, self.xpcooking, self.xpcookingnext, self.xpfishing, self.xpfishingnext, self.xpforaging, self.xpforagingnext, self.xpmining, self.xpminingnext, self.xpalch, self.xpalchnext, self.xpgunsmith, self.xpgunsmithnext, self.xpforaging, self.xpforagingnext, self.xpleatherwork, self.xpleatherworknext, self.stackinv, self.maxhealth, self.inventory, self.questlog, self.compquests, self.name, self.health, self.xpos, self.ypos, self.rs, self.ms, self.hs, self.cs, self.ps, self.fs, self.damage, self.gundamage, self.shot, self.reloading, self.defence, self.status, self.fighting, self.ammo, self.gold, self.devenabled = pickle.load(open("{0}.tin".format(load), "rb"))
        #City and town data
        TDB.narja.bankamount, TDB.narja.generalstore, TDB.narja.blacksmith, TDB.narja.gunsmith = pickle.load(open("{0}.tin".format(load + "cd"), "rb"))
        #POIData
        dynlDB.p12.description, dynlDB.p27.description, dynlDB.p27.items, dynlDB.p27.enemies = pickle.load(open("{0}.tin".format(load + "poi"), "rb"))
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
            #""" % (self.fighting.name, self.fighting.health, self.health, self.playerhit, self.enemyhit)
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
        8. Smelting Menu 
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
    def devt(self):
        print("You magically teleported to developer town")
        system("pause")
        self.clear()
        self.location = self.devtown
        self.towndisp()
Commands = {
  'help': Main.help,
  'area': Main.area,
  'ci': Main.clearinv,
  'inventory': Main.cinventory,
  'north': Main.gonorth,
  'read': Main.read,
  'town': Main.town,
  'east': Main.goeast,
  'south': Main.gosouth,
  'west': Main.gowest,
  'search': Main.search,
  'equip': Main.equip,
  'status': Main.status,
  'clear': Main.clear,
  'dev1': Main.dev1,
  'devt': Main.devt,
  'dev2': Main.dev2,
  'dev3': Main.dev3,
  'changelog': Main.changelog,
  'examine': Main.examine,
  '20657': Main.enabledev,
  'ddev': Main.disabledev,
  'save': Main.save,
  'stats': Main.stats,
  'loadt': Main.loadt,
  'testload': Main.loadt,
  'dev4': Main.dev4,
  'dropt': Main.dropt,
  'speak': Main.talkto,
  'dev5': Main.drop,
  '06': Main.alchcraft,
  '07': Main.bscraft,
  '08': Main.smeltcraft,
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
  '00': Main.devmenu,
  'map': Main.map,
  }
p = Main()
p.clear()
cprint(Style.DIM + "█████████████████████████████████████████", 'green')
cprint(Style.BRIGHT + "         The Time is Now v0.5.1", 'green')
cprint(Style.BRIGHT + "1. New Game", 'green')
cprint(Style.BRIGHT + "2. Load game", 'green')
cprint(Style.BRIGHT + "3. About", 'green')
cprint(Style.DIM + "█████████████████████████████████████████", 'green')
menuchoice = input("Type the number: ")
if menuchoice == "1":
    p.name = input("What is your name? ")
    p.clear()
    print("""
    You wake up groggy and in pain, your gold and your map have been stolen
    off of you. You can barely remember what happened in your drunken stupor but
    you know you were robbed by a mugger when you left the tavern from Narja. 
    Maybe just a little too much to drink?.. Either way, you see the smoke 
    from a campfire creeping up into the air in the distant east. Maybe thats
    where the man who mugged you went? It's up to you to decide if you chase after
    him, or if you forget about the whole thing for now.
    """)
    cprint(Style.BRIGHT + "(type help to get a list of actions)", 'yellow')
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
looperCPU = 500
printerLooper = True
secondsPause = 0
while(p.health > 0):
  line = input(Fore.GREEN + Style.BRIGHT + "> ").lower()
  print(Style.RESET_ALL)
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
