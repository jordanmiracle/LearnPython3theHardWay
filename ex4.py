#  car variable
cars = 100 
#  space in car variable
space_in_a_car = 4
# drivers variable
drivers = 30
# passengers variable
passengers = 90
# cars not driven variable
cars_not_driven = cars - drivers
#  cars driven variable
cars_driven = drivers
# carpool variable
carpool_capacity = cars_driven * space_in_a_car
# passengers per car variable
average_passengers_per_car = passengers / cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

