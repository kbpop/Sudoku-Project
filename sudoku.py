import pygame
from cell import Cell

pygame.init()
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
screen.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()

    pygame.display.update()
