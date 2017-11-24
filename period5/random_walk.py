import turtle
import random

def is_still_in_window(canvas, some_turtle):
    left_bound = -(window.window_width() / 2)
    right_bound = window.window_width() / 2
    top_bound = window.window_height() / 2
    bottom_bound = -(window.window_height() / 2)
    
    still_inside = True
    
    if some_turtle.xcor() < left_bound or some_turtle.xcor() > right_bound:
        still_inside = False
    if some_turtle.ycor() < bottom_bound or some_turtle.ycor() > top_bound:
        still_inside = False
    
    return still_inside

window = turtle.Screen()
tyrese = turtle.Turtle()

while is_still_in_window(window, tyrese):
    coin_flip = random.randrange(0, 2)
    if coin_flip == 0:
        tyrese.left(90)
    else:
        tyrese.right(90)
    tyrese.forward(50)

print("I'm outside the window. The program is done.")