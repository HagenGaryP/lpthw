# Exercise 44: Inheritance versus Composition

#               What is Inheritance?

# Inheritance is used to indicate that one class will get most or all of its features from a parent class.
# This happens implicitly whenever you write class Foo(Bar), which means "Make a class Foo that inherits
#   from Bar."  When you do this, the language makes any action that you do on instances of Foo also work
#   as if they were done to an instance of Bar.  Doing this lets you put common functionality in the
#   Bar class, then specialize that functionality in the Foo class as needed.


# When you are doing this kind of speciliaztion, there are three ways that the parent and child classes
#   can interact:

#   1. Actions on the child imply an action on the parent.

#   2. Actions on the child override the action on the parent.

#   3. Actions on the child alter the action on the parent.


# I will now demonstrate each of these in order and show you code for them.


#                                    Implicit Inheritance

# First, I will show you the implicit actions that happen when you define a function in the parent but NOT
#   in the child.

class Parent(object): # Parent() is the base class

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent): # Child() is a subclass of Parent()
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# The use of pass under the class Child: is how you tell Python that you want an empty block.
# This creates a class named Child but says that there's nothing new to define in it.  Instead it
#   will inherit all of its behavior from Parent. When you run this code you get the following:

#       python ex44a.py
#       PARENT implicit()
#       PARENT implicit()

# Notice how even though i'm calling son.implicit() and even though Child does not have an implicit
#   function defined, it still works, and it calls the one defined in Parent.  This shows you that
#   if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child) will
#   automatically get those features.  Very handy for repetitive code you need in many classes.


#                               Override Explicitly

# The problem with having functions called implicitly is sometimes you want the child to behave
#   differently.  In this case you want to override the function in the child, effectively replacing
#   the functionality.  To do this, just define a function with the same name as in Child.  Example:

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")
    
dad = Parent()
son = Child()

dad.override()
son.override()

# In this example I have a function named override in both classes.  This is what happens when you run it:

#   python ex44b.py
#   PARENT override()
#   CHILD override()

# As you can see, it runs the Parent.override fucntion because that variable (dad) is a Parent.
# But it prints out the Child.override message because  son  is an instance of Child and Child overrides
#   that function by defining its own version.



#                       Alter Before or After

# The third way to use inheritance is a special case of overriding where you want to alter the behavior 
#   before or after the Parent class's version runs.  You first override the function just like in the last
#   example, but then you use a Python built-in function named super to get the Parent version to call.

# Here's the example of doing that so you can make sense of this description:

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
    
dad = Parent()
son = Child()

dad.override()
son.override()


# The important lines here are under the Child class where the altered() function is defined,
#   between both print functions
# Where in the Child I do the following when son.altered() is called:

#   1. Because I've overriden Parent.altered the Child.altered version runs, and Child's print
#       executes like you'd expect.

#   2. In this case I want to do a before and after, so after Child's first print ("before parent"),
#       I want to use  super  to get the Parent.altered version.

#   3. super(Child, self).altered()  which is aware of inheritance, will get the Parent class for you.
#       You should be able to read this as "call super with arguments Child and self, then call the
#       function altered on whatever it returns."

#   4. At this point, the Parent.altered version of the function runs, and that prints out the Parent message.

#   5. Finally, this returns from the Parent.altered, and the Child.altered function continues to print out 
#       the after message.



#                           All Three Combined

class Parent(object): # Base class

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent): # Child() is a subclass of the base class, Parent()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
    
dad = Parent()  # the variable 'dad' is now an instance of Parent(), calling upon the Parent() class
son = Child()   # son calls on Child()

dad.implicit()  # calls on Parent()'s implicit() fxn, which prints "PARENT implicit()"
son.implicit()  # calls on Child()'s implicit() fxn, which is inherited from Parent()

dad.override()
son.override()

dad.altered()
son.altered()



#                       The Reason for super()


# This should seem like common sense, but then we get into trouble with a thing called 
#   multiple inheritance; which is when you define a class that inherits from one or
#   more classes, like this:

class SuperFun(Child, BadStuff):
    pass

