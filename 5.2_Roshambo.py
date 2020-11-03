'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random
win = 0
loss = 0
tie = 0
cont = 1
while cont == 1:
    print("Choose Rock (1), Paper (2), or Scissors (3)")
    choice = int(input("Your choice:  "))

    i = random.randrange(1,4)
    if i == 1:
        print("Code: Rock")
    elif i == 2:
        print("Code: Paper")
    else:
        print("Code: Scissors")
    if choice == 1 and i == 2 or choice == 2 and i == 3 or choice == 3 and i == 1:
        print("How'd you lose? You can literally see the code fool")
        loss = loss + 1
        print("Your current score (win loss tie):", win, tie, loss)
        print()
    elif choice == 1 and i == 3 or choice == 2 and i == 1 or choice == 3 and i == 2:
        print("How'd you win? I thought I rigged this code")
        win = win + 1
        print("Your current score (win loss tie):", win, tie, loss)
        print()
    elif choice == 1 and i == 1 or choice == 2 and i == 2 or choice == 3 and i == 3:
        print("Ties are just undocumented losses, but I will document them so I can laugh at you")
        tie = tie + 1
        print("Your current score (win loss tie):", win, tie, loss)
        print()
    quit = input("Would you like to keep embarrassing yourself? (y)es or (n)o?  ")
    if quit == "y":
        print("Alright. Suffer then.")
        print()
        cont = 1
    else:
        print("Finally.  I need an actual person, not a bot")
        cont = 0
