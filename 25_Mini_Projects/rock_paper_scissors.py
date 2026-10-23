# Python Basics to Advanced Example
# Run: python rock_paper_scissors.py

import random

choices = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors: ").lower()
if user not in choices: print("Invalid choice")
else:
    computer = random.choice(choices)
    print("Computer:", computer)
    if user == computer: print("Draw")
    elif (user, computer) in [("rock","scissors"), ("paper","rock"), ("scissors","paper")]: print("You win")
    else: print("Computer wins")
