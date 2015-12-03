import pygame as pg

pg.init()

pg.mixer.music.load('track_4.mp3')
pg.mixer.music.play(-1, 0)

Done = False

while not Done:
    print(1)
