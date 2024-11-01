# Exercise 1:
# Print all even numbers from 1 to 20.
# Expected Result: 2 4 6 8 10 12 14 16 18 20

# The thinking behind the Solution:
# I create a loop with a range of numbers from 1 to 20. I divide all of them by 2.
# The numbers that, when divided by 2, have a remainder of 0, get printed out as the solution to the exercise.

# The Solution:
print("The solution to Exercise 1:")
for number in range(1,21):
    if number % 2 == 0:
        print(number)
print("---")


# Exercise 2:
# Calculate the factorial of the number 5.
# Expected Result: 120

# The thinking behind the Solution:
# I create a range from 1 to 5. I then declare a variable "x" that contains the
# result of the multiplication between each number in turn and every number before it in the range.
# I then print "x" to get the result.

# The Solution:
print("The solution to Exercise 2:")
for number in range (1,6):
    x = number * (number - 1) * (number - 2) * (number - 3) * (number - 4)
print(x)
# print(f"the factorial number is {x}")
print("---")


# Exercise 3:
# Print the elements of a list in reverse order -> List: [10, 20, 30, 40, 50]
# Expected Result: 50 40 30 20 10

# The thinking behind the Solution:
# I create a list containing the numbers mentioned. I create a second list that
# will contain the same numbers but in reverse order. I make a loop that goes through each element of the original
# list and inserts it in the second list. I then print the second list.

# The Solution:
print("The solution to Exercise 3:")
list = [10, 20, 30, 40, 50]
reversed_order_list = []

for number in list:
    reversed_order_list.insert(0, number)
print(reversed_order_list)
print("---")


# Exercise 4:
# Print a pattern of stars in a right triangle format with 5 rows.
# Expected Result:
#     *
#     **
#     ***
#     ****
#     *****

# The thinking behind the solution:
# I create a range between 1 and 5. I multiply every element in the range with the string: "*"
# and store the result in the "result" variable. I print out the variable.

# The Solution:
print("The solution to Exercise 4:")
for star in range (1,6):
    result = star * "*"
    print(result)
print("---")


# Exercise 5:
# Sum all the numbers in a list -> List: [1, 2, 3, 4, 5]
# Expected Result: 15

# The thinking behind the Solution:
# I first create a list. I then declare a variable with the value of 0. Finally, I create a loop that adds each
# number in the list to the variable's initial value of 0.

# The solution:
print("The solution to Exercise 5:")
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total = total + number
print(total)
print("---")


# Exercise 6:
# Print the multiplication table of 7.
# Expected Result:  # 7 x 1 = 7
                    # 7 x 2 = 14
                    # 7 x 3 = 21
                    # 7 x 4 = 28
                    # 7 x 5 = 35
                    # 7 x 6 = 42
                    # 7 x 7 = 49
                    # 7 x 8 = 56
                    # 7 x 9 = 63
                    # 7 x 10 = 70

# The thinking behind the Solutions:
# Solution 1: I declare a variable with the value of 7. I create a loop with a range from 1 to 10. I then declare
              #  a variable inside the loop by which I multiply the number in the initial variable by every number
              #  in the range. Lastly, I print out an f string containing 7 as a string and the two variables.
# Solution 2: I create a loop containing a list (as opposed to a range). I then create a variable inside the loop
              # through which I multiply every list item by 7. Lastly, I print out an f string containing 7 as a
              # string and the two variables.

# Solution 1:
print("The 1st solution to Exercise 6:")
number_7 = 7
for number in range(1,11):
    multiplication = number * number_7
    print(f"7 * {number} = {multiplication}")
print("---")

# Solution 2:
print("The 2nd solution to Exercise 6:")
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    multiplication = number * 7
    print(f"7 * {number} = {multiplication}")
print("---")


# Exercise 7:
# Use Python to iterate through a list of dictionaries.

# The thinking behind the Solutions:
# I create 2 dictionaries. I put both dictionaries in a single variable. I create a for loop that prints out everything the list contains.

# The Solution:
print("The solution to Exercise 7:")
dictionary_a = {"a": "cat", "b": "dog"}
dictionary_b = {1: 100, 2: 200}

list_of_dictionaries = [dictionary_a, dictionary_b]

for list_item in list_of_dictionaries:
    print(list_item)
print("---")


# Exercise 8:
# Use an else statement inside a for loop.

# The thinking behind the Solution:
# I create a list with several elements and try to add a new element to it if the new
# element is not already in the list.

# The Solution:
print("The solution to Exercise 8:")
exercise_8_List = ["bee", "bird", "aeroplane"]

element_0 = "bee"
element_1 = "rocket"

if element_0 not in exercise_8_List:
    exercise_8_List.append(element_0)
else:
    exercise_8_List.append(element_1)
print(exercise_8_List)
print("---")


# Exercise 9:
# Create a nested for loop.

# The thinking behind the Solution:
# I created 2 lists. Then I created a for loop that ads 1 to every element in the list and them multiplies
# the result by every number in the second list. Lastly, I print out the result of the multiplication.

# The Solution:
print("The solution to Exercise 9:")
exercise_9_list_1 = [2, 3, 4]
exercise_9_list_2 = [5, 6, 7]

for item in exercise_9_list_1:
    addition = item + 1
    for number in exercise_9_list_2:
        multiplication = addition * number
        print(multiplication)
print("---")


# Exercise 10:
# Use a "continue" statement  inside a loop.

# The thinking behind the Solution:
# I create a tuple. I create a loop that compares every element with a given string. If the element is equal to the
# string, all elements in the tuple up to that string get printed out.


# The Solution:
print("The solution to Exercise 10:")
myTuple = ("a", "b", "c")

for element in myTuple:
    if element == "a":
        continue
    print(element)
print("---")


# Exercise 11:
# Use a break statement inside a loop.

# The thinking behind the Solution:
# I create a list of elements. I then create an empty list and then a loop. If the loop runs into a certain element,
# it stops and adds all the elements it already looped through to the empty list.

# The Solution:
print("The solution to Exercise 11:")
some_list = [1, 2, 3, 4]
some_other_list = []

for item in some_list:
    some_other_list.append(item)
    if item == 3:
        break
print(some_other_list)
print("---")


# Exercise 12:
# Use Python to loop and print multiples of 3 using a range() function.

# The thinking behind the solutions:
# Solution 1: I create an empty list. I create a for loop that goes through every element in the list and checks if
            # the remainder of the division between each element and the number 3 is equal to 0. If so, the element gets appended
            # to the list. Lastly, I print out the list.
# Solution 2: I create a for loop that goes through every element in the list and checks if the remainder of the
            # division between each element and the number 3 is equal to 0. The numbers with this specific remainder
            # are then printed out.

# Solution 1:
print("The 1st solution to Exercise 12:")
multiples_of_3 = []

for element in range(1, 13):
    if element % 3 == 0:
        multiples_of_3.append(element)
print(multiples_of_3)
print("---")

# Solution 2:
print("The 2nd solution to Exercise 12:")
for element in range(1, 13):
    if element % 3 == 0:
        print(element)
print("---")

















