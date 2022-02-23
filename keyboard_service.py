import os
os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"
from raylibpy import *
from point import Point


class KeyboardService:
    # Detects when the player presses on the keyboard, and sets the direction of the player.
    def __init__(self, cell_size = 1):
        self._cell_size = cell_size

    def get_direction(self):
        dx = 0
        dy = 0

        if is_key_down(KEY_LEFT):
            dx = -.5
        
        if is_key_down(KEY_RIGHT):
            dx = .5
        
        if is_key_down(KEY_UP):
            dy = 0
        
        if is_key_down(KEY_DOWN):
            dy = 0

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction