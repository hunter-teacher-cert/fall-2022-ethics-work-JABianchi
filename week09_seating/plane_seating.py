# Plane Seating with Families Kept Together
# Author: Joel Bianchi
# Original Code: Mike Z

"""This program simulates the sales of tickets for a specific flight.

A plane is represented by a list. Each element of the list is a row in
the plane (with plane[0] being the front) and reach row is also a
list.

Seats can be purchased as economy_plus or regular economy.

Economy_plus passengers select their seats when they purchase their tickts.
Economy passengers are assigned randomly when the flight is closer to full

create_plane(rows,cols):
  Creates and returns a plane of size rowsxcols
  Planes have windows but no aisles (to keep the simulation simple)

get_number_economy_sold(economy_sold):
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex: {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3
    seats, the Lee family 2

    Returns: the total number of seats sold

get_avail_seats(plane,economy_sold):
    Parameters: plane : a list of lists representing plaine
    economy_sold : a dictionary of the economy seats sold but
                   not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats
           that are "avail" or "win" and removes the number of
           economy_sold seats

get_total_seats(plane):
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane

get_plane_string(plane):
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 

purchase_economy_plus(plane,economy_sold,name):
    Params: plane - a list of lists representing a plane

            economy_sold - a dictionary representing the economy
                           sold but not assigned
            name - the name of the person purchasing the seat

    This routine randomly selects a seat for a person purchasing
    economy_plus. Preference is given to window and front seats.

seat_economy(plane,economy_sold,name):
    Similar to purchase_economy_plus but just randomy assigns
    a random seat.

purchase_economy_block(plane,economy_sold,number,name):
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary


fill_plane(plane):
  takes an empty plane and runs our simulation to sell seats and then
  seat the economy passengers. See comments in the function for details. 

main():
  The main driver program - start here

"""
import random

# global variables for program
max_family_size = 4
pct_paid_seats = 70



