# A challenging triangle puzzle game 

Project for the Aalto University course CS-A1121 - Programming 2.

Developed in March, 2019.

## Description

This is a challenging triangle puzzle game with a sophisticated self-solving algorithm. Triangles are picked and
placed using the mouse and rotated clockwise and counterclockwise with `D` and `A` respectively. The task is to 
placen the triangles on the board so that the colors of the triangles' sides match. Also, the colors of the walls 
haveto match with the neighboring triangles.

The player can check the current solution by pressing `Check solution`, generate a new game by pressing 
`New Game` and ask for the correct solution by pressing `Solve`. 

No valid solution is held in the memory of the program. Instead, every time a player asks for a solution, the 
program solves the board by employing a sophisticated depth-first dynamic alogorithm. 


## Software prerequisites

Built on Python 3.7 with PyGame 1.9.5.


## Authors

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)