import random

class Environment:
    def __init__(self):
        self.grid = [random.choice(['UNDERLOADED','BALANCED','OVERLOADED']) for i in range(5)]

    def get_percept(self, position):
        return self.grid[position]

    def loadSubtracter(self, position):
        self.grid[position] = "BALANCED"
        print(f"Server {position+1} HAS BEEN BALANCED BY REMOVAL OF LOAD.")

    def loadAdder(self, position):
        self.grid[position] = "BALANCED"
        print(f"Server {position+1} HAS BEEN BALANCED BY ADDITION OF LOAD.")

class LoadBalancAgent:
    def __init__(self):
        self.position = 0

    def act(self, percept):
        if percept == "OVERLOADED":
            return "MOVE TASKS FROM THIS SERVER"
        elif percept == "UNDERLOADED":
            return "ADD TASKS IN THIS SERVER"
        elif percept == "BALANCED":
            return "ALL SORTED!"

    def move(self):
        if self.position < 4:
            self.position += 1
        return self.position

def run_agent(agnt,environment,steps):
    for step in range(steps):
        percept = environment.get_percept(agnt.position)
        action = agnt.act(percept)
        print(f"Step:{step+1} Server{agnt.position+1}: PERCEPT:{percept}  ACTION:{action}")

        if percept == "OVERLOADED":
            environment.loadSubtracter(agnt.position)
        elif percept == "UNDERLOADED":
            environment.loadAdder(agnt.position)
        agnt.move()
    print("\nFINAL STATUS:")
    for i, status in enumerate(environment.grid):
        print(f"Server {i+1}: {status}")


agnt = LoadBalancAgent()
environment = Environment()
print("INITIAL STATUS:")
for i, status in enumerate(environment.grid):
    print(f"Server {i+1}: {   status}")
print("\n")
run_agent(agnt,environment, 5)