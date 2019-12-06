# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:32:14 2019

@author: samat
"""

import turtle


players = []
players.append(input("Please enter your name, player 1: "))
players.append(input("Please enter your name, player 2: "))

print("Okay ", players[0], " and ", players[1], ". Let's play!")

ready = input("Enter START: ")

window = turtle.Screen()
window.title("Pong")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Score of players 1 and 2
score_1 = 0
score_2 = 0

# bats wil use class Turtle from turtle module
# Bat1
bat1 = turtle.Turtle()
bat1.speed(0)
bat1.shape("square")
bat1.color("black")
bat1.shapesize(stretch_wid=5, stretch_len=1)
bat1.penup()
bat1.goto(-350, 0)

# Bat2
bat2 = turtle.Turtle()
bat2.speed(0)
bat2.shape("square")
bat2.color("black")
bat2.shapesize(stretch_wid=5, stretch_len=1)
bat2.penup()
bat2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))


# Functions for movement
# shows y and x coordinates of bat 1 and 2
class move:
    def bat1_up():
        y = bat1.ycor()
        y += 20
        bat1.sety(y)

    def bat1_down():
        y = bat1.ycor()
        y -= 20
        bat1.sety(y)

    def bat2_up():
        y = bat2.ycor()
        y += 20
        bat2.sety(y)

    def bat2_down():
        y = bat2.ycor()
        y -= 20
        bat2.sety(y)


# Keyboard bindings
window.listen()

#I use classic wasd layout for player 1
window.onkeypress(move.bat1_up, "w")
window.onkeypress(move.bat1_down, "s")

#I use classic arrow layout for player 2
window.onkeypress(move.bat2_up, "Up")
window.onkeypress(move.bat2_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border bounce

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_1 += 1
        pen.clear() #needed to clear the original score
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_2 += 1
        pen.clear() #needed to clear the original score
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Bat and ball collisions
    if ball.xcor() < -340 and ball.ycor() < bat1.ycor() + 50 and ball.ycor() > bat1.ycor() - 50:
        ball.dx *= -1


    elif ball.xcor() > 340 and ball.ycor() < bat2.ycor() + 50 and ball.ycor() > bat2.ycor() - 50:
        ball.dx *= -1
