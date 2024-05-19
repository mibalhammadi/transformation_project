#!/usr/bin/env python3
import sys
import os
# Ensure the parent directory is in the sys.path for imports 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules
from transformation_classes.point2d import Point2D
from transformation_classes.translate import Translate
from transformation_classes.rotate import Rotate
from transformation_classes.transformation import Transformation
import numpy as np
from numpy import allclose
from matplotlib import pyplot as plt

def test_point_operations():
    p1 = Point2D(3, 4)
    p2 = Point2D(1, 2)
    p3 = p1 + p2
    assert p3 == Point2D(4, 6), "Addition failed"
    p4 = p1 - p2
    assert p4 == Point2D(2, 2), "Subtraction failed"
    print("Point Operations Passed")

def test_translation():
    p1 = Point2D(3, 4)
    t1 = Translate(1, 2)
    p2 = t1 * p1
    assert p2 == Point2D(4, 6), "Translation failed"
    print("Translation Passed")

def test_rotation():
    p1 = Point2D(1, 0)
    r1 = Rotate(np.pi / 2)  # 90 degrees rotation
    p2 = r1 * p1
    expected = Point2D(0, 1)
    tolerance = 1e-6
    assert np.allclose(p2.coords[:2], expected.coords[:2], atol=tolerance), "Rotation failed"
    print("Rotation Passed")

def test_transformation():
    p1 = Point2D(1, 0)
    t1 = Translate(1, 2)
    r1 = Rotate(np.pi / 2)  
    T1 = Transformation(t1, r1)
    p2 = T1 * p1
    expected = Point2D(1, 3)  
    print(f"Transformed Point: {p2}")
    assert p2.coords[0] == expected.coords[0] and p2.coords[1] == expected.coords[1], "Full Transformation failed"
    print("Full Transformation Passed")



if __name__ == "__main__":
    test_point_operations()
    test_translation()
    test_rotation()
    test_transformation()
