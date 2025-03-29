import random
import math

def euclideanDistance(pt1, pt2):
    return math.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
def TDist(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += euclideanDistance(route[i], route[i + 1])
    dist += euclideanDistance(route[-1], route[0])
    return dist





def hillClimbing(loc):
    currRoute = loc[:]
    random.shuffle(currRoute)
    currDistance = TDist(currRoute)
    while True:
        bestNeighbor = None
        bestDistance = currDistance
        for i in range(len(currRoute)):
            for j in range(i + 1, len(currRoute)):
                newRoute = currRoute[:]
                newRoute[i], newRoute[j] = newRoute[j], newRoute[i]
                newDistance = TDist(newRoute)
                if newDistance < bestDistance:
                    bestNeighbor = newRoute
                    bestDistance = newDistance
        if bestNeighbor is None:
            break
        currRoute = bestNeighbor
        currDistance = bestDistance
    return currRoute, currDistance

locations = [(0, 0), (2, 3), (5, 8), (1, 4), (7, 2)]
optRoute, minDist = hillClimbing(locations)
print("THE OPTIMIZED ROUTE IS:", optRoute)
print("TOTAL DISTANCE IS:", minDist)
