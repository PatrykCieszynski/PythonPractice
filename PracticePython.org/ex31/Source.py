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


word = "EVAPORATE"
letter = ""
guessedletters = []
good_guesses = []
wordset = set(word)
print("Welcome to Hangman\n")
while len(good_guesses) != len(wordset):
    hangman(word, good_guesses)
    print("Your guesses: ",guessedletters)
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
        print("Incorrect!")

print("Good Job its", word)