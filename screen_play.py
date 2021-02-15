from turtle import Turtle


# TODO: set a or tuple with left, right and floor boundaries to use in all the game. (-850, 850, -350) and modify files

class Play(Turtle):
    # TODO: line should just appear and not be seen as constructing itself
    def __init__(self):
        super().__init__()
        line = Turtle()
        line.speed('fastest')
        line.goto(0, -400)
        line.ht()
        line.color('white')
        line.penup()

        line.setheading(90)
        line.speed('fastest')
        for dashes in range(20):
            line.speed('fastest')
            line.forward(20)
            line.penup()
            line.forward(20)
            line.pendown()
