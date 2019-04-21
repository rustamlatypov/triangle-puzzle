import pygame as pg
from Element import Element
from res import *


# represents a static wall on the board
class Wall(Element):

    def __init__(self, x, y):
        Element.__init__(self, x, y)
        self.name = "wall"
        self.up = BLANK
        self.left = BLANK
        self.down = BLANK
        self.right = BLANK
        self.color = BLANK


    # draw a wall
    def draw(self, screen):

        x = self.x
        y = self.y

        pg.draw.circle(screen, BLACK, (y + 50, x + 50), 12)
        pg.draw.circle(screen, self.color, (y + 50, x + 50), 10)