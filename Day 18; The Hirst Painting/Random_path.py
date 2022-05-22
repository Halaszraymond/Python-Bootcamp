import turtle
from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.shape("arrow")
tim.speed(20)
tim.width(10)


def turtle_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    tim.color(r, b, g)
    return tim.color(r, b, g)


for walk in range(200):
    angle = random.randint(0, 3) * 90
    tim.right(angle)
    tim.forward(50)
    turtle_color()

screen = Screen()
screen.exitonclick()
