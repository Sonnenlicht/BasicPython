#! python3

import math

class Point:

    def __init__(self, x_coord, y_coord, z_coord):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def distance(self, otherpoint):
        new_x = (self.x - otherpoint.x) ** 2
        new_y = (self.y - otherpoint.y) ** 2
        new_z = (self.z - otherpoint.z) ** 2
        return (new_x + new_y + new_z) ** 0.5
        
    #def shift(self, otherpoint):
    def __add__(self, otherpoint):    
        new_x = self.x + otherpoint.x
        new_y = self.y + otherpoint.y
        new_z = self.z + otherpoint.z
        return (new_x, new_y, new_z)

    #def scale(self, val):
    def __mul__(self, val):
        return (self.x * val, self.y * val, self.z * val)

    def __str__(self):
        return "Point with coordinates ({}, {}, {})".format(self.x, self,y, self.z)

    def __repr__(self):
        return "Point(x={},y={},z={})".format(self.x, self,y, self.z)


p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
p3 = p1 + p2 #p2.shift(p1)
print(p3)
p3 = p1*2 #p1.scale(2)
print(p3)
dist = p1.distance(p2)

print(dist)

