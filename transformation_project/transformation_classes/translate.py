import numpy as np
from .point2d import Point2D

class Translate:
    def __init__(self, dx, dy):
        self.matrix = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ])

    def __str__(self):
        return f"Translate(dx={self.matrix[0,2]}, dy={self.matrix[1, 2]})"

    def __add__(self, other):
        if isinstance(other, Translate):
            new_dx = self.matrix[0,2] + other.matrix[0, 2]
            new_dy = self.matrix[1,2] + other.matrix[1, 2]
            return Translate(new_dx, new_dy)

    def __sub__(self, other):
        if isinstance(other, Translate):
            new_dx = self.matrix[0,2] - other.matrix[0, 2]
            new_dy = self.matrix[1,2] - other.matrix[1, 2]
            return Translate(new_dx, new_dy)

    def __mul__(self, point):
        if isinstance(point, Point2D):
            new_coords = self.matrix @ point.coords
            return Point2D(new_coords[0], new_coords[1])
