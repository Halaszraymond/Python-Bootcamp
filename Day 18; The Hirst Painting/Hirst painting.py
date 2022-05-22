import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 35)
#
# color_list = []
#
# for color in colors:
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     color = (r, g, b)
#     color_list.append(color)
# print(color_list)

color_list = [(11, 16, 38), (196, 161, 113), (168, 62, 36), (140, 163, 194), (37, 9, 6), (232, 205, 95), (37, 9, 18),
              (181, 155, 29), (14, 43, 26), (71, 97, 132), (168, 49, 68), (188, 139, 152), (158, 25, 14), (207, 70, 85),
              (158, 172, 159), (68, 116, 91), (148, 19, 41), (42, 49, 103), (203, 89, 72), (219, 176, 182),
              (77, 83, 20), (37, 85, 41), (221, 178, 172), (85, 111, 178), (175, 189, 214), (234, 207, 7), (41, 74, 78),
              (107, 140, 123), (184, 196, 188), (112, 137, 139), (177, 196, 202)]

tim = Turtle()
tim.penup()
tim.speed("fastest")
tim.setposition(-250, -250)
turtle.colormode(255)
tim.hideturtle()

rows = 10
dots_per_row = 8

for row in range(rows):
    y_position = tim.ycor()
    new_x = -250
    new_y = (y_position + 50)
    tim.setposition(new_x, new_y)
    for dot in range(dots_per_row):
        random_color = color_list[random.randint(0, 29)]
        tim.dot(20, random_color)
        tim.forward(50)

screen = Screen()
screen.exitonclick()
