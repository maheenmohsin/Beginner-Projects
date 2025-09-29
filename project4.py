import random

print("Welcome to Rock, Paper, Scissor Game")

choices = ["rock", "paper", "scissor"]

user_choice = input("Enter your choice (rock, paper, scissor)").lower()

computer_choice = random.choice(choices)

print("Your choice", user_choice)
print("Computer choice", computer_choice)

if user_choice == computer_choice:
    print("It's a tie")
elif (user_choice == "rock" and computer_choice == "scissor") or \
     (user_choice == "paepr" and computer_choice == "rock")or \
     (user_choice == "scissor" and computer_choice == "paper"):
    print ("You win")
elif user_choice in choices:
    print("Computer wins")
else:
    print("Invalid input! Please choose rock, paper, scissor")