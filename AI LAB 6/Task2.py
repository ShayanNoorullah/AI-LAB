from collections import deque

def bfsLargestLandmass(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    largestLandmass = [[0 for _ in range(cols)] for _ in range(rows)]
    

    
    def bfs(start_i, start_j):
        queue = deque([(start_i, start_j)])
        landmass = []
        visited[start_i][start_j] = True
        while queue:
            i, j = queue.popleft()
            landmass.append((i, j))
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
        return landmass
    maxLandmass = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                landmass = bfs(i, j)
                if len(landmass) > len(maxLandmass):
                    maxLandmass = landmass
    for i, j in maxLandmass:
        largestLandmass[i][j] = 1
    return largestLandmass



def computePerimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter






grid = [
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

largestLandmass = bfsLargestLandmass(grid)
print("LARGEST LANDMARK:")
for row in largestLandmass:
    print(row)
    
perimeter = computePerimeter(largestLandmass)
print("PERIMETER:", perimeter)
