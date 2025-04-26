import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RED = (255, 0, 0)
BG_COLOR = (255, 255, 245)
LINE_COLOR = (245, 152, 66)
CIRCLE_COLOR = (155, 155, 155)
CROSS_COLOR = (66, 66, 66)
CHIP_FONT = 400
GAME_OVER_FONT = 40


class Board:
    def __init__(self, width, height, screen, difficulty):
        #''' screen is a window from PyGame.
	    #difficulty is a variable to indicate if the user chose easy medium, or hard.'''
        self.width = width
        self.height = height
        self.screen = screen
        self.difficult = difficulty
        self.cells=[]
        self.selected_cell=None



    def draw(self):
        self.screen.fill((255,255,255))
        for i in range(10):
            if i%3==0:
                thickness=4
            else:
                thickness=1
            pygame.draw.line(self.screen, (0,0,0), (0,i*(self.height//9)), (self.width,i*(self.height//9)), thickness)
            pygame.draw.line(self.screen, (0,0,0), (i*(self.width//9),0), (i*(self.width//9), self.height), thickness)
        for row in self.cells:
            for cell in row:
                cell.draw()
        #'''Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board.'''
        # draw horizontal lines
        #for i in range(1, BOARD_ROWS):
            #pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        # draw vertical lines
        #for i in range(1, BOARD_COLS):
            #pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        return None

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected=False
        self.selected_cell=self.cells[row][col]
        self.selected_cell.selected=True

        #'''Marks the cell at (row, col) in the board as the current selected cell.
	#Once a cell has been selected, the user can edit its value or sketched value.'''

        return None

    def click(self, x, y):
        #'''If a tuple of (x,y) coordinates is within the displayed board,
        #this function returns a tuple of the (row, col) of the cell which was clicked.
        #Otherwise, this function returns None.'''
        if x<self.width and y<self.height:
            row=y//(self.height//9)
            col=x//(self.width//9)
            return row, col
        return None

    def clear(self):
        #'''Clears the value cell.
        #Note that the user can only remove the cell values and
        #sketched values that are filled by themselves.'''
        if self.selected_cell and self.selected_cell.value==0:
            self.selected_cell.sketched_value=0
        return None

    def sketch(self, value):
        #'''Sets the sketched value of the current selected cell equal to the user entered value.
	#It will be displayed at the top left corner of the cell using the draw() function.'''
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)
        return None

    def place_number(self, value):
        #'''Sets the value of the current selected cell equal to the user entered value. Called when the user presses the Enter key.'''

        return None

    def reset_to_original(self):
        '''Resets all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).'''

        return None

    def is_full(self):
        '''Returns a Boolean value indicating whether the board is full or not.'''

        return None

    def update_board(self):
        '''Updates the underlying 2D board with the values in all cells.'''

        return None

    def find_empty(self):
        '''Finds an empty cell and returns its row and col as a tuple (x,y).'''

        return None

    def check_board(self):
        '''Check whether the Sudoku board is solved correctly.'''

        return None


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode()
    screen.fill((255, 255, 255))
    board = Board(1000, 1000, screen, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()

        pygame.display.update()
        board.draw()