import random


def get_list(text="Give me a number: "):
    return [int(x) for x in (input(text))]


def generatenumber():
    num.append(random.randint(1, 9))
    while len(num) != 4:
        i=random.randint(0, 9)
        if i not in num:
            num.append(i)


def check(a):
    i=0
    cows=0
    bulls=0
    for x in guess:
        if x in num:
            bulls += 1
        if x == num[i]:
            cows += 1
        i += 1
    return [cows, bulls-cows]


if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game!")
    num = []
    guess = []
    counter = 0
    generatenumber()
    while guess != num:
        guess=get_list("Enter a number:")
        counter += 1
        print(counter, "guess")
        results=check(guess)
        if results[0] > 1:
            print(results[0], "cows ")
        else:
            print(results[0], "cow ")
        if results[1] > 1:
            print(results[1], "bulls ")
        else:
           print(results[1], "bull ")
    print("You guessed it right, its", num)
