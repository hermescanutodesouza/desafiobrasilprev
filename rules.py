import numpy as np


class Rules:

    def __init__(self, playername, playermoney, rouseprice, rouserent=0, debug=True):
        self.impulsive = "player1"
        self.demanding = "player2"
        self.cautious = "player3"
        self.aleatory = "player4"
        self.playername = playername
        self.playermoney = playermoney
        self.rouseprice = rouseprice
        self.rouserent = rouserent
        self.debug = debug

    def hasmoney(self):
        if self.playermoney > self.rouseprice:
            if self.debug:
                print("Has money to buy the house")
            return True

    def aply(self):
        if self.hasmoney():
            if self.playername == self.impulsive:
                return True
            elif self.playername == self.demanding:
                if self.rouserent > 50:
                    if self.debug:
                        print("Rent > 50")
                    return True
            elif self.playername == self.cautious:
                if self.playermoney - self.rouseprice > 80:
                    if self.debug:
                        print("Playermoney - buy 80 =", self.playermoney - self.rouseprice)
                    return True
            elif self.playername == self.aleatory:
                if np.random.choice(np.arange(0, 2)):
                    if self.debug:
                        print("Aleatory True")
                    return True
        return False
