from turtle import *
from players import Player
from screen_play import Play

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')
screen.title('Pong')
line = Play()
player_left = Player('left')
player_right = Player("right")

screen.listen()
print(player_left.pos())
print(player_right.pos())
screen.onkey(player_left.up, 'w')
screen.onkey(player_left.down, 's')
screen.onkey(player_right.up, 'Up')
screen.onkey(player_right.down, 'Down')



screen.exitonclick()
