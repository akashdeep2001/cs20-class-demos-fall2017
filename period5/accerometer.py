import microbit

def horizontal_tilt(sensitivity_amount):
    """Returns left or right, depending on which way the micro:bit is tilted. Small sensitivity_amount is more sensitive, large sensitivity_amount is less sensitive."""
    x_tilt = microbit.accelerometer.get_x()

    if x_tilt > sensitivity_amount:
        return "right"

    elif x_tilt < -1 * sensitivity_amount:
        return "left"


while True:
    horizontal_tilt_direction = horizontal_tilt(100)

    if horizontal_tilt_direction == "right":
        microbit.display.show("R")
        print("Tilted right.")

    elif horizontal_tilt_direction == "left":
        microbit.display.show("L")
        print("Tilted left.")

    else:
        microbit.display.show("-")
        print("Flat!")