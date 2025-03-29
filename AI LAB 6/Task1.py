import heapq
import math

def isValid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0
def getNeighbors(x, y):
    return [(x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)





def findShortestPath(grid, start, target):
    pq = []
    heapq.heappush(pq, (0, start))
    cameFrom = {start: None}
    costSoFar = {start: 0}
    
    while pq:
        currentCost, current = heapq.heappop(pq)
        if current == target:
            path = []
            while current:
                path.append(current)
                current = cameFrom[current]
            return path[::-1]
        
        for neighbor in getNeighbors(*current):
            if isValid(grid, *neighbor):
                newCost = costSoFar[current] + math.sqrt(2)
                if neighbor not in costSoFar or newCost < costSoFar[neighbor]:
                    costSoFar[neighbor] = newCost
                    priority = newCost + heuristic(neighbor, target)
                    heapq.heappush(pq, (priority, neighbor))
                    cameFrom[neighbor] = current
    
    return None





grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
start = (0, 0)
target = (3, 3)
path = findShortestPath(grid, start, target)
print("THE SHORTEST PATH IS:", path)
