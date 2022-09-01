# Conway's Game of Life (Python Version)
# Joel Bianchi
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 
# Original Java collaborators: Thea Williams, Ed Hawkins 


# create a new board
rows, cols = (25, 25)
board = []
    board = createNewBoard(25,25);

# setup another board to track the previous generation
    char[][] oldBoard = createNewBoard(board.length, board[0].length);
    
# set the random percentage to populate 
    double pctToPopulate = 0.125;

# Create gens until there are less than 2 changes OR stop after 2
    int numChanges = -1;
    int maxGens = 100;
    
    for(int i=0; i <= maxGens && (numChanges > 2 || numChanges == -1); i++){
      
      # populate the new board for Gen 0
      if(i == 0){
        # breathe life into some cells:
        randomlyPopulateBoard(board, pctToPopulate);
        #  setCell(board, 0, 0, 'X');
        #  setCell(board, 0, 1, 'X');
        #  setCell(board, 1, 0, 'X');

      # Update the board for future Generations
      } else {
        board = generateNextBoard(board);     
      }

      # print out in console
      printGenReport(board, i, pctToPopulate);

      # determine how many changes occured from previous gen
      numChanges = totalChanges(board, oldBoard);
      System.out.println("Number of Changes: " + numChanges);

      # copy the board to oldBoard to analyze the differences later
      oldBoard = copyBoard(board);
    

