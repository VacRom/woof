############
#Made by VacRom for CS1113
#############


import pygame as pg
import colors
import random


class Actor(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface([25, 25])
        self.image.fill(colors.RED)
        self.rect = self.image.get_rect()
        self.rect.x = center_x-player_center
        self.rect.y = center_y-player_center
        self.walls = None

    def update(self):
        global current_x
        global current_y
        current_x += -dx
        current_y += -dy


class TextBox(pg.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pg.Surface([2*margins, 75])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = center_x-margins
        self.rect.y = screen_y-150
        self.wall = None

    def update(self):
        pass


class TextBorder(pg.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pg.Surface([2*margins+10, 85])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = center_x-margins-5
        self.rect.y = screen_y-155
        self.wall = None

    def update(self):
        pass


class Text():
    def mkText(text, font, color, size, row, textType):
        global all_text
        global all_caption
        row = row*22
        if textType < 3:
            text = [font.render(text, 1, color), center_x-margins+3, screen_y-170+row+3]
            all_text.append(text)
        elif textType is 3:
            all_caption = []
            text = [font.render(text, 1, color), center_x-margins+80, center_y-80+row+3]
            all_caption.append(text)
        else:
            text = [font.render(text, 1, color), center_x-margins+80, center_y-80+row+3]
            all_caption.append(text)
        Text.update()
        if textType is 0:
            pg.time.delay(2500)
        elif textType is 1:
            pg.time.delay(4500)
            all_text = []

    def update():
        if len(all_text) != 0:
            all_textBorder.draw(screen)
            all_textBox.draw(screen)
            for n in range(len(all_text)):
                screen.blit(all_text[n][0], (all_text[n][1], all_text[n][2]))
        if len(all_caption) != 0:
            for n in range(len(all_caption)):
                screen.blit(all_caption[n][0], (all_caption[n][1], all_caption[n][2]))
        pg.display.flip()


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


class Build():
    def mkRoom(x, y, t, w, h, wallColor, floorColor, version):
        x += -current_x+center_x
        y += -current_y+center_y

        if version is 'wall':
            wall = Wall(x, y, t, w, h, wallColor)
            all_walls.add(wall)

        elif version is 'box':
            wallTop = Wall(x, y, w, t, wallColor)
            wallLeft = Wall(x, y, t, h, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif version is 'background':
            floor = Background(x, y, w, h, floorColor)
            all_backgrounds.add(floor)

        elif version is 'wall_1':
            wallTop = Wall(x, y, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_backgrounds.add(floor)

        elif version is 'wall_2':
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif version is 'wall_3':
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif version is 'wall_4':
            wallLeft = Wall(x, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_backgrounds.add(floor)

        elif version is 'hall_1':
            wallLeft = Wall(x, y, t, h, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif version is 'hall_2':
            wallTop = Wall(x, y, w, t, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif version is 'corner_1':
            wallTop = Wall(x, y, w, t, wallColor)
            wallLeft = Wall(x, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_backgrounds.add(floor)

        elif version is 'corner_2':
            wallTop = Wall(x, y, w, t, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif version is 'corner_3':
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif version is 'corner_4':
            wallLeft = Wall(x, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif version is 'end_1':
            wallLeft = Wall(x, y, t, h, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif version is 'end_2':
            wallTop = Wall(x, y, w, t, wallColor)
            wallLeft = Wall(x, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif version is 'end_3':
            wallTop = Wall(x, y, w, t, wallColor)
            wallLeft = Wall(x, y, t, h, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif version is 'end_4':
            wallTop = Wall(x, y, w, t, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)


class World():
    def update():
        all_walls.update()
        all_backgrounds.update()
        all_actors.update()
        screen.fill(colors.BLACK)
        all_backgrounds.draw(screen)
        all_walls.draw(screen)
        all_actors.draw(screen)
        Text.update()
        pg.display.flip()

    def update_2():
        all_walls.update()
        all_backgrounds.update()
        all_actors.update()
        screen.fill(colors.WHITE)
        all_backgrounds.draw(screen)
        all_walls.draw(screen)
        all_actors.draw(screen)
        Text.update()
        pg.display.flip()

    def music(fileName):
        pg.mixer.music.stop
        pg.mixer.music.load(fileName)
        pg.mixer.music.play(-1, 0)
        pg.mixer.music.set_volume(0.7)

pg.init()

all_walls = pg.sprite.Group()
all_backgrounds = pg.sprite.Group()
all_actors = pg.sprite.Group()
all_sprites = pg.sprite.Group()
all_textBorder = pg.sprite.Group()
all_textBox = pg.sprite.Group()
all_text = []
all_caption = []

history = [False]
stage = 0

screen_x = 900
screen_y = 600
initial_x = 500+5
initial_y = 500+5
player_size = 25
thickness = 10
map_x = 3000
map_y = 3000
room_size = 50

mainFont = pg.font.SysFont('oldstandard', 18)
secondFont = pg.font.SysFont('ptsans', 18)
thirdFont = pg.font.SysFont('raleway', 18)

center_x = int(screen_x/2)
center_y = int(screen_y/2)
margins = int((screen_x-200)/2)
player_center = int(player_size/2)
current_x = initial_x
current_y = initial_y
dx = 0
dy = 0
hitWall = False
hitPosWall = ''

player = Actor(center_x-player_center, center_y-player_center)
all_actors.add(player)

textBorder = TextBorder(colors.BLUE_0)
all_textBorder.add(textBorder)

textBox = TextBox(colors.BLACK)
all_textBox.add(textBox)

#screen = pg.display.set_mode([screen_x, screen_y], pg.DOUBLEBUF)
screen = pg.display.set_mode([screen_x, screen_y], pg.DOUBLEBUF | pg.NOFRAME | pg.FULLSCREEN)
pg.display.set_caption(str(stage)+' '+str(current_x)+' '+str(current_y))

clock = pg.time.Clock()
done = False

#n = ['box', 'background', 'hall_1', 'hall_2', 'wall_1', 'wall_2', 'wall_3', 'wall_4', 'corner_1', 'corner_2', 'corner_3', 'corner_4', 'end_1', 'end_2', 'end_3', 'end_4']
n = ['background', 'hall_1', 'hall_2', 'wall_1', 'wall_2', 'wall_3', 'wall_4']

while not done:

    if stage is 0:
        if history[0] is False:
            history[0] = True

            for x in range(0, map_x, room_size-thickness):
                for y in range(0, map_y, room_size-thickness):
                    t = random.choice(n)
                    Build.mkRoom(x, y, thickness, room_size, room_size, colors.BROWN_0, colors.BROWN, t)

    if pg.key.get_pressed()[pg.K_ESCAPE] is 1:
        done = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

# Begin the story here.


    # This determines the player motion by scrolling all nonActors on
    # the screen in the opposite direction.
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

    World.update()
    clock.tick(600)

pg.quit()
