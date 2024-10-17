from turtle import Turtle
from config import * 
ALIGNMENT = "center"


class Scoreboard(Turtle):
    '''
    Scoreboard class created for displaying scores on singleplayer and multiplayer
    Each snake will have its own scoreboard
    '''
    def __init__(self, snake, position, id):
        super().__init__()
        self.snake = snake
        self.position = position
        self.id = id

    '''
    setup_scoreboard responsible for displaying scoreboards at the start of the game
    Player 1 scoreboard set as white and at the top, while player 2 scoreboard set as orane at the bottom
    '''

    #Position of scoreboard based on snake1 or snake2
    def setup_scoreboard(self):
        self.hideturtle()
        if self.id == "1":
            self.color("white")
        else:
            self.color("orange")
        self.penup()
        self.goto(self.position[0],self.position[1])

    '''
    Scoreboard is updated based on the assigned score variable of the snake accordingly
    '''

    #scoreboard updated based on score variable
    def update_scoreboard(self):
        score = self.snake.score
        self.write(f"Player {self.id}'s Score: {score}", align=ALIGNMENT, font=FONT_Score)

    '''
    Game over function displays 'GAME OVER' text once game ends
    depending on the scenario, additional text is displayed when:
    1. Snakes collided head on, displaying text: "Snakes Collided"
    2. Game is in singleplayer, hence no additional text is displayed
    3. A winner is declared as a parameter of the functiono, in which a winner is declared as additional text
    '''

    #Game over and winner's name is displayed
    def game_over(self, winner):
        self.goto(0, 0)
        self.write("       GAME OVER \n(Click space to restart)", align=ALIGNMENT, font=FONT_Score)
        self.goto(0, -100)
        if winner == "0":
            self.write("Snakes Collided", align=ALIGNMENT, font=FONT_Score)
        elif winner == "single":
            pass
        else:
            self.write("Player {} wins".format(winner), align=ALIGNMENT, font=FONT_Score)

    '''
    increase_score function increases the score variable of the snake by one, clears the scoreboard of the respective snake
    and calls the update_scoreboard function, which will display the new score of the snake
    '''
    #score is cleared. Note that score is increased under collectible_collision in multiPlayer.py
    def increase_score(self):
        self.snake.score += 1
        self.clear()
        self.update_scoreboard()
        
    '''
    decrease_score function decreases the score variable of the snake by one, clears the scoreboard of the respective snake
    and calls the update_scoreboard function, which will display the new score of the snake
    '''
    def decrease_score(self):
            self.snake.score -= 1
            self.clear()
            self.update_scoreboard()
