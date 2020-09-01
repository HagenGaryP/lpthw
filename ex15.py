# Exercise 15: Reading Files

# Be careful not to erase your work.

# This exercise involves writing two files.  One is the usual ex15.py file that
#   you will run, but the other is named "ex15_sample.txt". 
# This second file isn't a script but a plain text file our script will be reading.
# Here are the contents of that text file:
#        This is stuff I typepd into a file.
#        It is really cool stuff.
#        Lots and lots of fun to have in here.

# obviously don't need to include the # symbols.

# What we want to do is open that file in our script and print it out.
# However, we do not want to just hard code the name ex15_sample.txt into our script.

# "Hard coding" means putting some bit of info that should come from the user as a string
#   directly into our source code.  That's bad because we want it to load other files later.

# The solution is to use  'argv'  or  'input'  to ask the user what file to open instead
#   of hardcoding the file's name.


from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()


# A quick breakdown of what's going on here:

# argv is used to get a filename.  We use a new command "open", defined as follows:
# open(file, mode, buffering, encoding, errors, newline, closefd, opener)
# Open file and return a stream. Raise OSError upon failure.

# Notice how, like your own scripts and input, it takes a parameter and returns
#   a value you can set to your own variable.
# We call a function on the variable txt, named "read".  What we get back from 
#   open is a file, and it also has commands you can give it.
# You give a file a command by using the . (dot or period), the name of the
#   command, and parameters, just like with open and input.
# The difference is that txt.read() says, "hey txt! do your read command with
#   no parameters!"


# Note: We have been running scripts with just the name of the script, but now
#       that we are using argv, arguments have to be added.

# To run the script, follow the example of what to type in the command line:
#   > python ex15.py ex15_sample.txt

# Notice the extra argument "ex15_sample.txt" after the ex15.py script name.
#   If you do not type that, you will get an error.