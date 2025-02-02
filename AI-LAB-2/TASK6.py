class Building:
    def __init__(self):
        self.rooms = {'a':'SAFE','b':'SAFE','c':'FIRE','d':'SAFE','e':'FIRE','f':'SAFE','g':'SAFE','h':'SAFE','j':'FIRE'}
    
    def get_status(self, room):
        return self.rooms[room]
    
    def extinguishFire(self, room):
        if self.rooms[room] == 'FIRE':
            self.rooms[room] = 'SAFE'
            print(f"FIRE IN ROOM {room} HAS BEEN EXTINGUISHED!!!")
    
    def display(self):
        print("\nCURRENT STATUS:")
        grid = [[' ' for i in range(3)] for i in range(3)]
        mapping = {'a': (0, 0), 'b': (0, 1), 'c': (0, 2),'d': (1, 0), 'e': (1, 1), 'f': (1, 2),'g': (2, 0), 'h': (2, 1), 'j': (2, 2)}
        for room, status in self.rooms.items():
            row, col = mapping[room]
            grid[row][col] = '🔥' if status == 'FIRE' else '✅'
        for row in grid:
            print("|".join(row))

class FirefightingRobot:
    def __init__(self):
        self.position = 'a'
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']


    
    def move(self, building):
        for room in self.path:
            self.position = room
            status = building.get_status(room)
            print(f"\nSCANNING ROOM # { room  }: { status  }")
            if status == 'FIRE':
                building.extinguishFire(room)
            building.display()
        
        print("\nFINAL STATUS:")
        building.display()





building = Building()
robot = FirefightingRobot()
print("INITIAL BUILDING STATUS:")
building.display()
robot.move(building)