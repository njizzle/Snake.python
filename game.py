from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_on = True


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")  
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.add_point()
        
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_on = False
        score.game_over()
        
    # Detect collision with tail
    for bod in snake.body[1:]:
        if snake.head.distance(bod) < 10:
            game_on = False
            score.game_over()



screen.exitonclick()
