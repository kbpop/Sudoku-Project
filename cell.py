import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected=False

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
