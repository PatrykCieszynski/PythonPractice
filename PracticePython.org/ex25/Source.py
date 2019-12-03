print("Think of a number between 0 and 100")
guess = 50
counter = 1
win = 0
low = 0
hihg = 100
while win != 1:
    print("Guess number ", counter)
    print("My guess is ", int(guess))
    answer = input("Is my number lower, higher or just right? ")
    if answer == 'lower':
        low = guess + 1
    elif answer == 'higher':
        high = guess - 1
    elif answer == 'right':
        win = 1
    else:
        print("Something went wrong,reset...")
        counter -= 1
    counter += 1
    guess = (low + high) / 2
