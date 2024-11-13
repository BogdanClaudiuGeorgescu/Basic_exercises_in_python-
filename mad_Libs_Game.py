# The Challenge:
# Ask the user for different words (like a noun, adjective, verb), and use them to fill in the blanks in
# a pre-defined story (Mad Libs). Print the final story to the console.


# Solution 1 (Order):

# I first create 4 inputs for the 4 pieces of information I need from the user so that I can create a poem.
color1 = input("What color would you like roses to be? -> ")
color2 = input("What color would you like violets to be? -> ")
someone = input("Who is your favorite girl? -> ")
someone_else = input("Who is OK too? -> ")

# I then use the variables storing the input to fill in the f string making up the poem and print it to the console.
print()
print("The poem you wrote:")
the_story = f" Roses are {color1},\n Violets are {color2},\n {someone} is my favorite,\n But {someone_else} is OK too."
print(the_story)


# Solution 2 (Chaos):

import random

color1 = input("What color would you like roses to be? -> ")
color2 = input("What color would you like violets to be? -> ")
someone = input("Who is your favorite girl? -> ")
someone_else = input("Who is OK too? -> ")

randomization_list = [color1, color2, someone, someone_else]

# I shuffle the elements of the list ...
random.shuffle(randomization_list)

# ... and then print out one element of the shuffled list at a time, whichever one it might be.
print()
print("The poem you wrote:")
the_story = (f" Roses are {randomization_list[0]},\n Violets are {randomization_list[1]},"
             f"\n {randomization_list[2]} is my favorite,\n But {randomization_list[3]} is OK too.")
print(the_story)