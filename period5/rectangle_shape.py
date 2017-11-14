# Rectangle Shapes
# Nov 14, 2017
# Dan Schellenberg

import turtle

def draw_rectangle(my_turtle, length, width):
    """Draw a rectangle from the bottom left corner, with length and width."""
    for i in range(2):
        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(width)
        my_turtle.left(90)

def draw_rotated_rectangles(a_turtle, length, width, number_of_rectangles):
    """Draw number_of_rectangles, rotating in a full circle while doing so."""
    for rectangle in range(number_of_rectangles):
        draw_rectangle(a_turtle, length, width)
        a_turtle.left(360/number_of_rectangles)

canvas = turtle.Screen()
canvas.bgcolor("black")

travis = turtle.Turtle()
travis.color("hotpink")
travis.pensize(4)

draw_rotated_rectangles(travis, 150, 40, 4)
