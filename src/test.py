import unittest
from Piece import Piece
from Wall import Wall
from Blank import Blank
from Game import Game
from res import *
import copy
import os


# tests for the game logic
class Test(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.gen_board()


    def test_is_valid(self):

        valid = self.game.is_valid()

        self.assertTrue(valid, "Board is valid, but is_valid returns False")

        board = self.game.get_board()

        board[2][3] = Blank(2,3)

        valid = self.game.is_valid()

        self.assertFalse(valid, "Board is not valid (one element missing), but is_valid returns True")


    def test_dump_read(self):

        board = self.game.get_board()
        reference = copy.deepcopy(board)
        f = "reference.txt"

        self.game.dump_board(f)

        self.game.load_board(f)

        valid = True

        for i in range(9):
            for j in range(16):

                e = board[i][j]
                r = reference[i][j]

                if type(e) == type(None) and type(r) != type(None):
                    valid = False

                if type(e) != type(None) and type(r) == type(None):
                    valid = False

                if type(e) == Blank and type(r) != Blank:
                    valid = False

                if type(e) != Blank and type(r) == Blank:
                    valid = False

                if type(e) == Wall and type(r) != Wall:
                    valid = False

                if type(e) != Wall and type(r) == Wall:
                    valid = False

                if type(e) == Piece and type(r) != Piece:
                    valid = False

                if type(e) != Piece and type(r) == Piece:
                    valid = False

                if type(e) == Wall and type(r) == Wall:
                    if e.up != r.up or e.left != r.left or e.down != r.down or e.right != r.right or e.color != r.color:
                        valid = False

                if type(e) == Piece and type(r) == Piece:
                    if e.up != r.up or e.left != r.left or e.down != r.down or e.right != r.right or e.upside != r.upside:
                        valid = False


        os.remove(f)

        self.assertTrue(valid, "Data loss between dumping and reading a board")


    def test_gen_board(self):

        board = self.game.get_board()

        count = 0

        for row in board:
            for e in row:
                if type(e) == Piece:
                    count += 1

        self.assertEqual(28, count, "Wrong number of pieces overall")

        valid = self.game.is_valid()

        self.assertTrue(valid, "Generated board is invalid")

        self.game.shuffle()
        board = self.game.get_board()

        count = 0

        for cord in SHELF:
            e = board[cord[0]][cord[1]]
            if type(e) == Piece:
                count += 1

        self.assertEqual(26, count, "After shuffeling, wrong number of pieces on the board")

        count = 0

        for cord in INNER:
            e = board[cord[0]][cord[1]]
            if type(e) == Piece:
                count += 1

        self.assertEqual(2, count, "After shuffeling, wrong number of pieces on the shelf")


    def test_algothm_solve(self):

        board = self.game.get_board()
        solution = copy.deepcopy(board)
        self.game.shuffle()
        self.game.solve()
        board = self.game.get_board()

        identical = True

        for cord in INNER:
            sol = solution[cord[0]][cord[1]]
            algo = board[cord[0]][cord[1]]
            if sol.left != algo.left: identical = False
            if sol.right != algo.right: identical = False
            if sol.upside and sol.down != algo.down: identical = False
            if not sol.upside and sol.up != algo.up: identical = False

        valid = self.game.is_valid()

        self.assertTrue(identical or valid, "Algorithm's solution is not valid")

        count = 0

        for row in board:
            for e in row:
                if type(e) == Piece:
                    count += 1

        self.assertEqual(28, count, "After solving, wrong number of pieces overall")



if __name__ == '__main__':
    unittest.main()
