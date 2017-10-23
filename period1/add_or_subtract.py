# Add/Subtract Two Numbers
# Dan Schellenberg
# Oct 19, 2017

operation_chosen = input("Would you like to add or subtract? ")

if operation_chosen == "add":
    first_number = input("Please enter the first number: ")
    second_number = input("Please enter the second number: ")

    #convert input into numbers
    first_number = float(first_number)
    second_number = float(second_number)
    
    the_answer = first_number + second_number
    print("The answer when you add is", the_answer)

elif operation_chosen == "subtract":
    first_number = input("Please enter the first number: ")
    second_number = input("Please enter the second number: ")

    #convert input into numbers
    first_number = float(first_number)
    second_number = float(second_number)
    
    the_answer = first_number - second_number
    print("The answer when you subtract is", the_answer)

else:
    print("Error. I don't know what that means. Please enter 'add' or 'subtract'.")
    