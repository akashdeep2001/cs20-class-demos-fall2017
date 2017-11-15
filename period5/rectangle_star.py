import turtle

def draw_rectangle(my_turtle, length, width):
    """Draw a rectangle from the bottom left corner, with length and width."""
    for i in range(2):
        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(width)
        my_turtle.left(90)

def draw_rectangle_star(a_turtle, length, width, number_of_rectangles):
    """Draws a star shape using number_of_rectangles, rotating each time."""
    for rectangle in range(number_of_rectangles):
        draw_rectangle(a_turtle, length, width)
        a_turtle.left(90)
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.left(360/number_of_rectangles)

canvas = turtle.Screen()
canvas.bgcolor("black")

mashood = turtle.Turtle()
mashood.color("white")
mashood.pensize(5)
mashood.speed(6)

draw_rectangle_star(mashood, 150, 40, 8)
