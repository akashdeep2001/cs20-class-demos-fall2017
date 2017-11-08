import turtle

def draw_triangle(some_turtle, side_length):
    '''Draws a triangle with some_turtle, with each side being side_length long.'''
    for side in range(3):
        some_turtle.forward(side_length)
        some_turtle.left(120)

def draw_hexagon_with_triangles(a_turtle, length):
    '''Draws a hexagon, by drawing 6 triangles.'''
    for triangle in range(6):
        draw_triangle(a_turtle, length)
        a_turtle.left(60)


screen = turtle.Screen()
screen.bgcolor("lightgreen")

camila = turtle.Turtle()
camila.color("pink")
camila.pensize(4)


shape = turtle.textinput("Shape", "Do you want a 'triangle' or a 'hexagon'?")
if shape == "triangle":
    draw_triangle(camila, 150)
elif shape == "hexagon":
    draw_hexagon_with_triangles(camila, 150)