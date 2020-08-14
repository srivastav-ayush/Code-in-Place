"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    # This is a program that prints a countdown from 10 to 1 followed by a "Liftoff!"
    count = 10
    for i in range(10):
        print(count-i)
    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
