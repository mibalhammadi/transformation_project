import numpy as np
from matplotlib import pyplot as plt

'''
the below class is the basic class which it stores the x,y values and each function do a 
specific action as named. 
'''

class Point2D:
    def __init__(self, x=0, y=0):
        self.coords = np.array([x, y, 1]) 

    def __str__(self):
        return f"Point2D({self.coords[0]}, {self.coords[1]})"

    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.coords[0] + other.coords[0], self.coords[1] + other.coords[1])

    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.coords[0] - other.coords[0], self.coords[1] - other.coords[1])

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return np.array_equal(self.coords, other.coords)

    def __lt__(self, other):
        if isinstance(other, Point2D):
            return (self.coords[0], self.coords[1]) < (other.coords[0], other.coords[1])

    def plot(self, color='r'):
        plt.plot(self.coords[0], self.coords[1], marker='o', color=color)

a = Point2D(1,1)
print(a.coords)
