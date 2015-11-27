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
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(colors.BROWN_0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global hitWall
        global hitPosWall
        global all_walls
        global all_backgrounds
        global dx
        global dy
        test_walls = all_walls
        test_backgrounds = all_backgrounds
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
        if hitWall is True:
            all_walls = test_walls
            all_backgrounds = test_backgrounds
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

screen_x = 800
screen_y = 600
dx = 0
dy = 0
hitWall = False
hitPosWall = ''
screen = pg.display.set_mode([screen_x, screen_y])
pg.display.set_caption('Project')

all_walls = pg.sprite.Group()
all_backgrounds = pg.sprite.Group()
all_actors = pg.sprite.Group()
all_sprites = pg.sprite.Group()

'Generates the background.'
floor = Background(10, 10, 780, 580, colors.BROWN)
all_backgrounds.add(floor)

'Generates the stage.'
wall = Wall(0, 0, 10, 600)
all_walls.add(wall)
all_sprites.add(wall)

wall = Wall(10, 0, 790, 10)
all_walls.add(wall)
all_sprites.add(wall)

wall = Wall(790, 10, 10, 590)
all_walls.add(wall)
all_sprites.add(wall)

wall = Wall(10, 590, 790, 10)
all_walls.add(wall)
all_sprites.add(wall)

'Generates actors.'
player = Actor(400, 300)
all_actors.add(player)
all_sprites.add(player)

clock = pg.time.Clock()
done = False

while not done:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    if hitWall is False:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                dx = 2
            elif event.key == pg.K_RIGHT:
                dx = -2
            elif event.key == pg.K_UP:
                dy = 2
            elif event.key == pg.K_DOWN:
                dy = -2
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                dx = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                dy = 0
        hitPosWall = ''
    elif hitWall is True:
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

    all_walls.update()
    all_backgrounds.update()
    screen.fill(colors.BLACK)
    all_backgrounds.draw(screen)
    all_walls.draw(screen)
    all_actors.draw(screen)

    pg.display.flip()
    clock.tick(60)
    print(hitWall, hitPosWall, dx, dy)
pg.quit()
