# Color Selection

import turtle

the_background_color = input("Please enter the background color: ")
the_turtles_color = input("Please enter the color for the turtle: ")

# create window, and set it's color
canvas = turtle.Screen()
canvas.bgcolor(the_background_color)

#create the turtle, and it's attributes
bree = turtle.Turtle()
bree.color(the_turtles_color)
bree.pensize(3)

#draw!
bree.forward(100)
bree.right(60)
bree.forward(100)
