#import pygame
#from cell import Cell
#WIDTH = 600
#HEIGHT = 600
#LINE_WIDTH = 15
#WIN_LINE_WIDTH = 15
#BOARD_ROWS = 3
#BOARD_COLS = 3
#SQUARE_SIZE = 200
#CIRCLE_RADIUS = 60
#CIRCLE_WIDTH = 15
#CROSS_WIDTH = 25
# SPACE = 55
# RED = (255, 0, 0)
# BG_COLOR = (255, 255, 245)
# LINE_COLOR = (245, 152, 66)
# CIRCLE_COLOR = (155, 155, 155)
# CROSS_COLOR = (66, 66, 66)
# CHIP_FONT = 400
# GAME_OVER_FONT = 40
#
#
# pygame.init()
# WIDTH, HEIGHT = 1000, 1000
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Sudoku')
# screen.fill((255,255,255))
# test = Cell(1,1,1,1)
import pygame
import board import board
def main():
    pygame.init()
    WIDTH,HEIGHT=540,540
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Sudoku")

    board=board(WIDTH,HEIGHT,screen, "easy")


    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                clicked=board.click(pos[0], pos[1])
                if clicked:
                    row,col=clicked
                    board.select(rol,col)
            if event.tpe==pygame.KEYDOWN:



