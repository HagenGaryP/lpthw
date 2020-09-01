# Exercise 16: Reading and Writing Files

# List of easy commands to remember:

# close - closes the file.  Like File -> Save... in your editor.
# read - Reads the contents of the file.  You can assign the result to a variable.
# readline - Reads just one line of a text file.
# truncate - Empties the file.  Watch out if you care about the file.
# write('stuff') - Writes "stuff" to the file.
# seek(0) - Moves the read/write location to the beginning of the file.


from sys import argv
                            #                    |script||filename|
script, filename = argv     # run with >>> python ex16.py test.txt

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')    # makes a file object to write over, truncates if it exists.

print("Truncating the file.  Goodbye!")
target.truncate()       # truncates file to 0 bytes.  "truncate" means to shorten or trim

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()


#                           PYTHON NOTES on the open() function

# open(file, mode='r', buffering=-1, encodding=None, errors=None, newline=None, closefd=True, opener=None)

# Open file and return a corresponding file object.  If the file cannot be opened, an OSError is raised.

# file is a path-like object giving the pathname (absolute or relative to the current working directory)
#   of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file 
#   descriptor is given, it is closed when the returned I/O object is closed, unless closefd is set to False)

# mode (optional) specifies the mode to open file.  Defaults to 'r' meaning open for reading in txt mode.
#   'w' for writing (truncating the file if it already exists), 
#   'x' for exclusive creation, failing if the file already exists.
#   'a' for writing, apennding to the end of the file if it exists.
#   'b' binary mode
#   't' text mode (default)
#   '+' open a disk file for updating (reading and writing)