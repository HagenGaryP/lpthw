# Exercise 19: Functions and Variables

# There is one tiny point that you might not have realized.  The variables in your function
#   are not connected to the variables in your script.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man... that's enough for a party!")
    print("Get a blanket.\n") # Y doe?


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables form our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# This shows all the different ways we're able to give our function cheese_and_crackers the
#   values it needs to print them.  We can give it straight numbers, variables, math, or 
#   even combine math and variables.

# In a way, the arguments to a function are kind of like our = character when we make a variable.
# In fact, if you can use = to name something, you can usually pass it to a function as an argument.