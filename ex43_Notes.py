# Exercise 43: Basic Object-Oriented Analysis and Design


# Set of steps to use when building something using Python:

#   1. Write or draw out the problem

#   2. Extract key concepts from 1 and research them.

#   3. Create a class hierarchy and object map for the concepts.

#   4. Code the classes and a test to run them.

#   5. Repeat and refine.


# Zed starts by just writing about the problem and trying to think up anything he can about it.
# He writes up a plan, and draws a diagram if necessary, then goes through these notes, drawings and descriptions,
#   and pulls out key concepts.  He makes a list of all the nouns and verbs in his writing and drawings, then
#    writes out how they're related.  This gives him a good list of names for classes, objects, and functions.

# Once he has his list of concepts, he creates a simple outline/tree of the concepts and how they're related
#   as classes.  With class hierarchy figured out, he sits down and writes some basic skeleton code that has
#   just the classes, their functions, and nothing more.  Then writes a test that runs the code and makes sure
#   the classes he made make sense and work right.  

# Finally, he keeps cycling over this process, repeating it and refining as he goes, and making it as clear as
#   he can before doing more implememntation.  If he gets stuck at any particular part because of a concept or
#   problem that he didn't anticipate, then he sits down and starts the process over on just that part.


##################################################################################################################
#                                      The Analysis of a Simple Game Engine
##################################################################################################################

# The game I want to make is called "Gothons from Planet Percal #25," and it will be a small space adventure game.
# With nothing more than that concept in my mind, I can explore the idea and figure out how to make the game come
#   to life.

#                                   Write or Draw About the Problem

# I'm going to write a little paragraph for the game:

#"Aliens ahve invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape
#   into an escape pod to the planet below.  The game will be more like a Zork or Adventure type game with text
#   outputs and funny ways to die.  The game will involve an engine that runs a map full of rooms or scenes.
#   Each room will print its own description when the player enters it and then tell the engine what room to run
#   next out of the map."

# At this point I have a good idea for the game and how it would run, so now I want to describe each scene:

#   Death - This is when the player dies and should be something funny.

#   Central Corridor - This is the starting point and has a Gothon already standing there that the players have
#                       to defeat with a joke before continuing.

#   Laser Weapon Armory - This is where the hero gets a neutron bomb to blow up the ship before getting to the
#                           escape pod.  It has a keypad the hero has to guess the number for.

#   The Bridge - This is another battle scene with a Gothon where the hero places the bomb.

#   Escape Pod - This is where the hero escapes but only after guessing the right escape pod.


# At this point I might draw out a map of these, maybe write more descriptions of each room - Whatever comes
#   to mind as I explore the problem.


#                                 Extract Key Concepts and Research Them

# I now have enough info to extract some of the nouns and analyze theiir class hierarchy.
# First, I have to make a list of all the nouns: Alien, Player, Ship, Maze, Room, Scene, Gothon, Escape Pod, 
#   Planet, Map, Engine, Death, Central Corridor, Laser Weapon Armory, The Bridge

# I would also possibly go through all the verbs and see if any of them might be good function names.

# At this point I might also research each of these concepts and anything i don't know right now.  
# For example, I might play a few of these types of games and make sure i know how they work. I might research
#   how ships are designed or how bombs work.  Maybe I'll resarch some technical issue like how to store the 
#   game's state in a database.  After I've done this research I might start over at step 1 based on new
#   info I have and rewrite my description and extract new concepts.


#                            Create a Class Hierarchy and Object Map for the Concepts

# Once I have that I turn it into a class hierarchy by asking, "What is similar to other things?" I also ask,
#   "What is basically just another word for another thing?"

# Right away, I see that "Room" and "Scene" are basically the same thing depending on how I want to do things.
# I'm going to pick "Scene" for this game. Then I see that all the specific rooms, like "Central Corridor,"
#   are basically just Scenes.  I see also that Death is basically a Scene, which confirms my choice
#   of "Scene" over "Room," since you can have a death scene, but a death room is kind of odd.
# "Maze" and "Map" are basically the same, so I'm going to go with "Map" since I used it more often.  
# I don't want to do a battle system, so I'm going to ignore "Alien" and "Player" and save that for later.
# The "Planet" could also just be another scene instead of something specific.

# After all of that though process, I start to make a class hierarchy that looks like this in my text editor:

#   * Map
#   * Engine
#   * Scene
#       * Death
#       * Central Corridor
#       * Laser Weapon Armory
#       * The Bridge
#       * Escape Pod

# Then I go through and figure out what actions are needed on each thing based on verbs in the description.
# For example, I know from the description I'm going to need a way to "run" the engine, "get the next scene"
#   from the map, get the "opening scene", and "enter" a scene. I'll add those like this:

#   * Map
#     - neext_scene
#     - opening_scene
#   * Engine
#     - play
#   * Scene
#     - enter
#       * Death
#       * Central Corridor
#       * Laser Weapon Armory
#       * The Bridge
#       * Escape Pod


# Notice how I just put -enter under Scene since I know that all the scenes under it will inherit it and
#   have to override it later.



#                          Code the Classes and a Test to Run Them


# Once I have this tree of classes and some of the functions I open up a source file in my editor and try
#   to write the code for it.  Usually I'll just copy-paste the tree into the source file and then edit
#   it into classes.  Here's a small example of how this might look at first.

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass


class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# In this file  you can see that I simply replicated the hierarchy I wanted and then added a litte bit
#    of code at the end to run it and see if it all works in this basic structure.
# In the later sections of this exercise you'll fill in the rest of this code and make it work to match 
#   the description of the game.



