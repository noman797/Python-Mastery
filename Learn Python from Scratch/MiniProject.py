#Number Guessing Game 

import random
secret_number=random.randint(1,10)
attempts=3

print("I'm thinking of a number between 1 and 10")

while attempts>0:
     guess= int (input("Take a Guess: "))
     if guess==secret_number:
        print("You guessed it right!")
        break
     elif guess>secret_number:
        print("Too high!")
     else:
        print("Too low!")

        attempts=attempts-1

     if attempts == 0:
        print("You lost! The number was:", secret_number) 