from turtle import Turtle

MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

'''
Snake class: used to create snake object in both single and multi player game
Snake has 2 attributes:
1. start_pos: starting position of snake
2. segment list: to store the snake body blocks
'''
class Snake:

    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.segments = []
        self.score = 0

    '''
    This method creates your initial snake.
    Since start_pos is a list containing 3 coordinates, for each coordinate,
    call add_segment() and pass in each coordinate
    '''
    def create_snake(self, color):
        for position in self.start_pos:
            self.add_segment(position, color)


    '''
    This method takes in the parameter position.
    It creates a square using turtle and set it the position.
    The square added to the the list self.segments
    '''
    def add_segment(self, position, color):
        new_segment = Turtle("square")
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    '''
    This method adds a segment to the end of the snake of the same colour
    '''
    def extend(self, color):
        self.add_segment(self.segments[-1].position(), color)

    '''
    This method tells the snake to move forward.
    Runs a for loop to generate each segment of the snake.
    Creates new x,y coordinates of the current segment that is equal to the old x,y coordinates of the segment infront of current segment. 
    Tells the current segment to go to new x,y coordinates. 
    '''
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    '''
    This method checks that if the head of the snake is not facing DOWN, set the head to face UP
    '''
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    '''
    This method checks that if the head of the snake is not facing UP, set the head to face DOWN
    '''
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    '''
    This method checks that if the head of the snake is not facing RIGHT, set the head to face LEFT
    '''
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    '''
    This method checks that if the head of the snake is not facing LEFT, set the head to face RIGHT
    '''
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def delete_segments(self):
        self.segments[-1].hideturtle()
        self.segments = self.segments[0:-1]