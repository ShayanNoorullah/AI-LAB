import random

class Environment:
    def __init__(self):
        self.grid = [random.choice(  ['VULNERABLE❌', 'SAFE✔️'] ) for i in range(9)]
        
    def get_percept(self,position):
        return self.grid[position]
        
    def patch(self, position):
        self.grid[position] = "SAFE✔️"
        print(f"THE COMPONENT { chr(65 + position)  } HAS BEEN PATCHED SUCCESSFULLY💪")

class Agent:
    def __init__(self):
        
        self.position = 0
   
    
    
    def act(self, percept):
        if percept == "VULNERABLE❌":
            return "WARNING💀! ADDED TO THE PATCH LIST"
        elif percept == "SAFE✔️":
            return "COMPONENT IS SAFE!✔️"
    
    
    def move(self):
        if self.position < 8:
            self.position += 1
        return self.position

def run_agent(agent,environment,steps):
    
    patch_list = []
    
    
    for step in range(steps):
        percept = environment.get_percept( agent.position )
        
        action = agent.act(  percept)
        print(f"STEP{  step+1}: COMPONENT:{  chr(65 + agent.position  )}   {action}")
        
        
        if percept == "VULNERABLE❌":
            patch_list.append(agent.position)
        agent.move()

    print("\nPATCHING ALL THE VULNERABILITIES...")
    
    for c in patch_list:
        environment.patch(c)
    print("\nFINAL SYSTEM STATUS:")
    for i, status in enumerate(environment.grid):
        print(f"Component {chr(65 + i)}: { status}")
agent = Agent()
environment = Environment()
print("INITIAL SYSTEM STATUS:")
for i, status in enumerate(environment.grid):
    print(f"Component {  chr(65 + i) }: { status }")
print("\n")   

run_agent(agent,environment,9)
