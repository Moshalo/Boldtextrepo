from crecipe import RecipeDB as RDB

class scroll:
    def __init__(self, name, type, rt):
        self.name = name
        self.type = type
        self.rt = rt
class ScrollDB():
    # RECIPE SCROLLS
    recsmallhp = sc("Recipe scroll: Small Health Potion", 'alch', RDB.smallhpr)