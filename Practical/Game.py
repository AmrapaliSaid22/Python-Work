'''
computer_choice = rock/paper/scissors
user_choice = input
'''

import random

options=["rock","paper","scissors"]

computer_choice=random.choice(options)
user_choice=input("Enter your choice [rock/paper/scissors] = ")

if user_choice=="rock" and computer_choice=="scissors":
    print("You won")
elif user_choice=="paper" and computer_choice=="rock":
    print("You won")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You won")
elif user_choice==computer_choice:
    print("Game tied")
else:
    print(f"You lost, computer choose {computer_choice}")




