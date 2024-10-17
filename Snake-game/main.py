from turtle import Screen, Turtle
import time
from config import *
from GameOptions.singlePlayer import SinglePlayer
from GameOptions.multiPlayer import MultiPlayer
from design import Design 
'''
The functions singlePlayer() and multiPlayer() starts the game.
It first Instantiate SinglePlayer/multiPlayer class, and run the required setup methods.
When the game is True (ongoing), check for updates.
Speed of snake increases after every 10 seconds, but will hit a limit
When game update return false, end game.
When game_ongoing == False, spacebar on key is available to reset game
'''
def singlePlayer():
    game = SinglePlayer()
    exit = Design()
    home = Design()

    # setup game screen/ keyboard
    screen = Screen()
    game.setup_screen(screen)

    # create exit button
    exit.exit_button()

    # create home button
    home.home_button()

    #Initial game set up (creates food and snake)
    game.setup_game()

    # Click e to go back to homescreen
    screen.onkey(lambda: exit_to_home(), "e")

    start_time = time.time()
    game_ongoing = True
    
    while game_ongoing:
        screen.update() 
        elapsed_time = time.time() - start_time
        sleep_time = 0.05 - (elapsed_time//10)*0.005  # for every 10 seconds, decrease this value   
        if sleep_time < 0.01:
            sleep_time = 0.01
        time.sleep(sleep_time)
        
        if not game.update(): #Update snake movement, food and boundry collision
            game_ongoing = False # break loop when game.update == false 
        
    if game_ongoing == False:
        print("Game has ended")
        screen.onkey(lambda: restart(screen, "single"), "space")
    
        
    # screen.exitonclick()
    screen.mainloop()

def multiPlayer():
    game = MultiPlayer()
    exit = Design()
    home = Design()
    
    # setup game screen/ keyboard
    screen = Screen()
    game.setup_screen(screen)

    # create exit button
    exit.exit_button()

    # create home button
    home.home_button()


    #Initial game set up (creates food and snake)
    game.setup_game()

    # Click e to go back to homescreen
    screen.onkey(lambda: exit_to_home(), "e")
    
    start_time = time.time()
    game_ongoing = True
    while game_ongoing:
        screen.update()     

        elapsed_time = time.time() - start_time
        sleep_time = 0.05 - (elapsed_time//10)*0.005  # for every 10 seconds, decrease this value   
        if sleep_time < 0.01:
            sleep_time = 0.01
        time.sleep(sleep_time)

        
        if game.update() ==  False: #Update snake movement, food and boundry collision
            game_ongoing = False # break loop when game.update == false
        
    if game_ongoing == False:
        print("Game has ended")
        screen.onkey(lambda: restart(screen, "multi"), "space")
    
    # screen.exitonclick()
    screen.mainloop()

'''
Restart Game
Turtle Clear screen and re-run the singlePlayer or multiPlayer according to parameter gameType
'''
def restart(screen, gameType):
    screen.clear()
    if gameType == "single":
        singlePlayer()
    elif gameType == "multi":
        multiPlayer()
    else:
        print("Error: Unable to restart game")
    
'''
Clear homescreen and run singlePlayer
Turtle Clear homescreen and direct to singlePlayer screen
'''
def single_play_mode():
    screen = Screen()
    screen.clear()
    singlePlayer()

'''
Clear homescreen and run multiPlayer
Turtle Clear homescreen and direct to multiPlayer screen
'''
def multi_play_mode():
    screen = Screen()
    screen.clear()
    multiPlayer()

'''
Clear screen and run homescreen
Turtle Clear current game mode screen and redirect to homescreen 
'''
def exit_to_home():
    screen = Screen()
    screen.clear()
    homescreen()

'''
Homescreen 
Create a screen to decide which gamemode the player wants (singleplayer or multiplayer) or to exit the game depending on the button pressed.
Press 1 key single_play_mode function will run.
Press 2 key for multi_play_mode function will run.
Press esc key to close the game.
Screen contains instructions from the Design class, that guides the player to click the right keys, as well as a Game Title.
'''
def homescreen():
    # setup homescreen
    screen = Screen()
    screen.clear()
    screen.setup(width=screen_size, height=screen_size)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)
    screen.listen()

    # run singlePlayer mode
    screen.onkey(lambda: single_play_mode(), "1")

    # run multiPlayer mode
    screen.onkey(lambda: multi_play_mode(), "2")

    # exit game
    screen.onkey(lambda: screen.bye(), "Escape")

    # create homescreen Title
    Title = Turtle()
    Title.color("white")
    Title.write(' SNAKE \n  GAME ', align = "center", font = FONT_Title )

    # create singleplayer button
    Single = Design()
    Single.singleplayer_button()

    # create multiplayer button
    Multi = Design()
    Multi.multiplayer_button()

    # create Exit button
    exit = Design()
    exit.exit_button()

    # screen.exitonclick()
    screen.mainloop()

'''
Play the game
'''
homescreen()
