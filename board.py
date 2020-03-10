import pandas as pd
import numpy as np


def createboard():
    house = [i for i in range(1, 21)]
    buy = [np.random.randint(50, 120) for i in range(1, 21)]
    rent = [round(i / 2) for i in buy]
    b = {'house': house,
         "buy": buy,
         "rent": rent,
         "owner": [''],
         "tenant": [''],
         }
    board = pd.DataFrame(b, index=house)
    return board


def setpostion(current, new):
    p = current + new
    r = 0
    if p > 20:
        p = p - 20
        r = 1
    return p, r


def rolldice():
    return np.random.choice(np.arange(1, 7))


def getplayers():
    # order = [i for i in range(1, 5)]
    player = ["player{}".format(i) for i in range(1, 5)]
    position = [0 for i in range(1, 5)]
    d = {'player': player,
         'money': 300,
         'position': position
         }
    players = pd.DataFrame(d)
    players = players.sample(frac=1).reset_index(drop=True)
    return players


def getplayerstatus(player):
    if player == "player1":
        return "impulsive"
    elif player == "player2":
        return "demanding"
    elif player == "player3":
        return "cautious"
    else:
        return "aleatory"