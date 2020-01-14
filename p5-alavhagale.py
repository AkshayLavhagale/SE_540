""" Akshay Lavhagale
   P5: String manipulation
   Use a simplified set of rules for converting singular to plural.
"""


def plural():
    x = input('Please enter your input:')

    # x.lower() - Returns a copy of the string in which all case-based characters have been lowercase
    x = x.lower()

    # x.split() - Returns a list of strings after breaking the given string by the specified separator
    y = x.split()
    for elem in y:
        # Python string method isdigit() checks whether the string consists of digits only
        if elem.isdigit():
            print(f"{elem} is not a string")
        else:
            # endswith() returns True if the string ends with the specified suffix, otherwise return False
            # if the word ends in a 'y' preceded by a vowel (a,e,i,o,u), add 's'
            if elem.endswith(('ay', 'ey', 'iy', 'oy', 'uy')):
                new_x = elem + 's'
                print(new_x)
            # if the word ends in 'y' not preceded by a vowel, remove the 'y' and add 'ies'
            elif elem.endswith('y'):
                # slice object representing the set of indices specified by range
                new_x = elem[:-1] + 'ies'
                print(new_x)

            # if the word ends in 'o','ch', 's', 'sh', 'x', or 'z' then add 'es'
            elif elem.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
                new_x = elem + 'es'
                print(new_x)

            # if none of the above condition matches then just add 's' in element
            else:
                new_x = elem + 's'
                print(new_x)


plural()
