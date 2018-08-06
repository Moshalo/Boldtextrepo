class spec():
    def __init__(self, name, damtype, mindam, maxdam, desc, time):
        self.name = name
        self.damtype = damtype
        self.mindam = mindam
        self.maxdam = maxdam
        self.desc = desc
        self.time = time
class specialattacks():

    #Morkool
    mkhambash = spec("Hammer Bash", 'stun', 1, 2, "bashes you with his hammer!", 1)
    mkkick = spec("Swift Kick", 'blunt', 40, 100, "kicks you with his hoof!", 2)
