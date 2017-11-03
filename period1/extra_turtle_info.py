import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

avery = turtle.Turtle()
avery.color("red")
avery.pensize(5)
avery.shape("turtle")
avery.speed(1)

for tick_mark in range(12):
    avery.up()
    avery.forward(150)
    avery.stamp()
    avery.backward(150)
    avery.left(360/12)
