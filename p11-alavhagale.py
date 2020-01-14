""" Akshay Lavhagale
    P11: Browsing the Web
    Write a Python script that is able to read an arbitrary URL provided by the user and count the
    number of unique web links on that page """


import re
from urllib.request import urlopen
import urllib


def main():
    # web link can be identified with a regular expression that recognizes http and https references
    regex_characters = '("(?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*)")'
    # re.IGNORECASE perform case-insensitive matching; expressions like [A-Z] will match lowercase letters, too
    # re.DOTALL make the '.' special character match any character at all, including a newline
    rg = re.compile(regex_characters, re.IGNORECASE | re.DOTALL)
    link = input("Enter the link: ")
    try:
        fp = urlopen(link)
    except ValueError as ve:
        print(ve)
    # The reason for this error can be a message string or another exception instance
    except urllib.error.URLError as u_err:
        print(u_err)
    except Exception as e:
        print(e)
    else:
        my_file = fp.read()
        txt = str(my_file)
        # rg.findall = find all substrings where the regular expression matches, and returns them as a list
        find_text = rg.findall(txt)
        find_text_1 = set(find_text)
        print("The number of unique web links on that page = " + str(len(find_text_1)))


if __name__ == "__main__":
    main()

# https://google.com/maps
