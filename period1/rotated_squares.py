import turtle

def draw_square_from_centre(some_turtle, side_length):
    """Draws a square, beginning in the centre of the square, and ending once again in the centre."""
    #go to starting location
    some_turtle.up()
    for i in range(2):
        some_turtle.right(90)
        some_turtle.forward(side_length/2)
    some_turtle.right(180)
    some_turtle.down()
    
    #draw the square
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

    #go back to original location
    some_turtle.up()
    for i in range(2):
        some_turtle.forward(side_length/2)
        some_turtle.left(90)
    some_turtle.left(180)

window = turtle.Screen()
window.bgcolor("lightgreen")

fiza = turtle.Turtle()
fiza.color("red")
fiza.pensize(4)

draw_square_from_centre(fiza, 200)
fiza.left(45)
draw_square_from_centre(fiza, 200)