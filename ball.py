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
#TODO: modify the bouncing so it goes toward a direction but is stopped if it touches the paddle. (while loop?)
    def bouncing(self):
        """Depending on which side the ball is, it will bounce to the floor
        and head to a random point on the other side """
        x = random.randint(-250, 250)  # where the ball will bounce on the X axis
        left_x = -850
        right_x = 850
        rand_y = random.randint(-350, 350)  # random height where the ball goes
        floor = -350  # bouncing floor

        if self.xcor() > 300:
            self.goto(x, floor)
            self.goto(left_x, rand_y)
        elif self.xcor() < -300:
            self.goto(x, floor)
            self.goto(right_x, rand_y)






