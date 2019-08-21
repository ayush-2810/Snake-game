#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries to be used.
import turtle
import time
import random

delay = 0.1   # Delay variable which will be used for the delay of the screen.

score = 0   # Storing current score of your game.
high_score = 0   # Storing high score of your game.

win = turtle.Screen()   # Creating window for the game.
win.title("Snake Game")   # Creating the title of the game.
win.bgcolor("green")   # Setting background color of the game.
win.setup(width=600, height=600)   # Size of the window.
win.tracer(0)   # To avoid any updates in the game. 

snake = turtle.Turtle()   # Object snake.
snake.speed(0)   # To avoid in change in speed.    
snake.shape("square")   # Shape of the snake.
snake.color("yellow")   # Color of the snake.
snake.penup()   # To avoid any animations.
snake.goto(0,0)    # Initial position in the window.
snake.direction = "stop"

# Same thing as for food.
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []   # Creating list for the body of snake.

# Things for the scoreboard.
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()   # Hiding the turtle.
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Comic Sans MS", 24, "normal"))

# Functions for movement.
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

# Move function.
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# For taking input from keyboard.
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

while True:
    win.update()

    # Condition for player to lose.
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(0.8)   # For stopping window for sometime.
        snake.goto(0,0)
        snake.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()   # For changing the socres.(avoiding overlapping of scores)
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans MS", 24, "normal")) 

    # Condition for eating the food.
    if snake.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # New body of the snake after eating food.
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        # Changing the high score.
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans MS", 24, "normal")) 

    # Adding segments for the body of the snake.
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()    
    
    # If snake touches its own body.
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
        
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()

            score = 0

            delay = 0.1
        
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans MS", 24, "normal"))

    time.sleep(delay)   

wn.mainloop()

