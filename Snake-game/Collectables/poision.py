from turtle import Turtle
from Collectables.collectables import Collectables
import random
import time
from config import *


'''
The Poision class is the child class of Collectables

'''
class Poision(Collectables):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)

    '''
    The check_timer checks if the poison object has been on screen for more than 10 seconds
    This method utilizes the time_created attribute, which is assigned when we call spawn_collectables (Collectable Class)
    The method initially declares check as False
    As the method is called repeatedly in the update function singlePlayer and MultiPlayer class) in main.py, the current_time is always updated
    Therefore, we are able to compare the current_time and time_created.
    If the time_diff is >10 seconds, we assign check == True.
    The method returns check(Boolean), which will be used in the update function in both the singlePlayer and MultiPlayer class
    '''
    def check_timer(self):
        check = False
        current_time = time.time()
        time_diff = current_time - self.time_created
        # print("TIME DIFF:", time_diff)
        if time_diff > 10:
            check = True
        return check

        

     
   



        