from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_backwards():
    tim.backward(10)


def move_forwards():
    tim.forward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()


def keys(backwards, forwards, counter_clockwise, clockwise, clear):
    screen.onkey(key="s", fun=backwards)
    screen.onkey(key="w", fun=forwards)
    screen.onkey(key="a", fun=counter_clockwise)
    screen.onkey(key="d", fun=clockwise)
    screen.onkey(key="c", fun=clear)


keys(move_backwards, move_forwards, move_counter_clockwise, move_clockwise, clear_screen)
screen.exitonclick()
