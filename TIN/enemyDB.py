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

    #STATIC NPCS
    sqmugger = e("Mugger", 40, randint(40, 60), 60, 3, 1, 0, [
        {'item': I.irondagger, 'minqty': 1, 'maxqty': 2, 'dc': 40},
        {'item': I.clothshirt, 'minqty': 1, 'maxqty': 1, 'dc': 30},
        {'item': I.leathertunic, 'minqty': 1, 'maxqty': 1, 'dc': 20},
        {'item': I.clothpants, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.leatherboots, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.muggercap, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.goldpiece, 'minqty': 25, 'maxqty': 25, 'dc': 100}
    ], 1)
    bloodshieldmgguard = e("Bloodshield Guard", 120, randint(120, 145), 145, 45, 19, 0, [
        {'item': I.irondagger, 'minqty': 1, 'maxqty': 2, 'dc': 40},
        {'item': I.clothshirt, 'minqty': 1, 'maxqty': 1, 'dc': 30},
        {'item': I.leathertunic, 'minqty': 1, 'maxqty': 1, 'dc': 20},
        {'item': I.clothpants, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.leatherboots, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.muggercap, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.goldpiece, 'minqty': 25, 'maxqty': 25, 'dc': 100}
    ], 1)
    #Low Tier Enemies
    mugger = e("Mugger", 40, randint(40, 60), 60, 3, 1, 0, [
        {'item': I.irondagger, 'minqty': 1, 'maxqty': 2, 'dc': 40},
        {'item': I.clothshirt, 'minqty': 1, 'maxqty': 1, 'dc': 30},
        {'item': I.leathertunic, 'minqty': 1, 'maxqty': 1, 'dc': 20},
        {'item': I.clothpants, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.leatherboots, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.muggercap, 'minqty': 1, 'maxqty': 1, 'dc': 25}
    ], 1)

    fban = e("Woodland Bandit", 20, randint(20, 40), 40, 3, 1, 1, [], 2)
    wolf = e("Wolf", 10, randint(10, 30), 30, 2, 1, 1, [
        {'item': I.wolfpelt, 'minqty': 1, 'maxqty': 2, 'dc': 100},
        {'item': I.sharpcanine, 'minqty': 1, 'maxqty': 5, 'dc': 75},
        {'item': I.broketooth, 'minqty': 1, 'maxqty': 10, 'dc': 80}], 3)

    #Low-Mid Tier Enemies
    siban = e("Snake Bandit", 160, randint(160, 200), 200, 10, 8, 1, [], 100)

    #Mid Tier Enemies
    armcent = e("Armored Centaur", 260, randint(260, 350), 350, 60, 20, 0, [], 1010)

    #High Tier Enemies
    enraeth = e("Enraged Aetherial", 250, randint(250, 350), 350, 120, 45, 0, [], 1110)
    corruptroyalsquire = e("Corrupted Royal Squire", 200, randint(200, 400), 400, 115, 30, 0, [
        {'item': I.redsteelnightblade, 'minqty': 1, 'maxqty': 1, 'dc': 18},
        {'item': I.guildedcc, 'minqty': 1, 'maxqty': 1, 'dc': 15},
        {'item': I.guildedccp, 'minqty': 1, 'maxqty': 1, 'dc': 15},
        {'item': I.guildedcpants, 'minqty': 1, 'maxqty': 1, 'dc': 15},
        {'item': I.armleatherboots, 'minqty': 1, 'maxqty': 1, 'dc': 20},
        {'item': I.corruptedroyalsw, 'minqty': 1, 'maxqty': 1, 'dc': 12},
    ], 1119)
    corruptroyalknight = e("Corrupted Royal Knight", 400, randint(400, 500), 500, 180, 80, 0, [], 1120)

    enemylist = [bloodshieldmgguard, sqmugger, fban, wolf, mugger, siban, armcent, enraeth, corruptroyalknight, corruptroyalsquire]


    #QUEST ENEMIES
    lonebandit = qe("Lone Bandit", 10, 10, 4, 1, 0, QDB.sahandimerchantquest1, I.carvedpistol, 6, 5)

    qenemylist = [lonebandit]

    #BOSSES (EXPECT CHANGES)
    morkool = boss("Morkool the Unchained", 'red', Style.BRIGHT, 6000, 6000, 350, 110, [], [spec.mkhambash, spec.mkhambash, spec.mkkick, spec.mkhambash], [], 20, [], 1)


    #OTHER DROP TABLES(WIP)
    fbandt = []
    #Low-Mid Tier Drop tables