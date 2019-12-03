

def getlist(filename):
    list = []
    with open(filename + '.txt', 'r') as open_file:
        line = open_file.readline()
        while line:
            line = line.strip("\n")
            list.append(int(line))
            line = open_file.readline()
    return list


primenumbers = getlist("primenumbers")
happynumbers = getlist("happynumbers")
primehappy = [x for x in primenumbers if x in happynumbers]

print(primehappy)
