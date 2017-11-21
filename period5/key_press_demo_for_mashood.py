import turtle

def move_forward():
    bob.forward(10)
    
def turn_left():
    bob.left(45)


window = turtle.Screen()

bob = turtle.Turtle()


window.onkey(move_forward, "f")
window.onkey(turn_left, "l")

window.listen()