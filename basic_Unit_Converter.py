# The Challenge: Build a simple unit converter that can convert between kilometers and miles, Celsius and Fahrenheit,
# or other basic units of measurement.

# The Solution:

import pyinputplus as pyip

while True:
    funky_user_input = int(pyip.inputInt(
        "Please type in one of the following options: \n 1. Press 1 to convert miles to kilometers.\n "
        "2. Press 2 to convert kilometers to miles. \n 3. Press 3 to convert degrees Fahrenheit to degrees Celsius. "
        "\n 4. Press 4 to convert degrees Celsius to degrees Fahrenheit. \n\n here -> "))
    if funky_user_input in range(1,5):
        if funky_user_input == 1:
            miles_to_kilometers = input("How many miles? ")
            number_of_kilometers = round(float(miles_to_kilometers) * 1.60934, 2)
            print(f"The number is {number_of_kilometers} kilometers.")
        elif funky_user_input == 2:
            kilometers_to_miles = input("How many kilometers? ")
            number_of_miles = round(float(kilometers_to_miles) * 0.621371, 3)
            print(f"The number is {number_of_miles} kilometers.")
        elif funky_user_input == 3:
            fahrenheit_to_celsius = input("How many degrees Fahrenheit? ")
            number_of_degrees_Fahrenheit = round((float(fahrenheit_to_celsius) - 32) * (5/9), 1)
            print(f"The number is {number_of_degrees_Fahrenheit} degrees Celsius.")
        elif funky_user_input == 4:
            celsius_to_fahrenheit = input("How many degrees Celsius? ")
            number_of_degrees_Celsius = round(float(celsius_to_fahrenheit) * (9/5) + 32, 4)
            print(f"The number is {number_of_degrees_Celsius} degrees Fahrenheit.")
        break
    else:
        funky_user_input = input(
            "Please type in one of the following options: \n 1. Press 1 to convert miles to kilometers.\n "
            "2. Press 2 to convert kilometers to miles. \n 3. Press 3 to convert degrees Fahrenheit to degrees Celsius. "
            "\n 4. Press 4 to convert degrees Celsius to degrees Fahrenheit. \n\n here -> ")
