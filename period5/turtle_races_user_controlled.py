import turtle
import random
import microbit

def move_to_starting_locations(player1, player2, starting_x_cord):
    # move the turtles to their starting locations
    player1.up()
    player2.up()
    player1.goto(starting_x_cord,40)
    player2.goto(starting_x_cord,-40)

def draw_finish_line(finish_line_x_cord):
    #draw a finish line
    ref = turtle.Turtle()
    ref.up()
    ref.goto(finish_line_x_cord, -100)
    ref.down()
    ref.pensize(4)
    ref.goto(finish_line_x_cord, 100)
    ref.hideturtle()


window = turtle.Screen()
window.bgcolor('lightblue')

#create the turtles, and specify their attributes
lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')


draw_finish_line(200)
move_to_starting_locations(andy, lance, -200)


while andy.xcor() < 200 and lance.xcor() < 200:
    if microbit.button_a.was_pressed():
        andy_speed = random.randrange(1, 10)
        andy.forward(andy_speed)
    
    if microbit.button_b.was_pressed():
        lance_speed = random.randrange(1, 10)
        lance.forward(lance_speed)
    
if andy.xcor() > lance.xcor():
    andy.write("I win!", font=("Arial", 32, "normal"))
elif lance.xcor() > andy.xcor():
    lance.write("I win!", font=("Arial", 32, "normal"))
else:
    andy.write("Tie.", font=("Arial", 32, "normal"))
    lance.write("Tie.", font=("Arial", 32, "normal"))