import pygame

starting_point_x = 70
starting_point_y = 70

class Cell:
    def __init__(self, value, row, col, screen, editable):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.editable = editable

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        return None

    def draw(self):
        font = pygame.font.Font(None,100)
        if self.value != 0:
            cell_x_surf = font.render(str(self.value), 0, (100,200,0))
            cell_x_rect = cell_x_surf.get_rect(center=(self.row*800/9 +starting_point_x,self.col*800/9+starting_point_y))
            self.screen.blit(cell_x_surf, cell_x_rect)
    
    def draw_selected(self):
        font = pygame.font.Font(None,100)
        if self.value != 0:
            cell_x_surf = font.render(str(self.value), 0, (100,200,0))
            cell_x_rect = cell_x_surf.get_rect(center=(self.row*800/9 +starting_point_x,self.col*800/9+starting_point_y))
            self.screen.fill((230,230,230), rect=cell_x_rect)
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



