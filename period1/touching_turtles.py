import turtle

def are_they_touching(turtle1, turtle2, close_enough_distance):
    """Returns True or False, based on whether the turtles
       passed in are "close enough" to be touching."""
    
    x_change = (turtle1.xcor() - turtle2.xcor()) ** 2
    y_change = (turtle1.ycor() - turtle2.ycor()) ** 2
    
    dist_between = (x_change + y_change) ** 0.5
    
    if dist_between < close_enough_distance:
        return True
    else:
        return False


canvas = turtle.Screen()

bob = turtle.Turtle()
joe = turtle.Turtle()
bob.up()
joe.up()

bob.goto(-200, 0)
joe.goto(175, 3)
joe.left(180)

while not are_they_touching(bob, joe, 5):
    bob.forward(2)
    joe.forward(2)