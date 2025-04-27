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
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    return"easy"
                if event.key==pygame.K_2:
                    return"medium"
                if event.key==pygame.K_3:
                    return"hard"

def win_screen(screen):
    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 40)

    while True:
        screen.fill((255, 255, 255))

        win_text = font.render("You Solved It!", True, (0, 128, 0))
        instruction_text = small_font.render("Press ENTER to play again or ESC to quit.", True, (0, 0, 0))

        screen.blit(win_text, (screen.get_width()//2 - win_text.get_width()//2, 200))
        screen.blit(instruction_text, (screen.get_width()//2 - instruction_text.get_width()//2, 300))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # Restart
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
def game_over_screen(screen):
    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 40)

    while True:
        screen.fill((255, 255, 255))

        over_text = font.render("Game Over!", True, (255, 0, 0))
        instruction_text = small_font.render("Press ENTER to try again or ESC to quit.", True, (0, 0, 0))

        screen.blit(over_text, (screen.get_width()//2 - over_text.get_width()//2, 200))
        screen.blit(instruction_text, (screen.get_width()//2 - instruction_text.get_width()//2, 300))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # Restart
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()



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
                        if board.is_full():
                            if win_screen(screen):
                                difficulty=main_menu(screen)
                                board=Board(WIDTH,HEIGHT, screen, difficulty)
                            else:
                                if game_over_screen(screen):
                                    difficulty=main_menu(screen)
                                    board=Board(WIDTH,HEIGHT,screen, difficulty)
                    if event.key==pygame.K_BACKSPACE:
                        board.clear()

        screen.fill((255,255,255))
        board.draw()
        pygame.display.update()
    pygame.quit()
if __name__=="__main__":
    main()



