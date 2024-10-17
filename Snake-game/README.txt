# Snake Game

Welcome to our Computational Thinking For Design (Term 1) Python 1D project, where the classic Snake game takes on a whole new dimension! Our snake game comprises of two game modes: Single and Multiplayer. The goal of the game is to grow your snake by consuming more food while avoiding the poison consumable which would spawn randomly throughout the game. Points will be awarded and reflected in the scoreboard with a proportional increment in length of snake when the food item is consumed. Conversely, points will be deducted and snake will shrink in size if the snake consumed a poison item. In the multiplayer mode, we introduced a wildcard which could potentially change the fate of the game. Once consumed the wildcard item, your opponent immediately loses 2 health bars. In any instance where the snake collides with the boundary of the wall or bump into the body of the other snake, the game ends and the final score will be computed, and the winner will be announced. Colliding into your own body (head-on-tail collision)

## Scenario

Our snake game is designed to enhance the gameplay, catering to a myriad of audience including SUTD students who wants to take time-off from their work. The game caters to both recreational and competitive gamers, ranging from amateurs to professional levels. The game attracts players who seek for a sense of nostalgia as we re-create the snake game with a modern twist. Strategic thinking is employed, particularly during the multiplayer mode where users can add elements of their skills to win the game. Friendships can also be forged or strengthened as students come together to play in the multiplayer mode. Game can be held during meetings and breaks in classes for their respite. In essence, our multiplayer mode offers a twist from the original game, offering a novel experience to players. 

## Group Members

SC04 Team 4H
- @Brian Lian [1007769]
- @Madhushri [1008460]
- @Amestis [1008138]
- @Cyrus Yuen [1007689]
- @Jeffrey Ko [1008070]
- @Joel Yeo [1008112]
  
## Deployment

To deploy this project..

```
  cd to/path/Snake-game/main.py
  python main.py
```
or open in your preferred IDE choice and run main.py

## Game Instructions
Slither around the map and collect collectables! Beware... your snake increases in speed over time!

Collectables:
- Food (Blue): Gain 1 point/snake length
- Poison (Green): Lose 1 point/snake length
- Wildcard (Purple): Opponent loses 2 points/snake length
- Poison and Wildcard will constantly change location if not collected

Warning! DO NOT:
- Collide into other snakes or yourself
- Exceed screen boundary

## Demo
Watch our demo video here:
https://www.youtube.com/watch?v=BE1putgyWxo