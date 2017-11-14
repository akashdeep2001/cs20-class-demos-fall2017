# Rectangle Shapes
# Nov 14, 2017
# Dan Schellenberg

import turtle

def draw_rectangle(some_turtle, length, width):
    for i in range(2):
        some_turtle.forward(length)
        some_turtle.left(90)
        some_turtle.forward(width)
        some_turtle.left(90)

def draw_rotated_rectangles(some_turtle, length, width, number_of_rectangles):
    for rectangle in range(number_of_rectangles):
        draw_rectangle(some_turtle, length, width)
        some_turtle.left(360/number_of_rectangles)

canvas = turtle.Screen()
canvas.bgcolor("black")

wilson = turtle.Turtle()
wilson.color("yellow")
wilson.pensize(4)

draw_rotated_rectangles(wilson, 150, 50, 4)