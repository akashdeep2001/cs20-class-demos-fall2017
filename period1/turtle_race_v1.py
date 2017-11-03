import turtle
import random

window = turtle.Screen()
window.bgcolor('lightblue')

#create the turtles, and specify their attributes
lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

# move the turtles to their starting locations
andy.up()
lance.up()
andy.goto(-200,30)
lance.goto(-200,-30)

# your code goes here

#for step in range(200):
while andy.xcor() < 200 and lance.xcor() < 200:
    andy_step = random.randrange(1, 10)
    lance_step = random.randrange(1, 10)

    andy.forward(andy_step)
    lance.forward(lance_step)
