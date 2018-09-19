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
    mugger = e("Mugger", 40, randint(40, 60), 60, 3, 1, 0, [], 1)
    fban = e("Woodland Bandit", 20, randint(20, 40), 40, 3, 1, 1, [], 2)
    wolf = e("Wolf", 10, randint(10, 30), 30, 2, 1, 1, [], 3)

    #Low-Mid Tier Enemies
    siban = e("Snake Bandit", 160, randint(160, 200), 200, 10, 8, 1, [], 100)

    #Mid Tier Enemies
    armcent = e("Armored Centaur", 260, randint(260, 350), 350, 60, 20, 0, [], 1010)

    #High Tier Enemies
    enraeth = e("Enraged Aetherial", 250, randint(250, 350), 350, 120, 45, 0, [], 1110)
    corruptroyalsquire = e("Corrupted Royal Squire", 200, randint(200, 400), 400, 115, 30, 0, [], 1119)
    corruptroyalknight = e("Corrupted Royal Knight", 400, randint(400, 500), 500, 180, 80, 0, [], 1120)

    enemylist = [fban, wolf, mugger, siban, armcent, enraeth, corruptroyalknight, corruptroyalsquire]


    #QUEST ENEMIES
    lonebandit = qe("Lone Bandit", 10, 10, 4, 1, 0, QDB.sahandimerchantquest1, I.carvedpistol, 6, 5)

    qenemylist = [lonebandit]

    #BOSSES (EXPECT CHANGES)
    morkool = boss("Morkool the Unchained", 'red', Style.BRIGHT, 6000, 6000, 350, 110, [], [spec.mkhambash, spec.mkhambash, spec.mkkick, spec.mkhambash], [], 20, [], 1)


    #DROP TABLES(WIP)
    wofldt = [
        {'item': I.wolfpelt, 'minqty': 1, 'maxqty': 2, 'dc': 100},
        {'item': I.sharpcanine, 'minqty': 1, 'maxqty': 5, 'dc': 75},
        {'item': I.broketooth, 'minqty': 1, 'maxqty': 10, 'dc': 80}
    ]
    muggerdt = [
        {'item': I.irondagger, 'minqty': 1, 'maxqty': 2, 'dc': 40},
        {'item': I.clothshirt, 'minqty': 1, 'maxqty': 1, 'dc': 30},
        {'item': I.leathertunic, 'minqty': 1, 'maxqty': 1, 'dc': 20},
        {'item': I.clothpants, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.leatherboots, 'minqty': 1, 'maxqty': 1, 'dc': 25},
        {'item': I.muggercap, 'minqty': 1, 'maxqty': 1, 'dc': 25}
    ]
    fbandt = []
    #Low-Mid Tier Drop tables