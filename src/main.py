import pygame as pg
from pygame.locals import *
from Piece import Piece
from Blank import Blank
from Game import Game
from res import *

#-----------------initialize pygame-----------------#
pg.init()
pg.font.init()

#-----------------create the screen object
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Triangle puzzle")

#-----------------create board and texts-----------------#
game = Game()

#-----------------try to load board from an external file-----------------#
board_file = 'board.txt'

try:
    game.load_board(board_file)
except FileNotFoundError:
    game.gen_board()
    game.shuffle()

#-----------------set font and texts-----------------#
myfont = pg.font.SysFont('freesansbold.ttf', 30)

greatings_text = myfont.render('Welcome to the triangle puzzle game!', False, BLACK)

check_display1 = myfont.render('Your solution is correct!', False, GREEN)
check_display2 = myfont.render('Your solution is wrong!', False, RED)

solve_display = myfont.render('This wuold have been the correct solution.', False, BLACK)

newgame_display = myfont.render('Welcome to the triangle puzzle game!', False, BLACK)

illegal_display = myfont.render('Illegal move!', False, RED)

goodmove_display = myfont.render('Nice move.', False, BLACK)

check_button = pg.Rect(990, 790, 165, 40)
check_text = myfont.render('Check solution', False, BLACK)

solve_button = pg.Rect(1190, 790, 70, 40)
solve_text = myfont.render('Solve', False, BLACK)

newgame_button = pg.Rect(1390, 790, 120, 40)
newgame_text = myfont.render('New game', False, BLACK)

#-----------------variables for the main loop-----------------#
running = True
selected = False
console_text = greatings_text
delay = True
(x, y, t) = (-1, -1, None)
pos = (-1,-1)

#-----------------main loop-----------------#
while running:

    #-----------------event queue-----------------#
    for event in pg.event.get():

        #-----------------keyboard pressed-----------------#
        if event.type == KEYDOWN:
            if event.key == K_d and selected:   game.rotate_right(x,y)
            if event.key == K_a and selected:   game.rotate_left(x,y)

        #-----------------right mouse button pressed-----------------#
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            (x_prev, y_prev, t_prev) = (x, y, t)
            (x, y, t) = game.get_info(pos)

            if selected:
                if t == Blank:
                    if game.valid_switch(x, y, x_prev, y_prev):
                        game.switch(x, y, x_prev, y_prev)
                        console_text = goodmove_display
                    else:
                        console_text = illegal_display
                selected = False


            if not selected and t == Piece and (x,y) not in CENTER:
                selected = True

            if check_button.collidepoint(pos):
                if game.is_valid():
                    console_text = check_display1
                else:
                    console_text = check_display2

            if solve_button.collidepoint(pos):
                game.solve()
                console_text = solve_display

            if newgame_button.collidepoint(pos):
                game.gen_board()
                game.shuffle()
                console_text = newgame_display

        if event.type == QUIT:
            game.dump_board(board_file)
            running = False

    #-----------------draw elements-----------------#

    screen.fill(GRAY)

    game.draw_elements(screen)

    if selected:
        game.draw_selected(x, y, screen)

    screen.blit(console_text, (100, 800))

    pg.draw.rect(screen, DARK_GRAY, check_button)
    pg.draw.polygon(screen, BLACK, [(990, 790), (990, 830), (1155, 830), (1155, 790)], 1)
    screen.blit(check_text, (1000, 800))

    pg.draw.rect(screen, DARK_GRAY, solve_button)
    pg.draw.polygon(screen, BLACK, [(1190, 790), (1190, 830), (1260, 830), (1260, 790)], 1)
    screen.blit(solve_text, (1200, 800))

    pg.draw.rect(screen, DARK_GRAY, newgame_button)
    pg.draw.polygon(screen, BLACK, [(1390,790),(1390,830),(1510,830),(1510,790)], 1)
    screen.blit(newgame_text, (1400, 800))

    pg.display.flip()