from turtle import Turtle
import random

FONT = "Arial"
SIZE = 24

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-60, 260) 
        self.color("white")
        self.score = 0
        arg = "Score: " + str(self.score)
        self.write(arg, False, "left", (FONT, SIZE, "normal"))
    
    def add_point(self):
        self.score += 1
        arg = "Score: " + str(self.score)
        self.clear()
        self.write(arg, False, "left", (FONT, SIZE, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", False, "center", (FONT, SIZE, "normal"))

        

        
    
