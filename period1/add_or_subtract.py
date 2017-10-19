# Add/Subtract Two Numbers
# Dan Schellenberg
# Oct 19, 2017

operation_chosen = input("Would you like to add or subtract? ")

first_number = input("Please enter the first number: ")
second_number = input("Please enter the second number: ")

#convert input into numbers
first_number = float(first_number)
second_number = float(second_number)

if operation_chosen == "add":
    