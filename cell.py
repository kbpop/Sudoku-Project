import pygame



starting_point_x = 70
starting_point_y = 70


class Cell:
    def __init__(self, value, row, col, screen, editable):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.selected=False
        self.sketched_value=0

    def set_cell_value(self, value):
        self.value=value

    def set_sketched_value(self, value):
        self.sketched_value=value

    def draw(self):
        cell_size=540//9
        x=self.col*cell_size
        y=self.row*cell_size
        if self.selected:
            pygame.draw.rect(self.screen,(255,255,0), (x,y,cell_size, cell_size))
        font=pygame.font.SysFont(None,40)
        if self.value!=0:
            text=font.render(str(self.value), True, (0,0,0))
            text_rect=text.get_rect(center=(x+cell_size//2, y+cell_size//2))
            self.screen.blit(text,text_rect)
        elif self.sketched_value!=0:
            sketch_font=pygame.font.SysFont(None,20)
            text=sketch_font.render(str(self.sketched_value), True, (128,128,128))
            self.screen.blit(text, (x+5, y+5))
        return None

        self.editable = editable

    def set_cell_value(self, value):
        self.value = value

    def draw(self):
        font = pygame.font.Font(None,100)
        if self.value != 0:
            cell_x_surf = font.render(str(self.value), 0, (100,200,0))
            cell_x_rect = cell_x_surf.get_rect(center=(self.row*800/9 +starting_point_x,self.col*800/9+starting_point_y))
            self.screen.blit(cell_x_surf, cell_x_rect)
    
    def draw_selected(self,value):
        font = pygame.font.Font(None,100)
        if self.value != 0:
            cell_x_surf = font.render(str(self.value), 0, (100,200,0))
            cell_x_rect = cell_x_surf.get_rect(center=(self.row*800/9 +starting_point_x,self.col*800/9+starting_point_y))

            self.screen.fill((230,230,230), rect=cell_x_rect)
            self.screen.blit(cell_x_surf, cell_x_rect)

        if value:
            font = pygame.font.Font(None,50)
            cell_x_surf = font.render(str(value), 0, (0,0,0), (255,255,255))
            cell_x_rect = cell_x_surf.get_rect(center=(self.row*800/9 +starting_point_x - 30,self.col*800/9+starting_point_y-25))

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




