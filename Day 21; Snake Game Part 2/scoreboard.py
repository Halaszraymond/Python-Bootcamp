from turtle import Turtle
TEXT = "score"
MOVE = False
ALIGNMENT = "center"
FONTNAME = "Arial"
FONTSIZE = 24
FONTTYPE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.write(arg=f"{TEXT}: {self.score}", move=MOVE, align=ALIGNMENT, font=(FONTNAME, FONTSIZE, FONTTYPE))
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"{TEXT}: {self.score}", move=MOVE, align=ALIGNMENT, font=(FONTNAME, FONTSIZE, FONTTYPE))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", move=MOVE, align=ALIGNMENT, font=(FONTNAME, 50, FONTTYPE))