# This is like saying, "Make a class named SuperFun that inherits from the classes
#   Child and BadStuff at the same time."

# In this case, whenever you have implicit actions on any SuperFun instance, Python has
#   to look up the possible function in the class hierarchy for both Child and BadStuff,
#   but it needs to do this in a consisten order.  
# To do this, Python uses "method resolution order" (MRO) and an algorithm called C3 to
#   get it straight.

# Because the MRO is complex and a well-defined algorightm is used, Python can't leave it
#   to you to get the MRO right.  Instead, Python gives you the super() function, which
#   handles all of this for you in the places that you need the altering type of actions
#   as I did in Child.altered.  With supper() you don't have to worry about getting this
#   right, and Python will find the right function for you.



#                       Using super() with __init__

# The most common use of super() is actualy in  __init__  functions in base classes.
# This is usually the only place where you need to do some things in a child, then
#   complete the initialization in the parent.
# Here's a quick example of doing that in the Child:

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()


# This is pretty much the same as the Child.altered example above, except I'm setting
#   some variables in the  __init__  before having the Parent initialize with its
#       Parent.__init__



#                               Composition


# Inheritance is useful, but another way to do the exact same thing is just to use
#   other classes and modules, rather than rely on implicit inheritance.
# If you look at the three ways to exploit inheritance, two of the three involve
# writing new code to replace or alter functionality.  This can easily be replicated
#   by just calling functions in a module.  Here's an example of doing this:

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):
    
    def __init__(self):
        self.other = Other()    # self.other now calls on the Other class

    def implicit(self):
        self.other.implicit() # calls on the Other class's implicit() function
    
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()    #   calls on Other()'s altered() function
        print("CHILD, AFTER OTHER altered()")

son = Child()    # variable 'son' now is an instance of Child(), calling on Child() class

# Method Objects that are instance attribute references.  A method is a function that
#       "belongs to" an object.

son.implicit()   # calling on implicit() function from Child class, which calls on Other's implicit()

son.override()  # calls on Child()'s override() function

son.altered()   # calls on Child()'s altered() function

# By definition, all attributes of a class that are function objects define corresponding methods
#   of its instance.  So, son.implicit is a valid method reference, since Child.implicit is a function.
#   son.implicit is a method object, not a function object.

# The special thing about methods is that the instance object is passed as the first argument of
#   the function.  

# In this code I'm not using the name Parent, since there is not a parent-child
#   "is-a" relationship.  This is a "has-a" relationship, where Child has-a Other
#   that it uses to get its work done.  When I run this I get the following output:

#   python ex44e.py
#   OTHER implicit()
#   CHILD override()
#   CHILD, BEFORE OTHER altered()
#   OTHER altered()
#   CHILD, AFTER OTHER altered()


# You can see that most of the code in Child and Other is the same to accomplish the
#   same thing.  The only difference is that I had to define a Child.implicit function
#   to do that one action.  I could then ask myself if I need this Other to be a class,
#   and could I just make it into a module named other.py?



#               When to Use Inheritance or Composition


# The question of "inheritance vs composition" comes down to an attempt to solve the problem
#   of reusable code. You don't want to have duplicate code all over your software, since 
#   that's not clean and efficient. 
# Inheritance solves this problem by creating a mechanism for you to have implied features
#   in base classes.
# Composition solves this by giving you modules and capability to call functions in other classes.


# If both solutions solve the problem of reuse, then which one is appropriate in which situations?
# The answer is subjective, but here are some guidelines for when to do which:

#   1. Avoid multiple inheritance at all costs, as it's too complex to be reliable.
#       If you're stuck with it, then be prepared to know the class hierarchy and spend
#           time finding where everything is coming from.

#   2. Use composition to package code into modules that are used in many different 
#       unrelated places and situations.

#   3. Use inheritance only when there are clearly related reusable pieces of code that
#       fit under a single common concept, or only if you have to.



#                       Class and Instance Variables


# Generally speaking, instance variables are for data, unique to each instance.
# Class variables are for attributes and methods shared by all instances of the class.

# For example:
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'