import turtle
import random

def is_in_screen(the_window, the_turtle):
    left_bound = -(the_window.window_width() / 2)
    right_bound = the_window.window_width() / 2
    top_bound = the_window.window_height() / 2
    bottom_bound = -(the_window.window_height() / 2)
    
    turtle_x = the_turtle.xcor()
    turtle_y = the_turtle.ycor()
    
    still_in = True
    
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False
    
    return still_in


canvas = turtle.Screen()
austin = turtle.Turtle()

while is_in_screen(canvas, austin):
    heads_or_tails = random.randrange(0, 2)
    if heads_or_tails == 0:
        austin.left(90)
    else:
        austin.right(90)
    austin.forward(50)

print("It's over. I'm outside the screen.")