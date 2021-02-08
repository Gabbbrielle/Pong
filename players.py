from turtle import Turtle
MOVE_DISTANCE = 100
DOWN = 270
UP = 90
class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        if position == "left":
            self.goto(-650, 0)
        else:
            self.goto(650, 0)
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.setheading(90)
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.penup()


    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)


    # TODO: each player must be independent. Does that mean that they must be in a list?



