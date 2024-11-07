# The Challenge:
# Write a short program that prints each number from 1 to 100 on a new line. For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


# Solution 1: FizzBuzz with a hardcoded fixed range 
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Solution 2: FizzBuzz with a dinamic range 
user_input_minimum = input("What is the minimum number you want for the range to to capped at? ")
user_input_maximum = input("What is the maximum number you want for the range to to capped at? ")

def test():
    user_input_minimum = input("What is the minimum number you want for the range to to capped at? ")
    user_input_maximum = input("What is the maximum number you want for the range to to capped at? ")

if user_input_maximum < user_input_minimum:
    print("The minimum number needs to be smaller by at least 10 than the maximum number. Try again! ")
    test()
else:
    for number in range (int(user_input_minimum), int(user_input_maximum)):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
