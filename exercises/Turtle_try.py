"""TODO: Describe your scene program."""

__author__ = "730325952"

from turtle import Turtle, colormode, done 


def main() -> None:
    """The entrypoint of my scene."""
    a_turtle: Turtle = Turtle()
    draw_square(a_turtle, -5, 5, 10)
    done()


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1