from turtle import Screen, Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.body = []
        self.build_snake()
        self.head = self.body[0]
        
    def add_body(self, x, y):
        self.new_body = Turtle("square")
        self.new_body.penup()
        self.new_body.color("white")
        self.new_body.goto(x, y)
        self.body.append(self.new_body)

    def grow(self):
        self.add_body(self.body[-1].xcor(), self.body[-1].ycor())
        

    def build_snake(self):  
        self.add_body(0, 0)
        self.add_body(-20, 0)
        self.add_body(-40, 0)


    def move(self):        
        for bod_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[bod_num - 1].xcor()
            new_y = self.body[bod_num - 1].ycor()
            self.body[bod_num].goto(new_x, new_y)
            

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:   
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
