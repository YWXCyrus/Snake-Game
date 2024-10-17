from snake import Snake
from Collectables.food import Food
from scoreboard import Scoreboard
from Collectables.poision import Poision
from config import *
from turtle import Turtle

'''
The Single Player class is the brains behind the game.
There is 1 snake and Food and Poison is spawned at random location.
A scoreboard is also assigned to the snake
'''
class SinglePlayer:
    def __init__(self):
        self.snake = Snake(STARTING_POSITIONS)
        self.food = Food()
        self.poision = Poision()
        self.scoreboard = Scoreboard(self.snake, SCOREBOARD_POS1, "1")

    
    '''
    This function creates the game window. 
    There is a parameter, screen. We pass in Screen from Turtle when we call this function.
    The game controls are also asigned to the different snakes.
    '''
    def setup_screen(self, screen):
        screen.setup(width=screen_size, height=screen_size)
        screen.bgcolor("black")
        screen.title("Snake game")
        screen.tracer(0)

        # set keyboard listener
        screen.listen()
        screen.onkey(self.snake.up, "Up")
        screen.onkey(self.snake.down, "Down")
        screen.onkey(self.snake.left, "Left")
        screen.onkey(self.snake.right, "Right")
        screen.onkey(lambda: screen.bye(), "Escape")
    
    
    '''
    This function creates the snake, collectables and scoreboard on the screen in the initial stage.
    '''
    def setup_game(self):
        self.snake.create_snake("white")
        self.scoreboard.setup_scoreboard()
        self.food.spawn_collectables()
        self.poision.spawn_collectables()
    
    
    '''
    This function contains all the functions that should be constantly updated.
    1. Update snake movement
    2. Check if snake collides into collectables -> returns Boolean and assign to collectable_collision
    3. Check if snake is within boundries -> returns Boolean and assign to s_boundry
    4. updates scoreboard
    5. Check poison timer -> If it returns True, poison on screen has appeared for more than 10 seconds, therefore call spawn_collectables to change location of poison
    The function initially declares game_is_on as True
    If collectable_collision or s_boundry return false, game is over, therefore set game_is_on = False
    The function returns game_is_on to main.py to stop the game loop
    '''
    def update(self):   
        game_is_on = True
        self.snake.move()
        self.collectable_collision('white')
        game_is_on = self.verify_boundaries()
        self.scoreboard.update_scoreboard()
        collectable_collision = self.collectable_collision('white')
        s_boundry = self.verify_boundaries()
        
        # If check_timer == True (more than 10 seconds), spawn a new poison
        if self.poision.check_timer() == True:
            self.poision.spawn_collectables()
        
        if (collectable_collision and s_boundry) == False:
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
    def verify_boundaries(self):
        game_is_on = True
        
        x_cor = self.snake.segments[0].xcor()
        y_cor = self.snake.segments[0].ycor()
        
        # If snake hit edge
        if x_cor > half_screen_size-20 or x_cor < -half_screen_size+10 or y_cor > half_screen_size-10 or y_cor < -half_screen_size+20:
            print("Boundry Hit")
            game_is_on = False
            self.scoreboard.game_over("single")
        
        # snake head hit body
        # when head of snake to distance of body <5, game end
        # First condition check if snake is less than 3 block, code won't run as head too close to new block
        if len(self.snake.segments) >2 :      
            for segment in self.snake.segments[1:]:
                if self.snake.segments[0].distance(segment)<5:
                    game_is_on = False
                    self.scoreboard.game_over("single")
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
    def collectable_collision(self, color):
        game_is_on = True
        
        # Snake east food
        if self.snake.segments[0].distance(self.food) < 15:
            print("Food eaten")
            self.food.spawn_collectables()
            self.snake.extend(color)
            self.scoreboard.increase_score()
        
        # Spawn new food if food is spawned over snake body
        for segments in self.snake.segments[1:]:
            if segments.distance(self.food) < 15:
                self.food.spawn_collectables() 

        # Snake eats poison
        # Spaw new poison, Delete last snake segment, decrease score
        if self.snake.segments[0].distance(self.poision)<15:
            print("Poison eaten")
            if len(self.snake.segments) == 1:
                game_is_on =False
                self.scoreboard.game_over("single")
            else:        
                self.snake.delete_segments()
                self.scoreboard.decrease_score()
                self.poision.spawn_collectables()
        return game_is_on

        
            
            
            