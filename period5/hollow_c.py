import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

sebastian = turtle.Turtle()
sebastian.color("blue")
sebastian.pensize(5)
sebastian.shape("turtle")
sebastian.speed(7)

sebastian.left(90)

#get to a better starting location
sebastian.left(90)
sebastian.up()
sebastian.backward(150)
sebastian.down()

for side in range(3):
    sebastian.forward(150)
    sebastian.right(90)

sebastian.forward(20)
sebastian.right(90)
sebastian.forward(130)
sebastian.left(90)
sebastian.forward(110)
sebastian.left(90)
sebastian.forward(130)
sebastian.right(90)
sebastian.forward(20)

#put sebastian back to the start
sebastian.right(90)
sebastian.forward(150)
sebastian.right(90)
