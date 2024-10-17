from turtle import Turtle
from config import *
import random
import time

'''
Collectables are the items a snake can pick up.
This is the parent class. Therefore, child classes, food, poision and wildcard will inherit the traits of this class
'''
class Collectables(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.time_created = 0 


    '''
    The method spawn_food creates a random x and y location within the stated bounds and creates a food at the location
    '''
    def spawn_collectables(self):
        random_x = random.randint(-half_screen_size+20, half_screen_size-20)
        random_y = random.randint(-half_screen_size+20, half_screen_size-20)
        self.goto(random_x, random_y)
        self.time_created = time.time()
    


