import pygame as pg
import colors


class Actor(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface([15, 15])
        self.image.fill(colors.RED)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.walls = None

    def update(self):
        global hitWall


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global hitWall
        global hitPosWall
        global dx
        global dy
        self.rect.x += dx
        self.rect.y += dy
        checkWall = pg.sprite.spritecollide(self, all_actors, False)
        for player in checkWall:
            hitWall = True
            if dy > 0:
                hitPosWall = 'Top'
            if dy < 0:
                hitPosWall = 'Bottom'
            if dx > 0:
                hitPosWall = 'Left'
            if dx < 0:
                hitPosWall = 'Right'
        if hitWall is not True:
            hitPosWall = ''


class Background(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += dx
        self.rect.y += dy

pg.init()

all_walls = pg.sprite.Group()
all_backgrounds = pg.sprite.Group()
all_actors = pg.sprite.Group()
all_sprites = pg.sprite.Group()

player = Actor(400, 300)
all_actors.add(player)

t = 0
screen_x = 800
screen_y = 600
dx = 0
dy = 0
hitWall = False
hitPosWall = ''
screen = pg.display.set_mode([screen_x, screen_y])
pg.display.set_caption('Project')

floor = Background(10, 10, 780, 580, colors.BROWN)
all_backgrounds.add(floor)

wall = Wall(0, 0, 10, 600, colors.BROWN_0)
all_walls.add(wall)
all_sprites.add(wall)

wall = Wall(10, 0, 790, 10, colors.BROWN_0)
all_walls.add(wall)
all_sprites.add(wall)

wall = Wall(790, 10, 10, 590, colors.BROWN_0)
all_walls.add(wall)
all_sprites.add(wall)

wall = Wall(10, 590, 790, 10, colors.BROWN_0)
all_walls.add(wall)
all_sprites.add(wall)
clock = pg.time.Clock()
done = False

while not done:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    if hitWall is False:
        if pg.key.get_pressed()[pg.K_LEFT] is 0 or pg.key.get_pressed()[pg.K_RIGHT] is 0:
            dx = 0
        if pg.key.get_pressed()[pg.K_UP] is 0 or pg.key.get_pressed()[pg.K_DOWN] is 0:
            dy = 0
        if pg.key.get_pressed()[pg.K_LEFT] is 1:
            dx = 2
        if pg.key.get_pressed()[pg.K_RIGHT] is 1:
            dx = -2
        if pg.key.get_pressed()[pg.K_UP] is 1:
            dy = 2
        if pg.key.get_pressed()[pg.K_DOWN] is 1:
            dy = -2

    else:
        if hitPosWall is 'Top':
            dy = -2
            dx = -dx
        if hitPosWall is 'Right':
            dx = 2
            dy = -dy
        if hitPosWall is 'Bottom':
            dy = 2
            dx = -dx
        if hitPosWall is 'Left':
            dx = -2
            dy = -dy
        hitWall = False
        hitPosWall = ''

    all_walls.update()
    all_backgrounds.update()
    screen.fill(colors.BLACK)
    all_backgrounds.draw(screen)
    all_walls.draw(screen)
    all_actors.draw(screen)

    pg.display.flip()
    clock.tick(60)
    t += 1
    print(t)
pg.quit()
