"""
File: listparameter.py
---------------------
This program contains examples of using lists as parameters,
especially in different type of for loops.
"""


def add_five_buggy(alist):
    """
    Attempts to add 5 to all the elements in the list.
    BUGGY CODE!  Does not actually add 5 to the list elements
    if values are primitive type (like int or float), since
    value would just be a local copy of such variables.
    """
    for value in alist:
        value += 5


def add_five_working(alist):
    """
    Successfully adds 5 to all the elements in the list.
    Changes made to the list persist after this function ends
    since we are changing actual values in the list.
    """
    for i in range(len(alist)):
        alist[i] += 5


def create_new_list(alist):
    """
    Shows an example of what happens when you create a new list
    that has the same name as a parameter in a function.  After
    you create the new list, you are no longer referring to the
    parameter "alist" that was passed in
    """
    # This "alist" is referring to the parameter "alist"
    alist.append(9)

    # Creating a new "alist". This is not the same as the parameter
    # passed in.  After this line references to "alist" are no longer
    # referring to the parameter "alist" that was passed in.
    alist = [1, 2, 3]


def main():
    values = [5, 6, 7, 8]
    add_five_working(values)
    print(values)

    values = [5, 6, 7, 8]
    create_new_list(values)
    print(values)


if __name__ == '__main__':
    main()
