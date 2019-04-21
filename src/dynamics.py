from Piece import Piece
from Wall import Wall
from Blank import Blank
import os
from res import *
import copy


# depth-first dynamic optimization solver for the game
def algorithm_solve(board):

    elements = []

    for cord in SHELF:
        e = copy.copy(board[cord[0]][cord[1]])
        orientations = []
        for i in range(6):
            orientations.append(e)
            next_e = copy.copy(e)
            next_e.rotate_right()
            e = next_e
        elements.append(orientations)


    IN = [x for x in INNER if x not in CENTER]

    board = copy.deepcopy(board)
    for row in board:
        del row[9:]
    del board[7:]


    def inner(board, IN, elements):

        if not elements:
            return board

        target = IN[0]

        matches = find(elements, target, board)

        for match in matches:

            orientation = match[0]
            indx = match[1]

            board_n = copy.deepcopy(board)
            IN_n = [x for x in IN if x != target]
            elements_n = [x for x in elements if elements.index(x) != indx]

            orientation.x = target[0]*100
            orientation.y = target[1]*100
            board_n[target[0]][target[1]] = orientation

            B = inner(board_n, IN_n, elements_n)

            if type(B) is not type(None):
                return B

    return inner(board, IN, elements)


# helper function
def find(elements, target, board):

    matches = []
    for piece in elements:
        for orientation in piece:
            if fit(orientation, target, board):
                matches.append((orientation, elements.index(piece)))
    return matches


# helper function
def fit(e, cord, B):

        if cord in UPSIDE and not e.upside or cord not in UPSIDE and e.upside:
            return False

        if e.upside:
            n_down = B[cord[0] + 1][cord[1]]
        else:
            n_up = B[cord[0] - 1][cord[1]]

        n_left = B[cord[0]][cord[1] - 1]
        n_right = B[cord[0]][cord[1] + 1]

        if type(n_left) != Blank and n_left.right != e.left:
            return  False

        if type(n_right) != Blank and n_right.left != e.right:
            return False

        if e.upside and type(n_down) != Blank and n_down.up != e.down:
            return False

        if not e.upside and type(n_up) != Blank and n_up.down != e.up:
            return False

        return True


# write board to an external file
def dump(B, file):

    with open(file, "w+") as f:
        for row in B:
            for e in row:
                if type(e) == Piece:
                    if e.upside:
                        o = 1
                    else:
                        o = 0
                    f.write("{};{};{};{};{};{};{};{}\n".
                            format(e, e.x, e.y, e.up, e.left, e.down, e.right, o))
                if type(e) == Wall:
                    f.write("{};{};{};{};{};{};{};{}\n".
                            format(e, e.x, e.y, e.up, e.left, e.down, e.right, e.color))
                if type(e) == Blank:
                    f.write("{};{};{}\n".
                            format(e, e.x, e.y))


# read board from an external file
def read(file):

    with open(file, 'r') as f:
        if os.stat(file).st_size == 0:
            raise FileNotFoundError
        lines = f.readlines()
        B = [[None for x in range(16)] for y in range(9)]
        for line in lines:
            line = line.strip('\n')
            l = line.split(';')
            x = int(int(l[1]) / 100)
            y = int(int(l[2]) / 100)
            if l[0] == 'wall':
                e = Wall(x, y)
                e.up = to_rgb(l[3])
                e.left = to_rgb(l[4])
                e.down = to_rgb(l[5])
                e.right = to_rgb(l[6])
                e.color = to_rgb(l[7])
                B[x][y] = e
            if l[0] == 'piece':
                e = Piece(x, y)
                e.up = to_rgb(l[3])
                e.left = to_rgb(l[4])
                e.down = to_rgb(l[5])
                e.right = to_rgb(l[6])
                if int(l[7]) == 1:
                    e.upside = True
                B[x][y] = e
            if l[0] == 'blank':
                e = Blank(x, y)
                B[x][y] = e
    return B


# text to rgb
def to_rgb(l):

    l = l.strip(')')
    l = l.strip('(')
    l = l.split(',')
    return int(l[0]), int(l[1]), int(l[2])


# print out the board for debugging
def debug(board):

    for x in board:
        for y in x:
            print("{:5s}".format(str(y)), end=' ')
        print("")
    print("")