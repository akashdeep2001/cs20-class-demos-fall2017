# Gas Mileage Calculator
# Dan Schellenberg
# Oct 19, 2017

kilometers_driven = input("How many kilometers did you drive? ")
litres_used = input("How many litres of gas did it take? ")

#convert user input to numbers
kilometers_driven = float(kilometers_driven)
litres_used = float(litres_used)

gas_usage = litres_used / kilometers_driven * 100

print("Your car is using", gas_usage, "L/100km")