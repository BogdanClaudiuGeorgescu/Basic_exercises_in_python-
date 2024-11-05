arithmetic_operation = input("What operation do you want to perform? Please reply by typing in either"
                             " \"addition\", \"subtraction\", \"multiplication\" or \"division\" -> ").lower()

first_number= int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

if arithmetic_operation == "addition":
    result1 = first_number + second_number
    print(round(result1, 2))
elif arithmetic_operation == "subtraction":
    result2 = first_number - second_number
    print(round(result2, 2))
elif arithmetic_operation == "multiplication":
    result3 = first_number * second_number
    print(round(result3, 2))
elif arithmetic_operation == "division":
    result4 = first_number / second_number
    print(round(result4, 2))


