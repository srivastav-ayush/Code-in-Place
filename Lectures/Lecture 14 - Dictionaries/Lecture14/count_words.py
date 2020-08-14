"""
File: count_words.py
--------------------
This program counts the number of words in a text file.
"""

import sys


def count_words(filename):
    """
    Counts the total number of words in the given file and
    print it out.
    """
    count = 0
    with open(filename, 'r') as file:   # Open file to read
        for line in file:
            line = line.strip()         # Remove newline
            word_list = line.split()    # Create list of words
            for word in word_list:      # Print words
                print("#" + str(count) + ": " + word)
                count += 1
    print(filename + " contains " + str(count) + " words")


def main():
    """
    The name of the file to count words in should be the first
    (and only) command line argument.
    """
    args = sys.argv[1:]

    if len(args) == 1:
        count_words(args[0])


# Python boilerplate.
if __name__ == '__main__':
    main()
