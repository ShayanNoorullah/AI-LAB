import random

class Environment:

    def __init__(self):
        self.components = [random.choice(  ['SAFE', 'LOW RISK VULNERABLE', 'HIGH RISK VULNERABLE'] ) for i in range(9)]
    
    
    def get_percept(self, position):
        return self.components[ position ]

    
    def patch(self, position):
        if self.components[position] == 'LOW RISK VULNERABLE':
            self.components[position] = 'SAFE'
            print(f"THE COMPNENT {chr( 65 + position ) } HAS BEEN PATCHED WITH SUCCESS!")

class SecurityAgent:
    def __init__(self):
        self.position = 0
    
    def act(self, percept):
        if percept == 'LOW RISK VULNERABLE':
            return "PATCHING LOW RISK VULNERABILITY"
        elif percept == 'HIGH RISK VULNERABLE':
            return "WARNING! PREMIUM SERVICE IS REQUIRED FOR PATCHING!"
        else:
            return "THE COMPONENT IS ALREADY SECURED!"
    
    def move(self):
        if self.position < 8:
            self.position += 1
        return self.position

def run_agent(agent, environment, steps):
    for step in range(steps):
        current_pos = agent.position
        percept = environment.get_percept(current_pos)
        action = agent.act(percept)
        component = chr(65 + current_pos)
        print(f"SCANNING COMPONENT {  component }: PERCEPT:{  percept} || ACTION:{ action }")
        if percept == 'LOW RISK VULNERABLE':
            environment.patch(current_pos)
        agent.move()
    print("\nFINAL SYSTEM STATUS:")
    for i in range(9):
        print(f"COMPONENT {  chr(65 + i)}: {  environment.components[i] }")


print("INITIAL SYSTEM STATUS:")
env = Environment()
for i in range(9):
    print(f"COMPONENT {chr(65 + i  )}: {  env.components[i] }")


agent = SecurityAgent()
print("\n")

run_agent(agent, env, 9)