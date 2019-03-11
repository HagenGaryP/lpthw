# Exercise 6: Strings and Text

# In ex5, you embed variables inside a string by using a special {} sequence and then
#   put the variable you want inside the {} characters.
# You also must start the string with the letter 'f' for "format,"
#   as in f"Hello {somevar}".  This f before the double-quotes " and the {} characters
#   tell Python 3 to format the strings and put those variables in there.

# Strings can contain any number of variables that are in your Python script.
# The use of a special type of string to "format"; called an "f-string" and looks like this:
#       f"some stuff here {avariable}"
#       f"some other stuff {anothervar}"

types_of_people = 10
# the variable x uses an "f-string" 
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Python also has another kind of formatting using the .format() syntax.
# Used to apply a format to an alread-created string, such as in a loop.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)