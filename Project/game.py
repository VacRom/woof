import pygame as pg
import colors

'Define the Actor as your character.'
class Actor(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface([15, 15])
        self.image.fill(colors.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.walls = None

    def changevel(self, x, y):
        self.vel_x += x
        self.vel_y += y

    def update(self):
        self.rect.x += self.vel_x
        all_blocks = pg.sprite.spritecollide(self, self.walls, False)
        for block in all_blocks:
            if self.vel_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.rect.y += self.vel_y
        all_blocks = pg.sprite.spritecollide(self, self.walls, False)
        for block in all_blocks:
            if self.vel_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

'Define a Wall as an inanimate object that blocks Actors.'
class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(colors.BROWN_0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

'Define the Background as inanimate objects that do not block Actors'
class Background(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pg.init()

screen_x = 1200
screen_y = 800
screen = pg.display.set_mode([screen_x, screen_y])
pg.display.set_caption('Project')

all_walls = pg.sprite.Group()
all_backgrounds = pg.sprite.Group()
all_sprites = pg.sprite.Group()

'Generates the background.'
floor = Background(0, 0, 800, 600, colors.BROWN)
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
player = Actor(50, 50)
player.walls = all_walls
all_sprites.add(player)

clock = pg.time.Clock()
done = False

while not done:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.changevel(-2, 0)
            elif event.key == pg.K_RIGHT:
                player.changevel(2, 0)
            elif event.key == pg.K_UP:
                player.changevel(0, -2)
            elif event.key == pg.K_DOWN:
                player.changevel(0, 2)

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.changevel(2, 0)
            elif event.key == pg.K_RIGHT:
                player.changevel(-2, 0)
            elif event.key == pg.K_UP:
                player.changevel(0, 2)
            elif event.key == pg.K_DOWN:
                player.changevel(0, -2)

    all_sprites.update()
    screen.fill(colors.BLACK)
    all_backgrounds.draw(screen)
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(120)

pg.quit()
