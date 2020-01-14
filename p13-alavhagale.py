
""" Akshay Lavhagale
   P13: Data Visualization
   Read the contents of the file and calculate how many emails are sent each day of the week.
"""

import matplotlib.pyplot as mp


def name_of_file():
    """ asking user for name of the file """
    name_of_file = input("Enter the name of the file: ")
    return name_of_file


def read_file(file):
    name_of_file = input("Enter the name of the file: ")
    try:
        fp = open(name_of_file, 'r')
    except FileNotFoundError:
        print("This file does not exist, please provide the correct input.")
        exit()
    else:
        with fp:
            for line in fp:
                line = line.strip("\n")
                email = line.find("From")
                email_character_1 = line.find("@")
                line = line[-24:]
                email_character_2 = line.find("@")
                if email == 0 and email_character_1 > 0 and email_character_2 == -1:
                    line = line[:-21]
                    yield line


def main():
    """ Using Dictionary, keys = days of email and value = count of respective email """
    name = name_of_file()
    dictionary = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0}
    mails = read_file(name)
    count = 0
    for cnt in mails:
        if cnt in dictionary:
            dictionary[cnt] += 1
        count += len(cnt)
    value = dictionary.values()
    key = dictionary.keys()
    zip_dictionary = zip(dictionary.keys(), dictionary.values())
    for cnt in value:
        cnt = value
        cnt_1 = key
        mp.bar(cnt_1, cnt, align='center', alpha=0.5)

    mp.ylabel("Total number of emails")
    mp.title("Number of emails as per day")
    mp.show()


if __name__ == '__main__':
    main()