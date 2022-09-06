# Game of Nim (Python Version)
# Joel Bianchi
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 
# original Java collaborators: Joshua Higgins, Moo Joon Park, Marieke Thomas, Rachel Kaufman

import random

print('Game of Nim starting!')

#define initial variables for the game
OPPONENTS = ["Josh", "Marieke", "Rachel", "Moo Joon", "Joel"]
stones = 12
player_first = True
player_turn = True
opp_index = int(random.random() * len(OPPONENTS));
user_response = ''

# determine if player or cpu goes first
user_response = input('Would you like to go first? [Y/N]').lower()
if user_response == 'n':
    playerFirst = False
    

# loop until game ends
while stones > 0:
    
    # prompt user input (user turn)
    stones_taken = int(input('How many stones would you like to take?'))
    
    # calculate numbers of stone remaining
    stones -= stones_taken;
    print('Number of stones remaining: ',stones);
    
    # check for win
    if stones <= 0:
        print('You win!')
        break
     
    # machine's turn
    # if 3 or fewer, take all the remaining stones
    if stones <=3:
        stones_taken = stones
    else:
        stones_taken = int((random.random() * 3) + 1)        

    print('Computer takes ', stones_taken, ' stones')
    
    # calculate numbers of stone remaining
    stones -= stones_taken
    print('Number of stones remaining: ', stones)
    
    # check win
    if stones <= 0:
        print('You lose!')
        break


print('Game over!')
