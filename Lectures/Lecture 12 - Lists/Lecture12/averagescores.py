"""
File: averagescores.py
----------------------
This program reads score values from a user and computes their
average.  It also adds extra credit to all the scores and computes
the new average.
"""


EXTRA_CREDIT = 5


def get_scores():
    """
    Asks the user for a list of scores (numbers).
    Returns a list containing the scores
    """
    score_list = []
    while True:
        score = float(input("Enter score (0 to stop): "))
        if score == 0:
            break
        score_list.append(score)
    return score_list


def compute_average(score_list):
    """
    Returns the average value of the list of scores passed in.
    >>> compute_average([1.0, 2.0, 3.0, 4.0])
    2.5
    >>> compute_average([1.0, -1.0])
    0.0
    """
    num_scores = len(score_list)
    total = sum(score_list)
    return total / num_scores


def give_extra_credit(score_list, extra_credit_value):
    """
    Adds extra_credit_value to all the values in score_list.
    """
    for i in range(len(score_list)):
        score_list[i] += extra_credit_value


def print_list(alist):
    """
    Prints all the values in the list passed in
    """
    for value in alist:
        print(value)


def main():
    """
    Computes average for a set of scores entered by the user.
    Then adds extra credit to scores and recomputes average.
    """
    scores = get_scores()
    print("Scores are:")
    print_list(scores)
    avg = compute_average(scores)
    print('Average score is ' + str(avg))

    print('Adding extra credit: ' + str(EXTRA_CREDIT) + " points")
    give_extra_credit(scores, EXTRA_CREDIT)
    print("New scores are:")
    print_list(scores)
    avg = compute_average(scores)
    print('New average is ' + str(avg))


if __name__ == '__main__':
    main()
