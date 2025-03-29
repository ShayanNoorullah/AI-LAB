import itertools
import random

class WarehouseCSP:
    def __init__(self, gridSize=6, numRobots=5, numPackages=10):
        self.gridSize = gridSize
        self.numRobots = numRobots
        self.numPackages = numPackages
        self.robotPositions = {r: (random.randint(0, gridSize-1), random.randint(0, gridSize-1)) for r in range(numRobots)}
        self.packagePositions = {p: (random.randint(0, gridSize-1), random.randint(0, gridSize-1)) for p in range(numPackages)}
        self.robotCapacities = {r: 5 for r in range(numRobots)}
        self.robotBatteries = {r: 100 for r in range(numRobots)}
        self.solution = []




    def isValidMove(self, x, y):
        return 0 <= x < self.gridSize and 0 <= y < self.gridSize
    def moveRobot(self, robot, dx, dy):
        x, y = self.robotPositions[robot]
        newX, newY = x + dx, y + dy
        if self.isValidMove(newX, newY):
            self.robotPositions[robot] = (newX, newY)
            self.robotBatteries[robot] -= 1
            return True
        return False
    def assignPackages(self):
        assignments = {}
        for p, (px, py) in self.packagePositions.items():
            closestRobot = min(self.robotPositions.keys(), key=lambda r: abs(px - self.robotPositions[r][0]) + abs(py - self.robotPositions[r][1]))
            assignments[p] = closestRobot
        return assignments





    def solve(self):
        packageAssignments = self.assignPackages()
        for package, robot in packageAssignments.items():
            px, py = self.packagePositions[package]
            while self.robotPositions[robot] != (px, py):
                rx, ry = self.robotPositions[robot]
                if rx < px:
                    self.moveRobot(robot, 1, 0)
                elif rx > px:
                    self.moveRobot(robot, -1, 0)
                elif ry < py:
                    self.moveRobot(robot, 0, 1)
                elif ry > py:
                    self.moveRobot(robot, 0, -1)
                self.solution.append((robot, self.robotPositions[robot]))
        
        for robot, pos in self.robotPositions.items():
            print(f'ROBOT{robot}-FIANLPOS: {pos}')
        print("THE SOLUTION PATH IS:", self.solution)

if __name__ == "__main__":
    warehouseCSP = WarehouseCSP()
    warehouseCSP.solve()
