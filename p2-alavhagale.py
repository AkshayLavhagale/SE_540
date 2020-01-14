# Akshay Lavhagale
# P2: Convert numeric scores to grades.
# Write a script that asks the user for a quiz score and converts that numeric score to a letter grade."""


def get_grades():
    # Function helps to avoid repetition and makes code reusable.
    while True:
        # If no exception occurs, the except clause is skipped and execution of the try statement is finished.
        try:
            # Value input is in float number.
            score = float(input("Enter a number between 0 and 100: "))
            break
        except ValueError:
            print("Please enter numerical value")
    if (score > 100) or (score < 0):
        print("Please enter your response in between 0 to 100")
    elif score >= 93:
        print("A")
    elif score >= 90:
        print('A-')
    elif score >= 87:
        print('B+')
    elif score >= 83:
        print('B')
    elif score >= 80:
        print('B-')
    elif score >= 70:
        print('C')
    else:
        print('F')


get_grades()
