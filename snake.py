from turtle import Turtle


class Snake:
    def __init__(self):
       self.snake_segments = []
       self.create_snake()

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.penup()
            segment.goto(position)
            self.snake_segments.append(segment)

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0,-1):
            new_x = self.snake_segments[segment-1].xcor()
            new_y = self.snake_segments[segment-1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
            
        self.snake_segments[0].forward(20)

        
