# Exercise 5: More Variables and Printing

name = 'Gary P. Hagen'
age = 31
height = 76 # inches
weight = 220 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
cm = 2.54 * height
kg = 0.453592 * weight

print(f"Let's talk about {name}.")
print(f"He's {height} inches, or {cm} centimeters tall.")
print(f"He weighs {weight} pounds, or {kg} kilograms.")
print(f"He has {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} inches, and {weight} lbs, I get {total}.")
print(f"If I add {age}, {cm} centimeters, and {kg} kilograms, I get {total}.")