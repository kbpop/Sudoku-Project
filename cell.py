import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        return None

    def draw(self):
        font = pygame.font.Font(None,100)
        cell_x_surf = font.render(self.value, 0, (100,200,0))
        cell_x_rect = cell_x_surf.get_rect(center=(self.row*100,self.col*100))
        self.screen.blit(cell_x_surf, cell_x_rect)

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode()
    test_cell = Cell("2",2,2,screen)
    screen.fill((255,255,255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()

        pygame.display.update()
        test_cell.draw()



