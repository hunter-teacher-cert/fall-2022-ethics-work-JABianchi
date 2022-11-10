# Binary Search (Python Version)
# Joel Bianchi
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

print('Binary Search python program')

# the binSearch function in Python
def bin_search(list, target):
   
    # initial value for the target (if not found)  
    target_position = -1

    #initial values for lo & high
    lo = 0
    hi = len(list)

    
    # Keep looping until search is done
    while lo <= hi:
        
        # Print the current state of the variables
        mid = (lo + hi) // 2 
        print(lo, mid, hi)
        
        # Case 1: the target is found
        if target == list[mid]:
            return mid
        
        # Case 2: the target is above the mid
        elif target > list[mid]:
            lo = mid + 1
            
        # Case 3: the target is below the mid
        elif target < list[mid]:
            hi = mid -1        

    # return if NOT found
    return -1


# generate an ordered list to search through
list = [2,4,6,8,10,12]
target = 10

# print the array
print('We are looking for the target',target,'in the list', list)

# call the binSearch function on list
found_location = bin_search(list, target)
print(target, 'was found at index', found_location)





