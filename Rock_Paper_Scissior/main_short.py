import random

computer = random.choice([1, -1, 0])
print("Welcome to the Rock, Paper, Scissors Game!")
name = input("Enter your Name : ")
print('Enter from the above choices "Rock", "Paper", "Scissor"')
user = input().lower()

dict = {"scissior": 1, "paper": -1, "rock": 0}
reversedict = {1: "scissior", -1: "paper", 0: "rock"}

if user in dict:
    userchoice = dict[user]
    print(f"YOU HAVE CHOOSEN {reversedict[userchoice].upper()}, COMPUTER HAS CHOOSEN {reversedict[computer].upper()}")

    if computer == userchoice:
        print("The Game is Draw")
    else:
        if (computer == 1 and userchoice == -1) or (computer == 0 and userchoice == 1) or (computer == -1 and userchoice == 0):
            print("Computer Wins")
        else:
            print(f"{name.capitalize()} Wins")
else:
    print('Invalid choice! Please enter from the above choices: "Rock", "Paper", "Scissor"')
