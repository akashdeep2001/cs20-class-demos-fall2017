import microbit
import turtle

def horizontal_tilt(sensitivity_amount):
    """Returns left or right, depending on which way the micro:bit is tilted. Small sensitivity_amount is more sensitive, large sensitivity_amount is less sensitive."""
    x_tilt = microbit.accelerometer.get_x()

    if x_tilt > sensitivity_amount:
        return "right"

    elif x_tilt < -1 * sensitivity_amount:
        return "left"


window = turtle.Screen()
window.bgcolor("black")

david = turtle.Turtle()
david.color("white")
david.pensize(5)

while True:
    horizontal_tilt_direction = horizontal_tilt(100)

    if horizontal_tilt_direction == "right":
        microbit.display.show("R")
        david.forward(10)

    elif horizontal_tilt_direction == "left":
        microbit.display.show("L")
        david.backward(10)

    else:
        microbit.display.show("-")
        david.left(5)