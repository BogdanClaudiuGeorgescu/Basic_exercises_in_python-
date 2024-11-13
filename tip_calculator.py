# The Challenge:
# Description: Create a program that calculates the tip amount and total bill based on the bill amount and
# the percentage tip the user wants to give.


# The Solution:
# I start by importing pyinputplus to check that the input I get is only accepted if of float type.
import pyinputplus as py

# I ask the user for 2 inputs: one for the amount to pay out and one for how much of that amount the user would like
# to tip (in the form of a percentage). I also set minimum and maximum amounts.
money_spent = float(py.inputFloat("How much is your bill? -> ", min=5))
tip_percentage = float(py.inputFloat("What percentage of your bill would you like to leave as a tip? -> ",
                                     min=10, max=20))

# I create a variable that will contain the value of the tip.
tip_amount = 0

# I take the precaution of checking that the tip percentage is one of 3 preset values and if so, I calculate
# the tip using a conditional statement.
while tip_percentage not in [10, 15, 20]:
    money_spent = int(input("How much is your bill? -> "))
    tip_percentage = int(input("What percentage of your bill would you like to leave as a tip? -> "))
else:
    if tip_percentage == 10:
        tip_amount = money_spent * 0.10
    elif tip_percentage == 15:
        tip_amount = money_spent * 0.15
    elif tip_percentage == 20:
        tip_amount = money_spent * 0.20

# I create
total_amount = tip_amount + money_spent

# I print out the value of the tip and the total amount of money to be paid.
print(f"The tip is {tip_amount}.")
print(f"The total amount to pay out is {total_amount}.")


