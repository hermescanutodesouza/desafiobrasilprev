import pandas as pd

from board import getplayerstatus
from game import game

if __name__ == '__main__':
    player, round, counteshift = [], [], 0
    for i in range(0, 300):
        result = game(debug=False)
        print("Game:{} Winner:{} Shift:{}".format(i, result['winner'], result['shift']))
        player.append(result['winner'])
        round.append(result['shift'])
        if result['shift'] == 1000:
            counteshift += 1

    df = pd.DataFrame({"player": player, "shift": round})
    allplayers = ((df['player'].value_counts() / df['player'].count()) * 100)
    print("\nResults\n")
    winner = df['player'].describe()['top']
    print("Winner {} {} \n".format(winner, getplayerstatus(winner)))
    print("Shifts average {:.2f}\n".format(df['shift'].mean()))
    print("Time out {}\n".format(counteshift))
    for index, value in allplayers.items():
        print("{} {:.2f} %".format(index, value))
