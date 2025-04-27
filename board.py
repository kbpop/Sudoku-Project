import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

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

class Board:
    def __init__(self, width, height, screen, difficulty):
        ''' screen is a window from PyGame.
	    difficulty is a variable to indicate if the user chose easy medium, or hard.'''
        self.row_length = 9 
        self.width = width    
        self.height = height
        self.screen = screen   
        self.difficult = difficulty    
        self.cells = [[Cell(c,r_index,c_index,screen,c==0) for c_index, c in enumerate(r)] for r_index, r in enumerate(generate_sudoku(9,difficulty)) ]
        self.square_size = width / 9
        self.selected_cell = None
        self.sketched_value = None

    def draw(self):
        '''Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board.'''
        self.draw_horizontal_grid_lines()
        self.draw_vertical_grid_lines()
        self.draw_cells()
        
    def draw_horizontal_grid_lines(self):
        '''Draws the horizontal grid lines'''
        for i in range(0, self.row_length+1):
            line_width = LINE_WIDTH
            if (i) % 3 == 0:
               line_width = LINE_WIDTH_BOLD 
            pygame.draw.line(self.screen, LINE_COLOR, (starting_point_x, i * self.square_size+starting_point_y), (self.width+starting_point_x, i * self.square_size+starting_point_y), line_width)

    def draw_vertical_grid_lines(self):
        '''Draws the vertical grid lines'''
        for i in range(0, self.row_length+1):
            line_width = LINE_WIDTH
            if (i) % 3 == 0:
               line_width = LINE_WIDTH_BOLD
            pygame.draw.line( self.screen, LINE_COLOR, (i * self.square_size+starting_point_x, starting_point_y), (i * self.square_size+starting_point_x, self.height+starting_point_y), line_width)
    
    def draw_cells(self):
        for r in self.cells:
            for c in r:
                if c is self.selected_cell:
                    c.draw_selected(self.sketched_value)
                else:
                    c.draw()

    def select(self, row, col):
        '''Marks the cell at (row, col) in the board as the current selected cell.
	Once a cell has been selected, the user can edit its value or sketched value.'''
        self.sketched_value = None
        if self.cells[row][col].editable:
            self.selected_cell = self.cells[row][col]

    def click(self, x, y):
        '''If a tuple of (x,y) coordinates is within the displayed board, 
        this function returns a tuple of the (row, col) of the cell which was clicked. 
        Otherwise, this function returns None.'''

        if x > starting_point_x and x < (starting_point_x+self.width) and y > starting_point_y and y < (starting_point_y+self.height):
            r = int((x-starting_point_x)//(self.width/9))
            c = int((y-starting_point_y)//(self.height/9))
            self.select(r,c)
        else:
            self.select_cell = None

    def clear(self):
        '''Clears the value cell. 
        Note that the user can only remove the cell values and 
        sketched values that are filled by themselves.'''    
        if self.selected_cell:
            self.selected_cell.set_cell_value(0)
            self.sketched_value = None
        

    def sketch(self, value):
        '''Sets the sketched value of the current selected cell equal to the user entered value.
	It will be displayed at the top left corner of the cell using the draw() function.'''
        self.sketched_value = value


    def place_number(self):
        '''Sets the value of the current selected cell equal to the user entered value. Called when the user presses the Enter key.'''    
        if self.selected_cell and self.sketched_value:
            self.selected_cell.set_cell_value(int(self.sketched_value))
            self.sketched_value = None

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

    def check_rows(self):
            full_set = {i for i in range(1,self.row_length+1)}
            for r in self.cells:
                com = {c.value for c in r}
                if {c.value for c in r} != full_set:
                    return False
            return True

    def check_board(self):
        '''Check whether the Sudoku board is solved correctly.'''
        return self.check_rows()

    def go_right(self):
        if self.selected_cell:
            r_init, c_init = self.selected_cell.row, self.selected_cell.col
            for r in range(r_init,self.row_length):
                for c in range(0,self.row_length):
                    if r == r_init:
                        if c >= c_init:
                            if self.cells[r][c].editable and self.selected_cell is not self.cells[r][c]:
                                self.select(r,c)
                    else:
                        if self.cells[r][c].editable and self.selected_cell is not self.cells[r][c]:
                            self.select(r,c)
    def go_left(self):
        if self.selected_cell:
            r_init, c_init = self.selected_cell.row, self.selected_cell.col
            for r in range(r_init,0, -1):
                for c in range(self.row_length-1,0,-1):
                    if r == r_init:
                        if c < c_init:
                            if self.cells[r][c].editable and self.selected_cell is not self.cells[r][c]:
                                self.select(r,c)
                    else:
                        if self.cells[r][c].editable and self.selected_cell is not self.cells[r][c]:
                            self.select(r,c)

    def game_animation(self, event):
        if event.type == pygame.quit:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            self.click(x,y)
        if event.type == pygame.KEYDOWN:
            if event.key > 0x10000:
                None
            elif chr(event.key).isdigit():
                char = chr(event.key)
                if char != '0':
                    self.sketch(char)
            elif event.key == pygame.K_RETURN:
                    self.place_number()
                    if self.check_board():
                        return True
            elif event.key == pygame.K_RIGHT or event.key == 100:
                self.go_right()                    
            elif event.key == pygame.K_LEFT or event.key==97:
                self.go_left()
            elif event.key == pygame.K_BACKSPACE:
                self.clear()
     
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode()
    screen.fill((255,255,255))
    board_width = 800
    board_height = 800
    board = Board(board_width,board_height,screen,4)

    while True:
        for event in pygame.event.get():
            board.game_animation(event)
        board.draw()

        pygame.display.update()
