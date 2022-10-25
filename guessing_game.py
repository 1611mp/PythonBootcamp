# Guessing Game Project

import random
random_number = random.randint(1,20)

guess = None

while guess != random_number:
    guess = int(input("Please guess a number between 1 and 20: "))
    if guess > random_number:
        print("Guess Lower")
    elif guess < random_number:
        print("Guess Higher")
    else:
        print("You guessed correctly!!!")
