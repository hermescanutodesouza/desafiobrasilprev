from board import createboard, setpostion, rolldice, getplayers
from rules import Rules


def game(debug=True):
    # set the players
    players = getplayers()

    # set the board , random values for house
    board = createboard()
    if debug:
        print(players)
        print(board)

    counter = 0
    while counter < 1000:
        if debug:
            print("\n\n----> Round   ", counter)

        for index, _ in players.iterrows():

            countorow = players.shape[0]
            if countorow <= 1:
                if debug:
                    print("=" * 60, "\n")
                    print("We have a Winner, shift", counter, "\n")
                    print(players)
                    print("\n")
                    # print(board)
                    print("=" * 60, "\n")
                df = players.reset_index()
                return {"winner": df['player'][0],
                        "shift": counter}
                break

            dice = rolldice()

            playername = players['player'][index]
            playermoney = players.at[index, 'money']

            current = players['position'][index]
            new, lap = setpostion(players['position'][index], dice)
            players.at[index, 'position'] = new
            if debug:
                print(playername,
                      "rolled the dice and get", dice,
                      ", current postion", current,
                      "new postion", new)

            # check the current player reach the end of lap
            if lap:
                players.at[index, 'money'] = playermoney + 100
                playermoney = players.at[index, 'money']
                if debug:
                    print(playername, "completed a lap of the track and wins 100 , now you have",
                          players.at[index, 'money'])

            # check if the house has a owner
            if board['owner'][new] == '':
                buy = board['buy'][new]
                if debug:
                    print(playername, "found a free house to buy on position", new, ",cost", buy, "rent",
                          board['rent'][new])
                if Rules(playername, playermoney, buy, board['rent'][new], False).aply():
                    board.at[new, 'owner'] = playername
                    players.at[index, 'money'] = playermoney - buy
                else:
                    if debug:
                        print("Rule say no to buy")

            else:
                # if has a owner than pay the rent
                rent = board['rent'][new]
                if debug:
                    print(playername, "found a house with a owner on position", new, ",must pay the rent",
                          rent)
                players.at[index, 'money'] = playermoney - rent

            # check money is positive, if is not then player is out of the game lose all the rouse in the game
            if players['money'][index] < 0:
                if debug:
                    print(playername, "is out of the game ", players['money'][index])
                players = players.drop([index])
                board['owner'] = board['owner'].apply(lambda x: '' if x == playername else x)

        counter += 1

        if debug:
            print("\n")
            print(players)
            print("\n")
    else:
        # counter = 1000:
        if debug:
            print("=" * 60, "\n")
            print("Round 1000")
            print(players)
            print("=" * 60, "\n\n")
    winner = players[players.money == players.money.max()].reset_index(drop=True)['player'][0]

    return {"winner": winner,
            "shift": counter,
            }
