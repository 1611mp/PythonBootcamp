# Guessing Game Project Infinite Play

import random
random_number = random.randint(1,20)

# guess = None

while True: # guess != random_number:
    guess = int(input("Please guess a number between 1 and 20: "))
    if guess > random_number:
        print("Guess Lower")
    elif guess < random_number:
        print("Guess Higher")
    else:
        print("You guessed correctly!!!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!!!")
            break