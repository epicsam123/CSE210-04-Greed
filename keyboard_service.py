
import pyray
from point import Point


class KeyboardService:
    # Detects when the player presses on the keyboard, and sets the direction of the player.
    def __init__(self, cell_size = 1):
        self._cell_size = cell_size

    def get_direction(self):
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            dy = 0
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 0

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction