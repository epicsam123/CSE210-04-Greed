from actor import Actor
from point import Point
import random

class Object(Actor):
    """
    The responsibility of an Object is to provide a score, the speed of the object, and have the objects move.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        self._speed = random.randint(1,3)
    def move_next(self, max_x, max_y):
        x = (self._position.get_x()) % max_x
        y = (self._position.get_y() + self._speed) 
        self._position = Point(x, y)
    def set_score(self,character): 
        if character == "*":
            self._score+=1
        else:
            self._score-=1
        return self._score