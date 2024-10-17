from config import *
from turtle import Screen, Turtle

'''
The design class sets the User Interface for the game
'''
class Design(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    '''
    This method displays the instructions for single player gamemode.
    Tells the player to Press 1 key if they want to play single player gamemode.
    '''
    def singleplayer_button(self):
        self.goto(-150,-150)
        self.write('     To play \nSingle Player \n      Press 1', align = "Center", font = FONT)
    
    '''
    This method displays the instructions for multiplayer gamemode.
    Tells the player to Press 2 key if they want to play multiplayer gamemode.
    '''
    def multiplayer_button(self):
        self.goto(150,-150)
        self.write('    To play \nMulti Player \n    Press 2', align = "Center", font = FONT)
    
    '''
    This method displays the instructions to exit the game.
    Tells the player to Press esc key if they want to exit the game.
    '''
    def exit_button(self):
        self.color('red')
        self.goto(-280,250)
        self.write('    EXIT \n(Click esc)', align = "left", font = FONT)

    '''
    This method displays the instructions to go back to homescreen.
    Tells the player to Press e key if they want to go back to homescreen.
    '''
    def home_button(self):
        self.goto(280,250)
        self.write(' HOME \n(Click e)', align = "right", font = FONT)


    