def create_plane(rows,cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists. 

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

class Block:
    "This is a class to define a block of seats in a row"

    def __init__(self, r=-1, c=-1, ns=-1):
        self.row = r
        self.col = c
        self.num_seats = ns

    
    def __str__(self):
        return "Starting @ Seat(" + str(self.row) + ", " + str(self.col) + ")" + "-->" + str(self.num_seats) + " total seats"

    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    def get_num_seats(self):
        return self.num_seats


def get_number_eu_sold(eu_sold):
    """
    Input: a dictonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in eu_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane,eu_sold):
    """
    Parameters: plane : a list of lists representing plaine
                eu_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of eu_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_eu_sold(eu_sold)
    return avail

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_ep(plane,eu_sold,name):
    """
    Params: plane - a list of lists representing a plane
            eu_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])

    
    # total unassigned seats
    seats = get_avail_seats(plane,eu_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    
    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


def find_biggest_block(plane, eu_sold, target_seats):
    # check if there is a contiguous block available
        
    # initialize arguments needed for block
    row = -1
    start_seat = 0
    num_seats = target_seats
    
    # define rows & cols of the plane
    rows = len(plane)
    cols = len(plane[0])
    
    # init vars to track during loop
    current_size = 0
    is_block_found = False
    
    # loop through each row
    for r in range(rows):
        
        # reset the contiguous seats for each row tested
        current_size = 0
        
        # loop through each seat in the row
        for c in range(cols):
            
            # check if the seat is available
            if not(is_block_found) and is_avail_seat(plane,r,c):
                
                #increment
                current_size = current_size + 1
                
                #check if reached target
                if(current_size == num_seats):
                    is_block_found = True
                    row = r
                        
            elif not(is_block_found):
                #reset
                current_size = 0
                start_seat = c + 1

    return Block(row, start_seat, num_seats)


def seat_eu_block(plane,eu_sold,name):
    """
    Assigns eu seats after ep seats are sold
    Attempt to keep families together
    """
    
    # determine how many seats looking for
    target_size = eu_sold[name]
    
    # determine maximum number of seats found
    found_block = find_biggest_block(plane, eu_sold, target_size)
    
    #print block
    if(found_block.get_row() != -1):
        print("Block ", end =" ")
        print(found_block, end =" ")
    else:
        print("No block found :(", end = " ")
    print(" for the " + name + " family [" + str(eu_sold[name]) + "]")
    
    # If the block was found (row wasn't -1), then fill it in
    if found_block.get_row() != -1:
        print("----> Found Seats for family!")
        
        # loop through all of the avail seats
        for seat in range(found_block.get_col(), found_block.get_col()+found_block.get_num_seats()):
            
            # print ("looping seat " + str(seat))

            #assign each seat
            plane[found_block.get_row()][seat] = name

            # print(str(r) + "," + str(c))
        
        # delete the key/name from the dictionary
        del eu_sold[name]
    
    return plane

def seat_eu_next(plane,eu_sold,name):
    """
    Assigns eu seats to next available after trying to keep families together
    """

    rows = len(plane)
    cols = len(plane[0])

    # loop through each row
    for r in range(rows):
        
        # loop through each seat in the row
        for c in range(cols):
            
            # check if the seat is available
            if is_avail_seat(plane,r,c):
                
                # assign the seat
                plane[r][c] = name

                # return immediately
                return plane
    
    #if no seats available
    print("No seats available for " + name + "!!!")
    return plane


def is_avail_seat(plane,r,c):
    return plane[r][c] == "win" or plane[r][c] == "avail"


def purchase_eu_block(plane,eu_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_eu_sold(eu_sold)

    if seats_avail >= number:
        eu_sold[name]=number
    return eu_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane
    """

    print("\n ---------- Filling the plane!----------\n")
    
    eu_sold={}
    total_seats = get_total_seats(plane)

    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    eu_number=1

    unprocessed_paid_seats = pct_paid_seats * get_avail_seats(plane, eu_sold) / 100
    unpaid_seats = int(total_seats - unprocessed_paid_seats)
    print("Processing " + str(int(unprocessed_paid_seats)) + " PAID seats out of " + str(total_seats) + " total seats on the plane...\n" )
    
    # PROCESS ALL PAID SEATS FIRST
    while unprocessed_paid_seats > 1.0:
        plane = purchase_ep(plane,eu_sold,"ep-%d"%ep_number) 
        ep_number = ep_number + 1
        unprocessed_paid_seats = unprocessed_paid_seats - 1.0
        
        #print(unprocessed_paid_seats)
    
    # PROCESS ALL UNPAID SEATS IN GROUPS
    
    print("Processing " + str(unpaid_seats) + " UNPAID seats...\n")
    
    # generate an array of blocks of unpaid seats
    available_seats = get_avail_seats(plane,eu_sold)
    
    # random names list
    names = ["Bianchi", "Johnson", "Chen", "Jackson", "Hodge", "Thomas", "Z", "Leimberger", "Jordan", "Diggs"]
    
    # loop process until guaranteed that any block can be accommodated    
    while available_seats >= max_family_size:
    
        # generate a random block sized 1-4
        block_size = 1+random.randrange(max_family_size)
        
        # generate name for block
        block_name = "eu-" + str(eu_number) + "-" + str(names[eu_number-1])
    
        # purchase a block of eu seats
        eu_sold = purchase_eu_block(plane,eu_sold,block_size, block_name)

        # update the number of available seats
        available_seats = get_avail_seats(plane,eu_sold)
    
        # update the family number
        eu_number = eu_number + 1
        # print("new eu block assigned")

    # Iterate the eu_sold dict by largest family to smallest, and assign seats, attempting to keep families together
    for key, value in sorted(eu_sold.items(),
                            key=lambda item: item[1],
                            reverse=True):
        plane = seat_eu_block(plane,eu_sold,key)

    # Iterate again through the families that could not be seated together and assign to next available seats :(
    for name in eu_sold.keys():
        for i in range(eu_sold[name]):
            plane = seat_eu_next(plane,eu_sold,name)

    return plane
    
    
    
def main():
    plane = create_plane(10,5)
    plane = fill_plane(plane)
    print()
    print(get_plane_string(plane))

if __name__=="__main__":
    main()
    
    
    
    
