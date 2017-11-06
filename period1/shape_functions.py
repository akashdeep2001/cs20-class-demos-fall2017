import turtle

def draw_cross(some_turtle, side_length):
    """Draws a cross shape with some_turtle, with each side being side_length long."""
    for tower in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)

def draw_hollow_c(a_turtle, longest_side_length, width_of_c):
    """Draws a hollow C shape, with the sides being calculated from longest_side_length and width_of_c."""
    a_turtle.right(-90)
    for side in range(2):
        a_turtle.forward(longest_side_length)
        a_turtle.right(90)

    a_turtle.forward(width_of_c)
    a_turtle.right(90)
    a_turtle.forward(longest_side_length-width_of_c)
    a_turtle.right(-90)
    a_turtle.forward(longest_side_length-width_of_c*2)
    a_turtle.right(-90)
    a_turtle.forward(longest_side_length-width_of_c)
    a_turtle.right(90)
    a_turtle.forward(width_of_c)

    a_turtle.right(90)
    a_turtle.forward(longest_side_length)
    a_turtle.right(90)

########################################################

the_window = turtle.Screen()
the_window.bgcolor("blue")

roger = turtle.Turtle()
roger.color("yellow")
roger.pensize(4)

#draw_cross(roger, 150)
draw_hollow_c(roger, 250, 50)