# Conway's Game of Life (Python Version)
# Joel Bianchi
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 
# Original Java collaborators: Thea Williams, Ed Hawkins 

import random
import time

# Grid Constants
ROWS = 15
COLUMNS = 45
FRAME_RATE = 0.100
IS_ANIMATING = True

# set the random percentage to populate 
PCT_TO_POPULATE = 0.16
MAX_GENS = 100

# Unicode Symbols
# Other unicode symbols: https://unicode-table.com/en/blocks/geometric-shapes/
# ALIVE = 'O'
# ALIVE = '■'
ALIVE = "\u25C9"
DEAD = ' '

# Color declarations to help with printing in color
# https://www.geeksforgeeks.org/how-to-print-colored-text-in-java-console/
ANSI_RESET = "\u001B[0m"
ANSI_GREEN_BG = "\u001B[42m"
ANSI_YELLOW_BG = "\u001B[43m"
ANSI_RED_TEXT = "\u001B[31m"
ANSI_BLACK_TEXT = "\u001B[30m"
ANSI_GREEN_TEXT = "\u001B[32m"
ANSI_BLUE_BG = "\u001B[44m"
ANSI_WHITE_TEXT = "\u001B[37m"
ANSI_BLUE_TEXT = "\u001B[34m"

# HEADER = '\033[95m'
# OKBLUE = '\033[94m'
# OKCYAN = '\033[96m'
# OKGREEN = '\033[92m'
# WARNING = '\033[93m'
# FAIL = '\033[91m'
# ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

DEAD_COLOR = ANSI_BLUE_BG;
ALIVE_COLOR = ANSI_GREEN_BG;  

# Animation Constants
CLEAR_SCREEN =  "\033[2J"
TO_TOP_OF_SCREEN = "\033[1;1H"
HIDE_CURSOR = "\033[?25l"


# function to set a cell (r,c) to val
def set_cell(board, r: int, c: int, val: str):
      board[r][c] = val


# function to randomly populate the board
def randomly_populate_board(board, pct):
      # traverse board
      rows = len(board)
      cols = len(board[0])
      for r in range(rows):
            for c in range(cols):
                  # Each cell has a random chance of living if over the 'pct' threshhold
                  if random.random() < pct:
                        set_cell(board, r, c, ALIVE)
                        
                        
# function that returns number of living neigbours of board[r][c]
def count_neighbours( board, row: int, col: int ):
  
  count = 0
  
  # determine the indices for the 4 main directions
  up = row - 1
  down = row + 1
  right = col + 1
  left = col - 1

  # loop through a 3x3 box surrounding the desired cell
  for r in range(up, down+1):
    for c in range(left, right+1):
      # check if r and c are in bounds
      if r>=0 and r<len(board) and c>=0 and c<len(board[r]):
            
        # also check that you don't count the middle cell
        if r != row or c != col:
                  
          # finally, check if the cell is living
          if board[r][c] == ALIVE:
                        
            # increment the count if a neighbour is alive
            count +=1
            
  return count


# function to return next generation cell state based on CGOL rules
def get_next_gen_cell( board, r: int, c: int ):
      
      # initialize cell's char as dead by default
      next_gen_cell_status = DEAD
      
      # check if the earlier cell was living
      isLiving = False
      if board[r][c] == ALIVE:
            isLiving = True
      # check for number of living neighbours
      num_living_neighbours = count_neighbours(board,r,c)
    
      #CASE 1: LIVING --> LIVING
      if isLiving and (num_living_neighbours == 2 or num_living_neighbours == 3):
            # cell keeps living
            next_gen_cell_status = ALIVE
      
      # CASE 2: DEAD --> BIRTH
      elif num_living_neighbours == 3:
            next_gen_cell_status = ALIVE
      
      # CASE 3: --> DEAD
      # No need to write code for this since all other cases are dead by default

      # return the char
      return next_gen_cell_status
                       
                        
