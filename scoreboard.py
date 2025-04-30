from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.update_text()

    def update_text(self):
        self.write(f"Score: {self.current_score}", align="center", font=("Arial", 16, "normal"))

    def add_to_score(self):
        self.current_score += 1
        self.clear()
        self.update_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 28, "normal"))
