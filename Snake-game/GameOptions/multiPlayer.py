from snake import Snake
from Collectables.food import Food
from Collectables.poision import Poision
from Collectables.wildcard import Wildcard
from scoreboard import Scoreboard
from config import *

'''
The Multiplayer class is the brains behind the game.
Two snakes are given different starting positions
Food, Poison and Wildcard will spawn at random locations
Two scoreboards are created for two snakes. Player 1's score displayed at the top while player 2's score displayed at the bottom
'''
class MultiPlayer:
    def __init__(self):
        self.snake1 = Snake(STARTING_POSITION1)
        self.snake2 = Snake(STARTING_POSITION2)
        self.food = Food()
        self.poision = Poision()
        self.wildcard = Wildcard()
        self.scoreboard1 = Scoreboard(self.snake1, SCOREBOARD_POS1, "1")
        self.scoreboard2 = Scoreboard(self.snake2, SCOREBOARD_POS2, "2")
    
    '''
    This function creates the game window. 
    There is a parameter, screen. We pass in Screen from Turtle when we call this function.
    The game controls are also asigned to the different snakes.
    Snake1 uses the arrow keys, while Snake2 uses the alphabate keys
    '''
    def setup_screen(self, screen):
        screen.setup(width=screen_size, height=screen_size)
        screen.bgcolor("black")
        screen.title("Snake game")
        screen.tracer(0)
        
        # set keyboard listener
        screen.listen()
        screen.onkey(self.snake1.up, "Up")
        screen.onkey(self.snake1.down, "Down")
        screen.onkey(self.snake1.left, "Left")
        screen.onkey(self.snake1.right, "Right")
        
        screen.onkey(self.snake2.up, "w")
        screen.onkey(self.snake2.down, "s")
        screen.onkey(self.snake2.left, "a")
        screen.onkey(self.snake2.right, "d")
        
        screen.onkey(lambda: screen.bye(), "Escape")
    
    '''
    This function creates the snakes, collectables and scoreboards on the screen in the initial stage.
    '''
    def setup_game(self):
        self.snake1.create_snake("white")
        self.snake2.create_snake("orange")
        self.food.spawn_collectables()
        self.poision.spawn_collectables()
        self.wildcard.spawn_collectables()
        self.scoreboard1.setup_scoreboard()
        self.scoreboard2.setup_scoreboard()
    
    '''
    This function contains all the functions that should be constantly updated.
    1. Update snakes movement
    2. Check if the snakes collides into collectables -> returns Boolean and assign to colllectable_col_1 anf colllectable_col_1
    3. Check if the snakes are within boundries -> returns Boolean and assign to s1_boundry and s2_boundry
    4. updates scoreboards
    5. Check if snakes collide with each other -> returns Boolean and assign to snake_col
    5. Check poison timer -> If it returns True, poison on screen has appeared for more than 10 seconds, therefore call spawn_collectables to change location of poison
    The function initially declares game_is_on as True
    If colllectable_col_1/2 or s1/2_boundry or snake_col return false, game is over, therefore set game_is_on = False
    The function returns game_is_on to main.py to stop the game loop
    '''
    def update(self):   
        game_is_on = True

        #Update snake movement
        self.snake1.move()
        self.snake2.move()

        #Update scireboard
        self.scoreboard1.update_scoreboard()
        self.scoreboard2.update_scoreboard()

        #check if snake hit collectables
        colllectable_col_1 = self.collectable_collision(self.snake1, 'white')
        colllectable_col_2 = self.collectable_collision(self.snake2, 'orange')

        #check if snake hits boundries
        s1_boundry = self.verify_boundaries(self.snake1)
        s2_boundry = self.verify_boundaries(self.snake2)

        #check if snake hit each other
        snake_col = self.snake_to_snake_collision()

        # If check_timer == True (more than 10 seconds), spawn a new poison
        if self.poision.check_timer() == True:
            self.poision.spawn_collectables()

        # If check_timer == True (more than 10 seconds), spawn a new wildcard
        if self.wildcard.check_timer() == True:
            self.wildcard.spawn_collectables()
        
        if (s1_boundry and s2_boundry and snake_col and colllectable_col_1 and colllectable_col_2) == False: #If any of the checks return false, end game
            game_is_on = False
            
        return game_is_on
    
    '''
    This function verifies the boundries of the game (Screen boundry and Snake body)
    The method initially declares game_is_on as True
    x_cor = x coordinate of snake's head 
    y_cor = x coordinate of snake's head 
    
    1. Check screen boundry
    If snake head x_cor or y_cor exceed screen boundries, assign game_is_on = False and call game_over method
    
    2. check if snake hit body
    If the snake head to distance of body is <5, it means snake head has hit body. Therefore assign game_is_on = False and call game_over method
    We have placed a length of snake check around the 'if' condition above. 
    This is to prevent the game from crashing when the snake has 1 body block and has gained an additional block from eating food
    As the new block gained will be <5 distance away from the snake head
    
    The function returns game_is_on to main.py to stop the game loop when a boundry is hit
    '''
    def verify_boundaries(self, snake):
        game_is_on = True
        
        x_cor = snake.segments[0].xcor()
        y_cor = snake.segments[0].ycor()
        
        # If snake hit edge
        if x_cor > half_screen_size-20 or x_cor < -half_screen_size+10 or y_cor > half_screen_size-10 or y_cor < -half_screen_size+20:
            game_is_on = False
            if snake == self.snake1:
                winner = "2"
                self.scoreboard2.game_over(winner)
            else:
                self.scoreboard1.game_over("1")
        
        # snake head hit body
        # when head of snake to distance of body <5, game end
        # First condition check if snake is less than 3 block, code won't run as head too close to new block
        if len(snake.segments) >2 :  
            for segment in snake.segments[1:]:
                if snake.segments[0].distance(segment)<5:
                    print("snake collide itself")
                    game_is_on = False
                    if snake == self.snake1:
                        winner = "2"
                        self.scoreboard2.game_over(winner)
                    else:
                        self.scoreboard1.game_over("1")
        
        return game_is_on
    
    '''
    This function checks if snake hits each other.
    If snakes collide head on, game ends and no winner
    If snake 1 collide with body of snake 2, snake 2 wins and vice versa
    '''
    def snake_to_snake_collision(self):
        game_is_on = True
        # Check if both snake heads collided head-on
        if self.snake2.segments[0].distance(self.snake1.segments[0])<5:
            game_is_on = False
            self.scoreboard1.game_over("0")
            print("Snakes collided")

        # Check for collision when snake 1 hit snake 2
        for segment in self.snake2.segments[1:]:
            if self.snake1.segments[0].distance(segment)<5:
                game_is_on = False
                self.scoreboard1.game_over("2")
                print("Snakes collided")
                
        # Check for collision when snake 2 hit snake 1
        for segment in self.snake1.segments[1:]:
            if self.snake2.segments[0].distance(segment)<5:
                game_is_on = False
                self.scoreboard1.game_over("1")
                print("Snakes collided")
                
        return game_is_on
    
    '''
    This function checks for collision for collectables
    The method initially declares game_is_on as True
    
    1. If the snake head is <15 distance from food means the snake has eaten the food
    Therefore, spawn new food, extend snake body and increase snake score.
    
    2. If the food is spawned on the snake's body, spawn the food again
    
    3. if the snake head is <15 distance from poison means the snake has eaten the poison
    Verify snake length. 
    If snake length is already 1, it isn't able to lose another body. Therefore end game and assign game_is_on = False 
    Else, reduce snake length by 1, decrease snake score and spawn new poison
    
    The function returns game_is_on to main.py to stop the game loop when the snake length cannot be decreased anymore
    '''
    def collectable_collision(self, snake, color):
        game_is_on = True
        # Snake eats food
        if snake.segments[0].distance(self.food) < 15:
            self.food.spawn_collectables()
            snake.extend(color)
            if snake == self.snake1:
                self.scoreboard1.increase_score()
            else:
                self.scoreboard2.increase_score()
            
        # Spawn new food if food is spawned over snake body
        for segments in snake.segments[1:]:
            if segments.distance(self.food) < 15:
                self.food.spawn_collectables() 
        
        # Snake eats poison
        # Spaw new poison, Delete last snake segment, decrease score
        if snake.segments[0].distance(self.poision) < 15:

            # if len of snake is 1, end game as len cannot be 0
            if len(snake.segments) == 1:
                game_is_on =False
                if snake == self.snake1:
                    self.scoreboard2.game_over("2")
                else:
                    self.scoreboard1.game_over("1")

            # else len of snake > 1, delete segment and decrease score
            else:      
                if snake == self.snake1:
                    snake.delete_segments()
                    self.scoreboard1.decrease_score()
                else:
                    snake.delete_segments()
                    self.scoreboard2.decrease_score()
                self.poision.spawn_collectables()  
        
        # Snake eats wildcard
        # Spawn new wildcard, Delete last snake segment with a for loop, decrease score (both by two)
        # Original plan was to create two options, one of which was too time consuming in terms of implementing the logic, hence gave up
        if snake.segments[0].distance(self.wildcard) < 15:
            if snake == self.snake1:
                if len(self.snake2.segments) <= 2:
                    game_is_on = False
                    self.scoreboard1.game_over("1")
                else:
                    for i in range(2):
                        self.snake2.delete_segments()
                        self.scoreboard2.decrease_score()
                    self.wildcard.spawn_collectables()

            else:
                if len(self.snake1.segments) <= 2:
                    game_is_on = False
                    self.scoreboard2.game_over("2")
                else:
                    for i in range(2): 
                        self.snake1.delete_segments()
                        self.scoreboard1.decrease_score()
                    self.wildcard.spawn_collectables()

        return game_is_on
                