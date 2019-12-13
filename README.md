# Triangle puzzle game 

Developed in March, 2019.

## Description

This is a challenging triangle puzzle game with a sophisticated self-solving algorithm. Triangles are picked up and placed using the mouse and rotated clockwise and counterclockwise with `D` and `A` respectively. The task is to place the triangles on the board so that the colors of the triangles' sides match. Also, the colors of the walls have to match with the neighboring triangles.

The player can check the validity of the current solution by pressing `Check solution`, generate a new game by pressing `New Game` and ask for the correct solution by pressing `Solve`. 

No valid solution is held in the memory of the program. Instead, every time a player asks for a solution, the program solves the board by employing a depth-first dynamic algorithm. Due to the nature of the game there may be more than one correct solution, and the algorithm displays the first one it encounters. 


## Running

Built with Python 3.7.2 and `pygame 1.9.4`.<br/>
In `/src` run `python3 main.py`.


## Author

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)
