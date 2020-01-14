""" Akshay Lavhagale
   P7: Finding unique strings
   Using mbox.txt file, find the lines that start with From: and determine how many unique sender email addresses.
"""


def read_file():
    name = input('Enter the file name: ')
    try:
        file = open(name, 'r')
    except FileNotFoundError:
        print(f'File {name} cannot be opened.')
    else:
        ''' set() method is converts any of the iterable to the distinct element and sorts sequence of elements '''
        s1 = set()
        ''' for loop reads the data one line at a time '''
        for line in file:
            ''' rstrip() method returns copy of the string in which all chars have been stripped from end of string '''
            line = line.rstrip()
            ''' only print out lines which started with "From:" using string method startswith() '''
            if line.startswith("From:"):
                ''' find() function looks for an occurrence of  a string within another string and either 
                    returns the position of the string or -1 if the string was not found '''
                value = line[line.find("From:") + 1:]
                s1.add(value)
            else:
                if not line.startswith('From:'):
                    continue
        print(f"There are {len(s1)} unique email addresses.")


def main():
    read_file()


if __name__ == "__main__":
    main()
