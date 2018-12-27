from weapon import weapon as w
from armor import armor as a
from misc import misc as m
from potion import potion as p
from os import system
import sys
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style

class ItemDB:
    #SCROLLS
    smallhpscroll = m("Recipe: Small Health Potion", 'scroll', 0, 0, 250, 175, 'white', Style.DIM, 99)
    #CURRENCY
    goldpiece = m("Gold Pieces", "currency", 0, 0, 0, 0, 'yellow', Style.BRIGHT, 1)
    #QUEST ITEMS
    carvedpistol = m("Carved Pistol", "quest", 0, 0, 0, 0, 'blue', Style.BRIGHT, 32000)
    # ---UTILITIES---
    simplemap = m("Simple Map", 'map', 0, 0, 15, 6, 'white', Style.DIM, 2)
    #MiscItems
    bread = m("Loaf of bread", "food", 5, 5, 2, 1, 'white', Style.DIM, 10)
    charredpork = m("Charred pork", 'food', 9, 6, 8, 4, 'white', Style.DIM, 99)
    wberries = m("Wild Berries", "food", 10, 2, 5, 3, 'white', Style.DIM, 11)
    boarjerky = m("Boar jerky", 'food', 7, 4, 4, 2, 'white', Style.DIM, 99)
    aitem = m("34y6y734577562735723", "admin", 0, 0, 0, 0, 'white', Style.DIM, 1000000)
    #CRAFTING ITEMS(STACKABLE)
    coal = m("Coal", "ore", 0, 0, 10, 5, 'white', Style.DIM, 89000)
    ironore = m("Iron Ore", "ore", 0, 0, 60, 30, 'white', Style.DIM, 89001)
    ironingot = m("Iron Ingot", "craft", 0, 0, 70, 35, 'white', Style.BRIGHT, 89002)
    woodrod = m("Wooden Rod", "craft", 0, 0, 20, 10, 'white', Style.DIM, 88000)
    aethdust = m("Aetherial Dust", "craft", 0, 0, 400, 200, 'cyan', Style.BRIGHT, 90000)
    centhorn = m("Centaur Horn", "craft", 0, 0, 0, 0, 'green', Style.BRIGHT, 90001)
    wolfpelt = m("Wolf Pelt", "craft", 0, 0, 30, 15, 'white', Style.DIM, 90002)
    sharpcanine = m("Sharp Canine", "craft", 0, 0, 10, 5, 'white', Style.DIM, 90003)
    broketooth = m("Broken Tooth", "craft", 0, 0, 5, 2, 'white', Style.DIM, 90004)
    bottlewater = m("Bottle of Water", "craft", 0, 5, 20, 10, 'white', Style.DIM, 91000)
    salt = m("Salt", "craft", 0, 0, 5, 2, 'white', Style.DIM, 91001)
    potatoweed = m("Potato Weed", "craft", 0, 0, 15, 7, 'white', Style.DIM, 91002)
    tumblethorn = m("Tumblethorn", "craft", 0, 0, 25, 12, 'white', Style.BRIGHT, 91003)
    largebottle = m("Large Bottle of Water", "craft", 0, 0, 60, 30, 'white', Style.BRIGHT, 91004)
    #Potion
    lowhp = p("Small Health Potion", "potion", 20, 0, 10, 5, 'white', Style.DIM, 86000)
    hp = p("Health Potion", "potion", 35, 0, 30, 15, 'white', Style.BRIGHT, 86001)
    medhp = p("Medium Health Potion", "potion", 60, 0, 90, 45, 'green', Style.DIM, 86002)
    largehp = p("Large Health Potion", "potion", 120, 0, 270, 135, 'green', Style.BRIGHT, 86003)
    hugehp = p("Huge Health Potion", "potion", 200, 0, 400, 200, 'cyan', Style.DIM, 86004)
    royalhp = p("Royal Health Potion", "potion", 350, 0, 650, 300, 'cyan', Style.BRIGHT, 86005)
    smaethhp = p("Small Aetherial Potion", "spotion", 80, 0, 450, 200, 'magenta', Style.DIM, 86100)
    aethhp = p("Aetherial Potion", "spotion", 130, 0, 800, 400, 'magenta', Style.BRIGHT, 86101)
    largeaethhp = p("Large Aetherial Potion", "spotion", 250, 0, 1700, 850, 'magenta', Style.BRIGHT, 86102)
    pureaethhp = p("Pure Aetherial Potion", "spotion", 410, 0, 3000, 1500, 'yellow', Style.BRIGHT, 86103)

    #Poisons
    poison = p("Simple Poison", "potion", -20, 0, 30, 15, 'white', Style.BRIGHT, 87010)
    # ---WEAPONS---
    #Common
    ironsword = w("Iron Shortsword", "mwep", 6, 0, 10, 5, 'white', Style.DIM, 1, 100)
    ironlsword = w("Iron Longsword", "mwep", 9, 0, 15, 7, 'white', Style.DIM, 1, 101)
    irondagger = w("Iron Dagger", "mwep", 5, 0, 6, 3, 'white', Style.DIM, 1, 102)
    #Common+
    steelsword = w("Steel Shortsword", "mwep", 12, 0, 100, 50, 'white', Style.BRIGHT, 5, 200)
    steellsword = w("Steel Longsword", "mwep", 15, 0, 120, 60, 'white', Style.BRIGHT, 5, 201)
    #Uncommon
    bsteelsword = w("Blacksteel Shortsword", "mwep", 18, 0, 300, 150, 'green', Style.DIM, 15, 300)
    #Uncommon+
    bsteellsword = w("Blacksteel Longsword", "mwep", 21, 0, 450, 225, 'green', Style.BRIGHT, 15, 301)
    #Rare
    disasterblade = w("Disaster Blade", "mwep", 55, 0, 1400, 700, 'cyan', Style.DIM, 22, 3000)
    #Rare+
    goldkho = w("Golden Khopesh", "mwep", 63, 0, 2200, 1100, 'cyan', Style.BRIGHT, 25, 3500)
    #Epic
    sfsword = w("Star-forged Sword", "mwep", 85, 0, 5000, 2500, 'magenta', Style.DIM, 30, 900)
    #Mythic
    bladeofeternity = w("Blade of Eternity", "mwep", 105, 0, 12300, 6150, 'magenta', Style.BRIGHT, 35, 950)
    redsteelnightblade = w("Redsteel Nightmareblade", "mwep", 110, 0, 14000, 7000, 'magenta', Style.BRIGHT, 36, 951)
    corruptedroyalsw = w("Corrupted Royal Shortsword", "mwep", 120, 0, 14000, 7000, 'magenta', Style.BRIGHT, 38, 952)
    #Legendary
    gsofkings = w("Greatsword of Kings", "mwep", 145, 0, 22500, 15000, 'yellow', Style.BRIGHT, 45, 980)
    #Uniques
    mkwarhammer = w("Morkool's Warhammer", "mwep", 225, 0, 30000, 20000, 'red', Style.BRIGHT, 50, 9000)
    # ---GUNS---
    shodpistol = w("Shoddy Pistol", 'rwep', 20, 15, 55, 20, 'white', Style.DIM, 1, 1003)
    flpistol = w("Flintlock Pistol", "rwep", 30, 25, 100, 50, 'white', Style.DIM, 1, 1000)
    gppistol = w("Gold Pistol", "rwep", 90, 38, 400, 200, 'white', Style.BRIGHT, 5, 1001)
    guildpistol = w("Guilded Pistol", "rwep", 120, 55, 6000, 3000, 'green', Style.DIM, 25, 1002)
    # ---HELMETS---
    armnemes = a("Armored Nemes", "helm", 35, 40, 39500, 34900, 'red', Style.BRIGHT, 50, 9010)
    clothcap = a("Cloth cap", "helm", 1, 0, 10, 5, 'white', Style.DIM, 1, 2000)
    muggercap = a("Mugger's cap", "helm", 2, 0, 10, 5, 'white', Style.DIM, 1, 2101)
    leathercap = a("Leather cap", "helm", 3, 0, 13, 6, 'white', Style.DIM, 1, 99)
    reinleathcap = a("Reinforced Leather Cap", "helm", 4, 0, 20, 10, 'white', Style.BRIGHT, 2, 99)
    aetherialhelm = a("Aetherial Headwrap", "helm", 22, 40, 24000, 14000, 'magenta', Style.BRIGHT, 36, 600)
    guildedcc = a("Guilded Chainmail Coif", "helm", 28, 30, 26000, 13000, 'magenta', Style.BRIGHT, 38, 715)
    guildedhelm = a("Guilded Helm", "helm", 32, 50, 29000, 14500, 'yellow', Style.BRIGHT, 42, 720)
    # ---CHESTPLATES---
    clothshirt = a("Cloth shirt", 'chest', 2, 0, 5, 3, 'white', Style.DIM, 1, 1999)
    leathertunic = a("Leather tunic", "chest", 3, 0, 15, 7, 'white', Style.DIM, 1, 2001)
    reinleathtunic = a("Reinforced Leather tunic", 'chest', 5, 0, 30, 15, 'white', Style.BRIGHT, 2, 99)
    leathcolbp = a("Colonial Breastplate", "chest", 10, 0, 100, 50, 'white', Style.BRIGHT, 10, 100)
    aetherialcp = a("Aetherial Chestplate", "chest", 30, 55, 30000, 20000, 'magenta', Style.BRIGHT, 36, 601)
    guildedccp = a("Guilded Chainmail Vest", "chest", 35, 45, 38000, 19000, 'magenta', Style.BRIGHT, 38, 716)
    guildedcp = a("Guilded Chestplate", "chest", 40, 60, 45000, 28000, 'yellow', Style.BRIGHT, 42, 721)
    bjarncp = a("Bjarn's Chestplate", "chest", 50, 100, 40000, 35000, 'red', Style.BRIGHT, 50, 9050)
    # ---LEGPLATES---
    clothpants = a("Cloth pants", "legs", 2, 0, 12, 6, 'white', Style.DIM, 1, 2002)
    leatherchaps = a("Leather chaps", 'legs', 4, 0, 22, 11, 'white', Style.BRIGHT, 2, 99)
    guildedlp = a("Guilded Legplates", "legs", 37, 50, 32000, 17500, 'yellow', Style.BRIGHT, 42, 722)
    guildedcpants = a("Guilded Chainmail Pants", "legs", 31, 40, 30000, 15000, 'magenta', Style.BRIGHT, 38, 717)
    aetheriallp = a("Aetherial Legwraps", "legs", 27, 45, 28000, 18000, 'magenta', Style.BRIGHT, 36, 602)
    # ---BOOTS---
    ruggedshoes = a("Rugged shoes", "foot", 1, 0, 10, 5, 'white', Style.DIM, 1, 2003)
    leatherboots = a("Leather boots", 'foot', 2, 0, 20, 10, 'white', Style.DIM, 1, 2004)
    paddedleathboots = a("Padded Leather boots", 'foot', 3, 0, 25, 12, 'white', Style.BRIGHT, 2, 99)
    armleatherboots = a("Armored Leather boots", 'foot', 21, 0, 12000, 6000, 'white', Style.DIM, 1, 2005)
    aetherialwraps = a("Aetherial Footwraps", "foot", 22, 5, 24000, 14000, 'magenta', Style.BRIGHT, 36, 603)
    guildedboots = a("Guilded Boots", "foot", 30, 10, 28000, 14000, 'yellow', Style.BRIGHT, 38, 718)

    itemlist = [smallhpscroll, charredpork, reinleathtunic, leatherchaps, paddedleathboots, leathercap, reinleathcap, leatherboots, shodpistol, corruptedroyalsw, guildedcpants, guildedcc, guildedccp, guildedboots, guildedhelm, guildedcp, guildedlp, coal, royalhp, ironore, ironingot, woodrod, wberries, aethdust, centhorn, wolfpelt, bottlewater, salt, potatoweed, armnemes, ironsword, ironlsword, irondagger, steelsword, steellsword, bsteelsword, bsteellsword, disasterblade, sfsword, bladeofeternity, gsofkings, mkwarhammer,
                flpistol, gppistol, guildpistol, clothcap, clothpants, clothshirt, leathertunic, leathcolbp, aetherialcp, aetherialhelm, aetheriallp, aetherialwraps, ruggedshoes,
                lowhp, hp, medhp, largehp, smaethhp, aethhp, largeaethhp, pureaethhp, bjarncp, goldkho, redsteelnightblade, carvedpistol, simplemap]
    stackablelist = [boarjerky, goldpiece, coal, ironore, ironingot, woodrod, aethdust, centhorn, wolfpelt, bottlewater, salt, potatoweed, wberries]