import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    def get_distance(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    
    # __lt__ is used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    # __str__ is used to print the x and y values
    def __str__(self):
        return '[{self.x}, {self.y}]'.format(self=self)

    # distance_from_origin calculates the distance using x, y coordinates
    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    __repr__ = __str__