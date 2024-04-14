name = 'Div S. Kumar'
age = 32
height = 165 #cms
weight = 65 #kg
eyes = 'black'
teeth = 'White'
hair = 'black'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} Kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}")

weight_in_pounds = round(weight * 2.20462)


height_in_inches = round(height / 2.54)

print(f"Height in inches is {height_in_inches} and weight in pounds is {weight_in_pounds}.")
new_total = age + weight_in_pounds + height_in_inches
print(f"If I add {age}, {weight_in_pounds} and {height_in_inches}, I get {new_total}.")
