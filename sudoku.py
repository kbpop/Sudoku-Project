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
from board import Board

def main_menu(screen):
    font=pygame.font.SysFont(None,60)
    small_font=pygame.font.SysFont(None,40)
    while True:
        screen.fill((255,255,255))
        title=font.render("Sudoku Game", True, (0,0,0))
        screen.blit(title, (screen.get_width()//2-title.get_width()//2, 100))

        easy=small_font.render("Press 1 for Easy", True, (0,0,0))
        medium=small_font.render("Press 2 for Medium", True, (0,0,0))
        hard=small_font.render("Press 3 for HARD", True, (0,0,0))

        screen.blit(easy,(screen.get_width()//2-easy.get_width()//2,250))
        screen.blit(medium, (screen.get_width() // 2 - medium.get_width() // 2, 300))
        screen.blit(hard, (screen.get_width() // 2 - hard.get_width() // 2, 350))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT():
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    return"easy"
                if event.key==pygame.K_2:
                    return"medium"
                if event.key==pygame.K_3:
                    return"hard"



def main():
    pygame.init()
    WIDTH,HEIGHT=540,540
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Sudoku")
    difficulty=main_menu(screen)

    board=Board(WIDTH,HEIGHT,screen, difficulty)


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
                    board.select(row,col)
            if event.type==pygame.KEYDOWN:
                if board.selected_cell:
                    if event.key==pygame.K_1:
                        board.sketch(1)
                    if event.key==pygame.K_2:
                        board.sketch(2)
                    if event.key==pygame.K_3:
                        board.sketch(3)
                    if event.key == pygame.K_4:
                        board.sketch(4)
                    if event.key == pygame.K_5:
                        board.sketch(5)
                    if event.key == pygame.K_6:
                        board.sketch(6)
                    if event.key == pygame.K_7:
                        board.sketch(7)
                    if event.key == pygame.K_8:
                        board.sketch(8)
                    if event.key == pygame.K_9:
                        board.sketch(9)
                    if event.key==pygame.K_RETURN:
                        board.place_number(board.selected_cell.sketched_value)
                    if event.key==pygame.K_BACKSPACE:
                        board.clear()

        screen.fill((255,255,255))
        board.draw()
        pygame.display.update()
    pygame.quit()
if __name__=="__main__":
    main()



