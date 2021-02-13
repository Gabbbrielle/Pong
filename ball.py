from turtle import Turtle
from players import X
import random
import pyautogui
PADDLE = X - 20 #distance where the ball touches the paddle. X being the x coordonate of the paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.setheading(0)
        self.ht()
        flip_a_coin = random.choice([1, 2])
        if flip_a_coin == 1:
            pyautogui.alert('left starts')
            self.setposition(-PADDLE, 0)
        if flip_a_coin == 2:
            pyautogui.alert('right starts')
            self.setposition(PADDLE, 0)
        self.st()






