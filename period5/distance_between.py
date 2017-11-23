import turtle

def turtles_are_touching(first_turtle, second_turtle, close_enough_distance):
    """Returns True or False, based on whether two turtles are 'close enough' to be touching."""

    x_dist = first_turtle.xcor() - second_turtle.xcor()
    y_dist = first_turtle.ycor() - second_turtle.ycor()
    
    distance_apart = ( x_dist**2 + y_dist**2) ** 0.5
    
    if distance_apart < close_enough_distance:
        return True
    else:
        return False


canvas = turtle.Screen()
canvas.bgcolor("black")

charlie = turtle.Turtle()
charlie.color("blue")
charlie.up()

musawer = turtle.Turtle()
musawer.color("red")
musawer.up()

charlie.goto(-200, 0)
musawer.goto(200, 5)

musawer.left(180)

while not turtles_are_touching(charlie, musawer, 7):
    charlie.forward(5)
    musawer.forward(2)


print("close enough")