import turtle

def draw_rectangle(my_turtle, length, width):
    """Draw a rectangle from the bottom left corner, with length and width."""
    for i in range(2):
        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(width)
        my_turtle.left(90)

def draw_rectangle_star(some_turtle, length, width, number_of_rectangles):
    """Draw a star out of number_of_rectangles, rotating each time."""
    for rectangle in range(number_of_rectangles):
        draw_rectangle(some_turtle, length, width)
        some_turtle.left(90)
        some_turtle.forward(width)
        some_turtle.right(90)
        some_turtle.left(360/number_of_rectangles)

window = turtle.Screen()

asir = turtle.Turtle()
asir.color("blue")
asir.pensize(5)

draw_rectangle_star(asir, 125, 30, 8)
