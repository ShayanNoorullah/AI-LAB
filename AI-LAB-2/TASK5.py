import random

class HospitalEnvironment:
    def __init__(self):
        self.components = [random.choice(['CORRIDORS', 'PATIENT ROOMS', 'NURSE STATIONS', 'MEDICINE STORAGE AREAS']) for _ in range(9)]
        
        self.medicines = {i: random.choice(  ['MEDICINE-A', 'MEDICINE-B', None ]) for i in range(9)}
    def get_percept(self, position):
        return self.components[position], self.medicines[position]
    def pick(self, position):
        
        if self.medicines[position]:
            medicine = self.medicines[position]
            self.medicines[position] = None
            return medicine
        return None

    
    def deliver(self, position, medicine):
        if self.components[position] == 'PATIENT ROOMS':
            print(f"THE MEDICINE {medicine} HAS BEEN DELIVERED TO THE ROOM {  chr(65 + position)  }")
        else:
            print(f"ISSUE OCCURED IN DELIVERING THE MEDICINE TO {self.components[position]}.")

class HospitalRobot:
    def __init__(self):
        self.position = 0
        self.medicine = None


    
    def act(self, percept, environment):
        location, med_need = percept
        if location == 'MEDICINE STORAGE AREAS' and not self.medicine:
            self.medicine = environment.pick(self.position)
            return f"THE MEDICINE {self.medicine} HAS BEEN PICKED UP FROM STORAGE" if self.medicine else "SORRY! NO MEDICINE AVAILABLE!"
        elif location == 'PATIENT ROOMS' and self.medicine:
            environment.deliver(self.position, self.medicine)
            self.medicine = None
            return "MEDICINE HAS BEEN DELIVERED SUCCESSFULLY!"
        return "MOVING TO THE OTHER POSSIBLE LOCATION"
    
    def move(self):
        if self.position < 8:
            self.position += 1
        return self.position

def run_robot(robot, environment, steps):
    for step in range(steps):
        current_pos = robot.position
        
        
        percept = environment.get_percept(current_pos)
        action = robot.act(percept, environment)
        component = chr(65 + current_pos)
        print(f"At {component}: {percept[0]} || MEDICINE REQUIRED ->  PERCEPT: {percept[1]} && ACTION: {action}")
        robot.move()
    
    print("\nFINAL HOSPITAL STATUS:")
    for i in range(9):
        print(f"LOCATION -> {chr(65 + i)}: {environment.components[i]} || MEDICINE REQUIRED: {  environment.medicines[i]}")

print("INITIAL HOSPITAL STATUS:")
env = HospitalEnvironment()
for i in range(9):
    print(f"LOCATION -> {chr(65 + i)}: {env.components[i]} || MEDICINE REQUIRED: {env.medicines[i]}")



robot = HospitalRobot()
print("\n")


run_robot(robot, env, 9)