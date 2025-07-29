from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

car_manager = CarManager()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def hit_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            car_manager.increase_speed()


    def move_up(self):
        self.forward(MOVE_DISTANCE)

        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(x=self.xcor(), y=new_y)
