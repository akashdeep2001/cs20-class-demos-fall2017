# Gas Mileage Calculator
# Dan Schellenberg
# Oct 19, 2017

amount_of_gas_used = input("How many litres did the trip take? ")
distance_travelled = input("How far did you drive (in km's): ")

#convert user input to numbers
amount_of_gas_used = float(amount_of_gas_used)
distance_travelled = float(distance_travelled)

car_efficiency = amount_of_gas_used/distance_travelled*100

#make the final answer look nicer!
car_efficiency = round(car_efficiency, 2) 

print("Your car used", car_efficiency, "L/100kms")