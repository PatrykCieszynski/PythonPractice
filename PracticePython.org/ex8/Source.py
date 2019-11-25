def winner(p1_choice,p2_choice):
    if (p1_choice == "rock" and p2_choice == "scissors") or (p1_choice == "scissors" and p2_choice == "paper") or (p1_choice == "paper" and p2_choice == "rock"):
        print(player1," Wins!!!")
    elif (p2_choice == "rock" and p1_choice == "scissors") or (p2_choice == "scissors" and p1_choice == "paper") or (p2_choice == "paper" and p1_choice == "rock"):
        print(player2, " Wins!!!")
    else:
        print("Draw")


player1 = input("Player 1 Name: ")
player2 = input("Player 2 Name: ")
quit=""

while (quit != "q"):
    p1_choice = input("Type Rock/Scissors/Paper: ")
    p2_choice = input("Type Rock/Scissors/Paper: ")
    p1_choice=p1_choice.lower()
    p2_choice=p2_choice.lower()
    winner(p1_choice,p2_choice)
    quit = input("Type q to quit, anything else will restart game")
