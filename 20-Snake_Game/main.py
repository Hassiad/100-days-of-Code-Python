# Day 20 and 21 Snake Game

from turtle import Turtle, Screen
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Timmy Snake Game")
screen.tracer(0)

# Initial 3 segments of snake named Timmy
timmy = Snake()

# Snake movement
screen.listen()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")
screen.onkey(timmy.left, "Left")
screen.onkey(timmy.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    timmy.move()

screen.exitonclick()