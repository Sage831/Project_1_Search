import sys
import heapq                                                        #for Uniform-Cost Search


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

    return map, start, dirty_set                                    #returns map, start, and dirty_set


def find_goal(state):
    
    clean = False                                                   #set clean to False
    position, dirty_set = state                                     #pull dirty_set from current state
    
    if len(dirty_set) == 0:                                         #if dirty_set is empty
        clean = True                                                #set clean to True
        return clean                                                #return clean
    else:                                                           #if dirty_set not empty, return clean as False
        return clean                                            


def successors(state, map):
    
    position, dirty_set = state                                     #unpacks robot position and dirty set from the state
    successor_states = []                                           #initializes empty list for successor states
    
    directions = {                                                  #dictionary with movement choices
                   'N': (-1, 0),                                    #up movement
                   'S': (1 ,0),                                     #down movement
                   'E': (0, 1),                                     #right movement
                   'W':(0, -1)                                      #left movement
                                 }

    rows = len(map)                                                 #determines number of rows
    columns = len(map[0])                                           #determines number of columns
    row, column = position                                          #determines robot position

    for action, (change_row, change_column) in directions.items():                                          #iterate over directions
        new_row = row + change_row                                                                          #change row
        new_column = column + change_column                                                                 #change column
        if (0 <= new_row < rows) and (0 <= new_column < columns) and map[new_row][new_column] != '#':       #makes sure position is within boundaries
            new_state = ((new_row, new_column), dirty_set.copy())                                           #creates new state with copy of dirty_set
            successor_states.append((action, new_state))
    
    if position in dirty_set:                                       #check if position is in dirty_set
        dirty_set_copy = dirty_set.copy()                           #makes a copy of dirty_set
        dirty_set_copy.remove(position)                             #remove position from dirty_set
        new_state = (position, dirty_set_copy)                      #create a new state with altered dirty_set
        successor_states.append(('V',new_state))                    #append state to successor_states with 'V' (vacuum) action
    
    return successor_states


def depth_first_search(start_state, map):

    stack = [(start_state, [])]                                     #initialize a stack with a starting state and empty path
    visited = set()                                                 #initialize empty visited set 
    nodes_generated = 0                                             #initialize nodes_generated counter
    nodes_expanded = 0                                              #initialize nodes_expanded counter

    while stack:                                                    #loop for when stack is not empty
        state, path = stack.pop()                                   #pop top state and its path from stack
        position, dirty_set = state                                 #capture position and dirty_set from popped state
        visited_state = (position, tuple(sorted(dirty_set)))        #store position and dirty_set (as a sorted tuple) in visited_state
        
        if visited_state in visited:                                #check if state has already been visited
            continue                                                #if visited, move on to next state

        visited.add(visited_state)                                  #if not visited, mark state as visited
        nodes_expanded += 1                                         #increment nodes_expanded counter

        if find_goal(state):                                        #if dirty_set is empty, return the path, nodes generated, and nodes expanded
            return path, nodes_generated, nodes_expanded 

        for action, successor in successors(state, map):            #iterate through successors
            stack.append((successor, path + [action]))              #push successor and new path onto the stack
            nodes_generated += 1                                    #increment nodes_generated counter

    return None, nodes_generated, nodes_expanded                    #if no solution, return path, nodes_generated, and nodes_expanded
   


def uniform_cost_search(start_state, map):

    pq = [(0, start_state, [])]                                     #initialize a priority queue for cost, state, and path
    visited = {}                                                    #initialize empty visited dictionary
    nodes_generated = 0                                             #initialize nodes_generated counter
    nodes_expanded = 0                                              #initialize nodes_expanded counter

    while pq:                                                       #loop for when queue is not empty
        cost, state, path = heapq.heappop(pq)                             #pop state at front of pq (lowest-cost state)
        position, dirty_set = state                                 #capture position and dirty_set from popped state
        visited_state = (position, tuple(sorted(dirty_set)))        #store position and dirty_set (as a sorted tuple) in visited_state

        if visited_state in visited and visited[visited_state] <= cost:         #skip state if already visited with a lower cost
            continue

        visited[visited_state] = cost                                #if visited with a lower cost, update cost to new lowest cost
        nodes_expanded += 1

        if find_goal(state):                                         #if dirty_set empty, return path, nodes_generated, nodes_expanded
            return path, nodes_generated, nodes_expanded             

        for action, successor in successors(state, map):                        #iterate through successors
            new_cost = cost + 1                                                 #increment cost to find new cost
            heapq.heappush(pq, (new_cost, successor, path + [action]))          #push new cost, successor, and path into priority queue
            nodes_generated += 1                                                #increment nodes_generated counter

    return None, nodes_generated, nodes_expanded                     #if no solution, return path, nodes_generated, and nodes_expanded
