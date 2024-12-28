from utils.point import Point
from heapq import *

def k_closest(points, k):
    max_heap = []

    for i in range(k):
        point = points[i]
        distance = point.get_distance()
        heappush(max_heap, (-distance, point.x, point. y))
    
    current_pos = k - 1

    while current_pos + 1 < len(points):
        (closest_distance, closest_x, closest_y) = max_heap[0]
        point = Point(closest_x, closest_y)

        current_pos += 1
        next_point = points[current_pos]
        next_point_distance = next_point.get_distance() * - 1
        if next_point_distance >= closest_distance:
            heappop(max_heap)
            heappush(max_heap, (next_point_distance, next_point.x, next_point.y))
    
    results = []

    for item in max_heap:
        (distance, x, y) = item
        results.append(Point(x, y))

    return results


### answer

def k_closest_answer(points, k):
    max_heap = []
    for i in range(k):
        heappush(max_heap, points[i])
    
    for i in range(k, len(points)):
        if points[i].get_distance() < max_heap[0].get_distance():
            heappop(max_heap)
            heappush(max_heap, points[i])

    return list(max_heap)


point_arr = [[1,3],[2,4],[2,-1],[-2,2],[5,3],[3,-2]] 
k = 3
points = [Point(pair[0], pair[1]) for pair in point_arr]
result = k_closest(points, k)

for item in result:
    print(item)