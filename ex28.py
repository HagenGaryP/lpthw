# Exercise 28: Boolean Practice

 1.   True and True                                                     #True
 2.   False and True                                                    #False
 3.   1 == 1 and 2 == 1                                                 #False
 4.   "test" == "test"                                                  #True
 5.   1 == 1 or 2 != 1                                                  #True
 6.  True and 1 == 1                                                    #True
 7.   False and 0 != 0                                                  #False
 8.   True or 1 == 1                                                    #True
 9.   "test" == "testing"                                               #False
10.   1 != 0 and 2 == 1                                                 #False
11.    "test" != "testing"                                              #True
12.    "test" == 1                                                      #False
13.    not (True and False)                                             #True
14.    not (1 == 1 and 0 != 1)                                          #False
15.    not (10 == 1 or 1000 == 1000)                                    #False
16.   not (1 != 10 or 3 == 4)                                           #False
17.    not ("testing" == "testing" and "Zed" == "Cool Guy")             #True
18.    1 == 1 and (not ("testing" == 1 or 1 == 0))                      #True
19.    "chunky" == "bacon" and (not (3 == 4 or 3 == 3))                 #False
20.    3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))   #False


# Whenever you see these Boolean logic statements, you can solve them easily by 
#   this simple process:

#   1. Find an equality test(== or !=) and replace it with its truth.
#   2. Find each and/or inside parentheses and solve those first.
#   3. Find each not and invert it.
#   4. Find any remaining and/or and solve it.
#   5. When you are done y ou should have True or False.

# A demonstration using item 20 from above:

# 3 != 4 and not ("testing" != "test" or "Python" == "Python")

# Going through each of the steps and translating:

#   1. Solve each equality test:
#       3 != 4 and not ("testing" != "test" or "Python" == "Python")
#       "testing" != "test" is True:True and not (True or "Python" == "Python")
#       "Python" == "Python":True and not (True or True)

#   2. Find each and/or in parentheses():
#       (True or True) is True:True and not (True)

#   3. Find each not and invert it:
#       not (True) is False: True and False

#   4. Find any remaining and/ors and solve them:
#       True and False is False

# With that we're done, and know the result is False.