# Python Basics to Advanced Example
# Run: python number_guessing_game.py

import random

secret = random.randint(1, 100)
print("Guess a number from 1 to 100. Type q to quit.")
while True:
    answer = input("Guess: ").strip()
    if answer.lower() == "q": break
    try: guess = int(answer)
    except ValueError:
        print("Enter an integer or q."); continue
    if guess < secret: print("Too low")
    elif guess > secret: print("Too high")
    else:
        print("Correct!"); break
