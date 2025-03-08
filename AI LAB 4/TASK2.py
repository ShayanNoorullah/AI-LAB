import heapq
import random
import time
import threading

class Graph:    
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        


    def add_node(self,value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = {}
    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node][to_node] = cost
        self.edges[to_node][from_node] = cost


    def get_neighbors(self,node):
        return self.edges.get(node, {}).keys()
    


    def get_cost(self, from_node, to_node):
        return self.edges[from_node].get(to_node, float('inf'))
    

    def update_edge_cost(self, from_node, to_node, new_cost):

        if from_node in self.edges and to_node in self.edges[from_node]:
            self.edges[from_node][to_node] = new_cost
            self.edges[to_node][from_node] = new_cost



def heuristic(node, goal):
    x1,y1 = node
    x2,y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def AStar(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        

        for neighbor in graph.get_neighbors(current):
            tscore = g_score[current] + graph.get_cost(current, neighbor)
            if tscore < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tscore
                f_score[neighbor] = tscore + heuristic(neighbor, goal)
                heapq.heappush(open_set,(f_score[neighbor], neighbor))
    
    return None  # No path found

# Dynamic cost update simulator
def RandomChange(graph, nodes, interval=3):
    while True:
        node1, node2 = random.sample(nodes, 2)
        new_cost = random.randint(1, 10)
        graph.update_edge_cost(node1, node2, new_cost)
        print(f"UPDATING COST BETWEEN {node1} & {node2} --> {new_cost}")
        time.sleep(interval)


graph = Graph()
nodes = [(x, y) for x in range(5) for y in range(5)]
for node in nodes:
    graph.add_node(node)

for x in range(5):

    for y in range(5):

        if x < 4:
            graph.add_edge((x, y), (x+1, y), random.randint(1, 5))


        if y < 4:
            graph.add_edge((x, y), (x, y+1), random.randint(1, 5))

start,goal=(0, 0),(4, 4)



threading.Thread(target=RandomChange,args=(graph, nodes),daemon=True).start()
count = 0
while True:
    path = AStar(graph,start,goal)
    print("THE OPTIMAL PATH is:",path)
    time.sleep(5)
    count += 1
    if count == 20:
        break

