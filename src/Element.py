# upper class for the elements on the board
class Element:

    def __init__(self, x, y):

        self.name = "element"
        self.x = x * 100
        self.y = y * 100


    def __str__(self):
        return self.name