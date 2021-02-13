from turtle import *
from players import Player
from screen_play import Play
from ball import Ball
import random
import time

screen = Screen()
screen.screensize()
screen.setup(width=1.0, height=1.0, startx=-0.5, starty=0)
screen.bgcolor('black')
screen.title('Pong')
line = Play()
player_left = Player('left')
player_right = Player("right")

pl = player_left.pos()
pr = player_right.pos()
ball = Ball()


# the heading should be changed to head "toward" a x, y coordinate
def move2left():
        ball.setheading(180)
        ball.goto(player_left.pos())
        ball.forward(40)


def move2right():
        ball.setheading(0)
        ball.goto(player_right.pos())
        ball.forward(40)

def bouncing():
    x = random.randint(-250, 250)
    left_x = player_left.xcor()-40
    right_x = player_right.xcor()+40
    rand_y = random.randint(-350, 350)
    bounce = -350

    if ball.xcor() > 200:
        ball.goto(x, bounce)
        ball.goto(left_x, rand_y)
        ball.forward(40)
    elif ball.xcor() < -200:
        ball.goto(x, bounce)
        ball.goto(right_x, rand_y)
        ball.forward(40)

def start():
    if player_left.distance(ball) <= 40:
        move2right()
    elif player_right.distance(ball) <= 40:
        move2left()


bouncing()







screen.listen()
screen.onkey(start, 'space')
screen.onkey(player_left.up, 'w')
screen.onkey(player_left.down, 's')
screen.onkey(player_right.up, 'Up')
screen.onkey(player_right.down, 'Down')




screen.exitonclick()
