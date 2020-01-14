""" Akshay Lavhagale
    P10: Writing Regex's
    From the file, compute the average of the numbers, rounded to a single decimal place, and
    print out the average and the number of lines used for the computation
"""

import re


def writing_regex():
    name = input('Enter the file name: ')
    try:
        fp = open(name, 'r')
    except FileNotFoundError:
        print(f'File {name} cannot be opened.')
    else:
        values_list = list()
        with fp:
            for line in fp:
                regex_1 = r'New Revision: (\d+)'
                # Extract the number from each of the lines using a regular expression and the findall() method
                find_all = re.findall(regex_1, line)
                if find_all:
                    values_list.append(int(find_all[0]))
            try:
                avg = sum(values_list) / len(values_list)
            except ZeroDivisionError as e:
                print(e)
            else:
                print("Average: " + str(round(avg, 1)))
                print("Number of lines: " + str(len(values_list)))


if __name__ == "__main__":
    writing_regex()
