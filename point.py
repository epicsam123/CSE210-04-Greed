#from object import Object
import random

class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.
    """
    
    def __init__(self, x, y):

        self._x = x
        self._y = y

    def add(self, other):
        # Adds coordinate points together. 
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)
   
    def equals(self, other):
        # Checks if two coordinate points are equal.
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        # Gets X.
        return self._x

    def get_y(self):
        # Gets Y.
        return self._y

    def scale(self, factor):
        return Point(self._x * factor, self._y * factor)