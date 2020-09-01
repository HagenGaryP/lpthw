# Exercise 40:  Modules, Classes, and Objects

# Python is called an "object-oriented programming language."  This means there is a construct in Python
#   called a class that lets you structure your software in a particular way.  Using classes, you can  
#   add consistency to your programs so that they can be used in a cleaner way.  At least in theory.


#       Modules are like dictionaries

# You know how a dictionary is created and used and that it is a way to map one thing to another. That
#   means if you have a dictionary with a key "apple" and you want to get it then you do this:

# mystuff = {'apple': "I AM APPLES!"}
# print(mystuff['apple'])

# Keep this idea of "get X from Y" in your head, and now think about modules.  You've made a few so far,
#   and you should know they are:

#   1. A python file with some functions or variables in it...

#   2. Which you can import...

#   3. And access the functions or variables of with the . (dot) operator.


# Imagine I have a module that i decide to name mystuff.py and I put a function in it called apple.
#   Here's the module mystuff.py:

# def apple():
#     print("I AM APPLES!")


# # Once i have this code, I can use the module MyStuff with import and then access the apple function:

# import mystuff
# mystuff.apple()

# # I could also put a variable in it named tangerine:
# def apple():
#     print("I AM APPLES!")

# #this is just a variable
# tangerine = "Living reflection of a dream"

# # I can access that the same way:

# import mystuff

# mystuff.apple()
# print(mystuff.tangerine)

# Refer back to the dictionary, and you should start to see how this is similar to using a dictionary, but the
#   syntax is different.  Let's compare:

# mystuff['apple']    # get apple from dict
# mystuff.apple()     # get apple from the module
# mystuff.tangerine   # same thing, it's just a variable


# This means we have a very common pattern in Python:
#   1.  Take a key=value style container.
#   2.  Get something out of it by the key's name.


# In the case of the dictionary, the key is a string and the syntax is [key].  In the case of the module, the
#   key is an identifier, and the syntax is .key
# Other than that they are nearly the same thing.


#               Classes are like Modules

# You can think about a module as a specialized dictionary that can store Python code so you can access it 
#   with the . operator.  Python also has another construct that serves a similar purpose called a class.  
# A class is a way to take a grouping of functions and data and place them inside a container so you can access 
#   them with the . (dot) operator.

# If I were to create a class just like the mystuff module, i'd do something like this:
# class MyStuff(object):

#     def __init__(self):
#         self.tangerine = "And now a thousand years between"

#     def apple(self):
#         print("I AM CLASSY APPLES!")


# That looks complicated compared to modules, and there is definitely a lot going on by comparison, but 
#   you should be able to make out how this is like a 'mini-module' with MyStuff having an apple() function
#   in it.  What is probably confusing is the  __init__() function and use of self.tangerine for setting
#   the tangerine instance variable.

# Here's why classes are used instead of modules: You can take this MyStuff class and use it to craft
#   many of them, millions at a time if you want, and each one won't interfere with each other.
# When you import a module there is only one for the entire program unless you do some monster hacks.

# Before you can understand this, though, you need to know what an "object" is and how to work with MyStuff
#   just like you do with the mystuff.py module.



#               Objects Are Like Import


# If a class is like a "mini-Module," then there has to be a concept similar to import but for classes.  
# That concept is called "instantiate," which is just a fancy, obnoxious, overly smart way to say "create."
# When you instantiate a clas, what you get is called an object.

# You instantiate (create) a class by calling the class like it's a function, like this:
# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)

# The first line is the "instantiate" operation, and it's a lot like calling a function.  However, Python
#   coordinates a sequence of events for you behind the scenes.  I'll go through these steps using the 
#   preceding code for MyStuff:

#   1. Python looks for MyStuff() and sees that it is a class you've defined.

#   2. Python crafts an empty object with all the functions you've spepcified in the class using def.

#   3. Python then looks to see if you made a "magic" __init__ function, and if you have it call that function
#       to initialize y our newly created empty object.

#   4. In the MyStuff function __init__ you then get this extra variable, self, which is that empty object
#       Python made for you, and you can set variables on it just like you would with a module, dictionary,
#       or other object.

#   5. In this case, you set self.tangerine to a song lyric and then you've initialized this object.

#   6. Now Python can take this newly minted object and assign it to the  thing  variable for you to work with.


# That's the basics of how Python does this "mini-import" when you call a class like a function. 
# Remember that this is not giving you the class, but instead is using the class as a blueprint for
#   building a copy of that type of thing.

# Keep in mind that I'm giving you a slightly inaccurate idea of how these work so that you can start to
#   build up an understanding of classes based on what you know about modules.  The truth is, classes and
#   objects suddenly diverge from modules at this point.  If I were being totally honest, I'd say
#   something more like this:

#   Classes are like blueprints or definitions for creating new mini-modules.

#   Instantiation is how you make one of these mini-modules and import it at the same time.
#           "instantiate" just means to create an object from the class.

#   The resulting created mini-module is called an object, and you then assign it to a variable to work with.

# At this point objects behave differently from modules, and this should only serve as a way for you to bridge
#   over to understanding classes and objects.



#               Getting Things from Things

# I now have three ways to get things from things:

# # dict style
# mystuff['apples']


# # module style
# mystuff.apples()
# print(mystuff.tangerine)

# #class style
# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)



#               A First Class Example

# You should start seeing the similarities in these three key=value container types and probably have a 
#   bunch of questions.  Hang on with the questions, as the next exercise will hammer home your 
#   "object-oriented vocabulary."  In this exercise, I just want you to type in this code and get it working
#   so that you have some experience before moving on.


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        
happy_bday = Song(["Happy birhtday to you",
                    "I don't want to get sued",
                    "So I'll stop right there."])

bulls_on_parade = Song(["They rally round the family",
                        "With a pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()