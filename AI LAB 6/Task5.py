import itertools

def isValidSudoku(grid):
    def isUnique(lst):
        nums = [num for num in lst if num != 0]
        return len(nums) == len(set(nums))
    for row in grid:
        if not isUnique(row):
            return False
    for col in zip(*grid):
        if not isUnique(col):
            return False
    for boxI in range(3):
        for boxJ in range(3):
            box = [grid[i][j] for i in range(boxI * 3, (boxI + 1) * 3)
                                 for j in range(boxJ * 3, (boxJ + 1) * 3)]
            if not isUnique(box):
                return False
    
    return True






def checkDiagonalSum(grid):
    return sum(grid[i][i] for i in range(9)) % 3 == 0 and sum(grid[i][8 - i] for i in range(9)) % 3 == 0
def noAdjacentPrimes(grid):
    primes = {2, 3, 5, 7}
    for i in range(9):
        for j in range(9):
            if grid[i][j] in primes:
                if i > 0 and grid[i - 1][j] in primes:
                    return False
                if j > 0 and grid[i][j - 1] in primes:
                    return False
                if i < 8 and grid[i + 1][j] in primes:
                    return False
                if j < 8 and grid[i][j + 1] in primes:
                    return False
    return True
def findEmptyCell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None
def solveSudoku(grid):
    if not isValidSudoku(grid) or not checkDiagonalSum(grid) or not noAdjacentPrimes(grid):
        return None
    empty = findEmptyCell(grid)
    if not empty:
        return grid
    i, j = empty
    for num in range(1, 10):
        grid[i][j] = num
        if isValidSudoku(grid) and checkDiagonalSum(grid) and noAdjacentPrimes(grid):
            result = solveSudoku(grid)
            if result:
                return result
        grid[i][j] = 0
    return None





Grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]



for i in range(9):
    for j in range(9):
        if (i + j) % 2 == 0:
            Grid[i][j] = 0
solution = solveSudoku(Grid)
if solution:
    for row in solution:
        print(row)
else:
    print("NO SOLUTION FOUND")
