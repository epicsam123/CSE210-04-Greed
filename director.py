from object import Object
from point import Point
import random
from color import Color
CELL_SIZE = 15
COLS = 60
ROWS = 40
class Director:
    """
        Creates the actual game, determines game rules and makes sure the game follows those rules.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = Object()
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with objects.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        object = cast.get_actors("objects")
        score = cast.get_first_actor("score")

        banner.set_text("Score:")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for objects in object:
            if robot.get_position().equals(objects.get_position()):
                cast.remove_actor("objects",objects)
                character = objects.get_text()
                text = self._score.set_score(character)
                score.set_text(str(text))
            objects.move_next(max_x, max_y)
            if objects.get_position().get_y()>=max_y:
                cast.remove_actor("objects",objects)
        
        if len(object)<40:
            character = ['*','o']
            text = character[random.randint(0,1)]
            x = random.randint(5, COLS - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
                
            symbol = Object()
            symbol.set_text(text)
            symbol.set_font_size(20)
            symbol.set_color(color)
            symbol.set_position(position)
            cast.add_actor("objects", symbol)
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()