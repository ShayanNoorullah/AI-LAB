import random

class Environment:
    def __init__(self):
        self.grid = [random.choice(['COMPLETED', 'FAILED']) for i in range(5)]

    def get_percept(self, position):
        return self.grid[position]

    def retry_backup(self, position):
        self.grid[position] = "COMPLETED"
        print(f"Backup task {position+1} has been retried and completed.")

class BackupManagementAgent:
    def __init__(self):
        self.position = 0

    def act(self, percept):
        if percept == "FAILED":
            return "RETRYING TO BACK UP"
        elif percept == "COMPLETED":
            return "ALL SET!"

    def move(self):
        if self.position < 4:
            self.position += 1
        return self.position

def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.act(percept)
        print(f"Step {step+1}, Backup Task {agent.position+1}: {percept} - {action}")
        if percept == "Failed":
            environment.retry_backup(agent.position)
        agent.move()
    print("\nFINAL STATUS:")
    for i, status in enumerate(environment.grid):
        print(f"Backup Task {i+1}: {status}")





agent = BackupManagementAgent()
environment = Environment()
print("INITIAL STATUS:")
for i, status in enumerate(environment.grid):
    print(f"Backup Task {i+1}: {status}")
print("\n")
run_agent(agent, environment, 5)