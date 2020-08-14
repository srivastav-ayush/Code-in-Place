"""
File: nimm.py
-------------------------
Add your comments here.
"""

# Total number of stones present at the starting of the game
TOTAL = 20


def main():
    # Setting the value of stones equal to the total number of stones present in the pile at the start of the game
    stones = TOTAL

    while stones > 0:

        # Turn of Player 1 to pick the stones
        print("There are " + str(stones) + " stones left")
        player1 = int(input("Player 1 would you like to remove 1 or 2 stones? \n"))
        while player1 < 1 or player1 > 2:
            player1 = int(input("Please enter 1 or 2: \n"))
        # Remove the number of stones picked by Player 1 from the total number of stones in pile
        stones = stones - player1
        # If no stones are left in the pile of stones Player 2 wins the game of Nimm
        if stones == 0:
            print("Player 2 wins!")
            break

        # Turn of Player 2 to pick the stones
        print("There are " + str(stones) + " stones left")
        player2 = int(input("Player 2 would you like to remove 1 or 2 stones? \n"))
        while player2 < 1 or player2 > 2:
            player2 = int(input("Please enter 1 or 2: \n"))
        # Remove the number of stones picked by Player 2 from the total number of stones in pile
        stones = stones - player2
        # If no stones are left in the pile of stones Player 1 wins the game of Nimm
        if stones == 0:
            print("Player 1 wins!")
            break


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
