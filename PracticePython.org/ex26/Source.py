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
    if list[0][0] == list[1][1] == list[2][2] == 2:
        return 2
    elif list[0][0] == list[1][1] == list[2][2] == 1:
        return 1
    else:
        return 0


def winner(list, sizex, sizey):
    winnervh = vert_hori(list, sizex, sizey)
    winnerd = diagonal(list)
    if winnervh == 2 or winnerd == 2:
        print("player 2 wins")
    elif winnervh == 1 or winnerd == 1:
        print("player 1 wins")
    else:
        print("draw")


sizex = 3
sizey = 3
list = [[2, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]
winner(list, sizex ,sizey)
