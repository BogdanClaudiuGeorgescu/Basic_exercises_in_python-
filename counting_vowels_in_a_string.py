# The Challenge:

# Create a program that takes a string input and counts how many vowels are in the string.


# The Solution:

# I start by creating two lists: one that contains all the vowels in the English language vocabulary
# and one that contains all the consonants.
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# I then create two variables with the value zero that will hold the number of vowels and consonants in the user input
# that will be provided.
number_of_vowels = 0
number_of_consonants = 0

# Next, I ask the user for input and split the given string into individual characters.
user_provided_string = input("Please type in a word -> ")
string_characters = list(user_provided_string)


# I create a loop to check that the information provided is indeed a word. If not, the user is prompted again.
for x in user_provided_string:
    if x not in string_characters:
        user_provided_string = input("Please type in a word -> ")

# I create another loop to check if the characters in the string provided are contained in either the list of vowels or
# the list of consonants. When a character coincides with the element of a list, the loop increments the
# number_of_vowels or number_of_consonants variables, respectively.
for x in user_provided_string:
    if x in string_characters:
        if x in vowels:
            number_of_vowels = number_of_vowels + 1
        if x in consonants:
            number_of_consonants = number_of_consonants + 1

# Finally, an f string prints out the numbers.
print(f"The word contains {number_of_vowels} vowel(s) & {number_of_consonants} consonant(s).")

