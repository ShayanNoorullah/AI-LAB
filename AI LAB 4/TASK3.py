import heapq
import math

class DeliveryPoint:
    def __init__(self,id,x,y,t):
        self.id = id
        self.x = x
        self.y = y
        self.t = t
    


    def distance(self,other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)




def GBFS(start,delivery_points):
    route = []
    current=start
    priority_queue = []
    
    for point in delivery_points:
        heapq.heappush(priority_queue, (point.t[1], point))
    


    while priority_queue:
        _, next = heapq.heappop(priority_queue)
        route.append(next)
        current_location = next
    return route


deliveryPts = [
    DeliveryPoint(1, 2, 3, (8, 10)),

    DeliveryPoint(2, 5, 1, (7, 9)),

    DeliveryPoint(3, 6, 4, (6, 8)),
    
    DeliveryPoint(4, 1, 7, (9, 11))
]
start = DeliveryPoint(0, 0, 0, (0, 24))
optimize = GBFS(start, deliveryPts)


print("OPTIMIZED DELIVERY ROOTE:")
for point in optimize:
    print(f"DELIVERY FROM POINT {point.id} AT ({point.x}, {point.y}) WITHIN {point.t}")
