from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 260)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.write(arg=f"Level : {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
