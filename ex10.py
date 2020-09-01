# Exercise 10: What Was That?

# Ex9 showed two ways to make a string that goes across multiple lines.
# First way, by using the characters \n (backslash n) between month names
#   This puts a "new line" character into the string at that point.

# An important escape sequence is to escape a single-quote (') or 
#   double-quote (").  i.e., "I "understand" joe." would confuse python,
#   because it thinks the double-quotes around "understand" actually ends
#   the string.  To solve this problem you escape double-quotes and 
#   single-quotes so Python knows to include them in the string.
# For example:
#   "I am 6'4\" tall."  # escape double-quote inside string
#   'I am 6\'4" tall.'  # escape single-quote inside string

# The second way is by using triple-quotes, which is just """ and works
#   like a string, but you also can put as many lines of text as you want
#   until you type """ again.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

##########################################################################
#                           Escape Sequences
##########################################################################
#   Escape      |       What it does.
#   \\          |       Backslash(\)
#   \'          |       Single-quote (')
#   \"          |       Double-quote (")
#   \a          |       ASCII bell (BEL)
#   \b          |       ASCII backspace (BS)
#   \f          |       ASCII formfeed (FF)
#   \n          |       ASCII linefeed (LF)
#   \N{name}    |       Character named name in the Unicode database
#   \r          |       Carriage return (CR)
#   \t          |       Horizontal tab (TAB)
#   \uxxxx      |       Character with 16-bit hex value xxxx
#   \Uxxxxxxxx  |       Character with 32-bit hex value xxxxxxxx
#   \v          |       ASCII vertical tab (VT)
#   \000        |       Character with octal value 000
#   \xhh        |       Character with hex value hh