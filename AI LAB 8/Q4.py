import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
transitionMatrix = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

stateIndex = {'Sunny': 0, 'Cloudy': 1, 'Rainy': 2}
initialState = 'Sunny'
numDays = 10
numSimulations = 10000
countAtLeast3Rainy = 0

for _ in range(numSimulations):
    currentState = stateIndex[initialState]
    rainyDays = 0
    for _ in range(numDays):
        nextState = np.random.choice([0, 1, 2], p=transitionMatrix[currentState])
        if nextState == stateIndex['Rainy']:
            rainyDays += 1
        currentState = nextState
    if rainyDays >= 3:
        countAtLeast3Rainy += 1

probability = countAtLeast3Rainy / numSimulations
print(probability)
