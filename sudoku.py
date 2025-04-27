import pygame
from board import Board

LINE_WIDTH = 7
LINE_WIDTH_BOLD = 15

WIN_LINE_WIDTH = 15
SQUARE_SIZE = 100
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RED = (255, 0, 0)
BG_COLOR = (255, 255, 245)
LINE_COLOR = (245, 152, 66)

starting_point_x = 20
starting_point_y = 20


def home_screen(ev):

    smallfont = pygame.font.SysFont('Corbel',35)  
    text = smallfont.render('quit' , True , (100,20,20))

    if ev.type == pygame.QUIT:  
        pygame.quit()  
            
    if ev.type == pygame.KEYDOWN:  
        print('something is happening')
        return 1


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode()
    screen.fill((255,255,255))
    board_width = 800
    board_height = 800
    board = Board(board_width,board_height,screen,1)
    mode = 1
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if mode == 0:
                mode = home_screen(event, board_width, board_height)
            if mode == 1:
                if board.game_animation(event):
                    font = pygame.font.Font(None,300)

                    cell_x_surf = font.render("YOU WIN YAY", 0, (100,200,0))
                    cell_x_rect = cell_x_surf.get_rect(center=(board_width/2,board_height/2))

                    screen.fill((230,230,230), rect=cell_x_rect)
                    screen.blit(cell_x_surf, cell_x_rect)
                board.draw()

        pygame.display.update()


