"""A triangle cabin on a starry night.""" 

__author__ = "730325952"

from turtle import Turtle, colormode, done
colormode(255)

"""Broke up complex function: Line 83 with fn 47-64.""" 
"""Something fun: Line 15-17 in main fn."""


def main() -> None:
    """The entry point of my scene."""
    a_turtle: Turtle = Turtle()
    i: int = 0
    x: float = -2.5
    a_turtle.pensize(10)
    triangle_house(a_turtle, -150.0, -200.0, 300.0)
    a_turtle.pensize(1)
    while i < 2:
        windows(a_turtle, (i * -1) * 50, -100.0, 40.0)
        i += 1
    door(a_turtle, -20.0, -200.0, 40.0, 60.0) 
    while x < 2:
        star(a_turtle, x * 100.0, 200.0, 30.0)
        x += 1
    done()


def triangle_house(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """The base shape of my triangle cabin located at point x,y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.fillcolor(226, 91, 57)
    a_turtle.pencolor(130, 54, 12)

    a_turtle.begin_fill()
    i: int = 0
    while i < 3:
        a_turtle.forward(width)
        a_turtle.left(120)
        i += 1
    a_turtle.end_fill()


def window_pane(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Window panes that will built into the windows using a function call."""
    a_turtle.penup()
    a_turtle.goto(x + (width / 2), y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.pencolor(0, 0, 0)
    a_turtle.left(90)
    a_turtle.forward(width)

    a_turtle.penup()
    a_turtle.goto(x, y + (width / 2))
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.pencolor(0, 0, 0)
    a_turtle.forward(width)


def windows(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Both square windows on the triangle cabin located at point x,y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.fillcolor(218, 240, 246)
    a_turtle.pencolor(58, 130, 12)

    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()
    window_pane(a_turtle, x, y, width)

    
def door(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Rectangular door on the cabin located at point x,y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(50)
    a_turtle.fillcolor(58, 130, 12)
    a_turtle.pencolor(58, 130, 12)
    
    a_turtle.begin_fill()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(length)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()


def star(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Fancy, five stars in the sky located at point x,y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(100)
    a_turtle.fillcolor(238, 144, 241)
    a_turtle.pencolor(26, 32, 131)
    
    a_turtle.begin_fill()
    i: int = 0 
    while i < 50:
        a_turtle.left(60)
        a_turtle.forward(width)
        a_turtle.right(120)
        a_turtle.forward(width)
        i += 1
        width = width * 0.97
    a_turtle.end_fill()


if __name__ == "__main__":
    main()
