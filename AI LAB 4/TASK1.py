import heapq
from itertools import permutations



def BFS(maze, start, goal):
    rows =len(maze)
    cols =len(maze[0])
    q = [(HEUR(start, goal), start)]
    came_from = {start: None}


    while q:
        _,current =heapq.heappop(q)
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        



        for a, b in [(-1, 0),  (1, 0), (0,  -1),   (0, 1)]:
            next=(current[0] + a, current[1] + b)


            if (0 <=  next[0] < rows and 0 <= next[1] < cols and maze[next[0]][next[1]] !='#' and next not in came_from):
                heapq.heappush(q,(HEUR(next,goal),next))
                came_from[next] = current
    
    return None



def HEUR(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def GetShortestPath(maze, start, goals):
    spath = None
    slength = float('inf')
    
    for perm in permutations(goals):
        path = [start]
        tpath = []
        
        for goal in perm:
            x = BFS(maze, path[-1], goal)
            if x is None:
                break
            tpath.extend(x[:-1])
            path.append(goal)
        
        tpath.append(path[-1])
        
        if len(tpath) < slength:
            slength = len(tpath)
            spath = tpath
    
    return spath

maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', 'G', '#', '.', '#', '.'],
    ['.', '.', '.', '.', 'G', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.']
]

goals = [(1, 2), (2, 4)]
start = (0, 0)

spath = GetShortestPath(maze, start, goals)
print("THE SHORTEST PATH IS:", spath)
