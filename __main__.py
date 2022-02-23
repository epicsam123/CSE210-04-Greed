import os
import random
import pyray



from actor import Actor
from object import Object
from cast import Cast

from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point


FRAME_RATE = 25
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Collect The Gems"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_OBJECTS = 40
DONE = False


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(15)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    score = Actor()
    score.set_text("")
    score.set_font_size(15)
    score.set_color(WHITE)
    score.set_position(Point(60, 0))  
    cast.add_actor("score", score)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 100)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(20)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # creates the gems and rocks
    for h in range(DEFAULT_OBJECTS):
        character = ['*','o']
        text = character[random.randint(0,1)]
        x = random.randint(0, COLS - 1)
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
        
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()