from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nabil's Snake Game")
# Turn off turtle animation to update the drawings. Screen will be refreshed later.
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    # Refreshing the screen
    screen.update()
    time.sleep(0.1)

    snake.move()














screen.exitonclick()
