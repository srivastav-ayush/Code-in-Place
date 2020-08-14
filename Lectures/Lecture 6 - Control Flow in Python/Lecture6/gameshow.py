"""
File: gameshow.py
------------------
Lets play a gameshow!
"""


def main():
    print("Welcome to the CS106A Game Show")
    print("Chose a door and pick a prize")
    print("-------------")

    # PART 1: Get the door number from the user
    door = int(input("Door: "))
    # while the input is invalid
    while door < 1 or door > 3:
        # tell the user the input was invalid
        print("Invalid door!")
        # ask for a new input
        door = int(input("Door: "))

    # PART 2: Compute the prize.
    prize = 4
    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        locked = prize % 2 != 0
        if not locked:
            prize += 5
    elif door == 3:
        for i in range(door):
            prize += i

    print('You win: $' + str(prize))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()