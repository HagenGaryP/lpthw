# Exercise 11:  Asking Questions

print("How old are you?", end=' ')
age = input()                       # takes input() from user as variable
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall, and weigh {weight}.")

# NOTE: end=' '   at the end of each print line so the print function
#       doesn't end the line with a newline character and go to next line.