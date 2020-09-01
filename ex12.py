# Exercise 12: Prompting People

# When you typed input() you were typing the "(" and ")" characters,
#   which are parenthesis characters.  This is similar to when you
#   used them to do a format with extra variables, as in  f"{x} {y}".

# For  input  you can also put in a prompt to show the user, so they
#   know what to type.  

# Put a string that you want for the prompt inside the () 
#   i.e.,   y = input("Name? ")
# This prompts the user with "Name?" and puts the reslut into the 
#   variable 'y'.  

# We can rewrite ex11 by using input for all the prompting.

age = input("How old are you, in years? ")
height = input("How tall are you, in inches? ")
weight = input("How much do you weigh, in pounds? ")

print(f"So, you're {age} years old, {height} inches tall, and weigh {weight}lbs.")