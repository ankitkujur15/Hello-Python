

import random

choices = ["rock", "paper", "scissor"]

user_choice = input("choose between - 'rock', 'paper' or 'scissor': ").lower()

computer_choice = random.choice(choices)
print (f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("--------- Its a tie!----------")

elif (user_choice == "rock" and computer_choice == "scissor") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissor" and computer_choice == "paper"):
    print(" Congratulations you win🎉 ")

elif (user_choice == "rock" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "scissor") or \
     (user_choice == "scissor" and computer_choice == "rock"):
    print("Sorry you lose! 😢 ")

else:
    print("Invalid input! Please choose between 'rock', 'paper' or 'scissor'")
