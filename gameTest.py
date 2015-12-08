############
#Made by VacRom for CS1113
#Music Credits to The Blake Robinson Synthetic Orchestra:
#############


import pygame as pg
import colors

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

history = [False, False, False, False, False]
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

    if stage is 0 and history[0] is False:
        history[0] = True
        # Make the tutorial rooms.
        Build.mkRoom(0, 50, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'box')
        Build.mkRoom(200, 50, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'background')
        Build.mkRoom(400, 50, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'hall_1')
        Build.mkRoom(600, 50, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'hall_2')
        Build.mkRoom(0, 250, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'wall_1')
        Build.mkRoom(200, 250, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'wall_2')
        Build.mkRoom(400, 250, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'wall_3')
        Build.mkRoom(600, 250, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'wall_4')
        Build.mkRoom(0, 450, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'end_1')
        Build.mkRoom(200, 450, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'end_2')
        Build.mkRoom(400, 450, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'end_3')
        Build.mkRoom(600, 450, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'end_4')
        Build.mkRoom(0, 650, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'corner_1')
        Build.mkRoom(200, 650, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'corner_2')
        Build.mkRoom(400, 650, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'corner_3')
        Build.mkRoom(600, 650, 15, 100, 100, colors.BROWN_0, colors.BROWN, 'corner_4')

        Text.mkText("This is a test of the Build class. We can build the world by making many small builds.", mainFont, colors.WHITE, 18, 1, 2)
        Text.mkText("Use the directional arrow keys to move and explore this area.", mainFont, colors.WHITE, 18, 2, 2)
        Text.mkText("When finished with exploring this part, press 2 to continue.", mainFont, colors.WHITE, 18, 3, 2)

    if stage is 1 and history[1] is False:
        history[1] = True
        'First Hall'
        Build.mkRoom(-36, -24, 5, 72, 48, colors.BLUE_1, colors.BLUE_3, 'end_1')
        Build.mkRoom(-55, -348, 15, 112, 324, colors.BROWN_0, colors.RED_3, 'hall_1')
        Build.mkRoom(-40, -39, 15, 15, 15, colors.BROWN_0, colors.RED_3, 'box')
        Build.mkRoom(27, -39, 15, 15, 15, colors.BROWN_0, colors.RED_3, 'box')
        Build.mkRoom(-55-15, -460, 15, 112, 112, colors.BROWN_0, colors.RED_3, 'background')

        'North Hall'
        Build.mkRoom(-55, -760, 15, 112, 300, colors.BROWN_0, colors.RED_3, 'hall_1')

        'Office'
        Build.mkRoom(-55-112, -760-336, 15, 336, 336, colors.BROWN_0, colors.RED_3, 'hall_1')
        Build.mkRoom(-55-112, -760-336, 15, 112+15, 336, colors.BROWN_0, colors.RED_3, 'wall_3')
        Build.mkRoom(-55+112-15, -760-336, 15, 112+15, 336, colors.BROWN_0, colors.RED_3, 'wall_3')

        'West Hall'
        Build.mkRoom(-55-300-1700, -348-112, 15, 300+15+1700, 112, colors.BROWN_0, colors.RED_3, 'hall_2')
        Build.mkRoom(-55-300-1700-112, -348-112, 15, 112, 112, colors.BROWN_0, colors.BLACK, 'end_2')

        'East Hall'
        Build.mkRoom(-55+112-15, -348-112, 15, 1000, 112, colors.BROWN_0, colors.RED_3, 'hall_2')

        'Rooms'
        Build.mkRoom(-200, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-400, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-600, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-800, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1000, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1200, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1400, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1600, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1800, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-2000, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')

        Build.mkRoom(-200, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-400, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-600, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-800, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1000, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1200, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1400, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1600, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-1800, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(-2000, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')

        Build.mkRoom(-200+112+160-30, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(0+112+160-30, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(200+112+160-30, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(400+112+160-30, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(600+112+160-30, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(800+112+160-30, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(1000+112+160-30, -600, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')

        Build.mkRoom(-200+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(0+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(200+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(400+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(600+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(800+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')
        Build.mkRoom(1000+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')

        Text.mkText("Here is an entire floor of a building from my game.", mainFont, colors.WHITE, 18, 1, 2)
        Text.mkText("Note that colors can be changed according to the user's needs.", mainFont, colors.WHITE, 18, 2, 2)
        Text.mkText("This is tutorial room 2. Press 3 to continue, or 1 to visit the previous tutorial.", mainFont, colors.WHITE, 18, 3, 2)

    if stage is 2:
        if history[2] is False:
            history[2] = True
            musicOn = False

            Build.mkRoom(-200, 50, 15, 100, 100, colors.BROWN_0, colors.RED_0, 'background')
            Build.mkRoom(-100, 50, 15, 100, 100, colors.BROWN_0, colors.RED_1, 'background')
            Build.mkRoom(0, 50, 15, 100, 100, colors.BROWN_0, colors.RED_2, 'background')
            Build.mkRoom(100, 50, 15, 100, 100, colors.BROWN_0, colors.RED_3, 'background')
            Build.mkRoom(200, 50, 15, 100, 100, colors.BROWN_0, colors.RED_4, 'background')
            Build.mkRoom(300, 50, 15, 100, 100, colors.BROWN_0, colors.WHITE, 'background')

            Text.mkText("Here is a demonstration of the custom color pallets that you can make.", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("Furthermore, step in these squares to play some music! Step out to reset the music", mainFont, colors.WHITE, 18, 2, 2)
            Text.mkText("and step in another to choose a different song. Press 4 to continue.", mainFont, colors.WHITE, 18, 3, 2)

        if current_y in range(50, 150) and musicOn is 0:
            if current_x in range(-200, -100):
                World.music('track_1.mp3')
                musicOn = 1
            elif current_x in range(-100, 0):
                World.music('track_2.mp3')
                musicOn = 2
            elif current_x in range(0, 100):
                World.music('track_3.mp3')
                musicOn = 3
            elif current_x in range(100, 200):
                World.music('track_4.mp3')
                musicOn = 4
            elif current_x in range(200, 300):
                World.music('track_5.mp3')
                musicOn = 5
            elif current_x in range(300, 400):
                World.music('track_6.mp3')
                musicOn = 6
        if current_y not in range(50, 150) or current_x not in range(-200, 400):
                musicOn = 0
                pg.mixer.music.fadeout(10)

    if stage is 3:
        if history[3] is False:
            pg.event.set_allowed(None)

            Text.mkText('This is an example of a cutscene.', mainFont, colors.WHITE, 18, 1, 0)
            Text.mkText('Players cannot interact with actors during a cutscene.', mainFont, colors.WHITE, 18, 2, 0)
            Text.mkText('However, the code can still manipulate the world.', mainFont, colors.WHITE, 18, 3, 1)

            Build.mkRoom(0, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'box')
            World.update()

            Text.mkText('For example, we can build this room.', mainFont, colors.WHITE, 18, 1, 1)

            Build.mkRoom(200, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'box')
            Build.mkRoom(-200, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'box')
            World.update()

            Text.mkText('Or any of these rooms.', mainFont, colors.WHITE, 18, 1, 1)

            Text.mkText('You can move as soon as the cutscene is over', mainFont, colors.WHITE, 18, 1, 0)
            Text.mkText('Press 5 to continue.', mainFont, colors.WHITE, 18, 2, 1)
            pg.event.set_blocked(None)

            history[3] = True
            all_text = []
            # Due to a bug, the map gets erased upon completing this
            # specific cutscene.

    if stage is 4 and history[4] is False:
        history[4] = True
        current_x = 80
        current_y = 30
        'Starting office'
        Build.mkRoom(0, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'end_3')
        Build.mkRoom(0, 145, 15, 60, 15, colors.BROWN_0, colors.BLUE, 'box')
        Build.mkRoom(100, 145, 15, 60, 15, colors.BROWN_0, colors.BLUE, 'box')
        'Closed offices'
        Build.mkRoom(200, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        Build.mkRoom(400, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        Build.mkRoom(600, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        Build.mkRoom(-210, 105, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        Build.mkRoom(0, 210, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        Build.mkRoom(200, 210, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        Build.mkRoom(400, 210, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        Build.mkRoom(600, 210, 15, 160, 160, colors.BROWN_0, colors.BROWN_1, 'box')
        'Hallway'
        Build.mkRoom(100, 145, 15, 750, 80, colors.BROWN_0, colors.BROWN, 'hall_2')
        Build.mkRoom(-50, 145, 15, 115, 80, colors.BROWN_0, colors.BROWN, 'hall_2')
        Build.mkRoom(0, 145, 15, 160, 80, colors.BROWN_0, colors.BROWN, 'wall_3')

        Text.mkText("This final tutorial is on captions. Captions are text that pop up", mainFont, colors.WHITE, 4, 1, 2)
        Text.mkText("when you press the interact (SPACE) button in certain rooms.", mainFont, colors.WHITE, 4, 2, 2)
        Text.mkText("This is the end of the mini-tutorial. Press ESC to exit.", mainFont, colors.RED, 4, 3, 2)

    # Captions
    if pg.key.get_pressed()[pg.K_SPACE] is 1:
        if stage is 4:
            if current_x in range(25, 136) and current_y in range(25, 136) and stage < 11:
                Text.mkText("This is an example of a caption.", mainFont, colors.BLUE_3, 4, 1, 3)
            elif current_x in range(-41, -35) and current_y in range(169, 199) and stage < 11:
                Text.mkText("Room 855: Lunch Room.", mainFont, colors.BLUE_3, 4, 1, 3)
                Text.mkText("Today's lunch menu: Turkey surprise!", mainFont, colors.BLUE_3, 4, 2, 4)
                Text.mkText("The surprise is that there is no turkey.", mainFont, colors.BLUE_3, 4, 3, 4)
            elif current_x in range(77, 83) and current_y in range(193, 199) and stage < 11:
                Text.mkText("Room 856: Button Presser.", mainFont, colors.BLUE_3, 4, 3, 3)
            elif current_x in range(277, 283) and current_y in range(193, 199) and stage < 11:
                Text.mkText("Room 857: Pencil Sharpener-er.", mainFont, colors.BLUE_3, 4, 3, 3)
            elif current_x in range(477, 483) and current_y in range(193, 199) and stage < 11:
                Text.mkText("Room 858: Lever puller.", mainFont, colors.BLUE_3, 4, 3, 3)
            elif current_x in range(677, 683) and current_y in range(193, 199) and stage < 11:
                Text.mkText("Room 859: Lever pusher.", mainFont, colors.BLUE_3, 4, 3, 3)
            elif current_x in range(77, 83) and current_y in range(169, 173) and stage < 11:
                Text.mkText("Room 854: Starer.", mainFont, colors.BLUE_3, 4, 3, 3)
            elif current_x in range(277, 283) and current_y in range(169, 173) and stage < 11:
                Text.mkText("Room 853: vacant.", mainFont, colors.BLUE_3, 4, 3, 3)
            elif current_x in range(477, 483) and current_y in range(169, 173) and stage < 11:
                Text.mkText("Room 852: vacant.", mainFont, colors.BLUE_3, 4, 3, 3)
            elif current_x in range(677, 683) and current_y in range(169, 173) and stage < 11:
                Text.mkText("Room 851: Safety inspector.", mainFont, colors.BLUE_3, 4, 3, 3)
            else:
                all_caption = []

    if pg.key.get_pressed()[pg.K_SPACE] is 0:
        all_caption = []

    # Change stage
    if event.type is pg.KEYDOWN and event.key is pg.K_1:
        history[stage] = False
        stage = 0
        current_x = current_y = 0
        all_text = []
        all_caption = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()

    if event.type is pg.KEYDOWN and event.key is pg.K_2:
        history[stage] = False
        stage = 1
        current_x = current_y = 0
        all_text = []
        all_caption = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()

    if event.type is pg.KEYDOWN and event.key is pg.K_3:
        history[stage] = False
        stage = 2
        current_x = current_y = 0
        all_text = []
        all_caption = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()

    if event.type is pg.KEYDOWN and event.key is pg.K_4:
        history[stage] = True
        stage = 3
        current_x = 80
        current_y = 30
        all_text = []
        all_caption = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()

    if event.type is pg.KEYDOWN and event.key is pg.K_5:
        history[stage] = False
        stage = 4
        current_x = 80
        current_y = 30
        all_text = []
        all_caption = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()

    if stage not in range(0, len(history)):
        stage = 0

    # Player movement
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

pg.quit()
