category_counter = {}
names_counter = {}

with open('file.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip("\n")
        if line not in names_counter:
            names_counter[line] = 1
        else:
            names_counter[line] += 1
        line = open_file.readline()

print(names_counter)

with open('challenge.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip("\n")
        line = line[3:-25]
        if line not in category_counter:
            category_counter[line] = 1
        else:
            category_counter[line] += 1
        line = open_file.readline()

print(category_counter)
