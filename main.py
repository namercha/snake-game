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

# Start listening for key strokes from keyboard.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Refreshing the screen
    screen.update()
    time.sleep(0.1)

    snake.move()














screen.exitonclick()
