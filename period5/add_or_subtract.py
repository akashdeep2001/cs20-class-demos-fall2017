# Add/Subtract Two Numbers
# Dan Schellenberg
# Oct 23, 2017

operator_chosen = input("Would you like to add or subtract? ")

if operator_chosen == "add":
    number_one = input("Please enter the first number: ")
    number_two = input("Please enter the second number: ")

    #convert user input into numbers
    number_one = float(number_one)
    number_two = float(number_two)

    the_answer = number_one + number_two
    print("The answer when you add is", the_answer)

elif operator_chosen == "subtract":
    number_one = input("Please enter the first number: ")
    number_two = input("Please enter the second number: ")

    #convert user input into numbers
    number_one = float(number_one)
    number_two = float(number_two)
    the_answer = number_one - number_two
    print("The answer when you subtract is", the_answer)
    
else:
    print("Error. Please enter 'add' or 'subtract'.")