import random

def Guess(a,guess):
    if guess > a:
        print("Your guess is too high")
    elif guess < a:
        print("Your guess is too low")
    elif guess == a:
        print("You guessed it right")
    else:
        print("Something went wrong")


a=0
q = ""
guess = 0
counter = 0

while(q != "exit"):
    a = random.randint(1, 9)
    while(a != guess):
        counter += 1
        guess = int(input("Try to guess "))
        Guess(a,guess)
    print("You taken", counter, "guesses")
    counter = 0
    q = input("Type exit to close the game,anything else will restart guessing ")
