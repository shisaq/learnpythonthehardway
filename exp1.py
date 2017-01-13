# -*- coding: utf-8 -*-
# we have 100 cars
cars = 100
# every car has 4 spaces
space_in_a_car = 4.0
# we have 30 drivers
drivers = 30
# we have 90 passengers
passengers = 90
# we have 70 cars not been driven by any drivers
cars_not_driven = cars - drivers
# we have 30 cars driven by drivers
cars_driven = drivers
# the total space we have: 120
carpool_capacity = cars_driven * space_in_a_car
# 3 passengers in 1 car on everage
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaliable."
print "There are only", drivers, "deivers avaliable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"
