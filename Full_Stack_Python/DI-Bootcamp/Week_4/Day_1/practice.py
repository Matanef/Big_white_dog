#For example,  
#my_name = "Frank"  this line creates a name variable type: string 
#print("My name is {}".format(my_name))

# stores the amount of cars
cars = 100
print("type of cars is + {type(cars)}")
print("type of cars is ", {type(cars)})
space_in_a_car = 4.0
print(type(space_in_a_car))
drivers = 30
print(type(drivers))
passengers = 90
print(type(passengers))
cars_not_driven = cars - drivers
print(type(cars_not_driven))
cars_driven = drivers
print(type(cars_driven))
carpool_capacity = cars_driven * space_in_a_car
print(type(carpool_capacity))
average_passengers_per_car = passengers / cars_driven
print(type(average_passengers_per_car))


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")



age = input("How old are you? ")
print("You are {} years old".format(age))