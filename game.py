############
#Made by VacRom for CS1113
#Music Credits to The Blake Robinson Synthetic Orchestra:
#http://syntheticorchestra.com/
#http://blake.so/bandcamp
#http://youtube.com/dummeh
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
        row = row*22
        text = [font.render(text, 1, color), center_x-margins+3, screen_y-170+row+3]
        all_text.append(text)
        Text.update()
        # textType 0 is freeze the screen then wait 2s, 1 is freeze
        # then wait 5s, and 2 is display without freeze.
        if textType is 0:
            pg.time.delay(2500)
        elif textType is 1:
            pg.time.delay(4500)
            all_text = []
        elif textType is 2:
            pass

    def update():
        if len(all_text) != 0:
            all_textBorder.draw(screen)
            all_textBox.draw(screen)
            for n in range(len(all_text)):
                screen.blit(all_text[n][0], (all_text[n][1], all_text[n][2]))
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

        if version is 'box':
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

        if version is 'background':
            floor = Background(x, y, w, h, floorColor)
            all_backgrounds.add(floor)

        if version is 'wall_1':
            wallTop = Wall(x, y, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_backgrounds.add(floor)

        if version is 'wall_2':
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        if version is 'wall_3':
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        if version is 'wall_4':
            wallLeft = Wall(x, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_backgrounds.add(floor)

        if version is 'hall_1':
            wallLeft = Wall(x, y, t, h, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        if version is 'hall_2':
            wallTop = Wall(x, y, w, t, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        if version is 'corner_1':
            wallTop = Wall(x, y, w, t, wallColor)
            wallLeft = Wall(x, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_backgrounds.add(floor)

        if version is 'corner_2':
            wallTop = Wall(x, y, w, t, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        if version is 'corner_3':
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        if version is 'corner_4':
            wallLeft = Wall(x, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        if version is 'end_1':
            wallLeft = Wall(x, y, t, h, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        if version is 'end_2':
            wallTop = Wall(x, y, w, t, wallColor)
            wallLeft = Wall(x, y, t, h, wallColor)
            wallBottom = Wall(x, y+h-t, w, t, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallBottom)
            all_backgrounds.add(floor)

        if version is 'end_3':
            wallTop = Wall(x, y, w, t, wallColor)
            wallLeft = Wall(x, y, t, h, wallColor)
            wallRight = Wall(x+w-t, y, t, h, wallColor)
            floor = Background(x, y, w, h, floorColor)
            all_walls.add(wallTop)
            all_walls.add(wallLeft)
            all_walls.add(wallRight)
            all_backgrounds.add(floor)

        if version is 'end_4':
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

history = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

stage = 11

screen_x = 900
screen_y = 600
initial_x = 80
initial_y = 30
player_size = 25
mainFont = pg.font.SysFont('oldstandard', 18)
secondFont = pg.font.SysFont('ptsans', 18)
thirdFont = pg.font.SysFont('raleway', 18)
textBoxState = False

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

screen = pg.display.set_mode([screen_x, screen_y])
#screen = pg.display.set_mode([screen_x, screen_y], pg.DOUBLEBUF | pg.NOFRAME | pg.FULLSCREEN)
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

        pg.event.set_allowed(None)
        World.music('track_1.mp3')
        World.update()

        Text.mkText('This is the story of Red.', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('Red is a simple shape, and he leads a simple life.', mainFont, colors.WHITE, 18, 2, 0)

        Build.mkRoom(0, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'box')
        World.update()

        Text.mkText('Here is his office. It is his very own, and he is very glad to be in it.', mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText('For an uncountable number of days, Red sat in this office', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('completing a number of different assignments.', mainFont, colors.WHITE, 18, 2, 1)

        Text.mkText("Today's assignment was to stare at this wall", mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText("which he enjoyed far more than yesterday's assignment:", mainFont, colors.WHITE, 18, 2, 0)
        Text.mkText('to stare at the ceiling.', mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText('Although Red did not always understand why he continued with these tasks', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('Red decided to not question the assignment makers.', mainFont, colors.WHITE, 18, 2, 0)
        Text.mkText('After all, Red has always lived his life in this way.', mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText('Life is simple in this room - unlike the confusing world out there', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('with all those difficult decisions that are needed to be made.', mainFont, colors.WHITE, 18, 2, 0)
        Text.mkText('No, Red did not bother himself with those things in life.', mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText('And so, Red stared and stared and stared...', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('and stared and stared...', mainFont, colors.WHITE, 18, 2, 0)
        Text.mkText('and most importantly, did not leave the room.', mainFont, colors.WHITE, 18, 3, 1)

        pg.event.set_blocked(None)

        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        stage = 1

    if stage is 1 and history[1] is False:
        history[1] = True

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

        'Main Room'
        Build.mkRoom(835, -55, 15, 900, 215, colors.BROWN_0, colors.BROWN, 'corner_1')
        Build.mkRoom(835, 210, 15, 900, 215, colors.BROWN_0, colors.BROWN, 'corner_4')
        Build.mkRoom(835, 150, 0, 900, 100, colors.BROWN_0, colors.BROWN, 'background')
        Build.mkRoom(1735, -55, 15, 15, 96, colors.BROWN_0, colors.BROWN, 'wall_2')
        Build.mkRoom(1735, -55+2*96, 15, 15, 96, colors.BROWN_0, colors.BROWN, 'wall_2')
        Build.mkRoom(1735, -55+4*96, 15, 15, 96, colors.BROWN_0, colors.BROWN, 'wall_2')

        'Top Door'
        Build.mkRoom(1735, -55+1*96, 15, 800, 96, colors.BROWN_0, colors.BROWN, 'hall_2')

        'Bottom Door'
        Build.mkRoom(1735, -55+3*96, 15, 800, 96, colors.BROWN_0, colors.BROWN, 'hall_2')

        'Door Colors'
        Build.mkRoom(1735, -55+1*96-30, 15, 96, 30, colors.RED_3, colors.RED_3, 'background')
        Build.mkRoom(1735, -55+2*96, 15, 96, 30, colors.RED_3, colors.RED_3, 'background')

        Build.mkRoom(1735, -55+3*96-30, 15, 96, 30, colors.BLUE_3, colors.BLUE_3, 'background')
        Build.mkRoom(1735, -55+4*96, 15, 96, 30, colors.BLUE_3, colors.BLUE_3, 'background')

        'Second Room'
        Build.mkRoom(2535, -55, 15, 350, 400, colors.BROWN_0, colors.BROWN, 'corner_2')
        Build.mkRoom(2535, -55, 15, 15, 96+15, colors.BROWN_0, colors.BROWN, 'box')
        Build.mkRoom(2535, -55+96*2-15, 15, 15, 96+30, colors.BROWN_0, colors.BROWN, 'box')
        Build.mkRoom(2535, -55+96*4-15, 15, 150, 96, colors.BROWN_0, colors.BROWN, 'corner_4')
        Build.mkRoom(2735, -55+96*4-15, 15, 150, 96, colors.BROWN_0, colors.BROWN, 'corner_3')
        Build.mkRoom(2635, -55+96*4-15, 0, 150, 96, colors.BROWN_0, colors.BROWN, 'background')
        Build.mkRoom(2675, -55+96*5-15, 5, 72, 48, colors.BLUE_1, colors.BLUE_3, 'end_1')

        timer1_time = 0
        timer1 = pg.time.Clock()

    if stage is 1 and current_y > 158:
        stage = 2

    if stage is 1 and timer1_time > 60000:
        pg.event.set_allowed(None)
        pg.mixer.music.fadeout(2000)
        all_text = []
        screen.fill(colors.BLACK)
        pg.display.flip()
        Text.mkText('And all was good.', mainFont, colors.WHITE, 18, 1, 1)
        pg.quit()

    if stage is 2 and history[2] is False:
        history[2] = True
        Text.mkText('Filled with curiosity, Red did the unimaginable:', mainFont, colors.WHITE, 18, 1, 2)
        Text.mkText('he left the room. Red had never made decisions before', mainFont, colors.WHITE, 18, 2, 2)
        Text.mkText('and it was an uneasy feeling that filled him with excitement.', mainFont, colors.WHITE, 18, 3, 2)

    if stage is 2 and current_x > 250:
        stage = 3

    if stage is 3 and history[3] is False:
        history[3] = True
        World.music('track_2.mp3')
        all_text = []

    if stage is 3 and current_x > 500:
        stage = 4

    if stage is 4 and history[4] is False:
        history[4] = True
        Text.mkText('Red continued down the hall.', mainFont, colors.WHITE, 18, 1, 2)

    if current_x in range(750, 800):
        all_text = []

    if history[4] is True and current_x in range(0, 160) and current_y in range(0, 160) and stage < 8:
        stage = 1
        timer1_time = 60000

    if stage is 4 and current_x > 1000:
        all_text = []
        stage = 5

    if stage is 5 and current_x > 1400 and history[5] is False:
        history[5] = True
        Text.mkText('Upon reaching the two doors, Red made the decision to enter into', mainFont, colors.WHITE, 18, 1, 2)
        Text.mkText('the blue one.', mainFont, colors.WHITE, 18, 2, 2)
        stage = 6

    if stage is 6 and current_x in range(1830, 1840) and current_y in range(30, 120):
        history[6] = True
        all_text = []
        dx = +200
        dy = -100
        World.update()
        Text.mkText('Red entered the BLUE door.', mainFont, colors.WHITE, 18, 1, 2)
        stage = 7

    if stage is 7 and current_x in range(1830, 1840) and current_y in range(30, 120) and history[7] is False:
        history[7] = True
        all_text = []
        dx = +200
        dy = -100
        all_walls.update()
        all_backgrounds.update()
        all_actors.update()

        Text.mkText('Red learned a valuable lesson on the inconvenience of colorblindness.', mainFont, colors.WHITE, 18, 1, 2)
        Build.mkRoom(1740, 245-96*2, 15, 15, 96-15, colors.BROWN_0, colors.BROWN_0, 'box')
        Build.mkRoom(800, 110, 15, 40, 35, colors.RED_3, colors.RED_3, 'background')
        Build.mkRoom(800, 110+96+15, 15, 40, 35, colors.RED_3, colors.RED_3, 'background')
        stage = 8

    if stage is 8 and current_x < 800 and history[8] is False:
        history[8] = True

        pg.event.set_allowed(None)

        all_text = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()

        current_x = 80
        current_y = 30

        World.update()
        World.music('track_1.mp3')

        Text.mkText('This is the story of Red.', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('Red is incapable of listening to others.', mainFont, colors.WHITE, 18, 2, 0)

        Build.mkRoom(0, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'box')
        World.update()

        Text.mkText('Here he is all alone in his office.', mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText('Did you know the color red symbolizes braveness?', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('And also arrogance. I thought you should know that.', mainFont, colors.WHITE, 18, 2, 1)

        Text.mkText("This aside, clearly Red does not understand the consequences", mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText("of not following the script. Well, how about this:", mainFont, colors.WHITE, 18, 2, 1)

        Text.mkText('Red did whatever he wanted.', mainFont, colors.WHITE, 18, 1, 1)

        pg.event.set_blocked(None)

        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()

        Build.mkRoom(0, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'box')
        stage = 9

    if stage is 9:
        if history[9] is False:
            timer1 = pg.time.Clock()
            timer1_time = 1
        history[9] = True
        if timer1_time > 20000 and history[20] is False:
            history[20] = True
            all_text = []
            Text.mkText('Marvelous, Red. This story is far more interesting', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('than that one I had in mind.', mainFont, colors.WHITE, 18, 2, 2)
        if timer1_time > 25000 and history[21] is False:
            history[21] = True
            all_text = []
        if timer1_time > 60000 and history[22] is False:
            history[22] = True
            all_text = []
            Text.mkText('Are you having fun?', mainFont, colors.WHITE, 18, 1, 2)
        if timer1_time > 65000 and history[23] is False:
            history[23] = True
            all_text = []
        if timer1_time > 100000 and history[24] is False:
            history[24] = True
            Text.mkText('Wait here for just a little longer I have a secret to tell you.', mainFont, colors.WHITE, 18, 1, 2)
        if timer1_time > 110000 and history[25] is False:
            history[25] = True
            all_text = []
        if timer1_time > 300000 and history[26] is False:
            history[26] = True
            Text.mkText('The secret is that you have been in here for five minutes now.', mainFont, colors.WHITE, 18, 1, 2, 2)
            Text.mkText("Wait just a moment, let me change the music for you.", mainFont, colors.WHITE, 18, 2, 2)
        if timer1_time > 302000 and history[27] is False:
            history[27] = True
            pg.mixer.music.stop
            pg.mixer.music.load('track_4.mp3')
            pg.mixer.music.play(-1, 0)
        if timer1_time > 305000 and history[28] is False:
            history[28] = True
            all_text = []
        if timer1_time > 430000 and history[29] is False:
            pg.mixer.music.stop
            Text.mkText("Alright, Red, let's give this another go, shall we?", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("I'll forget that any of this ever happened.", mainFont, colors.WHITE, 18, 2, 2)
        if timer1_time > 435000:
            stage = 11

    if stage in range(4, 9) and current_x in range(1830, 1840) and current_y in range(150, 350):
        all_text = []
        stage = 10
        Text.mkText('At the end of this hall was an elavator which would take him to the above floor.', mainFont, colors.WHITE, 18, 1, 2)
        Text.mkText('Maybe there he would find an answer on what to do.', mainFont, colors.WHITE, 18, 2, 2)
        Build.mkRoom(1740, 245, 15, 15, 96-15, colors.BROWN_0, colors.BROWN_0, 'box')
        Build.mkRoom(1740, 245-96*2, 15, 15, 96-15, colors.BROWN_0, colors.BROWN_0, 'box')

    if stage is 10 and current_x in range(1900, 2000) and current_y in range(60, 120):
        history[10] = True
        all_text = []
        Text.mkText('That was really pointless, Red.', mainFont, colors.WHITE, 18, 1, 2)
        Text.mkText('Really, really, pointless.', mainFont, colors.WHITE, 18, 2, 2)

    if stage is 10 and current_x in range(2400, 2500) and current_y in range(60, 120):
        all_text = []

    if stage < 11 and current_x in range(2200, 2250) and current_y > 130:
        all_text = []

    if current_x in range(2675, 2725) and current_y in range(420, 430):
        stage = 11

    if stage is 11 and history[11] is False:
        history[11] = True
        timer1 = pg.time.Clock()
        timer1_time = 0
        all_text = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()
        screen.fill(colors.BLACK)
        World.music('track_5.mp3')
        current_x = 0
        current_y = 0
        World.update()
        pg.event.set_allowed(None)

        Text.mkText('Red stepped into the elavator, and the doors shut behind him.', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText('Strangely, the machine had no buttons. Instead, it began to move on its own,', mainFont, colors.WHITE, 18, 2, 0)
        Text.mkText('almost as if the destination were already decided for him.', mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText('Red wished that the doors would never open:', mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText("at the very least, in here there are no choices to be made.", mainFont, colors.WHITE, 18, 2, 1)

        Text.mkText('Moreover, what purpose would an elevator serve if it did not do as it was ordered?', mainFont, colors.WHITE, 18, 1, 1)

        pg.mixer.music.fadeout(3000)

        Text.mkText('The doors opened.', mainFont, colors.WHITE, 18, 1, 1)

        World.music('track_6.mp3')

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
        if history[8] is False:
            Build.mkRoom(-55, -348-112, 15, 116, 112, colors.BROWN_0, colors.RED_3, 'wall_2')

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
        Build.mkRoom(-200+112+160-30, -368, 15, 160, 160, colors.BROWN_0, colors.RED_4, 'box')

        pg.event.set_blocked(None)

        stage = 12

    if stage is 12 and current_y < -300 and history[13] is False:
        history[13] = True
        Text.mkText('Red continued directly down the hall towards his boss room.', mainFont, colors.WHITE, 18, 1, 2)
        Text.mkText("He'd finally discover exactly what he needs to do.", mainFont, colors.WHITE, 18, 2, 2)
        stage = 13

    if stage is 13 and current_y < -530:
        Build.mkRoom(-55, -460-6, 15, 112, 112, colors.BROWN_0, colors.RED_3, 'wall_1')
        all_text = []
        Text.mkText('Red walked into the next room and discovered the truth.', mainFont, colors.WHITE, 18, 1, 2)
        stage = 14

    if stage is 13 and current_y in range(-460, -340):
        if current_x < -100 and history[30] is False:
            history[30] = True
            all_text = []
            Text.mkText('Red walked down the West hallway', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('which is also known as the Wrong Hallway.', mainFont, colors.WHITE, 18, 2, 2)
        if current_x < -400 and history[31] is False:
            history[31] = True
            all_text = []
            Text.mkText('What Red did not know was that this hallway, was in fact,', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('was filled with thousands of extremely venomous spiders.', mainFont, colors.WHITE, 18, 2, 2)
        if current_x < -700 and history[32] is False:
            history[32] = True
            Text.mkText("... and a clown.", mainFont, colors.WHITE, 18, 3, 2)

        if current_x < -1000 and history[33] is False:
            history[33] = True
            all_text = []
            Text.mkText("It is determined that the company's clown detecting device must be dysfunctional.", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("All that's currently in this hallway is Red.", mainFont, colors.WHITE, 18, 2, 2)

        if current_x < -1300 and history[34] is False:
            history[34] = True
            all_text = []
            Text.mkText("Not that Red would have known, but his superiors have been keeping", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("a record on his recent performance. It says: failure.", mainFont, colors.WHITE, 18, 2, 2)

        if current_x < -1600 and history[35] is False:
            history[35] = True
            all_text = []
            Text.mkText("It's odd that someone would take the effort to write 'failure' a thousand times.", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("It's fortunate that Red would have no means of ever discovering these records.", mainFont, colors.WHITE, 18, 2, 2)

        if current_x < -1900 and history[36] is False:
            history[36] = True
            all_text = []
            Text.mkText("This is a pit. Why there's a pit here is nobody's business - except maybe", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("the safety manager. But he fell into the pit last week and now he is no more.", mainFont, colors.WHITE, 18, 2, 2)
            Text.mkText("Even Red knew the consequences of attempting to walk over a pit.", mainFont, colors.WHITE, 18, 3, 2)

        if current_x > -1700 and history[36] is True:
            all_text = []

        if current_x in range(-2060, -2050) and history[36] is True:
            pg.event.set_allowed(None)
            all_text = []
            screen.fill(colors.BLACK)
            pg.display.flip()
            Text.mkText("Red's decision was subpar.", mainFont, colors.WHITE, 18, 1, 1)
            pg.quit()
            
    if stage is 13 and current_y in range(-460, -340) and current_x > 170:
        all_text= []
        stage = 16
# History8 is the long one.
# People are not machines. Free will.

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

    timer1_time += timer1.get_time()

    World.update()

    timer1.tick(60)
    clock.tick(60)
    print(current_x,current_y, stage, timer1_time)

pg.quit()
