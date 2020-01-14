""" Akshay Lavhagale
    P9: Classic Books
    Program that prompts the user for the name of a file with an arbitrary ASCII document, reads the file,
    and prints a summary of the words in the document
"""

from collections import defaultdict
from operator import itemgetter
from string import punctuation


def remove_punctuation(clean_string):
    punc_translator = str.maketrans({key: None for key in punctuation})
    """ use translate() to remove all punctuation characters """
    clean_string_1 = clean_string.translate(punc_translator).replace('“', '').replace('”', '')
    return clean_string_1


def classic_books():
    name = input('Enter the file name: ')
    try:
        fp = open(name, 'r')
    except FileNotFoundError:
        print(f'File {name} cannot be opened.')
    else:
        with fp:
            words_count = 0
            """ The default value will be an int with value 0 """
            default_dict = defaultdict(int)
            default_dict_1 = defaultdict(int)
            for line in fp:
                total_words = remove_punctuation(line).lower().split()
                words_count = words_count + len(total_words)
                for new_key in total_words:
                    """ dd['newKey'] += 1 """
                    default_dict[new_key] += 1
                    for new_key_1 in new_key:
                        default_dict_1[new_key_1] += 1
            """  List is sorted by the key, not the value """
            sort_dict = sorted(default_dict.items(), key=itemgetter(1), reverse=True)
            sort_dict_1 = sorted(default_dict_1.items(), key=itemgetter(1), reverse=True)
            print("The summary of classic book includes:")
            """ When printing large numbers, we should include commas """
            print("Total words: " + str('{:,}'.format(words_count)))
            print("Total distinct words: " + str(len(sort_dict)))
            """ Identify the 25 most frequent words using slices """
            print("The top 25 most frequent words and counts: " + str(sort_dict[:25]))
            print("Character frequency: " + str(sort_dict_1))


def main():
    classic_books()


if __name__ == "__main__":
    main()
