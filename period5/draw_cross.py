import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

ramisa = turtle.Turtle()
ramisa.color("blue")
ramisa.pensize(4)

for tower in range(4):
    for side in range(3):
        ramisa.forward(100)
        ramisa.left(90)
    ramisa.left(180)

