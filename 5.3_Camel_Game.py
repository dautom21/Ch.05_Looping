'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

print("Tom and Jerry, but You're Jerry")                           #Can I use this and try to make a 2 player game for that last assignment?
print()

start = 1
while start == 1:
    play = input("Would you like to play? YES or NO?  ")
    print()
    if play.upper() == "YES":
        start = 0
    else:
        print("Too bad. This is an intentional game design.")       #I know how to make it end, I just don't want to.

print("You have stolen a piece of cheese from the fridge for Nibbles Mouse,")
print("but you accidentally closed the fridge a little too loud. You must run")
print("back 250 feet to the hole before Tom catches you.")
print()

ask = input("Would you like to see the controls? YES or NO?  ")
print()
if ask.upper() == "YES":
    print("Controls:")
    print("1: WALK - Walk randomly between 5-8 feet")
    print("2: SPRINT - Sprint randomly between 9-12 feet")
    print("3: EAT - Eat some cheese. You can only eat 5 times, otherwise there won't be enough for Nibbles")
    print("4: STATS - Opens stats (distance travelled, food eaten, hunger level, traps left, )")
    print()                                                         #I wanted to make a feature that allowed you to place traps
                                                                    #But 1: I couldn't figure it our 2: was stressing over other things
nom = 0                                                             #3: Panicking since we have 2 weeks left and i still havent started
cheese = 5                                                          #chapter 6. Sorry.
distance = 0
tomdistance = -20
endgame = False

while endgame == False:
    if distance >= 250:
        print("You've made it to the hole! Congratulations!")
        endgame = True
        continue

    player = input("1: WALK / 2: SPRINT / 3: EAT / 4: STATS  \n")

    if player.upper() == "WALK" or player == "1":
        nom = nom + 1
        if nom <= 2:
            distance = distance + random.randrange(5, 9)
            print("You've traveled", distance, "feet")
            print("You are not hungry\n")
        elif nom <= 5:
            distance = distance + random.randrange(5, 9)
            print("You've traveled", distance, "feet")
            print("You are hungry\n")
        elif nom <= 8:
            distance = distance + random.randrange(5, 9)
            print("You've traveled", distance, "feet")
            print("You are starving\n")
        elif nom > 8:
            print("You've travelled", distance, "feet")
            print("You are too exhausted to move. You must eat\n")

        tom = random.randrange(1, 3)
        if tom == 1 or tom == 2:
            tomdistance = tomdistance + random.randrange(9,13)
            if distance - tomdistance == 1:
                print("Tom is 1 foot behind you!")
                print()
            elif distance - tomdistance <= 0:
                print("Tom catches you and punts you out of the house")
                print()
                endgame = True
            else:
                print("Tom is", distance - tomdistance, "behind you")
                print()
        else:
            tomdistance = tomdistance + random.randrange (5, 9)
            if distance - tomdistance == 1:
                print("Tom is 1 foot behind you!")
                print()
            elif distance - tomdistance <= 0:
                print("Tom catches you and punts you out of the house")
                print()
                endgame = True
            else:
                print("Tom is:", distance - tomdistance, "behind you")



    elif player.upper() == "SPRINT" or player == "2":
        nom = nom + 2
        if nom <= 2:
            distance = distance + random.randrange(9, 13)
            print("You've traveled", distance, "feet")
            print("You are not hungry\n")
        elif nom <= 5:
            distance = distance + random.randrange(9, 13)
            print("You've traveled", distance, "feet")
            print("You are hungry\n")
        elif nom <= 8:
            distance = distance + random.randrange(9, 13)
            print("You've traveled", distance, "feet")
            print("You are starving\n")
        elif nom > 8:
            print("You've traveled", distance, "feet")
            print("You are too exhausted to move. You must eat.\n")

        tom = random.randrange(1, 3)
        if tom == 1 or tom == 2:
            tomdistance = tomdistance + random.randrange(9, 13)
            if distance - tomdistance == 1:
                print("Tom is 1 foot behind you!")
                print()
            elif distance - tomdistance <= 0:
                print("Tom catches you and punts you out of the house")
                print()
                endgame = True
            else:
                print("Tom is", distance - tomdistance, "behind you")
                print()
        else:
            tomdistance = tomdistance + random.randrange(5, 9)
            if distance - tomdistance == 1:
                print("Tom is 1 foot behind you!")
                print()
            elif distance - tomdistance <= 0:
                print("Tom catches you and punts you out of the house")
                print()
                endgame = True
            else:
                print("Tom is:", distance - tomdistance, "behind you")

    elif player.upper() == "EAT" or player == "3":
        if cheese == 0:
            print("You have to save some for Nibbles")
            print()
        else:
            cheese = cheese - 1
            nom = 0
            print("You have", cheese,"bites of cheese left")
            print()

    elif player.upper() == "STATS" or player == "4":
        print("You travelled", distance,"feet. You have", 250 - distance,"left.")
        print("You have", cheese,"bites of cheese left")
        if nom <= 4:
            print("You are not hungry\n")
        elif nom <= 10:
            print("You are hungry\n")
        elif nom <= 15:
            print("You are starving\n")