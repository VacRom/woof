import pygame as pg
import colors

'Define the Actor as your character.'
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
        global dx
        global dy
        hitbox = pg.sprite.spritecollide(self, all_walls, False)
        for wall in hitbox:
            if dx != 0:
                dx = -dx

        hitbox = pg.sprite.spritecollide(self, all_walls, False)
        for wall in hitbox:
            if dy != 0:
                dy = -dy

'Define a Wall as an inanimate object that blocks Actors.'
class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(colors.BROWN_0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x += dx
        self.rect.y += dy

'Define the Background as inanimate objects that do not block Actors'
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
screen = pg.display.set_mode([screen_x, screen_y])
pg.display.set_caption('Project')

all_walls = pg.sprite.Group()
all_backgrounds = pg.sprite.Group()
all_sprites = pg.sprite.Group()

'Generates the background.'
floor = Background(10, 10, 780, 580, colors.BROWN)
all_backgrounds.add(floor)
all_sprites.add(floor)

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
all_sprites.add(player)

clock = pg.time.Clock()
done = False

while not done:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                dx = 2
            elif event.key == pg.K_RIGHT:
                dx = -2
            elif event.key == pg.K_UP:
                dy = 2
            elif event.key == pg.K_DOWN:
                dy = -2

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                dx = 0
            elif event.key == pg.K_RIGHT:
                dx = 0
            elif event.key == pg.K_UP:
                dy = 0
            elif event.key == pg.K_DOWN:
                dy = 0

    all_sprites.update()
    screen.fill(colors.BLACK)
    all_sprites.draw(screen)

    pg.display.flip()
    clock.tick(60)
    print(player.rect.x, player.rect.y)
pg.quit()


































