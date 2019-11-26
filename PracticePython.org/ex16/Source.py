import random


def get_integer(text="Give me a number: "):
    return int(input(text))


def determine_char():
    return random.randint(0, 73)


def rand_lowercase():
    return chr(random.randint(97, 122))


def rand_uppercase():
    return chr(random.randint(65, 90))


def rand_number():
    return str(random.randint(0, 9))


def rand_symbol():
    return chr(random.choice([64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126]))


password = []
length = get_integer("Give me password length: ")
i = 0
while i != length:
    c = determine_char()
    if c >= 0 and c < 27 :
        password.append(rand_lowercase())
    elif c > 26 and c < 54 :
        password.append(rand_uppercase())
    elif c > 53 and c < 64 :
        password.append(rand_number())
    elif c > 63 and c < 74 :
        password.append(rand_symbol())
    i += 1
print("".join(password))
