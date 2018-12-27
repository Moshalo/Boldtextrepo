from crecipe import RecipeDB as RDB

class scroll:
    def __init__(self, name, name2, type, skill, rt):
        self.name = name
        self.name2 = name2
        self.type = type
        self.skill = skill
        self.rt = rt
class ScrollDB():
    # RECIPE SCROLLS
    recsmallhp = scroll("Recipe scroll: Small Health Potion", 'Small Health Potion', 'scroll', 'alch', RDB.smallhpr)


    allrecipescrolls = [recsmallhp]