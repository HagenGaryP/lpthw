# Exercise 35: Branches and Functions

from sys import exit

def gold_room():
    print("You enter a mysterious and magical room filled with gold coins.  How many do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You have offended the magic room... The gold turns into molten lava and leaves you a lifeless puddle of human remains.")


def bear_room():
    print("There is a bear here.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("1. Taunt the bear.  2. Kiss the bear.  3. Fight the bear.  4. Take its honey.  5. Leave and try the other door.")
    print("Type the number of your choice (1, 2, 3, 4, or 5)")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "4":   # take honey
            dead("The bear looks at you then slaps your face off.")
        elif choice == "2": # kiss bear
            print("The bear turns into a beautiful princess that falls in love with you at first sight, wishing to marry you.")
            print("I don't care what sexual preferences you and/or the princess have, because political correctness is overrated.")
            print("Either way, you have the choice: 'a' marry her, 'b' kill her, 'c' tell her she's in your way.")
            princess()
        elif choice == "3":     # fight bear
            dead("HAH!  Almost had him.  And by that, I mean he ripped you apart.")
        elif choice == "5":     # leave
            print("Maybe you'll have better luck with the other room.")
            cthulhu_room()
        elif choice == "1" and not bear_moved: # taunt bear, but bear has not moved yet
            print("The bear has moved from the door, allowing you to go through it.")
            print("Do you want to open the door?  Type 'y' to open it.")
            bear_moved = True
        elif choice == "1" and bear_moved:  # taunting bear again.. 
            dead("Umm.. w-why would you do that? That's just idiotic.. The bear gets pissed and crushes your skull.")
        elif choice == "y" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means.")


def princess():
    print("Which do you choose, 'a', 'b', or 'c'?")

    choice = input("> ")

    if choice == "a":   # marry
        print("The princess takes your hand as you both happily walk through the door together.")
        gold_room()
    elif choice == "b": # kill
        dead("The princess dodges your attack, and heel kicks you in the back of your head... severing your brain stem.")
    elif choice == "c": # get out of the way
        print("The princess respects your choice, but throws you through the door she was blocking.")
        gold_room()
    else:
        print("Have you never played a game before?  There are a finite amount of choices, and that wasn't one of them.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, or whatever.. stares at you and you go insane.")
    print("Do you flee for your life or eat your own head?")
    print("Type 'flee' to run away, or type 'eat' to start munching")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "eat" in choice:
        dead("You somehow consume your own head.. impressive, but....")
    else:
        cthulhu_room()


def dead(why):
    print(why, "\n\n\tYou died!  You stink, loser!\n")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve to death.")


start()