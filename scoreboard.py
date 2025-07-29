from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.update_level()


    def update_level(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", align="center", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_level()
