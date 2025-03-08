import heapq
import random

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def AStar(graph,start,goal,traffic_updates):
    open = []
    heapq.heappush(open, (0, start))

    came_from = {}

    gScore = {node: float('inf') for node in graph}
    gScore[start] = 0
    fScore={node: float('inf') for node in graph}
    fScore[start]=heuristic(start, goal)
    


    while open:
        _, current = heapq.heappop(open)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph[current]:
            updweight = round(graph[current][neighbor] * traffic_updates.get((current, neighbor), 1),3)

            Tgscore = gScore[current] + updweight
            if Tgscore < gScore[neighbor]:

                came_from[neighbor] = current
                gScore[neighbor]=round(Tgscore,3)
                fScore[neighbor]=gScore[neighbor] + round(heuristic(neighbor, goal),3)
                heapq.heappush(open, (round(fScore[neighbor], 3), neighbor))
    return None


def update_traffic(graph):
    traffic_updates = {}
    for node in graph:
        for neighbor in graph[node]:
            traffic_updates[(node, neighbor)] = round(random.uniform(0.5, 2),3)
    return traffic_updates



city_graph = {
    (0, 0): {(0, 1): 1, (1, 0): 4},
    (0, 1): {(0, 0): 1, (1, 1): 2, (0, 2): 3},
    (0, 2): {(0, 1): 3, (1, 2): 1},
    (1, 0): {(0, 0): 4, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 2, (1, 2): 2},
    (1, 2): {(0, 2): 1, (1, 1): 2},
}

start = (0, 0)
goal = (1, 2)
Dtraffic = update_traffic(city_graph)

shortestPath = AStar(city_graph,start,goal,Dtraffic)

print("TRAFFIC WEIGHT AFTER UPDATE:", Dtraffic)
print("SHORTEST Path:", shortestPath)
