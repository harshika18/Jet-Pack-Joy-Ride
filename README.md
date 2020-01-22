# OBJECTTIVE
The game must simulate a basic version of jetpack joyride. We need to defend the boss before the time specifies.The objective of the game is to collect as many coins as possible, fight the obstacles on the way, defeat the boss enemy and rescue Baby Yoda.

# RUNNING THE GAME
```
python3 is required 
python3 run.py
```

# FEATURES
- The game is implemented in Python3
- The code is modular and follows PEP8 standards
- Uses only core Python3 packages
- Player can move right, left, fly, shoot, use shield
- Enemies are placed in between.
- You can shoot the fire beam, enemy and boss enemy
- Colors are implemented

# MOVEMENT
- a - Move Backwards
- d - Move forward
- j - Fly
- s - implement shield
- space - shoot

# OOP
- #### Inheritance
    - Player, dragon and Enemy class inherit from the Person class
    - vertical, horizontal,forty five beam, coin class inherit from the Obstacle class
- #### Polymorphism
   - Gravity for dragon and hero are 2 different functions with same name
- #### Encapsulation
    - Class and object based approach for all the functionality implemented
- #### Abstraction
    - Properties of the every class are hidden from the user using abstraction and used by getter-setter method

# OBSTACLES
- three types of beam, enemy, coin, magnet, power booster, and boss enemy

# BACKGROUND AND SCENERY
- • The scenery and the obstacles must change as you move in and out of the window. There is a ground/platform and the sky, and the Mandalorian can’t go below the ground or above the sky.

# SCORE
- The final score is calculated as:
```
final score = 10 * (number of enemy kills) + 20 * (number of coins collected) + 10 * (number of obstacles)
```
