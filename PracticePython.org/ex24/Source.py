

def draw(sizex, sizey, size):
    for x in range(size):
        for y in range(sizex):
            print(" ---", end='')
        print(" ---")
        for z in range(sizey):
            print("|   ", end='')
        print("|   ")
    print(" ---"*sizey)


def check(sizex, sizey):
    a = sizex - sizey
    if sizex > sizey:
        size = sizex
    else:
        size = sizey
    if sizex == sizey:
        draw(sizex - 1, sizey, size)
    elif sizex > sizey:
        draw(sizex - 1, sizey + a, size - a)
    else:
        draw(sizex - 1, sizey + a, size)


check(int(input("x ")), int(input("y ")))
