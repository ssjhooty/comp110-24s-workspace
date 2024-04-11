"""Turtle tutorial."""
__author__ = "730475919"

from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

leo.begin_fill()
leo.fillcolor(32, 67, 93)  # code for shape to be filled
leo.end_fill()

done()