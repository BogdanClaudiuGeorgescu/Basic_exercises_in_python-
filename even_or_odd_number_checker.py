# The Challenge: Ask the user to input a number and determine if it is Even or Odd.
# You can also extend it by adding features like checking if it's Positive, Negative, or Zero.


# The Solution: 
user_input = int(input("Please provide a number: "))
print(user_input)

if user_input % 2 == 0:
    x = "and Even."
    if user_input == 0:
        print(f"The number is Zero {x}")
    elif user_input > 0:
        print(f"The number is Positive {x}")
    elif user_input < 0:
        print(f"The number is Negative {x}")

else:
    y = "and Odd."
    if user_input == 0:
        print(f"The number is Zero {y}")
    elif user_input > 0:
        print(f"The number is Positive {y}")
    elif user_input < 0:
        print(f"The number is Negative {y}")
