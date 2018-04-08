class enemy():
    def __init__(self, name, minhealth, health, maxhealth, damage, defence, hasgun, dp, id):
        self.name = name
        self.minhealth = minhealth
        self.health = health
        self.maxhealth = maxhealth
        self.damage = damage
        self.defence = defence
        self.id = id
        self.hasgun = hasgun
        self.dp = dp

class qenemy():
    def __init__(self, name, health, maxhealth, damage, defence, hasgun, quest, qi, xc, yc):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.damage = damage
        self.defence = defence
        self.hasgun = hasgun
        self.quest = quest
        self.qi = qi
        self.xc = xc
        self.yc = yc
        self.id = id
class boss():
    def __init__(self, name, color, style, health, maxhealth, basedamage, basedefence, immunitylist, specialmoves, dialogl, dp, drops, id):
        self.name = name
        self.color = color
        self.style = style
        self.health = health
        self.maxhealth = maxhealth
        self.basedamage = basedamage
        self.basedefence = basedefence
        self.immunitylist = immunitylist
        self.specialmoves = specialmoves
        self.dialogl = dialogl
        self.dp = dp
        self.drops = drops
        self.id = id