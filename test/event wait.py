import pygame as pg
from pygame import *
from pygame.locals import *

pg.init()
SCREEN = pg.display.set_mode((900,600))

pg.event.clear()

while True:
    event = pg.event.wait()
    print(event.type)
    if event.type == pg.KEYDOWN and event.key == pg.K_a:
        break

print(event.type, event.key)

pg.quit()
