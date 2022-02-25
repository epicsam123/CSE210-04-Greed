from color import Color
from point import Point
import pyray
class Actor:

    def __init__(self):
        # What each actor has, create new actor.
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        # Get the color of the actor or person
        return self._color

    def get_font_size(self):
        # Gets the font size of the player or object.
        return self._font_size

    def get_position(self):
        # Gets the position of the object or person.
        return self._position
    def create_rect(self,object):
        return pyray.Rectangle(object.get_position().get_x(),object.get_position().get_y(),12,12)
    def get_text(self):
        # Get the text of the object or player.
        return self._text

    def get_velocity(self):
        # Gets player velocity
        return self._velocity
    

    def move_next(self, max_x, max_y):
        # Moves the player and puts puts the player on the other side of the screen if they try to go off.
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_color(self, color):
        # Updates the color
        self._color = color

    def set_position(self, position):
        # Updates the position.
        self._position = position

    def set_font_size(self, font_size):
        # Updates the font size.
        self._font_size = font_size
    
    def set_text(self, text):
        # Updates the text.
        self._text = text

    def set_velocity(self, velocity):
        # Updates the velocity.
        self._velocity = velocity
    