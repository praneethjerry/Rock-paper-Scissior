import random

computer=random.choice([1,-1,0])
print("Welcome to the Rock, Paper,Scissior Game!")
name=input("Enter your Name : ")
print('Enter from the above choices "Rock","Paper","Scissior"')
user=input().lower()
dict={"scissior":1,"paper":-1,"rock":0}
reversedict={1:"scissior",-1:"paper",0:"rock"}
if user in dict:
 userchoice= dict[user]
 print(f"YOU HAVE CHOOSEN {reversedict[userchoice].upper()},COMPUTER HAS CHOOSEN {reversedict[computer].upper()}")
 if (computer==userchoice):
    print("The Game is Draw")
 else: 
      if(computer==1 and userchoice==-1):  #2
        print("Computer Wins")
      elif(computer==1 and userchoice==0): #1
        print(f"{name.capitalize()} Wins") 
      if(computer==0 and userchoice==1): #-1
        print("Computer Wins")
      elif(computer==0 and userchoice==-1): #1
        print(f"{name.capitalize()} Wins")
      if(computer==-1 and userchoice==0): #-1
        print("Computer Wins")
      elif(computer==-1 and userchoice==1):  #-2
        print(f"{name.capitalize()} Wins")      
else:
 print('"Invalid choice! Please enter from the above choices: "Rock", "Paper", "Scissor"')

    