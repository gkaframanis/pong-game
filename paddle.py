from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super(Paddle, self).__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def go_up(self):
        if self.ycor() <= 220:
            self.y_pos = self.ycor() + 40
            self.goto(self.xcor(), self.y_pos)

    def go_down(self):
        if self.ycor() >= -220:
            self.y_pos = self.ycor() - 40
            self.goto(self.xcor(), self.y_pos)
