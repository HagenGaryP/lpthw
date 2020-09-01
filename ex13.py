# Exercise 13: Parameters, Unpacking, Variables

# SORRY, THIS IS MESSY FROM ALL THE NOTES.

# In this exercise we will cover onemore input method you can use to pass 
#   variables to a script ('script' being another name for your .py files).
# We type python ex13.py to run that specific script, and the ex13.py part
#   of the command is called an argument.
# Now we will write a script that also accepts arguments.

# NOTE: To run a script with command line arguments, you must pass in the
#           proper amount of args.
#   For example, the command could look like any of the following:
# > python ex13.py first 2nd 3rd
# > python ex13.py stuff things that
# > python ex13.py hip hiphop hiphopanonymous

# If given fewer arguments, a ValueError will occur, telling you
#   "not enough values to unpack (expected 4, got 3)"
# If given more args - "ValueError: too many values to unpack (expected 4)"

# import adds features to script from Python feature set
from sys import argv   # argv  is the argument variable (standard name)
# this argv variable holds the arguments you pass to your script when executed.

# The next uncommented line "unpacks" argv so that, rather than holding all 
# the arguments, it gets assigned to four variables you can work with.
script, first, second, third = argv
# "unpack" basically means Python will "take whatever is in argv, unpack it,
#   and assign it to all of these variables on the left in order."

print("The script is called:", script) # first arg in command line after "python"
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third) # 4th and last arg in command line

#               Features Have Another Name --> modules (or libraries)


# Features are the things you import to make the Python program do more, 
#   but only the author, Zed Shaw, refers to them as "features".
# He used that name because he wanted to trick the reader into learning
#   what they are without confusing you with jargon.

# These "features" are actually called "modules", and will be referred to
#   as such from here out.  He will say things like, "You want to import
#   the sys module."  They are also called "libraries" by other programmers.


