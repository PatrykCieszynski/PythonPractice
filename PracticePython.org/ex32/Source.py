import random


def hangman(word, good_guesses):
    for l in word:
        if l in good_guesses:
            print(l," ", end='')
        else:
            print("_ ", end='')
    print("\n")


def guess(word, letter):
    if letter in word:
        return 1
    else:
        return 0


def check(letter, guessedletters):
    if letter in guessedletters:
        return 0
    else:
        guessedletters.append(letter)
        guessedletters.sort()
        return 1


def randomword(number):
    i=0
    with open('sowpods.txt', 'r') as f:
        line = f.readline()
        while line:
            i += 1
            line = line.strip("\n")
            if number == i:
                return line
            line = f.readline()


def game(word, counter, guessedletters, good_guesses, wordset):
    print("Welcome to Hangman\n")
    while len(good_guesses) != len(wordset):
        hangman(word, good_guesses)
        print("You have ", counter, " incorrect guesses left")
        print("Your guesses: ", guessedletters)
        if(counter == 0):
            return 0
        letter = input("Guess your letter: ")[0].upper()
        print(letter)
        while check(letter, guessedletters) == 0:
            print("You already guessed this letter")
            letter = input("Guess your letter: ")[0].upper()
            if check(letter, guessedletters) == 1:
                break
        if guess(word, letter) == 1:
            good_guesses.append(letter)
            print("Good Guess!")
        else:
            counter -= 1
            print("Incorrect!")
        if wordset == good_guesses:
            return 1


playagain = 'y'

while playagain == 'y':
    number = random.randint(1,267751)
    word = randomword(number)
    letter = ""
    counter = 6
    guessedletters = []
    good_guesses = []
    wordset = set(word)

    if game(word, counter, guessedletters, good_guesses, wordset) == 0:
        print("You lose :(")
    else:
        print("You win Yay :)")
    print("The word is",word)
    playagain = input("Want to play again? (y/n)")