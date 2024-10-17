from turtle import Turtle
from Collectables.collectables import Collectables
import random
from config import *

'''
The Food class is the child class of Collectables
'''
class Food(Collectables):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
