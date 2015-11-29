import pygame as pg
current_time = 0

n = 0
pg.init()
clock = pg.time.Clock()
timer1 = pg.time.Clock()

while n is 0:
    current_time += timer1.get_time()

    timer1.tick(60)
    clock.tick(60)
    print(timer1.get_time(), current_time)
