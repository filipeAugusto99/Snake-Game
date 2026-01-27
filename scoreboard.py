import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()