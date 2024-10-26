from collections import deque
import numpy as np
import heapq as hq


def BFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """

    # TODO: 
   
    path=[]
    visited={}
    from_node = {start: None}
    queue = deque([start]) # create a queue with start node

    while(queue): # loop until get an empty queue
        temp = queue.popleft()
        if(temp in visited):
            continue
        visited[temp] = from_node[temp] 

        if(temp == end): # get end node
            while(temp != start): 
                path.append(temp)
                temp = visited[temp]
            path.append(start)
            path = path[::-1]
            return visited, path
        """ loop from size - 1 to 0 because prioritize right branch traversal
         when weights are equal or weights are not important. """
        for i in range(len(matrix[temp]) - 1, -1, -1):
            if(matrix[temp][i] != 0 and i not in from_node):
                queue.append(i)
                from_node[i] = temp

    return visited, []

def DFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
    stack = deque([start])
    from_node = {start: None}

    while(stack): 
        temp = stack.pop()
        if(temp in visited):
            continue
        visited[temp] = from_node[temp]

        if(temp == end):
            while(temp != start):
                path.append(temp)
                temp = visited[temp]
            path.append(start)
            path = path[::-1]
            return visited, path
        """ loop from size - 1 to 0 because prioritize right branch traversal 
         when weights are equal or weights are not important. """
        for i in range(len(matrix[temp])):
            # if a node haven't been visited, then they can be added to stack although they can be added to stack before
            # and we must update in from_node
            if(matrix[temp][i] != 0 and i not in visited): 
                stack.append(i)
                from_node[i] = temp


    return visited, []
        



def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited={}
    count = 0 # use count variable to avoid case: weights are equal and the order in heapq is disturbance
    # example: 
        # without count variable:
            # heappush: (1, 5, 9), (1, 2, 5), (1, 4, 6)
            # when we print heapq: (1, 2, 5), (1, 4, 6), (1, 5, 9)  
    heap = [] 
    hq.heappush(heap, (0, count, start, None)) # heap(g, count, current node, previous node)
    count = count + 1
    
    cost_from_start = {start: 0} # store the cost 

    while(len(heap) > 0):
        firstElement = hq.heappop(heap)
        temp = firstElement[2] # current node
        if(temp in visited):
            continue
        visited[temp] = firstElement[3] # visited[current node] = previous node

        if(temp == end):
            while(temp != start):
                path.append(temp)
                temp = visited[temp]
            path.append(start)
            path = path[::-1]
            return visited, path

        for i in range(len(matrix[temp])):
            if(matrix[temp][i] != 0):
                if(i in visited):
                    continue
                g = firstElement[0] + matrix[temp][i] # calculate g: g = g of previous node + distance from previous node to current node
                # add g if not exist or update if have another way optimize distance get to node
                if(i not in cost_from_start or g < cost_from_start[i]):
                    cost_from_start[i] = g
                    hq.heappush(heap, (g, count, i, temp))
                    count = count + 1



    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm 
    heuristic : edge weights
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}

    heap = []
    count = 0
    # use count variable to avoid case: weights are equal and the order in heapq is disturbance
    # example: 
        # without count variable:
            # heappush: (1, 5, 9), (1, 2, 5), (1, 4, 6)
            # when we print heapq: (1, 2, 5), (1, 4, 6), (1, 5, 9)  
    
    hq.heappush(heap, (0, count, start, None)) # heap(heuristic, count, current node, previous node)
    count+=1

    heuristic = {end: 0} 

    # calculate heuristic except end
    # example: if matrix[0][1] = 2 (1 != end), that mean heuristic 1 to end equal to 2
    # if matrix[0][1] = 2 and matrix[2][1] = 1 then we choose the lower, that mean heuristic 1 to end equal to 1 
    for i in range(len(matrix)):
        if(i == end):
            continue
        heuristic[i] = matrix[0][i]
        for j in range(len(matrix[i])):
            if(matrix[j][i] != 0):
                if(matrix[j][i] < heuristic[i] or heuristic[i] == 0):
                    heuristic[i] = matrix[j][i]

    while(heap):
        firstElement = hq.heappop(heap)
        temp = firstElement[2]
        if(temp in visited):
            continue
        visited[temp] = firstElement[3]

        if(temp == end):
            while(temp != start):
                path.append(temp)
                temp = visited[temp]
            path.append(start)
            path = path[::-1]
            return visited, path
        
        for i in range(len(matrix[temp])):
            if(matrix[temp][i] != 0 and i not in visited):
                hq.heappush(heap, (heuristic[i], count, i, temp))
                count+=1
        


    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
    heuristic: eclid distance based positions parameter
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 

    def  eclidean_distance(current, goal):
        x1, y1 = pos[current]
        x2, y2 = pos[goal]
        h = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return h
    

    path=[]
    visited={}
    count = 0 # use count variable to avoid case: weights are equal and the order in heapq is disturbance
    # example: 
        # without count variable:
            # heappush: (1, 5, 9), (1, 2, 5), (1, 4, 6)
            # when we print heapq: (1, 2, 5), (1, 4, 6), (1, 5, 9)  
    heap = [] 
    cost_from_start = {start: 0}
    g = 0
    hq.heappush(heap, (0 + eclidean_distance(start, end), count, start, None, g)) #heap(f = h + g, count, current node, previous node, g)
    count = count + 1

    while(len(heap) > 0):
        firstElement = hq.heappop(heap)
        temp = firstElement[2] #current node
        if(temp in visited):
            continue
        visited[temp] = firstElement[3] #visited[current node] = previous node

        if(temp == end):
            while(temp != start):
                path.append(temp)
                temp = visited[temp]
            path.append(start)
            path = path[::-1]
            return visited, path

        for i in range(len(matrix[temp])):  
            if(matrix[temp][i] != 0):
                g = firstElement[4] + matrix[temp][i]
                
                if(i not in cost_from_start or g < cost_from_start[i]):
                    cost_from_start[i] = g
                    hq.heappush(heap, (g + eclidean_distance(i, end), count, i, temp, g))
                    count = count + 1


    return visited, path

