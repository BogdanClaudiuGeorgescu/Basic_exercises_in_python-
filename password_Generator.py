import random

# lists of available characters available to the user
list_Of_Lower_Case_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                              "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]
list_Of_Upper_Case_Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                              "Q", "R", "S","T", "U", "V", "W", "X", "Y", "Z"]
list_Of_Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_Of_Special_Characters = [".", "!", "?", "@", "#", "$", "%", "^", "&", "*", "()", "_", "-", "+", "=", "[]", "{}"]

# an empty list that will contain a random mix of characters from all 4 lists above
mixed_list = []

# loops that extract items from the 4 source lists above and append them to the mixed_list
for item1 in range( 1,5):
    item1 = random.choice(list_Of_Lower_Case_Letters)
    mixed_list.append(item1)

for item2 in range( 1,5):
    item2 = random.choice(list_Of_Upper_Case_Letters)
    mixed_list.append(item2)

for item3 in range( 1,5):
    item3 = random.choice(list_Of_Numbers)
    mixed_list.append(item3)

for item4 in range( 1,5):
    item4 = random.choice(list_Of_Special_Characters)
    mixed_list.append(item4)

# random.shuffle mixes the items in mixed_list in a random order every time the code is run.
# print(mixed_list)
random.shuffle(mixed_list)

# this join removes any empty spaces between the characters making up the password
result ="".join(mixed_list)
# print(mixed_list)

# and now we get the final result
print(f"This is your requested password: {result}")




