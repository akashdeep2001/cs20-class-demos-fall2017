# Color Selection

import turtle

# create window, and set it's color
canvas = turtle.Screen()
the_background_color = canvas.textinput("Color", "Please enter a background color: ")
canvas.bgcolor(the_background_color)

#create the turtle, and it's attributes
bree = turtle.Turtle()
brees_color = canvas.textinput("Color", "Please enter the color of the turtle: ")
bree.color(brees_color)
bree.pensize(3)

#draw!
bree.forward(100)
bree.right(60)
bree.forward(100)
