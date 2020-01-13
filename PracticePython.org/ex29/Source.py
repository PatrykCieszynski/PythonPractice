def draw(sizex, sizey, size, list):
    i = 0
    j = 0
    for x in range(size):
        for y in range(sizex):
            print(" ---", end='')
        print(" ---")
        for z in range(sizey):
            print("| ", end='')
            print(list[i][j], end=' ')
            j += 1
        j = 0
        i += 1
        print("| ")
    print(" ---"*sizey)


def vert_hori(list, sizex, sizey):
    x = 0
    while x < sizex:
        row = set([list[x][0], list[x][1], list[x][2]])
        if len(row) == 1 and list[x][0] != 0:
            return list[x][0]
        x += 1
    y = 0
    while y < sizey:
        column = set([list[0][y], list[1][y], list[2][y]])
        if len(column) == 1 and list[0][y] != 0:
            return list[0][y]
        y += 1
    return 0


def diagonal(list):
    x = 0
    y = 0
    if list[0][0] == list[1][1] == list[2][2] == 'X':
        return 1
    elif list[0][2] == list[1][1] == list[2][0] == 'X':
        return 1
    elif list[0][0] == list[1][1] == list[2][2] == 'Y':
        return 2
    elif list[0][2] == list[1][1] == list[2][0] == 'Y':
        return 2
    else:
        return 0


def winner(list, sizex, sizey, counter):
    winnervh = vert_hori(list, sizex, sizey)
    winnerd = diagonal(list)
    if winnervh == 'Y' or winnerd == 2:
        print("player 2 wins")
        return 1
    elif winnervh == 'X' or winnerd == 1:
        print("player 1 wins")
        return 1
    elif counter == 9:
        print("draw")
        return 1


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


X = 3
Y = 3
list = [[0]*3 for i in range(3)]
draw(X-1, Y, 3, list)
counter = 0

while 1:
    while player1(list) == 0:
        player1(list)
    counter += 1
    draw(X-1, Y, 3, list)
    if winner(list, X-1, Y-1, counter) == 1:
        break
    while player2(list) == 0:
        player2(list)
    counter += 1
    draw(X-1, Y, 3, list)
    if winner(list, X-1, Y-1, counter) == 1:
        break
