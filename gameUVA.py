
############
#Made by VacRom for CS1113
#############

import pygame as pg
import colors

# Actor represents all the players that are in the game.
class Actor(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface([player_size, player_size])
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


# The following three classes are utilized to make text in the
# game. The TextBox and TextBorder classes make the box in which the
# text is to be written. Text border takes in a color and makes a text
# box of that color.
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


# Text border takes in a color and makes a border for the text box of
# that color.
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


# The Text class generates the text. mkText takes in a text (string),
# font type (look at the list of fonts in the Notes folder), a font
# color (in form of a tuple), a font size (integer), a row (each
# increasing row 'indents' the text, and a text type.)
class Text(object):
    def __init__(self, text, font, color, size, row, textType):
        global all_text
        global all_caption
        self.text = text
        self.font = font
        self.color = color
        self.size = size
        self.textType = textType
        self.row = row*22
        if self.textType < 3:
            self.text = [font.render(self.text, 1, self.color), center_x-margins+3, screen_y-170+self.row+3]
            all_text.append(self.text)
        elif self.textType is 3:
            all_caption = []
            self.text = [font.render(self.text, 1, self.color), center_x-margins+80, center_y-80+self.row+3]
            all_caption.append(self.text)
        else:
            text = [font.render(self.text, 1, self.color), center_x-margins+80, center_y-80+self.row+3]
            all_caption.append(self.text)
        Text.update()
        # textType 0 is used for cutscenes and freezes the screen for
        # 2s. texType 1 is similar except that it freezes the screen
        # for 5s then erases the text in preparation for the next page
        # of text.
        if self.textType is 0:
            pg.time.delay(2500)
        elif self.textType is 1:
            pg.time.delay(4500)
            all_text = []

    # This update function ensures that text is only displayed when
    # the number of text to be displayed is not zero. Furthermore, the
    # text box automatically pops up if this condition is met.
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


# A wall is a sprite that Actors cannot pass through.
class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # This update function checks for collisions and furthermore
    # indicates which side of the actor the wall has hit.
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


# A Background is a sprite that Actors can pass through.
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


# This Build class makes a number of rooms, given their (x,y)
# coordinate and their width and height. Wall thickness and colors of
# the backgrounds and walls can also be generated. Version tells the
# program exactly what type of room (closed, 3 walls, etc.) to
# make. Check the notes folder for what all version types mean.
class Build(object):
    def __init__(self, x, y, t, w, h, wallColor, floorColor, version):
        self.x = x-current_x+center_x
        self.y = y-current_y+center_y
        self.t = t
        self.w = w
        self.h = h
        self.wallColor = wallColor
        self.floorColor = floorColor
        self.version = version

        if self.version is 'wall':
            wall = Wall(self.x, self.y, self.t, self.w, self.h, self.wallColor)
            all_walls.add(wall)

        elif self.version is 'box':
            wallTop = Wall(self.x, self.y, self.w, self.t, self.wallColor)
            wallLeft = Wall(self.x, self.y, self.t, self.h, self.wallColor)
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.wallColor)
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif self.version is 'background':
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_backgrounds.add(floor)

        elif self.version is 'wall_1':
            wallTop = Wall(self.x, self.y, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_backgrounds.add(floor)

        elif self.version is 'wall_2':
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif self.version is 'wall_3':
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif self.version is 'wall_4':
            wallLeft = Wall(self.x, self.y, self.t, self.h, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallLeft)
            all_backgrounds.add(floor)

        elif self.version is 'hall_1':
            wallLeft = Wall(self.x, self.y, self.t, self.h, wallColor)
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif self.version is 'hall_2':
            wallTop = Wall(self.x, self.y, self.w, self.t, self.wallColor)
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif self.version is 'corner_1':
            wallTop = Wall(self.x, self.y, self.w,self.t, self.wallColor)
            wallLeft = Wall(self.x, self.y, self.t, self.h, wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_backgrounds.add(floor)

        elif self.version is 'corner_2':
            wallTop = Wall(self.x, self.y, self.w, self.t, self.wallColor)
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif self.version is 'corner_3':
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.wallColor)
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif self.version is 'corner_4':
            wallLeft = Wall(self.x, self.y, self.t, self.h, wallColor)
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif self.version is 'end_1':
            wallLeft = Wall(self.x, self.y, self.t, self.h, wallColor)
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.wallColor)
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif self.version is 'end_2':
            wallTop = Wall(self.x, self.y, self.w, self.t, self.wallColor)
            wallLeft = Wall(self.x, self.y, self.t, self.h, wallColor)
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        elif self.version is 'end_3':
            wallTop = Wall(self.x, self.y, self.w, self.t, self.wallColor)
            wallLeft = Wall(self.x, self.y, self.t, self.h, self.wallColor)
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        elif self.version is 'end_4':
            wallTop = Wall(self.x, self.y, self.w, self.t, self.wallColor)
            wallRight = Wall(self.x+self.w-self.t, self.y, self.t, self.h, self.WallColor)
            wallBottom = Wall(self.x, self.y+self.h-self.t, self.w, self.t, self.wallColor)
            floor = Background(self.x, self.y, self.w, self.h, self.floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)


