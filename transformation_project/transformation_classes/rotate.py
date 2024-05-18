import numpy as np
from .point2d import Point2D

class Rotate:
    def __init__(self, theta):
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        self.matrix = np.array([
            [cos_theta, -sin_theta, 0],
            [sin_theta, cos_theta, 0],
            [0, 0, 1]
        ])

    def __str__(self):
        return f"Rotate(theta={np.arccos(self.matrix[0, 0])})"  # Assuming theta was the input

    def __add__(self, other):
        if isinstance(other, Rotate):
            new_theta = np.arccos(self.matrix[0, 0]) + np.arccos(other.matrix[0, 0])
            return Rotate(new_theta)

    def __sub__(self, other):
        if isinstance(other, Rotate):
            new_theta = np.arccos(self.matrix[0, 0]) - np.arccos(other.matrix[0, 0])
            return Rotate(new_theta)

    def __mul__(self, point):
        if isinstance(point, Point2D):
            new_coords = self.matrix @ point.coords
            return Point2D(new_coords[0], new_coords[1])

