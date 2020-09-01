# Exercise 38: Doing Things to Lists


# You have learned about lists.  When you learned about while-loops you "appended" numbers to the end
#   of a list and printed them out.  There were also Study Drills to find other things you can do to
#   lists in the Python documentation.

# When you did this, you had a list and "called" the function append on it.  However, you may not
#   really understand what's goin on so let's see what we can do to lists.

# When you write  mystuff.append('hello')  you are actually setting off a chain of events inside 
#   Python to cause something to happen to the  mystuff  list.  Here's how it works:

#   1. Python sees you mentioned  mystuff  and looks up that variable.  It might have to look backward
#       to see if you created it with =, if it is a function argument, or if it's a global variable.
#       Either way, it has to find  mystuff  first.

#   2. Once it finds  mystuff  it reads the  .  (period) operator and starts to look at variables that
#       are a part of  mystuff.  Since  mystuff  is a list, it knows that it has a bunch of functions.

#   3. It then hits append and compares the name to all the names that  mystuff  says it owns.  If
#       append is in there (it is), then Python grabs that to use.

#   4. Next Python sees the  (  (open parentheses) and realizes, "Oh hey, this should be a function."
#       At this point it "calls" (runs or executes) the function just like normal, but it calls the 
#       function with an extra argument.

#   5. That extra argument is...  mystuff!  I know, weird, right?  But that's how Python works, so it's
#       best to just remember it and assume that's the result.  What happens, at the end of all this, 
#       is a function call that looks like append(mystuff, 'hello') instead of what you read, which is
#       mystuff.append('hello').



ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list.  Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # prints the item that's in the LAST POSITION of the list.
print(stuff.pop()) # prints out and removes (with pop) the last item of list.
print(' '.join(stuff)) # joins the list's items together with ' ' between each item.
print('#'.join(stuff[3:5])) # the list reference is including position 3, and UP TO 5. (not including position 5)