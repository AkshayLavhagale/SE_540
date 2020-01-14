""" Akshay Lavhagale
   P3: User defined functions
   Define a function called 'maxOfThree' that takes three values and returns the maximum value of the three.
"""


def maxofthree():
    while True:
        try:
            x = float(input("Please enter first number: "))
            y = float(input("Please enter second number: "))
            z = float(input("Please enter third number: "))
            break
        # If no exception occurs, the except clause is skipped and execution of the try statement is finished
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    if x == y == z:
        print("They are equal")
    elif x > y and x > z:
        max_of_three = x
        print(max_of_three)
    else:
        if y > z:
            max_of_three = y
            print(max_of_three)
        else:
            max_of_three = z
            print(max_of_three)


maxofthree()
