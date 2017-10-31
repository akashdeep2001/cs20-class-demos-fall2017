# Drawing any Size of Square

import turtle

# create window, and set it's color
canvas = turtle.Screen()
the_background_color = canvas.textinput("Color", "Please enter the background color: ")
canvas.bgcolor(the_background_color)

#create the turtle, and it's attributes
bree = turtle.Turtle()
the_turtles_color = canvas.textinput("Turtle color", "Please enter the color for the turtle: ")
bree.color(the_turtles_color)
the_pensize = canvas.numinput("Pensize", "Please enter the pensize:")
bree.pensize(the_pensize)
side_length = canvas.numinput("Side length", "Please enter the length of the sides:")

#draw!
for i in range(4):
    bree.forward(side_length)
    bree.left(90)

