# Exercise 32: Loops and Lists

# We are going to use a "for-loop" in this exercise to build and print various lists.
# Before you can use a "for-loop", you need a way to STORE the results of loops somewhere.
# The best waay to do this is with lists.  A list is exactly what the name says: 
#   a container of things that are organized in order from first to last.

# Syntax:
#           hairs = ['brown', 'blond', 'red']
#           eyes = ['brown', 'blue', 'green']
#           weights = [1, 2, 3, 4]

# You start the list with the [ (left bracket) which "opens" the list.  Then you put each
#   item you want in the list separated by commas, similar to function arguments.
# Lastly, end the list with a ] (right bracket) to indicate that it's over.  Python then 
#   takes this list and all its contents and assigns them to the variable.

# We now will build some lists using some for-loops and print them out:

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")


# The range type represents an immutable sequence of numbers and is commonly used for
#    looping a specific number of times in for-loops.
# class range(start, stop[, step])
# The arguments to the range constructor must be integers (either built-in int or any 
#   object that implements the __index__ special method). If the step argument is omitted, 
#   it defaults to 1. If the start argument is omitted, it defaults to 0. If step is zero, 
#   ValueError is raised.

# For a positive step, the contents of a range r are determined by 
#   the formula     r[i] = start + step*i       where i >= 0 and r[i] < stop.

# For a negative step, the contents of the range are still determined by 
#   the formula     r[i] = start + step*i,      but the constraints are i >= 0 and r[i] > stop.



#                               Range examples:

# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(range(0, 30, 5))
# [0, 5, 10, 15, 20, 25]
# >>> list(range(0, 10, 3))
# [0, 3, 6, 9]
# >>> list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# >>> list(range(0))
# []
# >>> list(range(1, 0))
# []



#                                            Lists

# Lists are MUTABLE sequences, typically used to store collections of homogeneous items 
#   (where the precise degree of similarity will vary by application).

# Simply put, a MUTABLE object can be changed after it is created, and an IMMUTABLE object can't. 
# Objects of built-in types like (int, float, bool, str, tuple, unicode) are IMMUTABLE. 
# Objects of built-in types like (list, set, dict) are MUTABLE.

# class list([iterable])         Lists may be constructed in several ways:

# Using a pair of square brackets to denote the empty list: []
# Using square brackets, separating items with commas: [a], [a, b, c]
# Using a list comprehension: [x for x in iterable]
# Using the type constructor: list() or list(iterable)

# The constructor builds a list whose items are the same and in the same order as iterable’s items. 
#   iterable may be either a sequence, a container that supports iteration, or an iterator object. 
#   If iterable is already a list, a copy is made and returned, similar to iterable[:]. 
#   For example, list('abc') returns ['a', 'b', 'c'] and list( (1, 2, 3) ) returns [1, 2, 3]. 
#   If no argument is given, the constructor creates a new empty list, [].

# Many other operations also produce lists, including the sorted() built-in.

# Lists implement all of the common and mutable sequence operations. 

# Lists also provide the following additional method:

# sort(*, key=None, reverse=False)
# This method sorts the list in place, using only < comparisons between items.


# The operations in the following table are defined on mutable sequence types. 
#  The collections.abc.MutableSequence ABC is provided to make it easier to correctly implement 
#     these operations on custom sequence types.

# In the table s is an instance of a mutable sequence type, t is any iterable object 
#   and x is an arbitrary object that meets any type and value restrictions imposed by s 
#   (for example, bytearray only accepts integers that meet the value restriction 0 <= x <= 255).

########################################################################################################
# OPERATION	                    RESULT	                                                        NOTES
########################################################################################################
# ______________________________________________________________________________________________________
# s[i] = x	                    item i of s is replaced by x	 
# ______________________________________________________________________________________________________
# s[i:j] = t	                slice of s from i to j is replaced 
#                               by the contents of the iterable t	
# ______________________________________________________________________________________________________ 
# del s[i:j]	                same as s[i:j] = []	 
# ______________________________________________________________________________________________________
# s[i:j:k] = t	                the elements of s[i:j:k] are replaced by those of t	            (1)
# ______________________________________________________________________________________________________
# del s[i:j:k]	                removes the elements of s[i:j:k] from the list	 
# ______________________________________________________________________________________________________
# s.append(x)	                appends x to the end of the sequence 
#                               (same as s[len(s):len(s)] = [x])	 
# ______________________________________________________________________________________________________
# s.clear()	                    removes all items from s (same as del s[:])	                    (5)
# ______________________________________________________________________________________________________
# s.copy()	                    creates a shallow copy of s (same as s[:])	                    (5)
# ______________________________________________________________________________________________________
# s.extend(t) or s += t	        extends s with the contents of t 
#                               (for the most part the same as s[len(s):len(s)] = t)	 
# ______________________________________________________________________________________________________
# s *= n	                    updates s with its contents repeated n times	                (6)
# ______________________________________________________________________________________________________
# s.insert(i, x)	            inserts x into s at the index given by i 
#                               (same as s[i:i] = [x])	 
# ______________________________________________________________________________________________________
# s.pop([i])	                retrieves the item at i and also removes it from s	            (2)
# ______________________________________________________________________________________________________
# s.remove(x)	                remove the first item from s where s[i] is equal to x	        (3)
# ______________________________________________________________________________________________________
# s.reverse()	                reverses the items of s in place	                            (4)
# ______________________________________________________________________________________________________
########################################################################################################
# Notes (corresponding to table):

#   1. t must have the same length as the slice it is replacing.

#   2. The optional argument i defaults to -1, so that by default the last item is removed and returned.

#   3. "remove" raises ValueError when x is not found in s.

#   4. The reverse() method modifies the sequence in place for economy of space when reversing a large sequence. 
#       To remind users that it operates by side effect, it does not return the reversed sequence.

#   5. clear() and copy() are included for consistency with the interfaces of mutable containers that 
#       don’t support slicing operations (such as dict and set)

#       New in version 3.3: clear() and copy() methods.

#   6. The value n is an integer, or an object implementing __index__(). Zero and negative values of n clear 
#       the sequence. Items in the sequence are not copied; they are referenced multiple times, 
#       as explained for s * n under Common Sequence Operations.













