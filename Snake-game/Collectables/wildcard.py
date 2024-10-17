from turtle import Turtle
from Collectables.collectables import Collectables
import random
import time
from config import *
from snake import *

'''
The Wildcard class is the child class of collectables
'''

class Wildcard(Collectables):
    
    def __init__(self):
        super().__init__()
        self.color("purple")
    
    '''
    The check_timer checks if the wildcard object has been on screen for more than 15 seconds
    This method utilizes the time_created attribute, which is assigned when we call spawn_collectables (Collectable Class)
    The method initially declares check as False
    As the method is called repeatedly in the update function MultiPlayer class in main.py, the current_time is always updated
    Therefore, we are able to compare the current_time and time_created.
    If the time_diff is > 15 seconds, we assign check == True.
    The method returns check(Boolean), which will be used in the update function in MultiPlayer class
    '''

    def check_timer(self):
        check = False
        current_time = time.time()
        time_diff = current_time - self.time_created
        print("TIME DIFF:", time_diff)
        if time_diff > 10:
            check = True
        return check
