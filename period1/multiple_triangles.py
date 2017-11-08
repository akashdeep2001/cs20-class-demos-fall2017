import turtle

def draw_triangle(some_turtle, length):
    """Draws a triangle with some_turtle, with each side being length long."""
    for side in range(3):
        some_turtle.forward(length)
        some_turtle.left(120)
        
def draw_hexagon_with_triangles(a_turtle, side_length):
    '''Draw a hexagon out of triangles with a_turtle, and sides being side_length long.'''
    for triangle in range(6):
        draw_triangle(a_turtle, side_length)
        a_turtle.left(60)


screen = turtle.Screen()
screen.bgcolor("gray")

fiza = turtle.Turtle()
fiza.color("yellow")
fiza.pensize(4)

draw_hexagon_with_triangles(fiza, 150)
