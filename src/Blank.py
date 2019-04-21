import pygame as pg
from Element import Element
from res import *


# represents a blank on the board and on the shelf
class Blank(Element):

    def __init__(self, x, y):

        Element.__init__(self, x, y)
        self.name = "blank"

    # draw a blank
    def draw(self, screen):

        x = self.x
        y = self.y

        if (self.x/100,self.y/100) in INNER:
            if (self.x/100,self.y/100) in UPSIDE:
                pg.draw.polygon(screen, BLACK, [(y + 50, x + 9),
                                                (y + 2.5, x + 91),
                                                (y + 97.5, x + 91)], 1)
            else:
                pg.draw.polygon(screen, BLACK, [(y + 50, x + 91),
                                                (y + 2.5, x + 9),
                                                (y + 97.5, x + 9)], 1)
        else:
            pg.draw.polygon(screen, BLACK,
                                [(y + 50, x + 35),
                                 (y + 65, x + 50),
                                 (y + 50, x + 65),
                                 (y + 35, x + 50)], 1)