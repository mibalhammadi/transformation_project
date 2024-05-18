from .point2d import Point2D

class Transformation:
    def __init__(self, translate, rotate):
        # Ensure the translation is applied first, then the rotation
        self.matrix = translate.matrix @ rotate.matrix

    def __str__(self):
        return "Transformation combining translation and rotation"

    def __mul__(self, point):
        if isinstance(point, Point2D):
            new_coords = self.matrix @ point.coords
            return Point2D(new_coords[0], new_coords[1])
        
