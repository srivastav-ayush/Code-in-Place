"""
File: count_each_word.py
------------------------
This program counts the number of each word in a text file.
Uses a dictionary to store the results, where each key is a
word and the corresponding value is the number of times that
word appeared in the file.
"""

import sys

PUNCTUATION = '.!?,-:;'


def delete_punctuation(s):
    """
    Removes punctuation characters from a string and returns the
    resulting string (without punctuation).
    >>> delete_punctuation('REMOVE --the-- punctuation!!!!')
    'REMOVE the punctuation'
    """
    result = ''
    for char in s:
        # Check char is not a punctuation mark
        if char not in PUNCTUATION:
            result += char          # append non-punctuation characters

    return result


def get_counts_dict(filename):
    """
    Reads file and returns a dictionary with the words in the file
    and the number of occurrences of each word.
    """
    counts = {}                             # create empty dictionary

    with open(filename, 'r') as file:       # open file for reading
        for line in file:
            words = delete_punctuation(line).split()
            for word in words:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1

    return counts


def main():
    """
    The name of the file in which we should count the number of
    appearances of each words should be the first (and only)
    command line argument
    """
    args = sys.argv[1:]

    if len(args) == 1:
        print(get_counts_dict(args[0]))


# Python boilerplate.
if __name__ == '__main__':
    main()
