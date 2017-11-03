import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

sebastian = turtle.Turtle()
sebastian.color("blue")
sebastian.pensize(5)
sebastian.shape("turtle")
sebastian.speed(1)

sebastian.up()

for tick_mark in range(12):
    sebastian.forward(150)
    sebastian.stamp()
    sebastian.backward(150)
    sebastian.left(360/12)
