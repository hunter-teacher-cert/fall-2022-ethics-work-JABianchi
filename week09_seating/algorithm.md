** PLAN SEATING ALGORITHM **
-Joel Bianchi

/* Write up a description of the algorithm you will implement for plane_seating.py*/

The main objective of this edit is to allow unpaid blocks of economy tickets to automatically group together if possible.  This took way more code than I expected!

* Rename variables to ```ep``` for "PAID" and ```eu``` for "UNPAID"

* Revise ```fill_plane()``` function to handle ALL of the paid seats first, then process the unpaid seats

* For unpaid seats, iterate through each family, starting from largest to smallest attempting to find a block of seats where they can all sit together

    * Create a ```Block``` class to be able to return a contiguous group of seats, defined by first seat's row & col, and number of seats in the row
    * Write a function ```find_biggest_block()``` that loops through the available seats one row at a time, looking for a block of seats that is the same size as the target block -- return -1 for the row number if no block is found
    * Write a function ```is_available_seat()``` to help out

* For the UNPAID families that were not able to be sat together, loop through the remaining families and place them in the next available seats 