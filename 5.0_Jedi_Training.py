  #Sign your name:Tom Dau

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    i = int(input("Enter a number: "))
    total = total + i
print("The total is:", total)
  

cont = "no"
while cont == "no":                                         # This is just to keep things a little more clean rather than have it run all of them at the same time
    cont = input("Would you like to continue? Yes or no?  ")
    if cont == "no":
        print("Too bad lmao. I'll ask you again")


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(1,51):
    i = i * 2
    print(i)

cont = "no"
while cont == "no":
    cont = input("Would you like to continue? Yes or no? ")
    if cont == "no":
        print("Too bad lmao. I'll ask you again")

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
number = 10
while number >= 0:
    print(number)
    number = number - 1
print("Blast off!")

cont = "no"
while cont == "no":
    cont = input("Would you like to continue? Yes or no?  ")
    if cont == "no":
        print("Too bad lmao. I'll ask you again")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
print(random.randrange(1,11))

cont = "no"
while cont == "no":
    cont = input("Would you like to continue? Yes or no?  ")
    if cont == "no":
        print("Too bad lmao. I'll ask you again")


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
pos = 0
zero = 0
neg = 0
for i in range(7):
    i = int(input("Please enter a number"))
    if i > 0:
        pos = pos + 1
    elif i < 0:
        neg = neg + 1
    else:
        zero = zero + 1
    total = total + i
print("Your total is:", total)
print("The amount of positive numbers you entered is:", pos)
print("The amount of negative numbers you entered is:", neg)
print("The amount of zeros you entered is:", zero)