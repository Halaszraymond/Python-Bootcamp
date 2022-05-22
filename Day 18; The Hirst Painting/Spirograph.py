import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
tim.speed("fastest")
turtle.colormode(255)


def turtle_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    tim.color(r, b, g)
    return tim.color(r, b, g)


def draw_circle(gap_size):
    turtle_color()
    tim.circle(100)
    angle = 360 / gap_size
    tim.right(angle)

    return


spirograph = 100

for circle in range(spirograph):
    draw_circle(spirograph)

screen = Screen()
screen.exitonclick()
