# number of cars
cars = 100
space_in_car = 4 #available space in a car
drivers = 30 # available number of drivers
passengers = 90 # total number of available passengers
cars_not_driven = cars - drivers # total cars which are not driven
cars_driven = drivers # total cars which are driven
carpool_capacity = cars_driven * space_in_car # total carpool capacity which is multiplication of total number of cars driven and available space in car
average_passengers_per_car = passengers / cars_driven # average passengers per car which is division of passengers and total dars driven

print("There are ", cars, " cars available.")
print("There are only ", drivers, " drivers available.")
print("There will be ", cars_not_driven, " empty cars today.")
print("We can trasport ", carpool_capacity, " people today.")
print("We have ", passengers, " to carpool today.")
print("We need to put about ", average_passengers_per_car, " in each car.")

'''
When I wrote this program the first time I had a mistake, and Python told me about it like this:
Traceback (most recent call last):
File "ex4.py", line 8, in <module>
average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined
Explain this error in your own words. Make sure you use line numbers and explain why.
'''

print("In line 8, you have used the unknow variable which is car_pool_capacity instead of carpool_capacity")

'''
1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
'''
print("Nothing specific will happen, it will just show carpool_Capacity as 120 not 120.0, other than that no changes will occur in the program. But yes, floating point numbers are used for more accurate computations.")
