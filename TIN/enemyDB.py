from enemy import enemy as e
from enemy import qenemy as qe
from enemy import boss
from ItemDB import ItemDB as I
from random import randint, randrange
from npcDB import questDB as QDB
from specialattacks import specialattacks as spec
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style

class enemyDB:

    #ALL ENEMY DROPS ARE SUBJECT TO COMPLETE OVERHAUL


    #Low Tier Enemies
    mugger = e("Mugger", 40, randint(40, 60), 60, 10, 1, 0, [I.irondagger, I.irondagger, I.bread, I.bread, I.clothcap, I.clothpants], 1)
    fban = e("Woodland Bandit", 20, randint(20, 40), 40, 3, 1, 1, [I.wberries, I.wberries, I.irondagger, I.irondagger], 2)
    wolf = e("Wolf", 10, randint(10, 30), 30, 6, 1, 1, [I.wolfpelt], 3)

    #Low-Mid Tier Enemies
    siban = e("Snake Bandit", 160, randint(160, 200), 200, 35, 8, 1, [I.gppistol, I.ironlsword, I.ironlsword], 100)

    #Mid Tier Enemies
    armcent = e("Armored Centaur", 260, randint(260, 350), 350, 60, 20, 0, [I.bsteellsword, I.bsteellsword, I.bsteellsword, I.bsteellsword, I.disasterblade,
    I.disasterblade], 1010)

    #High Tier Enemies
    enraeth = e("Enraged Aetherial", 250, randint(250, 350), 350, 120, 45, 0, [I.disasterblade, I.disasterblade, I.disasterblade, I.disasterblade, I.aetherialhelm,
    I.aetheriallp, I.aetherialwraps, I.disasterblade,
    I.disasterblade, I.aetherialcp, I.aetheriallp, I.bladeofeternity, I.disasterblade,
    I.disasterblade, I.largehp, I.largehp, I.aethdust, I.aethdust, I.aethdust, I.aethdust, I.aethdust, I.aethdust,
    I.aethdust, I.aethdust, I.aethdust, I.aethdust, I.aethdust, I.aethdust, I.largehp, I.medhp, I.medhp], 1110)

    enemylist = [mugger, siban, armcent, enraeth]


    #QUEST ENEMIES
    lonebandit = qe("Lone Bandit", 10, 10, 4, 1, 0, QDB.sahandimerchantquest1, I.carvedpistol, 6, 5)

    qenemylist = [lonebandit]

    #BOSSES (EXPECT CHANGES)
    morkool = boss("Morkool the Unchained", 'red', Style.BRIGHT, 6000, 6000, 350, 110, [], [spec.mkhambash, spec.mkhambash, spec.mkkick, spec.mkhambash], [], 20, [], 1)