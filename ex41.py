# Exercise 41: Learning to Speak Object-Oriented

###############################################################################################################
#   WORD DRILLS
#______________________________________________________________________________________________________________

# class             Tell Python to make a new type of thing.

# object            Two meanings: the most basic type of thing, and any instance of some thing.

# instance          What you get when you tell Python to create a class.

# def               How you define a function inside a class.

# self              Inside the functions in a class, self is a variable for the instance/object being accessed.

# inheritance       The concept that one class can inherit traits from another class, much like you and your parents.

# composition       The concept that a class can be composed of other classes as parts, much like how a car has wheels.

# attribute         A property classes have that are from composition and are usually variables.

# is-a              A phrase to say that something inherits from another, as in a "salmon" is-a "fish"

# has-a             A phrase to say that something is composed of other things or has a trait, 
#                       as in "a salmon has-a mouth."
#______________________________________________________________________________________________________________


###############################################################################################################
#   PHRASE DRILLS
#______________________________________________________________________________________________________________

# class X(Y)                                            "Make a class named X that is-a Y."

# class X(object): def __init__(self, J)                "class X has-a __init__ that takes self and J parameters."

# class X(object): def M(self, J)                       "class X has-a function named M that takes self and J parameters."               

# foo = X()                                             "Set foo to an instance of class X."

# foo.M(J)                                              "From foo, get the M function, and call it with parameters self, J."

# foo.K = Q                                             "From foo, get the K attribute, and set it to Q."
#_____________________________________________________________________________________________________________

# In each of these, where you see X, Y, M, J, K, Q, and foo, you can treat those like blank spots.
# For example, I can also write these sentences as follows:

#   1. "make a class named ??? that is-a Y"

#   2. "class ??? has-a __init__ that takes self and ??? parameters"

#   3. "class ??? has-a function named ??? that tkaes self and ??? parameters."

#   4. "Set ??? to an instance of class ???"

#   5. "From ???, get the ??? function, and call it with self=??? and parameters ???."

#   6. "From ???, get the ??? attribute, and set it to ???."



#                       A READING TEST


# I now have a little Python hack script that will drill you on these words you know in an infinite manner.
# This is a simple script you should be able to figure out, and the only thing it does is use a library called
#   urllib to download a list of words I have.  Here's the script, which you should enter into oop_test.py to work with it:

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params.",
        "class %%%(object):\n\tdef ***(self, @@@)":
            "class %%% has-a function *** that takes self and @@@ params.",
            "*** = %%%()":
            "Set *** to an instance of class %%%.",
            "***.***(@@@)":
            "From *** get the *** function, call it with params self, @@@.",
            "***.*** = '***'":
            "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class name
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
    
    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")


#           The results of running this script


# PS C:\lpthw> python ex41.py
# class Dog(Degree):
# >
# ANSWER:  Make a class named Dog that is-a Degree.


# class Balloon(object):
#         def birthday(self, camp, curve)
# >
# ANSWER:  class Balloon has-a function birthday that takes self and camp, curve params.


# class Dinner(object):
#         def __init__(self, bulb)
# >
# ANSWER:  class Dinner has-a __init__ that takes self and bulb params.


# children = Beef()
# >
# ANSWER:  Set children to an instance of class Beef.


# achiever.crib(calendar, calculator)
# >
# ANSWER:  From achiever get the crib function, call it with params self, calendar, calculator.


# cry.appliance = 'crate'
# >
# ANSWER:  From cry get the appliance attribute and set it to 'crate'.


# airport.badge = 'can'
# >
# ANSWER:  From airport get the badge attribute and set it to 'can'.


# class Bubble(Birth):
# >
# ANSWER:  Make a class named Bubble that is-a Birth.


# approval = Bone()
# >
# ANSWER:  Set approval to an instance of class Bone.


# class Apparel(object):
#         def camp(self, cactus)
# >
# ANSWER:  class Apparel has-a function camp that takes self and cactus params.


# class Bone(object):
#         def __init__(self, cat)
# >
# ANSWER:  class Bone has-a __init__ that takes self and cat params.


# competition.beginner(attack)
# >
# ANSWER:  From competition get the beginner function, call it with params self, attack.


# battle = Cakes()
# >
# ANSWER:  Set battle to an instance of class Cakes.


# celery.bed(crook)
# >
# ANSWER:  From celery get the bed function, call it with params self, crook.


# class Duck(object):
#         def army(self, car, cast, daughter)
# >
# ANSWER:  class Duck has-a function army that takes self and car, cast, daughter params.