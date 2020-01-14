import re


def postcodegen():
    a = "79-900"
    b = "80-155"
    result = []
    a = a.split("-")
    b = b.split("-")
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    while a <= b:
        if a[1] < 10:
            result.append(str(a[0]) + "-" + str(a[1]) + "00")
        elif(a[1] > 9) and (a[1] < 100):
            result.append(str(a[0]) + "-" + str(a[1]) + "0")
        else:
            result.append(str(a[0]) + "-" + str(a[1]))
        a[1] += 1
        if a[1] == 1000:
            a[0] += 1
            a[1] = 0
    for x in result:
        print(x)


def missingelements():
    n = 10
    list = []
    for x in range(1, n+1):
        list.append(x)

    listtocheck = (input("Write numbers for list: "))
    listtocheck = re.split("[\[\]]", listtocheck)
    listtocheck = listtocheck[1].split(",")
    listtocheck = [int(x) for x in listtocheck]
    print([x for x in list if x not in listtocheck])


def generatelist():
    list = [float(2)]
    x = list[0]
    while x != 5.5:
        x += 0.5
        list.append(x)
    for x in list:
        print(x)


postcodegen()
missingelements()
generatelist()
