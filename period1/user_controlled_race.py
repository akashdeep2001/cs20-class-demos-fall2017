import turtle
import random
import microbit

def move_to_starting_locations(player1, player2, starting_x_cord):
    # move the turtles to their starting locations
    player1.up()
    player2.up()
    player1.goto(starting_x_cord,30)
    player2.goto(starting_x_cord,-30)

def draw_finish_line(finish_line_x_cord):
    #draw finish line
    ref = turtle.Turtle()
    ref.up()
    ref.pensize(5)
    ref.goto(finish_line_x_cord, -100)
    ref.down()
    ref.goto(finish_line_x_cord, 100)
    ref.hideturtle()

def move_racer(which_turtle, how_far):
    which_turtle.forward(how_far)

FINISH_LINE = 300

window = turtle.Screen()
window.bgcolor('lightblue')

#create the turtles, and specify their attributes
lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

draw_finish_line(FINISH_LINE)
move_to_starting_locations(lance, andy, -200)


while andy.xcor() < FINISH_LINE and lance.xcor() < FINISH_LINE:
    if microbit.button_a.is_pressed():
        andy_step = random.randrange(1, 10)
        move_racer(andy, andy_step)
        
    if microbit.button_b.is_pressed():
        lance_step = random.randrange(1, 10)
        move_racer(lance, lance_step)