#                                       Repeat and Refine


# The last step in my little process isn't so much a step as it is a while-loop. You don't ever do this
#   as a one-pass operation. Instead you go back over the whole process again and refine it based on
#   info you've learned from later steps.

# The other idea in this process is that it's not just something you do at one single level but something
# that you can do at every level when you run into a particular problem.  Let's say I don't know how to
#   write the Engine.play method yet.  I can stop and do this whole process on JUST that one function
#   to figure out how to write it.



#                                   Top Down Versus Bottom Up


# The process is typically labeled "top down" since it starts at the most abstract concepts (the top)
#   and works its way down to actual implementation.  I want you to use this process I just described
#   when analyzing problems in the boom from now on, but you should know that there's another way to 
#   solve problems in programming that starts with code and goes "up" to the abstract concepts.
# This other way is labeled "bottom up." Here are the general steps you follow to do this:

#   1. Take a small piece of the problem; hack on some code and get it to run barely.

#   2. Refine the code into something more formal with classes and automated tests.

#   3. Extract the key concepts you're using and research them.

#   4. Write a description of what's really going on.

#   5. Go back and refine the code, possibly throwing it out and starting over.

#   6. Repeat, moving on to some other piece of the problem.


# I find this process is better once you're more solid at programming and are naturally thinking
#   in code about problems.  This process is very good when you know small pieces of the overall
#   puzzle, but maybe don't have enough info yet about the overall concept.  Breaking it down in little
#   pieces and exploring with code helps you slowly grind away at the problem until you've solved it.
# However, remember that your solution will probably be meandering and weird, so that's why my version
#   of this process involves going back and finding research, then cleaning things up based on what
#   you've learned.


#                   The Code for "Gothons from Planet Percal #25"


# STOP! I'm going to show you my final solution to the preceding problem, but I don't want you to just
#   jump in and type this up.  I want you to take the rough skeleton code I did and try to make it work
#   based on the description. Once you have your solution, come back and see how I did it.





from sys import exit
from random import randint
from textwrap import dedent

# This is just our basic imports for the game.  The only new thing is the import of the dedent function
#   from the textwrap module.  This function helps us write our room descriptions using """ (triple-quote)
#   strings.  It simply strips leading white-space from the beginnings of the lines in a string. 
# Without this function, using """ style strings fails becausue they are indented on the screen the same
#   level as in the Python code.


class Scene(object):

    def enter(self):
        print("this scene is not your configured.")
        print("Subclass it and implement enter().")
        exit(1)

# As you saw in the skeleton code, I have a base class for Scene that will have the common things that all
#   scenes do.  In this simple program they don't do much, so this is more a demonstration of what you
#   would do to make a base class.


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finihsed')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

# I also have my Engine class, and you can see how I'm already using the methods for Map.opening_scene 
#   and Map.net_scene.  Because I've done a bit of planning I can just assume I'll write those and
#   then use them before I've written the Map class.

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
        "Your Mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

# My first scene is the odd scene named Death, which shows you the simplest kind of scene you can write.

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gorthons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew.  You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.
            
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body.  He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))
        
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire 
                it at the Gothon.  His clown costume is flowing and 
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead.  Then he eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head.  In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out.  You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy.  You tell the one Gothon joke you know:
                lbhe zbgure vf fv sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nevhaq gur ubhfr.  The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in 
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

# After that I've created the CentralCorridor, which is the start of the game.  I'm doing the scenes for the
#   game before the Map because I need to reference them later.  You should also see how I use the dedent function
#   on line 4.  Try removing it later to see what it does.

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding.  It's dead
            quiet, too quiet.  You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out.  If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb.  The
            code is 3 digits.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting 
                gas out.  You grab the neutron bomb and run as fast as 
                you can to the bridge where you must place it in the 
                right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a 
                sickening melting sound as the mechanism is fused
                together.  You decide to sit there, and finally the
                Gothons blow up the ship from their ship and you die.
                """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the neutron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship.  Each of them has an even uglier
            clown costume than the last.  They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't watn to set it off.
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door.  Right as you drop it a
                Gothon shoots you right in the back, killing you.  As
                you die, you see another Gothon frantically try to
                disarm the bomb.  You die knowing they will probably
                blow up when it goes off.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and 
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your 
                blaster at it.  You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out.  Now that the bomb is palced
                you run to the escape pod to get off this tin can.
                """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):
    
    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes.  It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference.  You get to the chamber with the 
            escape pods, and now need to pick one to take.  Some of 
            them could be damaged but you don't have time to look.
            There are 5 pods, which one do you take?
            """))
        
        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, then 
                implodes as the hull ruptures, crushing your body into
                jam jelly.
                """))
            return 'death'
        else:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to the
                planet below.  As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time.  You won!
                """))

            return 'finished'

class Finished(Scene):
    
    def enter(self):
        print("You won! Good job.")
        return 'finished'

# This is the rest of the game's scenes, and since I know I need them and have though about
#   how they'll flow together, I'm able to code them up directly.

# Incidentally, I wouldn't just type all this code in.  Remember I said to try and build this
#       incrementally, one little bit at a time.  I'm just showing you the final result.

class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

# After that I have my Map class, and you can see it is storing each scene by name in a dictionary,
#   and then I refer to that dict with Map.scenes.  This is also why the map comes after the scenes
#   because the dictionary has to refer to the scenes, so they have to exist.

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# Finally, I've got my code that runs the game by making a Map, then handing that map to an Engine
#   before calling play to make the game work