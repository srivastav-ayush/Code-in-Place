"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():

    # Setting the counter equals to 0 to count the number of times the loop runs
    count = 0
    # Asking a number as input from the user
    num = int(input("Enter a number: "))
    # Loop which runs till the final output number is 1
    while num != 1:
        # Counter increases by 1 each time the while loop runs
        count += 1
        # If the number is even the while loop enter this if command and produces an output number
        if num % 2 == 0:
            new_num = num / 2
            print(str(int(num)) + " is even, so I take half: " + str(int(new_num)))
            num = new_num
        # If the number is odd the while loop enter this if command and produces an output number
        elif num % 2 != 0:
            new_num = 3*num + 1
            print(str(int(num))+" is odd, so I make 3n + 1: "+str(int(new_num)))
            num = new_num
    # Printing the number of steps it takes to get 1 as the output number
    print("The process took "+str(int(count))+" steps to reach 1")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
