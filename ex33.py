# Exercise 33: While Loops

# A while-loop will keeep executing the code block under it as long as a Boolean expression is True.

# What they do is simply do a test like an if-statement, but instead of running the code block once,
#   they jump back to the 'top' where the while is and repeats.  A while loop runs until the expression is False.

# Here's the problem with while-loops: Sometimes they do not stop, i.e., an infinite loop.


# To avoid these problems, there are some rules to follow:

#   1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
# 
#   2. Review your while statements and make sure that the Boolean test will become False at some point.
# 
#   3. When in doubt, print out your test variable at the top and bottom of the while-loop to see results.


# In this exercise, you learn the while-loop as you're doing these three checks:


i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
    