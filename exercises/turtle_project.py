"""Drawing a beautiful forest with a turtle, went above and beyond by using a circle function."""
 
__author__ = "730576169"
 
from turtle import Turtle, done 
 
 
def main() -> None:
    """The entrypoint of my scene."""
    leo: Turtle = Turtle()
    draw_trunk(leo, 200, 300, 100, 500)
    draw_trunk(leo, -200, 300, 100, 500)
    draw_tree_top(leo, 250, 300, 100)
    draw_tree_top(leo, -150, 300, 100)
    draw_apple_triangle(leo, -160, 320, 50)
    draw_recursive_target(leo, 100, 0, 100)
    done()
 

def draw_trunk(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws the trunk of a tree and fills it in."""
    i: int = 0
    a_turtle.color("brown")
    a_turtle.penup()
    a_turtle.begin_fill()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(height)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_tree_top(b_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a circle to represent a tree top."""
    b_turtle.color("green")
    b_turtle.begin_fill()
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.pendown()
    b_turtle.circle(radius)
    b_turtle.end_fill()


def draw_apple_triangle(c_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Draws a triange to represent an apple."""
    c_turtle.color("red")
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.pendown()
    c_turtle.begin_fill()
    c_turtle.forward(side_length)
    c_turtle.left(120)
    c_turtle.forward(side_length)
    c_turtle.pendown()
    c_turtle.end_fill()


def draw_recursive_target(d_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Use recursion to make a target."""
    if radius <= 0:
        return
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.pendown()
    d_turtle.circle(radius)
    draw_recursive_target(d_turtle, x - 40, y - 29, radius - 50)


if __name__ == "__main__":
    main()