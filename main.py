import random
#this is a python rock, paper, scissors game.
#R is rock, P is paper, S is scissors
while True:
    options = ["R","P","S"]
    computer = random.choice(options)
    print("You are required to select an  option: R for Rock, P for Paper, S for scissors")
    user_input= input("Select an option: R, P, S \n")
    print(f"\n You chose {user_input}, computer chose {computer}")
    if user_input==computer:
        print(f" Both players selected {user_input}. it's a tie, play again")
    elif user_input == "R":
        if computer == "S":
            print("Rock smashes scissors, you win")
        else:
            print("Paper covers rock, you loose.")
    elif user_input == "S":
        if computer == "P":
            print("Scissors cuts paper, you win")
        else:
            print("Rock smashes scissors, you loose")
    elif user_input == "P":
        if computer == "R":
            print("Paper covers rock, You win")
        else:
            print("Scissors cuts paper, You loose")
    play_again = input ("Play again, Yes or No ").lower()
    if play_again != "Yes":
        break
print("Thank you for playing")                                   