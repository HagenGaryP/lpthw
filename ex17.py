# Exercise 17: More Files

# Writing a python script to copy one file to another.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# notice we import another command named "exists".  This returns True if a file exists,
#   based on its name in a string as an argument.  It treturns False if not.

# Using import is a way to get tons of free code that has already been written by
#   other programmers.

#           What you should see

# C:\lpthw> # first make a sample file
# C:\lpthw> echo "This is a test file." > test.txt
# C:\lpthw> cat test.txt
# This is a test file.
# C:\lpthw> python ex17.py test.txt new_file.txt
# Copying from test.txt to new_file.txt
# The input file is 46 bytes long
# Does the output file exist? False
# Ready, hit RETURN to continue, CTRL-C to abort.

# Alright, all done.


# NOTE: Used "echo" to make a file and "cat" to show the file.