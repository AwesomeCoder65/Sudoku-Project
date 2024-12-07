import math
import random
import pygame
import sys
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by
Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""
class SudokuGenerator:
  def __init__(self, row_length, removed_cells):
      self.row_length = row_length
      self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
      self.removed_cells = int(removed_cells)
      self.box_length = int(math.sqrt(row_length))
  '''
  Returns a 2D python list of numbers which represents the board
  Parameters: None
  Return: list[list]
  '''
  def get_board(self):
      return self.board
  '''
  Displays the board to the console
  This is not strictly required, but it may be useful for debugging purposes
  Parameters: None
  Return: None
  '''
  def print_board(self):
      pass
  '''
  Determines if num is contained in the specified row (horizontal) of the board
  If num is already in the specified row, return False. Otherwise, return True
  Parameters:
  row is the index of the row we are checking
  num is the value we are looking for in the row
  Return: boolean
  '''
  def valid_in_row(self, row, num):
      for i in range(9):
          if self.board[row][i] == num:
              return False
      return True
  '''
  Determines if num is contained in the specified column (vertical) of the board
  If num is already in the specified col, return False. Otherwise, return True
  Parameters:
  col is the index of the column we are checking
  num is the value we are looking for in the column
  Return: boolean
  '''
  def valid_in_col(self, col, num):
      for i in range(9):
          if self.board[i][col] == num:
              return False
      return True
  '''
  Determines if num is contained in the 3x3 box specified on the board
  If num is in the specified box starting at (row_start, col_start), return False.
  Otherwise, return True
  Parameters:
  row_start and col_start are the starting indices of the box to check
  i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
  num is the value we are looking for in the box
  Return: boolean
  '''
  def valid_in_box(self, row_start, col_start, num):
      for i in range(row_start, row_start + 3):
          for j in range(col_start, col_start + 3):
              if self.board[i][j] == num:
                  return False
      return True
  '''
  Determines if it is valid to enter num at (row, col) in the board
  This is done by checking that num is unused in the appropriate, row, column, and
  box
  Parameters:
  row and col are the row index and col index of the cell to check in the board
  num is the value to test if it is safe to enter in this cell
  Return: boolean
  '''




  def is_valid(self, row, col, num):
      if self.valid_in_box(row - row % 3, col - col % 3, num) and self.valid_in_row(row, num) and self.valid_in_col(
              col, num):
          return True
      return False
  '''
  Fills the specified 3x3 box with values
  For each position, generates a random digit which has not yet been used in the box
  Parameters:
  row_start and col_start are the starting indices of the box to check
  i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
  Return: None
  '''
  def fill_box(self, row_start, col_start):
      num = random.randint(1, 9)
      for i in range(row_start, row_start + 3):
          for j in range(col_start, col_start + 3):
              while not self.valid_in_box(row_start, col_start, num):
                  num = random.randint(1, 9)
              self.board[i][j] = num
  '''
  Fills the three boxes along the main diagonal of the board
  These are the boxes which start at (0,0), (3,3), and (6,6)
  Parameters: None
  Return: None
  '''
  def fill_diagonal(self):
      for i in range(0, 9, 3):
          self.fill_box(i, i)
  '''
  DO NOT CHANGE
  Provided for students
  Fills the remaining cells of the board
  Should be called after the diagonal boxes have been filled
  Parameters:
  row, col specify the coordinates of the first empty (0) cell
  Return:
  boolean (whether or not we could solve the board)
  '''
  def fill_remaining(self, row, col):
      if (col >= self.row_length and row < self.row_length - 1):
          row += 1
          col = 0
      if row >= self.row_length and col >= self.row_length:
          return True
      if row < self.box_length:
          if col < self.box_length:
              col = self.box_length
      elif row < self.row_length - self.box_length:
          if col == int(row // self.box_length * self.box_length):
              col += self.box_length
      else:
          if col == self.row_length - self.box_length:
              row += 1
              col = 0
              if row >= self.row_length:
                  return True
      for num in range(1, self.row_length + 1):
          if self.is_valid(row, col, num):
              self.board[row][col] = num
              if self.fill_remaining(row, col + 1):
                  return True
              self.board[row][col] = 0
      return False
  '''
  DO NOT CHANGE
  Provided for students
  Constructs a solution by calling fill_diagonal and fill_remaining
  Parameters: None
  Return: None
  '''
  def fill_values(self):
      self.fill_diagonal()
      self.fill_remaining(0, self.box_length)
  '''
  Removes the appropriate number of cells from the board
  This is done by setting some values to 0
  Should be called after the entire solution has been constructed
  i.e. after fill_values has been called
  NOTE: Be careful not to 'remove' the same cell multiple times
  i.e. if a cell is already 0, it cannot be removed again
  Parameters: None
  Return: None
  '''
  def remove_cells(self):
      count = self.removed_cells
      while count > 0:
          row = random.randint(0, 8)
          col = random.randint(0, 8)
          if self.board[row][col] != 0:
              self.board[row][col] = 0
              count -= 1
'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
  print("here")
  sudoku = SudokuGenerator(size, removed)
  sudoku.fill_values()
  board = sudoku.get_board()
  sudoku.remove_cells()
  board = sudoku.get_board()
  return board


class Cell:
   def __init__(self, value, row, col, screen, difficult):
       self.value = value
       self.original = value != 0
       self.difficult = difficult
       self.row = row
       self.col = col
       self.screen = screen
       self.sketched_value = None
       self.selected = False
   def set_cell(self, value):
       if not self.original:
           self.value = value
   def set_sketched_value(self, value):
       if not self.original:
           self.sketched_value = value
   def draw(self):
       cell_x, cell_y = self.col * 50, self.row * 50
       if self.selected:
           pygame.draw.rect(self.screen, "aquamarine", (cell_x, cell_y, 50, 50))
       for x in range(50, 450, 50):
           pygame.draw.line(screen, "purple", (x, 0), (x, 450), width=1)
       for x in range(150, 450, 150):
           pygame.draw.line(screen, "black", (x, 0), (x, 450), width=3)
       for y in range(50, 450, 50):
           pygame.draw.line(screen, "purple", (0, y), (450, y), width=1)
       for y in range(150, 450, 150):
           pygame.draw.line(screen, "black", (0, y), (450, y), width=3)
       font = pygame.font.SysFont('Arial', 36)
       text_surface = font.render(str(self.value), 0, ("lightsalmon3"))
       if self.value > 0:
           self.screen.blit(text_surface, (self.col * 50 + 15, self.row * 50 + 10))
       elif self.sketched_value is not None:
           sketch_font = pygame.font.SysFont('Arial', 20)
           sketch_surface = sketch_font.render(str(self.sketched_value), 0, ("lightsalmon"))
           self.screen.blit(sketch_surface, (cell_x + 5, cell_y + 5))








class Board:
  def __init__(self, width, height, scr, difficulty):
      self.width = width
      self.height = height
      self.screen = scr
      print(difficulty)
      self.board = generate_sudoku(9, difficulty)
      print(self.board)
      self.grid = [[Cell(self.board[row][col], row, col, screen, difficulty) for col in range(9)] for row in
      range(9)]
      self.selected_cell = None
  def draw(self):
      # for i in range(10):
      #     line_width = 4 if i % 3 == 0 else 1
      #     pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (540, i * 60),
      # line_width)
      #     pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, 540),
      # line_width)
      for row in self.grid:
          for cells in row:
              cells.draw()
  def select(self, row, col):
      if self.selected_cell:
          self.selected_cell.selected = False
      self.grid[row][col].selected = True
      self.selected_cell = self.grid[row][col]
  def click(self, x, y):
      if x < self.width and y < self.height:
          row = y // 50
          col = x // 50
          return row, col
      return None
  def clear(self):
      if self.selected_cell and not self.selected_cell.original:
          self.selected_cell.value = 0
          self.selected_cell.sketched_value = None
  def sketch(self, value):
      if self.selected_cell and not self.selected_cell.original:
          self.selected_cell.sketched_value = value
  def place_number(self, value):
      if self.selected_cell and not self.selected_cell.original:
          self.selected_cell.value = value
          self.selected_cell.sketched_value = None
  def reset_to_original(self):
      for row in self.grid:
          for cells in row:
              if not cells.original:
                  cells.value = 0
                  cells.sketched_value = None
  def is_full(self):
      return all(cells.value != 0 for row in self.grid for cells in row)
  def update_board(self):
      return [[cells.value for cells in row] for row in self.grid]
  def find_empty(self):
      for row in range(9):
          for col in range(9):
              if self.grid[row][col].value == 0:
                  return row, col
      return None
  def check_board(self):
      for row in self.grid:
          if len(set(cells.value for cells in row if cells.value != 0)) != len([cells.value for cells in row if cells.value != 0]):
              return False
      return True
def title_card(screen):
  screen.fill("orange")
  title_font = pygame.font.Font(None, 60)
  subtitle_font = pygame.font.Font(None, 50)
  start_screen_button_font = pygame.font.Font(None, 30)
  title_surface = title_font.render("Welcome to Sudoku", 0, "blue")
  title_rect = title_surface.get_rect(
  center=(450 // 2, 600 // 2 - 150))
  screen.blit(title_surface, title_rect)
  subtitle_surface = subtitle_font.render("Select Game Mode:", 0, "blue")
  subtitle_rect = subtitle_surface.get_rect(
  center=(450 // 2, 600 // 2))
  screen.blit(subtitle_surface, subtitle_rect)
  easy_text = start_screen_button_font.render("EASY", 0, "white")
  medium_text = start_screen_button_font.render("MEDIUM", 0, "white")
  hard_text = start_screen_button_font.render("HARD", 0, "white")
  easy_surface = pygame.Surface((easy_text.get_size()[0] + 20,
  easy_text.get_size()[1] + 20))
  easy_surface.fill("blue")
  easy_surface.blit(easy_text, (10,10))
  medium_surface = pygame.Surface((medium_text.get_size()[0] + 20,
  medium_text.get_size()[1] + 20))
  medium_surface.fill("blue")
  medium_surface.blit(medium_text, (10,10))
  hard_surface = pygame.Surface((hard_text.get_size()[0] + 20,
  hard_text.get_size()[1] + 20))
  hard_surface.fill("blue")
  hard_surface.blit(hard_text, (10,10))
  easy_rect = easy_surface.get_rect(
  center=(100, 600 // 2 + 150))
  medium_rect = medium_surface.get_rect(
  center=(225, 600 // 2 + 150))
  hard_rect = hard_surface.get_rect(
  center=(350, 600 // 2 + 150))
  screen.blit(easy_surface, easy_rect)
  screen.blit(medium_surface, medium_rect)
  screen.blit(hard_surface, hard_rect)
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if easy_rect.collidepoint(event.pos):
                  return 30
              elif medium_rect.collidepoint(event.pos):
                  return 40
              elif hard_rect.collidepoint(event.pos):
                  return 50
      pygame.display.update()


def draw_buttons():
   button_font = pygame.font.Font(None, 20)
   reset_text = button_font.render("RESET", 0, "white")
   restart_text = button_font.render("RESTART", 0, "white")
   exit_text = button_font.render("EXIT", 0, "white")
   reset_surface = pygame.Surface((reset_text.get_size()[0] + 20,
                                   reset_text.get_size()[1] + 20))
   reset_surface.fill("blue")
   reset_surface.blit(reset_text, (10, 10))
   restart_surface = pygame.Surface((restart_text.get_size()[0] + 20,
                                     restart_text.get_size()[1] + 20))
   restart_surface.fill("blue")
   restart_surface.blit(restart_text, (10, 10))
   exit_surface = pygame.Surface((exit_text.get_size()[0] + 20,
                                  exit_text.get_size()[1] + 20))
   exit_surface.fill("blue")
   exit_surface.blit(exit_text, (10, 10))
   reset_rect = reset_surface.get_rect(
       center=(100, 600 // 2 + 250))
   restart_rect = restart_surface.get_rect(
       center=(225, 600 // 2 + 250))
   exit_rect = exit_surface.get_rect(
       center=(350, 600 // 2 + 250))
   screen.blit(reset_surface, reset_rect)
   screen.blit(restart_surface, restart_rect)
   screen.blit(exit_surface, exit_rect)
   return [reset_rect, restart_rect, exit_rect]

def sudoku_screen(screen, difficulty):
   screen.fill("light blue")
   board = Board(540, 540, screen, difficulty)
   board.draw()
   sudoku_board = SudokuGenerator(9, difficulty)
   button_rect = draw_buttons()
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               position = pygame.mouse.get_pos()
               selected_cell = board.click(position[0], position[1])
               if selected_cell:
                   board.select(selected_cell[0], selected_cell[1])
               if button_rect[0].collidepoint(event.pos):
                   board.reset_to_original()
               elif button_rect[1].collidepoint(event.pos):
                   sudoku_screen(screen, title_card(screen))
               elif button_rect[2].collidepoint(event.pos):
                   sys.exit()
           elif event.type == pygame.KEYDOWN:
               if board.selected_cell:
                   selected_cell = board.selected_cell
                   if pygame.K_1 <= event.key <= pygame.K_9:
                       value = event.key - pygame.K_0
                       board.sketch(value)
                   elif event.key == pygame.K_RETURN:
                       if value:
                           row = selected_cell.row
                           col = selected_cell.col
                           if sudoku_board.is_valid(row, col, value):
                               board.place_number(value)
                               value = None
                               if board.is_full():
                                   if board.check_board():
                                       game_win_screen(screen)
                                   else:
                                       game_lose_screen(screen)
                           else:
                               game_lose_screen(screen)
                   elif event.key == pygame.K_BACKSPACE:
                       if selected_cell and not selected_cell.original:
                           selected_cell.value = 0
                           selected_cell.sketched_value = None
                           value = None

       screen.fill("light blue")
       board.draw()
       draw_buttons()
       pygame.display.update()
def game_win_screen(screen):
  screen.fill("purple")
  title_font = pygame.font.Font(None, 70)
  end_screen_button_font = pygame.font.Font(None, 40)
  title_surface = title_font.render("YOU WON!", 0, "blue")
  title_rect = title_surface.get_rect(
  center=(450 // 2, 600 // 2 - 150))
  screen.blit(title_surface, title_rect)
  restart_text = end_screen_button_font.render("RESTART", 0, "white")
  restart_surface = pygame.Surface((restart_text.get_size()[0] + 20,
  restart_text.get_size()[1] + 20))
  restart_surface.fill("blue")
  restart_surface.blit(restart_text, (10, 10))
  restart_rect = restart_surface.get_rect(
  center=(225, 600 // 2))
  screen.blit(restart_surface, restart_rect)
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if restart_rect.collidepoint(event.pos):
                  sudoku_screen(screen, title_card(screen))
      pygame.display.update()
def game_lose_screen(screen):
  screen.fill("orange")
  title_font = pygame.font.Font(None, 70)
  end_screen_button_font = pygame.font.Font(None, 40)
  title_surface = title_font.render("YOU LOSE", 0, "blue")
  title_rect = title_surface.get_rect(
  center=(450 // 2, 600 // 2 - 150))
  screen.blit(title_surface, title_rect)
  restart_text = end_screen_button_font.render("RESTART", 0, "white")
  restart_surface = pygame.Surface((restart_text.get_size()[0] + 20,
  restart_text.get_size()[1] + 20))
  restart_surface.fill("blue")
  restart_surface.blit(restart_text, (10, 10))
  restart_rect = restart_surface.get_rect(
  center=(225, 600 // 2))
  screen.blit(restart_surface, restart_rect)
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if restart_rect.collidepoint(event.pos):
                  sudoku_screen(screen, title_card(screen))
      pygame.display.update()
if __name__ == "__main__":
   pygame.init()
   screen = pygame.display.set_mode((450, 600))
   pygame.display.set_caption("Sudoku")
   while True:
       sudoku_screen(screen, title_card(screen))
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()




