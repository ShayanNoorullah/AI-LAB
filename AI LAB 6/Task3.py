from itertools import permutations
import random

def generateDistanceMatrix(n):
    return [[0 if i == j else random.randint(10, 100) for j in range(n)] for i in range(n)]
def calculateRouteCost(route, distances):
    cost = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    return cost + distances[route[-1]][route[0]]




def tspSolver(numCities):
    cities = list(range(numCities))
    distances = generateDistanceMatrix(numCities)
    bestRoute, minCost = None, float('inf')
    
    for perm in permutations(cities):
        cost = calculateRouteCost(perm, distances)
        if cost < minCost:
            minCost, bestRoute = cost, perm
    
    return bestRoute, minCost




numCities = 10
bestRoute, minCost = tspSolver(numCities)
print(f"THE EBST ROUTE IS: {bestRoute}")
print(f"THE MINIMUM COST IS: {minCost}")
