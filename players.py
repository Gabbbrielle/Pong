from turtle import Turtle
X = 800
MOVE_DISTANCE = 100
DOWN = 270
UP = 90
class Player(Turtle):
    def __init__(self, position):
        super().__init__()

        if position == "left":
            self.goto(-X, 0)
        else:
            self.goto(X, 0)
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.setheading(90)
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.penup()


#todo - set boundaries for the up and down
#todo - make players appear faster
    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)





