import microbit
import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

wendy = turtle.Turtle()
wendy.color("blue")
wendy.pensize(6)

angel = turtle.Turtle()
angel.color("white")
angel.pensize(6)

while True:
    if microbit.button_a.was_pressed():
        for side in range(4):
            wendy.forward(100)
            wendy.right(90)
            
    if microbit.button_b.was_pressed():
        for side in range(3):
            angel.forward(200)
            angel.left(120)

    