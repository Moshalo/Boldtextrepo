from dialog import dialog as D


class dialogDB():

    sahandi1 = D('itemquest', "Traveler, have you seen a bandit anywhere nearby? I've just been robbed.", 1)
    sahandi2 = D('itemquest', "He stole a pistol of mine, a very important pistol to me. I think he ran off into the woods to the east.", 2)
    sahandi3 = D('itemquest', "Would you be interested in helping? There'd be a reward involved, I'm afraid I'm just not as good of a fighter as I used to be.", 3)

    rdude1 = D('itemquest', "Hello Traveler, could you possibly give me a Iron Shortsword?", 1)
    rdude2 = D('itemquest', 'There are many wolves out here and I have no way to protect myself. It would be greatly appreciated.', 2)

    alldialog = [sahandi1, sahandi2, sahandi3, rdude1, rdude2]
