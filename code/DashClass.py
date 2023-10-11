import pygame as pg
from pygame import mixer
import random

from threading import Thread
from time import sleep


# background
BACKGROUND = pg.image.load('.\\images\\background.png')
DIRECTIONS = ("LEFT", "RIGHT", "UP", "DOWN")

# destination arrows
# paste them in background image

# input arrows
INP_ARROW_IMAGES = { "LEFT"  : pg.image.load('.\\images\\inp-arrow-left.png' ),
                     "DOWN"  : pg.image.load('.\\images\\inp-arrow-down.png' ),
                     "UP"    : pg.image.load('.\\images\\inp-arrow-up.png'   ),
                     "RIGHT" : pg.image.load('.\\images\\inp-arrow-right.png') }

# arr_img_left
LEFT_SIDE_ARROW_PROPS  = { "LEFT"  : {"image": INP_ARROW_IMAGES["LEFT"],  "coords" : ( 39, 564), "key": pg.K_a},
                           "DOWN"  : {"image": INP_ARROW_IMAGES["DOWN"],  "coords" : (137, 564), "key": pg.K_s},
                           "UP"    : {"image": INP_ARROW_IMAGES["UP"]  ,  "coords" : (235, 564), "key": pg.K_w},
                           "RIGHT" : {"image": INP_ARROW_IMAGES["RIGHT"], "coords" : (333, 564), "key": pg.K_d} }
# arr_img_right
RIGHT_SIDE_ARROW_PROPS = { "LEFT"  : {"image": INP_ARROW_IMAGES["LEFT"],  "coords" : (491, 564), "key": pg.K_LEFT},
                           "DOWN"  : {"image": INP_ARROW_IMAGES["DOWN"],  "coords" : (589, 564), "key": pg.K_DOWN},
                           "UP"    : {"image": INP_ARROW_IMAGES["UP"]  ,  "coords" : (687, 564), "key": pg.K_UP},
                           "RIGHT" : {"image": INP_ARROW_IMAGES["RIGHT"], "coords" : (785, 564), "key": pg.K_RIGHT} }



class Arrow:
    def __init__(self, left_side:bool=True, direction:str="LEFT"):
        ''' left_side: Which side of the screen is the arrow on
            direction: Direction the arrow is facing, "UP", "LEFT", "RIGHT", "DOWN"
        '''
        self.is_alive  = True
        self.in_range  = False

        self.left_side = left_side
        self.direction = direction
        # select arrow properties
        properties     = (LEFT_SIDE_ARROW_PROPS if left_side else RIGHT_SIDE_ARROW_PROPS)[direction]
        self.image     = properties["image"]
        self.x, self.y = properties["coords"]
        self.event_key = properties["key"]


    def move(self) -> bool:
        if self.is_alive:
            self.y -= 1
            self.display_arrow()

            if not self.in_range and self.y < 170:
                self.in_range = True

            if self.y < -50:
                miss_sound = mixer.Sound(".\\sound\\explosion.wav")
                miss_sound.play()
                self.is_alive = False

            return self.is_alive

    def check_input(self, key:str) -> int:
        if self.in_range and key == self.event_key:
            self.is_alive = False
            return self.get_score()
        return 0


    def get_score(self) -> int:
        difference = abs(20 - self.y)
        if difference > 50:
            miss_sound = mixer.Sound(".\\sound\\explosion.wav")
            miss_sound.play()
            return 0
            
        score_sound = mixer.Sound(".\\sound\\score_sound.mp3")
        score_sound.play()
        if difference < 20:     
            return 10
        
        return 5


    def display_arrow(self) -> None:
        SCREEN.blit(self.image, (self.x, self.y))


    def __repr__(self) -> str:
        return f"{self.direction} {self.y}"



class GameApp:
    def __init__(self):
        self.GAME_RUN = False
        self.score    = 0
        self.font     = pg.font.SysFont('minecraft', 25, pg.font.Font.bold)
        self.active_arrows = []


    def display_score(self):
        score = self.font.render(f"Score : {self.score}", True, (255, 255, 255))
        SCREEN.blit(score, (405,560))


    def generate_arrow(self):
        with open(".\\levels\\test.txt", 'r') as file:
            for command in file.readlines():
                duration, is_left_side, arrow_direction = command.split()
                sleep(float(duration))
                self.active_arrows.append( Arrow(int(is_left_side), arrow_direction) )

    
    def event_controller(self):
        # handle events
        pg.event.clear()

        while True:
            event = pg.event.wait()
            
            if event.type == pg.QUIT:
                self.GAME_RUN = False

            elif event.type == pg.KEYDOWN:
                pressed_key = event.key
                print("KEY:", pressed_key)
                for arrow in self.active_arrows:
                    self.score += arrow.check_input(pressed_key)


    def start(self):
        # show menu
        menu = self.font.render(f"Press S to start", True, (255, 255, 255))
        SCREEN.blit(menu, (405,560))
        pg.display.update()

        # press S begin game
        pg.event.clear()
        while True:
            event = pg.event.wait()
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                break

        thd_game = Thread(target = self.run_game)
        thd_game.start()

        print("Controller started")
        self.event_controller()
        thd_game.join()


    def run_game(self):
        self.GAME_RUN = True
        Thread(target = self.generate_arrow).start()

        pg.mixer.music.load(".\\sound\\background_music.mp3")
        pg.mixer.music.play(1)

        while self.GAME_RUN:
            SCREEN.blit(BACKGROUND, (0, 0))

            for arrow in self.active_arrows:
                # move each arrow forward and remove it if not alive
                if not arrow.move():
                    self.active_arrows.remove(arrow)
                    print("arrow killed")

            self.display_score()
            pg.display.update()

        pg.quit() #for quit event
        print("GAME EXITED")



if __name__ == "__main__":

    pg.init()
    SCREEN = pg.display.set_mode((900,600))
    pg.display.set_caption("Sensor Dash")
    # icon = pg.image.load(('icon location'))
    # pg.display.set_icon(icon)

    game = GameApp()
    game.start()
