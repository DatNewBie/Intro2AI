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
    visited={start: None}

    queue = deque([start]) # create a queue with start node

    while(queue): # loop until get an empty queue
        temp = queue.popleft()

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
            if(matrix[temp][i] != 0 and i not in visited):
                visited[i] = temp 
                queue.append(i)

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
    check = [] # save all the node which we passed it (different from {visited} list)
    stack = deque([start])

    while(stack):
        temp = stack.pop()
        check.append(temp)

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
            if(i not in check and matrix[temp][i] != 0): #if a node not in [check] list, it can be visited anytime
                visited[i] = temp
                stack.append(i)


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
    visited={start: None}
    count = 0 # use count variable to avoid case: weights are equal and the order in heapq is disturbance
    # example: 
        # without count variable:
            # heappush: (1, 5, 9), (1, 2, 5), (1, 4, 6)
            # when we print heapq: (1, 2, 5), (1, 4, 6), (1, 5, 9)  
    heap = [] 
    hq.heappush(heap, (0, count, start, start))
    count = count + 1


    while(len(heap) > 0):
        firstElement = heap[0]
        print(hq.heappop(heap))
        temp = firstElement[2]

        if(temp == end):
            while(temp != start):
                path.append(temp)
                temp = visited[temp]
            path.append(start)
            path = path[::-1]
            return visited, path

        for i in range(len(matrix[temp])):
            if(matrix[temp][i] != 0 and i not in visited):
                visited[i] = temp
                hq.heappush(heap, (matrix[temp][i], count, i, temp))
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

    path=[]
    visited={}
    return visited, path

