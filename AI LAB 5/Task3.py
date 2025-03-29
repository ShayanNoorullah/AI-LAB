import numpy as np
import random
from math import sqrt

numCities = 10
cityLocations = np.random.rand(numCities, 2) * 100
print("CITY LOCATIONS:")
for idx, (xCoord, yCoord) in enumerate(cityLocations):
    print(f"CITY {idx+1}: ({xCoord:5.1f}, {yCoord:5.1f})")

distanceGrid = np.zeros((numCities, numCities))
for i in range(numCities):
    for j in range(numCities):
        deltaX = cityLocations[i, 0] - cityLocations[j, 0]
        deltaY = cityLocations[i, 1] - cityLocations[j, 1]
        distanceGrid[i, j] = sqrt(deltaX**2 + deltaY**2)




def generateRandomRoute():
    return random.sample(range(numCities), numCities)
def computePathLength(path):
    total = 0.0
    for pos in range(len(path)):
        currentCity = path[pos]
        nextCity = path[(pos + 1) % len(path)]
        total += distanceGrid[currentCity, nextCity]
    return total




def evaluateFitness(path):
    return 1 / computePathLength(path)
def selectParents(population, fitnessScores, tournamentPool=3):
    chosen = []
    for _ in range(len(population)):
        candidates = random.sample(list(zip(population, fitnessScores)), tournamentPool)
        winner = max(candidates, key=lambda x: x[1])
        chosen.append(winner[0])
    return chosen




def combineRoutes(parentA, parentB):
    routeLength = len(parentA)
    startIdx, endIdx = sorted(random.sample(range(routeLength), 2))
    newRoute = [None] * routeLength
    newRoute[startIdx:endIdx+1] = parentA[startIdx:endIdx+1]
    remainingCities = [city for city in parentB if city not in newRoute[startIdx:endIdx+1]]
    fillPosition = 0
    for i in range(routeLength):
        if newRoute[i] is None:
            newRoute[i] = remainingCities[fillPosition]
            fillPosition += 1
    return newRoute
def applyMutation(path, mutationChance=0.02):
    if random.random() < mutationChance:
        swapA, swapB = random.sample(range(len(path)), 2)
        path[swapA], path[swapB] = path[swapB], path[swapA]
    return path

populationCount = 100
totalGenerations = 200
mutationProbability = 0.02
topRoutesToKeep = 5

currentPopulation = [generateRandomRoute() for _ in range(populationCount)]

print("ROUTE OPTIMIZATION INITIALIZATION:")
print(f"ROUTES CREATED: {populationCount}")
print(f"GENERATIONS: {totalGenerations}")
print(f"MUTATION RATE: {mutationProbability*100}%")

for generation in range(totalGenerations):
    pathLengths = [computePathLength(route) for route in currentPopulation]
    fitnessValues = [evaluateFitness(route) for route in currentPopulation]
    
    shortestPath = min(pathLengths)
    averagePath = np.mean(pathLengths)
    
    if generation % 20 == 0 or generation == totalGenerations-1:
        print(f"GENERATION {generation:4}: SHORTEST {shortestPath:7.1f} Average {averagePath:7.1f}")

    eliteRoutes = sorted(currentPopulation, key=lambda x: computePathLength(x))[:topRoutesToKeep]
    
    parentPool = selectParents(currentPopulation, fitnessValues)
    
    newGeneration = []
    for i in range(0, len(parentPool), 2):
        if i + 1 >= len(parentPool):
            break
        firstParent, secondParent = parentPool[i], parentPool[i+1]
        firstChild = combineRoutes(firstParent, secondParent)
        secondChild = combineRoutes(secondParent, firstParent)
        newGeneration.extend([firstChild, secondChild])
    
    mutatedGeneration = [applyMutation(route, mutationProbability) for route in newGeneration]
    
    currentPopulation = eliteRoutes + mutatedGeneration
    currentPopulation = currentPopulation[:populationCount]

bestSolution = min(currentPopulation, key=lambda x: computePathLength(x))
finalDistance = computePathLength(bestSolution)

print("\nOPTIMAL ROUTE:")
routeString = " → ".join(f"CITY {city+1}" for city in bestSolution)
print(f"{routeString} → City {bestSolution[0]+1}")
print(f"\nTOTAL DISTANCE TRAVELLED: {finalDistance:.1f}")