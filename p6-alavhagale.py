""" Akshay Lavhagale
   P6: Slicing & Dicing files
   Write a program to prompt for a file name, and then read through the file and look for lines
"""


def read_file():
    name = input('Enter the file name: ')
    try:
        file = open(name, 'r')
    except FileNotFoundError:
        print(f'File {name} cannot be opened.')
    else:
        total = 0.0
        count = 0.0

        ''' for loop reads the data one line at a time '''
        for line in file:
            ''' only print out lines which started with X-DSPAM-Confidence using string method startswith'''
            if line.startswith("X-DSPAM-Confidence:"):
                ''' find function looks for an occurrence of a string within another string and either returns 
                    the position of the string or -1 if the string was not found'''
                total += float(line[line.find(":") + 1:])
                count += 1

        if count > 0:
            print("Average spam confidence:", round((total / count), 4))
        else:
            print("file does not have X-DSPAM-Confidence")


def main():
    read_file()


if __name__ == "__main__":
    main()

