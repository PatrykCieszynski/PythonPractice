def player1(game):
    coords = input("Player 1 move (format row,col ex: 1,3): ")
    x = int(coords[0])-1
    y = int(coords[-1])-1
    if game[x][y] != "X" and game[x][y] != "O":
        game[x][y] = "X"
        return 1
    else:
        print("unsupported move")
        return 0


def player2(game):
    coords = input("Player 2 move (format row,col ex: 1,3): ")
    x = int(coords[0]) - 1
    y = int(coords[-1]) - 1
    if game[x][y] != "X" and game[x][y] != "O":
        game[x][y] = "O"
        return 1
    else:
        print("unsupported move")
        return 0


game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for x in game:
    print(x)
counter = 0
while 1:
    while player1(game) == 0:
        player1(game)
    counter += 1
    for x in game:
        print(x)
    if counter == 9:
        break
    while player2(game) == 0:
        player2(game)
    counter += 1
    for x in game:
        print(x)