# The World class updates the global state of the game. This includes
# drawing the world as well as managing the music.

class Circle(object):
    def __init__(self, color, x, y, radius, thickness):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.thickness = thickness
        circle = [self.color, self.x, self.y, self.radius, self.thickness]
        all_circles.append(circle)

    def update():
        for n in range(len(all_circles)):
            all_circles[n][1] += dx
            all_circles[n][2] += dy
            pg.draw.circle(screen, all_circles[n][0], (all_circles[n][1], all_circles[n][2]), all_circles[n][3], all_circles[n][4])


class World():
    def __init__():
        pass

    def update():
        all_walls.update()
        all_backgrounds.update()
        all_actors.update()
        screen.fill(colors.BLACK)
        all_backgrounds.draw(screen)
        all_walls.draw(screen)
        Circle.update()
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
all_circles = []
all_text = []
all_caption = []

history = [False, False]
stage = 0

screen_x = 900
screen_y = 600
initial_x = 0
initial_y = 0
player_size = 25

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

while not done:

    if pg.key.get_pressed()[pg.K_ESCAPE] is 1:
        done = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

# Begin the story here.
    if history[0] is False:
        history[0] = True

        # Rotunda
        Circle((255, 255, 255), 450, -100, 300, 0)
        Build(-350, -825, 15, 700, 800, (205, 205, 205), (150, 150, 150), 'box')
        Build(-750, -225, 15, 400, 200, (205, 205, 205), (150, 150, 150), 'box')
        Build(350, -225, 15, 400, 200, (205, 205, 205), (150, 150, 150), 'box')

        # Side paths
        Build(-550, -25, 15, 50, 1600, colors.BROWN, colors.BROWN, 'background')
        Build(500, -25, 15, 50, 1600, colors.BROWN, colors.BROWN, 'background')

        # Lawn and paths
        Build(-500, -25, 15, 1000, 500, (20, 150, 20), (20, 150, 20), 'background')
        Build(-500, 475, 15, 1000, 50, colors.BROWN, colors.BROWN, 'background')
        Build(-500, 525, 15, 1000, 200, (20, 150, 20), (20, 150, 20), 'background')
        Build(-500, 725, 15, 1000, 50, colors.BROWN, colors.BROWN, 'background')
        Build(-500, 775, 15, 1000, 600, (20, 150, 20), (20, 150, 20), 'background')

        # Building on side
        Build(-750, -25, 15, 200, 200, (130, 100, 100), (150, 150, 180), 'box')
        Build(-750, 175, 15, 200, 200, (125, 95, 95), (145, 145, 185), 'box')
        Build(-850, 375, 15, 300, 450, (150, 80, 80), (160, 40, 40), 'box')
        Build(-700, 825, 15, 150, 600, (160, 180, 160), (140, 120, 120), 'box')

        Build(550, -25, 15, 200, 200, (130, 100, 100), (150, 150, 180), 'box')
        Build(550, 175, 15, 200, 200, (125, 95, 95), (145, 145, 185), 'box')
        Build(550, 375, 15, 300, 450, (150, 80, 80), (160, 40, 40), 'box')
        Build(550, 825, 15, 150, 600, (160, 180, 160), (140, 120, 120), 'box')

        Text("Welcome to the Rotunda, at UVA.", mainFont, colors.WHITE, 18, 1, 2)

    if current_y > 200 and history[1] is False:
        history[1] = True
        all_text = []


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
    clock.tick(60)

    print(current_x, current_y)

pg.quit()
