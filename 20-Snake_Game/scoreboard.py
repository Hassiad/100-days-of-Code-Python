
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # move turtle before displaying
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        # display scoreboard
        self.color("white")
        self.write("Score: ", align="center", font=("Arial",24,"normal"))
    
    def increase_score(self):
        self.score += 1
        self.write("Score: ", align="center", font=("Arial",24,"normal"))    