# Exercise 18: Names, Variables, Code, Functions

# Functions can do three things: 
#       1.  The name pieces of code the way variables name strings and numbers. 
#       2.  They take arguments the way your scripts take argv. 
#       3.  Using 1 and 2, they let you make your own "mini-scripts" or "tiny commands."


# To create a function in Python, use the word "def"

# Making four different functions that work like the scripts.

# this one is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# that *args is actually pointletss. We can just do this instead...
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no arguments
def print_none():
    print("I got nothin for ya, sweetheart.")


print_two("Gary", "Hagen")
print_two_again("Gary", "Hagen")
print_one("First!")
print_none()

#               Breaking down the functions

# the print_two functions is most similar to what we already know from making scripts:
#   1.  We tell Python we want to make a function using def for "define."
#   2.  On the same line as def we give the function a name.  In this case, "print_two", 
#           but it could be anything.  Try to keep short if possible.
#   3.  We tell it we want *args (asterisk args), which is a lot like the argv parameter
#           but for functions.  This HAS to go inside parentheses to work.
#   4.  We end this line with a : (colon) and start indenting.
#   5.  After the colon, all the lines that are indented four spaces will become attached
#           to print_two.  Our first indented line is one that unpacks args, same as in scripts.
#   6.  To demonstrate how it works we print these arguments out, just like in a script.

# The problem with print_two is that it's not the easiest way to make a function.
# In Python, we can skip the whole unpacking arguments and just use the names we want
#   right inside parentheses.  That's what print_two_again does.


#               Function Checklist

#   1.  Start function with "def"   
#   2.  Function name should have only characters and _ (underscore) characters.    
#   3.  Must put open paranthesis right after the function name.    
#   4.  Arguments go after the parenthesis and are separated by commas. 
#   5.   Each argument must be unique (no duplicated names) 
#   6.  Close parenthesis, followed by a colon after the args.  
#   7.  Indent all lines of code you want in the function four spaces.  
#   8.  End the function by going back to writing with no indent (called dedenting).

# When you run ("use" or "call") a function, check these things:
#   1.  Did you call/use/run this function by typing its name?
#   2.  Did you put the ( character after the name to run it?
#   3.  Did you put the values you want into the parentheses separated by commas?
#   4.  Did you end the function call with a ) character?