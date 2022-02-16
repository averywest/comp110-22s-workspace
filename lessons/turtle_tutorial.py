"""Turtle practice."""

from turtle import Turtle, colormode, done
colormode(255)
side_length: float = 300.00
leo: Turtle = Turtle()

leo.penup()
leo.goto(-110, -30)
leo.pendown()
leo.color(170, 53, 246)
leo.speed(50)

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.penup()
bob.goto(-110, -30)
bob.pendown()
bob.color(35, 5, 55)
bob.speed(100)

i: int = 0
while (i < 60):
    bob.forward(side_length)
    bob.left(121)
    i = i + 1
    side_length = side_length * 0.97

done()
