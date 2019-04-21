from Piece import Piece
from Wall import Wall
from Blank import Blank
import dynamics
import copy
import random
from res import *
from datetime import datetime
random.seed(datetime.now())


class Game:

    def __init__(self):
        self.__board = None


    # generate a new random board
    def gen_board(self):

        # fill board with elements

        board = [[None for x in range(16)] for y in range(9)]

        for cord in WALLS:
            board[cord[0]][cord[1]] = Wall(cord[0],cord[1])

        for cord in INNER:
            board[cord[0]][cord[1]] = Piece(cord[0],cord[1])

        for cord in UPSIDE:
            board[cord[0]][cord[1]].upside = True

        for x in board:
            for y in x:
                if type(y) == Piece and y.upside: y.up = NOGO
                if type(y) == Piece and not y.upside: y.down = NOGO

        for cord in SHELF:
            board[cord[0]][cord[1]] = Blank(cord[0],cord[1])

        # color elements

        for cord in SP_WALLS:
            e = board[cord[0]][cord[1]]
            col = random.choice(COL)
            e.left = col
            e.right = col
            board[cord[0]][cord[1] - 1].right = col
            board[cord[0]][cord[1] + 1].left = col

        for cord in INNER:
            e = board[cord[0]][cord[1]]
            col = [random.choice(COL) for i in range(4)]
            if e.up == BLANK:
                e.up = col[0]
                board[cord[0]-1][cord[1]].down = col[0]
            if e.left == BLANK:
                e.left = col[1]
                board[cord[0]][cord[1]-1].right = col[1]
            if e.down == BLANK:
                e.down = col[3]
                board[cord[0]+1][cord[1]].up = col[3]
            if e.right == BLANK:
                e.right = col[2]
                board[cord[0]][cord[1]+1].left = col[2]

        self.set_wall_color(board)

        self.__board = board


    # set the color of the walls according to one of the border colors
    def set_wall_color(self, board):

        for cord in WALLS:
            e = board[cord[0]][cord[1]]
            collection = (e.up, e.left, e.down, e.right)
            for col in collection:
                if col != BLANK:
                    e.color = col


    # return the current board
    def get_board(self):
        return self.__board


    # load board from an external file
    def load_board(self, board_file):
        self.__board = dynamics.read(board_file)


    # write board to an external file
    def dump_board(self, board_file):
        dynamics.dump(self.__board, board_file)


    # call the algorthmic solver
    def solve(self):

        self.reset()
        board = dynamics.algorithm_solve(self.__board)

        for cord in INNER:
            self.__board[cord[0]][cord[1]] = board[cord[0]][cord[1]]

        for cord in SHELF:
            self.__board[cord[0]][cord[1]] = Blank(cord[0],cord[1])


    # draw all elements on the board
    def draw_elements(self, screen):

        for row in self.__board:
            for elem in row:
                if elem is not None:
                    elem.draw(screen)


    # draw the piece that is selected by the player
    def draw_selected(self, x, y, screen):
        self.__board[x][y].draw(screen, True)


    # return info of the element at a positions
    def get_info(self, pos):

        x = int(pos[1] / 100)
        y = int(pos[0] / 100)
        t = type(self.__board[x][y])
        return x,y,t


    # check if a switch is valid
    def valid_switch(self, x1, y1, x2, y2):

        if (x1,y1) in INNER:
            if self.__board[x2][y2].upside and (x1,y1) in UPSIDE:
                return True
            elif not self.__board[x2][y2].upside and (x1,y1) not in UPSIDE:
                return True
            else:
                return False
        else:
            return True


    # switch elements
    def switch(self, x1, y1, x2, y2):

        board = self.__board

        a = copy.deepcopy(board[x1][y1])
        b = copy.deepcopy(board[x2][y2])

        a.x = board[x2][y2].x
        a.y = board[x2][y2].y

        b.x = board[x1][y1].x
        b.y = board[x1][y1].y

        board[x1][y1] = b
        board[x2][y2] = a


    # check if the current board is a valid solution
    def is_valid(self):

        board = self.__board

        for cord in INNER:
            elem = board[cord[0]][cord[1]]
            if type(elem) == Blank:
                return False

        for cord in INNER:
            elem = board[cord[0]][cord[1]]
            if type(elem) == Piece:
                if elem.up != NOGO and elem.up != board[cord[0]-1][cord[1]].down:
                    return False
                if elem.left != NOGO and elem.left != board[cord[0]][cord[1]-1].right:
                    return False
                if elem.down != NOGO and elem.down != board[cord[0]+1][cord[1]].up:
                    return False
                if elem.right != NOGO and elem.right != board[cord[0]][cord[1]+1].left:
                    return False
        return True


    # shuffle the position and the orientation of all the pieces
    def shuffle(self):

        board = self.__board
        SH = copy.copy(SHELF)
        SH = list(SH)

        for cord in INNER:
            if cord not in CENTER:
                (x,y) = random.choice(SH)
                SH.remove((x,y))
                self.switch(cord[0],cord[1],x,y)
                t = random.randint(0, 5)
                for i in range(t): board[x][y].rotate_right()


    # reposition all of the pieces to the shelf
    def reset(self):

        for cord1 in INNER:
            if cord1 not in CENTER:
                e1 = self.__board[cord1[0]][cord1[1]]
                if type(e1) == Piece:
                    for cord2 in SHELF:
                        e2 = self.__board[cord2[0]][cord2[1]]
                        if type(e2) == Blank:
                            self.switch(cord1[0],cord1[1],cord2[0],cord2[1])


    # rotate the element at (x,y) clockwise
    def rotate_right(self, x, y):
        self.__board[x][y].rotate_right()


    # rotate the element at (x,y) counterclockwise
    def rotate_left(self, x, y):
        self.__board[x][y].rotate_left()
