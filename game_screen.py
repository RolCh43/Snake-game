from turtle import Screen, Turtle
from snake import Snake
from typing import Final
# This code defines a Screen class for a snake game using the turtle graphics library.

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.game_screensetup()
        

    def game_screensetup(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)  
         
        