from turtle import *
from players import Player
from screen_play import Play
from ball import Ball

#TODO: optimize screen to center and start with maximize window
screen = Screen()
screen.screensize()
screen.setup(width=1.0, height=1.0, startx=-0, starty=0)
screen.bgcolor('black')
screen.title('Pong')
line = Play()
player_left = Player('left')
player_right = Player("right")

pl = player_left.pos()
pr = player_right.pos()
ball = Ball()


def start():
    if player_left.distance(ball) <= 40:
        ball.bouncing()
    elif player_right.distance(ball) <= 40:
        ball.bouncing()




screen.listen()
screen.onkey(start, 'space')
screen.onkey(player_left.up, 'w')
screen.onkey(player_left.down, 's')
screen.onkey(player_right.up, 'Up')
screen.onkey(player_right.down, 'Down')

#TODO: get ball to bounce back once it reaches the paddle.
if player_left.distance(ball) <= 200:
    ball.bouncing()
elif player_right.distance(ball) <= 200:
    ball.bouncing()

screen.exitonclick()
