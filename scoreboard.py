from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        # self.color("black")
        self.hideturtle()
        self.penup()
        self.setposition(-280, 260)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
