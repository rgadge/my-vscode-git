# This is a fun program, it will pick a random number between 1 to 20 and will let you guess the number in 6 attempts.

import random

print("Please enter your name: ", end="")
name = input()

print("Hello, " + name + " This program will pick a random number and will give you 6 chances to correctly guess it")
secretnumber = random.randint(1, 20)
print("Guess the number")

for i in range(1, 7):
    try:
        guessnumber = int(input())
    except ValueError:
        print("Please enter a number between 1 to 20.")
        continue
    if guessnumber > secretnumber:
        print("Your guess is too high!")
        continue
    elif guessnumber < secretnumber:
        print("Your guess is too low!")
        continue
    else:
        break

if guessnumber == secretnumber:
    print("You guessed it right in ", i, " guesses!!")
else:
    print("Well tried but you failed to guess the number", secretnumber, "in 6 attemots") 
