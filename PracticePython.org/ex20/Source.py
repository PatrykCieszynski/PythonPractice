def check(number, list):
    while len(list) != 1:
        length = len(list)
        index = int(len(list) / 2)
        if length % 2 != 0:
            index += 1
        middle = list[index]
        if middle > number:
            new_list = list[0:index]
        else:
            new_list = list[index:length]
        list = new_list
    return list[0] == number


if __name__ == "__main__":
    list = [int(x) for x in ((input("Give me a list: ")).split(','))]
    list.sort()
    number = int(input("Give me a number: "))
    print(check(number, list))

