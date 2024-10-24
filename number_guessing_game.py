# The challenge: Create a game where the user has to guess a number between 1 and 100, with hints if the guess is too high or too low.

import random

the_number_to_be_guessed = random.randint(1,101)
print(the_number_to_be_guessed)

player_chosen_number = int(input("Take a guess :) "))

while player_chosen_number != the_number_to_be_guessed:
    if player_chosen_number > the_number_to_be_guessed:
        print("Try again but this time guess lower!")
    else:
        print("Try again but this time guess higher!")
    player_chosen_number = int(input("Try again :) "))
print("You guessed right!")

