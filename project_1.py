import sys
from heapq import heappush, heappop                                 #for Uniform-Cost Search


def load_world(filename):

    with open(filename, 'r') as file:                               #open file for reading
        columns = int(file.readline())                              #read the first line to get number of columns
        rows = int(file.readline())                                 #read the second line to get number of rows
    
        map = []                                                    #initialize an empty grid list
        
        for symbol in range(rows):                                  #iterates over each row
            line = file.readline()                                  #reads each line
            stripped_line = line.strip()                            #removes white spaces
            line_list = list(stripped_line)                         #turns stripped line into a list
            map.append(line_list)                                   #appends list to grid
            
        start = None                                                #sets 'start' as None
        dirty_set = set()                                           #sets 'dirty' as an empty set
        
        for row in range(rows):                                     #iterates over rows
            for column in range(columns):                           #iterates over columns
                if map[row][column] == '@':                         #determines starting point
                    start = (row, column)                           #sets starting point to that location
                elif map[row][column] == '*':                       #determines which cells are dirty
                    dirty_set.add((row, column))                    #adds dirty location to dirty set

    return map, start, dirty_set


def find_goal(state):
    clean = False                                                   #set clean to False
    position, dirty_set = state                                     #pull dirty_set from current state
    if len(dirty_set) == 0:                                         #if dirty_set is empty
        clean = True                                                #set clean to True
        return clean                                                #return clean
    else:                                                           #if dirty_set not empty, return clean as False
        return clean                                            


def successors(state, grid):
    # Unpack robot position and dirty set from the state
    # Initialize an empty list for successor states
    # Define possible movement directions (N, S, E, W) with their row and column changes
    # For each direction:
        # Calculate the new row and column
        # Check if the move stays inside grid boundaries and isn't blocked
        # If valid:
            # Add new state (new robot position, same dirty set) with the action (N/S/E/W)
    # If the robot is on a dirty tile:
        # Create a new dirty set without that tile
        # Add a new state with the 'V' (vacuum) action
    # Return the list of (action, new state) pairs
    pass


def depth_first_search(start_state, grid):
    # Create a stack to hold (state, path to state)
    # Create a visited set
    # Initialize nodes generated and nodes expanded counters
    # While the stack is not empty:
        # Pop the top (state, path) from the stack
        # If state is already visited, continue
        # Mark the state as visited
        # Increment nodes expanded
        # If state is a goal state:
            # Return path, nodes generated, nodes expanded
        # For each successor:
            # Push the successor state and updated path onto the stack
            # Increment nodes generated
    # If no solution found, return failure
    pass


def uniform_cost_search(start_state, grid):
    # Create a priority queue to hold (cost, state, path)
    # Create a visited dictionary to track best cost to each state
    # Initialize nodes generated and nodes expanded counters
    # While the queue is not empty:
        # Pop the (lowest cost) state from the queue
        # If state is already visited with a lower or equal cost, continue
        # Mark or update the cost in visited
        # Increment nodes expanded
        # If state is a goal state:
            # Return path, nodes generated, nodes expanded
        # For each successor:
            # Calculate new cost (current cost + 1)
            # Push (new cost, successor state, updated path) onto the queue
            # Increment nodes generated
    # If no solution found, return failure 
    pass