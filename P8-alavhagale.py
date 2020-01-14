""" Akshay Lavhagale
   P8: Counting unique items
   mbox.txt file from the previous assignment and counts the total number of email messages sent by each user.
"""
import re
from collections import defaultdict
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def check_valid_email(email):
    if re.search(regex, email):
        return True
    return False


def read_file():
    name = input('Enter the file name: ')
    try:
        fp = open(name, 'r')
    except FileNotFoundError:
        print(f'File {name} cannot be opened.')
    else:
        with fp:
            ''' A defaultdict will never raise a KeyError '''
            emails = defaultdict(int)
            for line in fp:
                ''' only print out lines which started with "From:" using string method startswith() '''
                name = line[5:].strip()
                if line.startswith("From:") and check_valid_email(name):
                    emails[name] += 1
            print(emails)
            try:
                q = max(emails, key=emails.get)
                ''' by using value of dictionary = emails[q] '''
                print("Maximum E-mails sent by E-mail address:" + q, "\nMax E-mails = " + str(emails[q]))
            except ValueError:
                print("File may be empty or it does not consist of sender E-mail addresses")


def main():
    read_file()


if __name__ == "__main__":
    main()
