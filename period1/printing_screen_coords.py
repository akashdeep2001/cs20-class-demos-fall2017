import turtle

def print_coordinates(x, y):
    print(x, y)

window = turtle.Screen()

dawson = turtle.Turtle()

window.onclick(print_coordinates)
window.listen()

