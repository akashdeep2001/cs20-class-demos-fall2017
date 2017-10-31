# Color Selection

import turtle

# create window, and set it's color
canvas = turtle.Screen()
the_background_color = canvas.textinput("Color", "Please enter the background color: ")
canvas.bgcolor(the_background_color)

#create the turtle, and it's attributes
bree = turtle.Turtle()
the_turtles_color = canvas.textinput("Turtle color", "Please enter the color for the turtle: ")
bree.color(the_turtles_color)
bree.pensize(3)

#draw!
bree.forward(100)
bree.right(60)
bree.forward(100)
