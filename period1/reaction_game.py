# Mico:bit Reaction Game
# Computer Science 20
# Dan Schellenberg

import microbit
import random
import time


def button_clicked(current_score, should_be_pressing):
    if should_be_pressing == True:
        current_score += 1
    else:
        current_score -= 2

    return current_score


# global variables
a_score = 0
b_score = 0
run_reset_code = True
showing_image = False
correct_image = False
time_to_wait = 0
starting_time = 0
ending_time = 0

# constants
POINTS_TO_WIN_GAME = 3
SKULL_WAIT_TIME = 2

# game loop
while True:
    # check if need to pick a new amount of time to wait
    if run_reset_code == True:
        microbit.display.clear()
        showing_image = False

        # pausing execution for 1 second stops players from accidentally clicking more than once
        time.sleep(1)

        time_to_wait = random.randrange(1, 6)
        starting_time = time.time()

        # decide whether to show the SKULL or HAPPY face
        some_number = random.randrange(0,100)
        if some_number < 30:
            correct_image = False
        else:
            correct_image = True

        # don't run this code again until a button is pressed, or skull is shown
        run_reset_code = False

    # check if it is time to display the image
    time_now = time.time()
    time_since_start = time_now - starting_time
    if time_since_start > time_to_wait:
        showing_image = True
        
        # reset image after additional wait time, if it's a SKULL
        if correct_image == False and time_since_start > time_to_wait + SKULL_WAIT_TIME:
            run_reset_code = True

    if showing_image == True:
        if correct_image == True:
            microbit.display.show(microbit.Image.HAPPY)
        else:
            microbit.display.show(microbit.Image.SKULL)

    # is this the right time to click?
    should_have_clicked = showing_image and correct_image

    # deal with a button being pressed
    if microbit.button_a.is_pressed():
        a_score = button_clicked(a_score, should_have_clicked)
        print("Player A:", a_score, "    Player B:", b_score)
        run_reset_code = True


    if microbit.button_b.is_pressed():
        b_score = button_clicked(b_score, should_have_clicked)
        print("Player A:", a_score, "    Player B:", b_score)
        run_reset_code = True

    # if somebody wins, end the game
    if a_score >= POINTS_TO_WIN_GAME or b_score >= POINTS_TO_WIN_GAME:
        break


print("Game over!")

if a_score > b_score:
    print("Player A wins!")
    microbit.display.show("A")

elif b_score > a_score:
    print("Player B wins!")
    microbit.display.show("B")

else:
    print("It's a tie!")
    microbit.display.show("?")
