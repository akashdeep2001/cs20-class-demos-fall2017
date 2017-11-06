import turtle

the_window = turtle.Screen()
the_window.bgcolor("blue")

roger = turtle.Turtle()
roger.color("yellow")
roger.pensize(4)

for tower in range(4):
    for side in range(3):
        roger.forward(100)
        roger.left(90)
    roger.left(180)
