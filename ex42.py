# Exercise 42: Is-A, Has-A, Objects, and Classes


# An important concept that you have to understand is the difference between a class and an object.
# The problem is, there is no real "difference" between a class and an object.
# They are actually the same thing at different points in time.  I will demonstrate with a Zen koan:
#       What is the difference between a fish and a salmon?

# Did that question sort of confuse you?  A fish and a salmon are different, but they still are the
#   same thing.  A salmon is a KIND of fish, so it's not entirely different.  
# But at the same time, a salmon is a particular TYPE of fish, so it's actually different from
#   all other fish.  That's what makes it a salmon and not a halibut.  So, a salmon and a fish are
#   the same but different.

# This question is confusing because most people do not think about real things this way, but they
#   intuitively understand them.  You do not need to think about the difference between a fish and
#   a salmon because you knkow how they are related.  You know a salmon is a KIND of fish and that
#   there are other kidns of fish without having to understant that.

# Let's take it one step further.  Let's say you have a bucket full of three salmon, and because
#   you are a nice person, you have decided to name them Frank, Joe, and Mary. 
# Now think about this question:
#       What is the difference between Marry and a salmon?

# Again, this is a weird question, but it's a bit easier than the fish vs salmon question.
# You know that Mary is a salmon, so she's not really different.  She's just a specific "instance"
#   of a salmon.  Joe and Frank are also instances of salmmon.  What do I mean when I say instance?
# I mean they were created from other salmon and represent a real thing that has salmon-like attributes.

# Now for the mind-bending idea: Fish is a class, and Salmon is a class, and Mary is an object.
# Think about that and break it down.

# A fish is a class, meaning it's not a real thing, but rather a word we attach to instances of
#   things with similar attributes.  
#   Got fins? Got gills? Lives in water? Probably a fish. (with exeptions like sharks and such..)

# Someone with a Ph.D. then comes along and says, "No, my young friend, this fish is actually
#   Salmo salar, affectionately known as a salmon."  This professor has just clarified the fish further,
#     and made a new class called "Salmon" that has more specific attributes.  Longer nose, reddish flesh,
#       big, lives in the ocean or fresh water, tasty? Probably a salmon.

# Finally, a cook comes along and tells the Ph.D., "No, you see this Salmon right here, I'll call her Mary,
#   and I'm going to make a tasty fillet out of her with a nice sauce."  
# Now you have this INSTANCE of a salmon (which also is an instance of a fish) named Mary turned into
#   something real that is filling your belly.  It has become an object.

# There you have it:  Mary is a kind of salmon that is a kind of fish--obect is a class in a class.


#               HOW THIS LOOKS IN CODE

# This is a weird concept, but to be very honest, you only have to worry about it when you make new classes
#    and when you use a class.  I will show you two tricks to help you figure out whether something is a 
#       class or an object.

# First, you need to learn two catch phrases: "is-a" and "has-a." You use the phrase is-a when you talk
#   about objects and classes being related to each other by a class relationship.  
# You use has-a when you talk about objects and classes that are related only because they reference
#    each other.

# Now, go through this piece of code and replace each ##?? comment with a comment that says whether the
#   next line represents an is-a or a has-a relationship and what the relationship is.
# In the beginning of the code, I've laid out a few examples, so you just have to write the remaining ones.

# Remember, is-a is the relationship between fish and salmon, while has-a is the relationship
#   between salmon and gills.



## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name           hmm what is this strnage magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## A Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


### rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Satan is-a pet. Mary has-a pet
mary.pet = satan

## Frank is-a Employee.  Frank/Employee has-a salary of 120000
frank = Employee("Frank", 120000)

## Rover is a pet.  Frank has-a pet
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()



#                           About class Name(object)


# In Python 3, you do not need to add the  (object)  after the name of the class, but the Python community
#   believes in "explicit is better than implicit," so I decided to include it.  
# You may run into code that does not have  (object)  after simple classes, and those classes are 
#   perfectly fine and will worth with classes you create that DO have  (object).
# At this point it is simply extra documentation and has no impact on how your classes work.

