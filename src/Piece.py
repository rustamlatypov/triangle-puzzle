import pygame as pg
from Element import Element
from res import *


# represents a piece on the board and on the shelf
class Piece(Element):

    def __init__(self, x, y):
        Element.__init__(self, x, y)
        self.name = "piece"
        self.up = BLANK
        self.left = BLANK
        self.down = BLANK
        self.right = BLANK
        self.upside = False


    # draw a piece
    def draw(self, screen, selected = False):

        y = self.y
        x = self.x

        if (x/100, y/100) in CENTER:
            width = 2
        else:
            width = 1

        if self.upside:

            pg.draw.polygon(screen, self.down,
                            [(y + 50, x + 59), (y + 2.5, x + 91), (y + 97.5, x + 91)])

            pg.draw.polygon(screen, self.right,
                            [(y + 50, x + 9), (y + 51, x + 59), (y + 97.5, x + 91)])

            pg.draw.polygon(screen, self.left,
                            [(y + 50, x + 9),(y + 2.5, x + 91),(y + 49, x + 59)])

            pg.draw.polygon(screen, BLACK,
                            [(y + 50, x + 9), (y + 2.5, x + 91), (y + 97.5, x + 91)], width)

            pg.draw.line(screen, BLACK, (y + 50, x + 60), (y + 2.5, x + 91), 1)

            pg.draw.line(screen, BLACK, (y + 50, x + 60), (y + 97.5, x + 91), 1)

            pg.draw.line(screen, BLACK, (y + 50, x + 60), (y + 50, x + 9), 1)

        else:

            pg.draw.polygon(screen, self.up,
                            [(y + 50, x + 40), (y + 2.5, x + 9), (y + 97.5, x + 9)])

            pg.draw.polygon(screen, self.left,
                            [(y + 50, x + 90), (y + 3, x + 10), (y + 50, x + 40)])

            pg.draw.polygon(screen, self.right,
                            [(y + 50, x + 90), (y + 50, x + 40), (y + 97.5, x + 9)])

            pg.draw.polygon(screen, BLACK,
                            [(y + 50, x + 91), (y + 2.5, x + 9), (y + 97.5, x + 9)], width)

            pg.draw.line(screen, BLACK, (y + 50, x + 40), (y + 97.5, x + 9), 1)

            pg.draw.line(screen, BLACK, (y + 50, x + 40), (y + 2.5, x + 9), 1)

            pg.draw.line(screen, BLACK, (y + 50, x + 40), (y + 50, x + 91), 1)


        if selected:

            if self.upside:
                pg.draw.polygon(screen, DARK_GRAY,
                                [(self.y + 50, self.x + 50),
                                 (self.y + 60, self.x + 60),
                                 (self.y + 50, self.x + 70),
                                 (self.y + 40, self.x + 60)])
                pg.draw.polygon(screen, BLACK,
                                [(self.y + 50, self.x + 50),
                                 (self.y + 60, self.x + 60),
                                 (self.y + 50, self.x + 70),
                                 (self.y + 40, self.x + 60)], 2)
            else:
                pg.draw.polygon(screen, DARK_GRAY,
                                [(self.y + 50, self.x + 30),
                                 (self.y + 60, self.x + 40),
                                 (self.y + 50, self.x + 50),
                                 (self.y + 40, self.x + 40)])
                pg.draw.polygon(screen, BLACK,
                                [(self.y + 50, self.x + 30),
                                 (self.y + 60, self.x + 40),
                                 (self.y + 50, self.x + 50),
                                 (self.y + 40, self.x + 40)], 2)


    # rotate clockwise
    def rotate_right(self):

        if (int(self.x/100),int(self.y/100)) not in INNER:
            if self.upside:
                self.up = self.left
                self.left = self.down
                self.down = NOGO
            else:
                self.down = self.right
                self.right = self.up
                self.up = NOGO

            self.upside = not self.upside


    # rotate counterclockwise
    def rotate_left(self):
        for i in range(5): self.rotate_right()