# function to generate and return a new board representing next generation
def generate_next_board( board ):
      
    rows, cols = (len(board), len(board[0]))
    new_board = [[0 for i in range(cols)] for j in range(rows)]
    
    # loop through all the cells in the board
    for r in range(rows):
      for c in range(cols):
            # assign the correct char to each cell
            board[r][c] = get_next_gen_cell(board, r, c)
    return board;


# function to print the board to the terminal
def print_board(board):
 
  # traverse 2D array
  for r in range(len(board)):
    for c in range(len(board[r])):
      
      # print out cell's char
      cell = board[r][c]
      
      print(str(cell),end=" ")

    # go to a new line for each row
    print("")
    
  # Code to reset the printout color
  print(ANSI_RESET)


# function to count living cells of a generation
def get_total_living_cells(board):

  # setup counter
  count = 0
  
  # use for each loops to traverse the board
  for r in range(len(board)):
    for c in range(len(board[r])):
      
      # count if living cell found
      cell = board[r][c]
      if(cell == ALIVE):
        count += 1 
    
  return count


# function to print report of a single generation
def print_gen_report(board, gen_num: int, pct_to_populate: float):

  # start the cursor at the top of the screen again
  print(TO_TOP_OF_SCREEN, end="")  
  print()
  print(ANSI_RESET,ANSI_BLACK_TEXT, ANSI_YELLOW_BG, BOLD)
  print("------------------------------------")
  print("Gen X+",  gen_num, ": \tSeed Pct: ", pct_to_populate)
  print("------------------------------------")
  print(ANSI_RESET, ANSI_GREEN_TEXT, ANSI_BLUE_BG)
  print_board(board)
  print(ANSI_RESET, ANSI_WHITE_TEXT, end="")
  print("------------------------------------")
  
  total = len(board) * len(board[0])
  living = get_total_living_cells(board)
  pct_living = float(living) / total * 100
  pct_living_round = round(pct_living,1)

  print("Total Living Cells: ", living )
  print("Total Cells: ", total)
  print("Percentage of Cells living: ", pct_living_round, '%')
  

# function that creates and returns a new 2D array of char the same size as
# original and copies all the elements
def copy_board(original):
  
  # create an array that's the same size as the original
  rows, cols = (len(original), len(original[0]))
  old_board = [[0 for i in range(cols)] for j in range(rows)]

  # copy all the elements over from original to the new "old" array
  for r in range(rows):
    for c in range(cols):
      old_board[r][c] = original[r][c]

  # return the new array
  # print("Original", original)
  # print("Old Board",old_board)
  return old_board


# function to track changes between generations
def total_changes(board, old_board):
  changes = 0
  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] != old_board[r][c]:
            changes += 1
  return changes




## MAIN CODE
# create a new board
board = [[0 for i in range(COLUMNS)] for j in range(ROWS)]

# setup another board to track the previous generation
old_board = [[0 for i in range(COLUMNS)] for j in range(ROWS)]


# Create gens until there are less than 2 changes OR stop after 2
num_changes = -1

# clear screen before printing out animation
if IS_ANIMATING:
  print(CLEAR_SCREEN, HIDE_CURSOR, end="")


i = 0
while i <= MAX_GENS and (num_changes > 2 or num_changes == -1):
  
  # populate the new board for Gen 0
  if i == 0:
        
    # breathe life into some cells:
    randomly_populate_board(board, PCT_TO_POPULATE)
    time.sleep(1)

    # set_cell(board, 0, 1, ALIVE)
    # set_cell(board, 0, 1, ALIVE)
    # set_cell(board, 1, 0, ALIVE)

  # Update the board for future Generations
  else:
    board = generate_next_board(board)
  
  # print out in console
  print_gen_report(board, i, PCT_TO_POPULATE)

  # determine how many changes occured from previous gen
  num_changes = total_changes(board, old_board)
  print("Number of Changes: ", num_changes)
  
  if IS_ANIMATING:
    # pause the screen for a certain amount of milliseconds
    time.sleep(FRAME_RATE);
    
    # cleanup glitch from initial frame
    if i==0:
      print(CLEAR_SCREEN)
      
  # copy the board to oldBoard to analyze the differences later
  old_board = copy_board(board)
  
  # increment the generation
  i += 1
    

