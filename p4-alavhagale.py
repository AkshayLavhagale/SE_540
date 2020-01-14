""" Akshay Lavhagale
   P4: Guess a Number using loops and a function
   Function that takes two parameters, the number to be guessed and the number that was guessed
   """

import random


def no_of_chances():
    # There are maximum of 6 chance for user and we counts it through variable called no_of_chance
    no_of_chance = 0
    # Randint takes two parameters, i.e., random.randint(lower-bound, upper-bound)
    n = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print("Well," + name + ",I am thinking of a number between 1 and 20")
    try:
        # The user guesses the number in < 6 tries
        while no_of_chance < 6:
            guess = int(input("Enter an integer from 1 to 20: "))
            # The user enters a value < 1 or > 20
            if guess <= 0:
                print("Please enter value in range of 1 to 20!")
                continue
            elif guess > 20:
                print("Please enter value in range of 1 to 20!")
                continue
            no_of_chance = no_of_chance + 1
            if n != guess:
                # If the number to be guessed is larger than the number that was guessed
                if guess < n:
                    print("guess is low")
                # If the number to be guessed is smaller than the number that was guessed
                elif guess > n:
                    print("guess is high")
            # If the two numbers match
            else:
                no_of_chance = str(no_of_chance)
                print("Good job, " + name + "! You guessed my number in " + no_of_chance + " guesses!")
                break
    # The user enters invalid input, e.g. twenty
    except ValueError:
        print("Please enter a number.")
    # The user doesn't guess the number in 6 tries
    finally:
        if guess != n:
            n = str(n)
            print('Nope. The number I was thinking of was ' + n)


no_of_chances()
