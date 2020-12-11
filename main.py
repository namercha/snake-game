from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nabil's Snake Game")
# Turn off turtle animation to update the drawings. Screen will be refreshed later.
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# Creating the snake body
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Refreshing the screen
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Getting the snake to move forward. Starting at tail, moving it forward one, all the way to the head.
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    # Moving the head forward after all of the body has moved forward.
    segments[0].forward(20)













screen.exitonclick()
