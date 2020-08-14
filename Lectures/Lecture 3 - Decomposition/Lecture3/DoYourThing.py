from karel.stanfordkarel import *

def main():
    while front_is_blocked():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()



if __name__ == "__main__":
    run_karel_program()