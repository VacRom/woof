############
#Made by VacRom for CS1113
#Music Credits to The Blake Robinson Synthetic Orchestra:
#http://syntheticorchestra.com/
#http://blake.so/bandcamp
#http://youtube.com/dummeh
#############


import pygame as pg
import colors


# Actor represents all the players that are in the game.
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
        # textType 0 is used for cutscenes and freezes the screen for
        # 2s. texType 1 is similar except that it freezes the screen
        # for 5s then erases the text in preparation for the next page
        # of text.
        if textType is 0:
            pg.time.delay(2500)
        elif textType is 1:
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


# The World class updates the global state of the game. This includes
# drawing the world as well as managing the music.
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

history = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

stage = 1

screen_x = 900
screen_y = 600
initial_x = 80
initial_y = 30
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

screen = pg.display.set_mode([screen_x, screen_y], pg.DOUBLEBUF)
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

    if stage is 0:
        if history[0] is False:
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
            Text.mkText('he decided to not question the assignment makers.', mainFont, colors.WHITE, 18, 2, 0)
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

    if stage is 1:
        if history[1] is False:
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

        if current_y > 158:
            stage = 2

        if timer1_time > 60000:
            pg.event.set_allowed(None)
            pg.mixer.music.fadeout(2000)
            all_text = []
            screen.fill(colors.BLACK)
            pg.display.flip()
            Text.mkText('And all was good.', mainFont, colors.WHITE, 18, 1, 1)
            done = True

    elif stage is 2:
        if history[2] is False:
            history[2] = True
            Text.mkText('Filled with curiosity, Red did the unimaginable:', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('he left the room. Red had never made a decision for himself before,', mainFont, colors.WHITE, 18, 2, 2)
            Text.mkText('and he felt uneasy as he walked down this hallway.', mainFont, colors.WHITE, 18, 3, 2)

        if current_x > 250:
            stage = 3

    elif stage is 3:
        if history[3] is False:
            history[3] = True
            World.music('track_2.mp3')
            all_text = []

        if current_x > 500:
            stage = 4

    elif stage is 4:
        if history[4] is False:
            history[4] = True
            Text.mkText('Red found it odd that the others rooms around him were locked.', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('Was he the only one here? Red needed to find out.', mainFont, colors.WHITE, 18, 2, 2)

        if current_x > 1000:
            all_text = []
            stage = 5

    elif stage is 5:
        if current_x > 1400 and history[5] is False:
            history[5] = True
            Text.mkText('Upon reaching the two doors, Red made the decision to enter into', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('the blue door.', mainFont, colors.WHITE, 18, 2, 2)
            stage = 6

    elif stage is 6:
        if current_x in range(1830, 1840) and current_y in range(30, 120):
            history[6] = True
            all_text = []
            dx = +200
            dy = -100
            World.update()
            Text.mkText('Red entered into the blue door.', mainFont, colors.WHITE, 18, 1, 2)
            stage = 7

    elif stage is 7:
        if current_x in range(1830, 1840) and current_y in range(30, 120) and history[7] is False:
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

    elif stage is 8:
        if current_x < 800 and history[8] is False:
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
            Text.mkText("of making incorrect decisions. Well, how about this:", mainFont, colors.WHITE, 18, 2, 1)

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
            Text.mkText('Are you having fun? It was your choice to come here.', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('You did this.', mainFont, colors.WHITE, 18, 2, 2)
        if timer1_time > 65000 and history[23] is False:
            history[23] = True
            all_text = []
        if timer1_time > 100000 and history[24] is False:
            history[24] = True
            Text.mkText('Wait here for just a little longer I have a secret to tell you.', mainFont, colors.WHITE, 18, 1, 2)
        if timer1_time > 110000 and history[25] is False:
            history[25] = True
            all_text = []
        if timer1_time > 180000 and history[26] is False:
            history[26] = True
            Text.mkText('The secret is that you have been in here for three minutes now.', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("Wait just a moment, let me change the music for you.", mainFont, colors.WHITE, 18, 2, 2)
        if timer1_time > 182000 and history[27] is False:
            history[27] = True
            pg.mixer.music.stop
            pg.mixer.music.load('track_4.mp3')
            pg.mixer.music.play(-1, 0)
        if timer1_time > 185000 and history[28] is False:
            history[28] = True
            all_text = []
        if timer1_time > 310000 and history[29] is False:
            history[29] = True
            pg.mixer.music.stop
            Text.mkText("Alright enough of this. Let's give this another go, shall we?", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("I'll forget that any of this ever happened.", mainFont, colors.WHITE, 18, 2, 2)
            Text.mkText("Onto the next stage we go!", mainFont, colors.WHITE, 18, 3, 2)
        if timer1_time > 315000:
            stage = 11

    elif stage is 10:
        if current_x in range(1900, 2000) and current_y in range(60, 120) and history[10] is False:
            history[10] = True
            all_text = []
            Text.mkText('That was really pointless, Red.', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('Really, really, pointless.', mainFont, colors.WHITE, 18, 2, 2)

        if current_x in range(2400, 2500) and current_y in range(60, 120):
            all_text = []

    elif stage is 11:
        if history[11] is False:
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

            'White door'
            Build.mkRoom(-55-112+168-13, -760-336-40, 15, 25, 25, colors.WHITE, colors.WHITE, 'background')

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

            pg.event.set_blocked(None)

            stage = 12

    elif stage is 12:
        if current_y < -300 and history[13] is False:
            history[13] = True
            Text.mkText('Red continued directly down the hall towards his boss room.', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("He'd finally discover exactly what he needs to do.", mainFont, colors.WHITE, 18, 2, 2)
            stage = 13

    elif stage is 13:
        if current_y < -530:
            Build.mkRoom(-55, -460-6, 15, 112, 112, colors.BROWN_0, colors.RED_3, 'wall_1')
            all_text = []
            Text.mkText('Red walked into the next room and discovered the truth.', mainFont, colors.WHITE, 18, 1, 2)
            stage = 14

        if current_y in range(-460, -340):
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

            if current_x > -1700 and history[36] is True and history[37] is False:
                history[37] = True
                all_text = []

            if current_x > -300 and history[37] is True and history[38] is False:
                history[38] = True
                Text.mkText("Red walked into the North hallway.", mainFont, colors.WHITE, 18, 1, 2)

            if current_x in range(-2060, -2050) and history[36] is True:
                pg.event.set_allowed(None)
                all_text = []
                screen.fill(colors.BLACK)
                pg.display.flip()
                Text.mkText("Red's decision was subpar.", mainFont, colors.WHITE, 18, 1, 1)
                done = True

        if current_y in range(-460, -340) and current_x > 170 and history[40] is False:
            history[40] = True
            all_text= []
            Text.mkText("Wait, that door's not supposed to be open.", mainFont, colors.WHITE, 18, 1, 2)

        if current_y in range(-460, -340) and current_x > 470 and history[41] is False:
            history[41] = True
            all_text = []
            Text.mkText("I'm warning you! Don't go there.", mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText("If you go any further you're going to break the game!", mainFont, colors.WHITE, 18, 2, 2)

        if current_y in range(-460, -340) and current_x > 770 and history[42] is False:
            history[42] = True
            all_text = []

        if current_x > 1000:
            pg.mixer.music.fadeout(1)
            stage = 16

    elif stage is 14:
        if current_y < -770:
            stage = 15

    elif stage is 15:
        all_text = []
        all_walls = pg.sprite.Group()
        all_backgrounds = pg.sprite.Group()
        all_sprites = pg.sprite.Group()
        screen.fill(colors.BLACK)
        World.music('track_7.mp3')
        World.update()
        pg.event.set_allowed(None)

        Text.mkText("Red entered the room.", mainFont, colors.WHITE, 18, 1, 1)

        Text.mkText("Sitting upon the armchair across the room was his boss.", mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText("And almost telepathically, Red's boss began to explain", mainFont, colors.WHITE, 18, 2, 0)
        Text.mkText("the nature of Red's very situation.", mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText("Boss: Red! It's so glad to see you here.", mainFont, colors.BLUE_1, 18, 1, 0)
        Text.mkText("I've been watching your progress. And I am pleased to tell you", mainFont, colors.BLUE_1, 18, 2, 0)
        Text.mkText("that you're being promoted!", mainFont, colors.BLUE_1, 18, 3, 1)

        Text.mkText("No longer will you have to stare at walls,", mainFont, colors.BLUE_1, 18, 1, 0)
        Text.mkText("no more of those pointless tasks. We NEED you for something greater.", mainFont, colors.BLUE_1, 18, 2, 1)

        Text.mkText("Now you will be managing levers. Yes, you can pull down on", mainFont, colors.BLUE_1, 18, 1, 0)
        Text.mkText("a number of levers. Some red and some blue.", mainFont, colors.BLUE_1, 18, 2, 0)
        Text.mkText("But there's no need to worry: it will all become clear to you later.", mainFont, colors.BLUE_1, 18, 3, 1)

        Text.mkText("You will have a new office. Square. Brown.", mainFont, colors.BLUE_1, 18, 1, 0)
        Text.mkText("It's nothing like your previous office. I promise you.", mainFont, colors.BLUE_1, 18, 2, 1)

        Text.mkText("Filled with joy that his decision to come here mattered,", mainFont, colors.WHITE, 18, 1, 0)
        Text.mkText("Red happily accepted the offer and headed down the hall, and stepped", mainFont, colors.WHITE, 18, 2, 0)
        Text.mkText("into the elevator.", mainFont, colors.WHITE, 18, 3, 1)

        Text.mkText("As far as Red was concerned, he was happy.", mainFont, colors.WHITE, 18, 1, 1)

        screen.fill(colors.BLACK)
        pg.mixer.music.fadeout(3000)
        Text.mkText("And all was good.", mainFont, colors.WHITE, 18, 1, 1)
        done = True

    elif stage is 16:
        if (current_x > 2500 or current_x < -2500 or current_y > 2500 or current_y < -2500):
            all_text = []
            all_walls = pg.sprite.Group()
            all_backgrounds = pg.sprite.Group()
            all_sprites = pg.sprite.Group()
            screen.fill(colors.BLACK)
            World.update()
            pg.event.set_allowed(None)

            Text.mkText("Red continued walking into the abyss", mainFont, colors.RED_1,  18, 1, 1)

            Text.mkText("and he lost track of time.", mainFont, colors.RED_1, 18, 1, 0)
            Text.mkText("For as far as Red could see, there was nothing here. No offices, no doors, no voices,", mainFont, colors.RED_1, 18, 2, 1)

            Text.mkText("and no walls.", mainFont, colors.RED_1, 18, 1, 1)

            Text.mkText("Red was finally free.", mainFont, colors.RED_1, 18, 1, 1)

            Text.mkText("And all was good.", mainFont, colors.RED_1, 18, 1, 1)

            done = True

        if current_x in range(-10, 20) and current_y in range(-1130, -1110):
            all_text = []
            all_walls = pg.sprite.Group()
            all_backgrounds = pg.sprite.Group()
            all_sprites = pg.sprite.Group()
            screen.fill(colors.BLACK)
            World.music('track_8.mp3')
            World.update_2()
            pg.event.set_allowed(None)

            Text.mkText("It was at this moment that Red realized the truth.", mainFont, colors.RED_1, 18, 1, 1)

            Text.mkText("There was no office, there was no boss,", mainFont, colors.RED_1, 18, 1, 0)
            Text.mkText("and certainly there was no voice that made decisions for him.", mainFont, colors.RED_1, 18, 2, 1)

            Text.mkText("The only thing holding himself back this entire time was himself.", mainFont, colors.RED_1, 18, 1, 1)

            Text.mkText("All along he, alone, had been the one making these decisions.", mainFont, colors.RED_1, 18, 1, 0)
            Text.mkText("And there was nothing to fear about making decisions for himself.", mainFont, colors.RED_1, 18, 2, 0)
            Text.mkText("There was no reason to continue this cycle over and over again.", mainFont, colors.RED_1, 18, 3, 1)

            Text.mkText("It did not matter if the path he took was unnecessarily long.", mainFont, colors.RED_1, 18, 1, 0)
            Text.mkText("for it was his path he forged by himself, and he was happy.", mainFont, colors.RED_1, 18, 2, 1)

            Text.mkText("Satisfied at his epiphany, Red escaped through the white door.", mainFont, colors.RED_1, 18, 1, 1)

            Text.mkText("And all was good.", mainFont, colors.RED_1, 18, 1, 1)

            done = True

    if stage < 8:
        if history[4] is True and current_x in range(0, 160) and current_y in range(0, 160):
            stage = 1
            timer1_time = 60000

    if stage in range(4, 9):
        if current_x in range(1830, 1840) and current_y in range(150, 350):
            all_text = []
            stage = 10
            Text.mkText('At the end of this hall was an elavator which would take him to the above floor.', mainFont, colors.WHITE, 18, 1, 2)
            Text.mkText('Maybe there he would find an answer on what to do next.', mainFont, colors.WHITE, 18, 2, 2)
            Build.mkRoom(1740, 245, 15, 15, 96-15, colors.BROWN_0, colors.BROWN_0, 'box')
            Build.mkRoom(1740, 245-96*2, 15, 15, 96-15, colors.BROWN_0, colors.BROWN_0, 'box')

    if stage < 11:
        if current_x in range(2200, 2250) and current_y > 130:
            all_text = []

        if current_x in range(2675, 2725) and current_y in range(420, 430):
            stage = 11


    # Here are the list of captions in the game.
    if pg.key.get_pressed()[pg.K_SPACE] is 1:
        if current_x in range(25, 136) and current_y in range(25, 136) and stage < 11:
            Text.mkText("Red knew that he shouldn't leave this room. And so, he didn't.", mainFont, colors.BLUE_3, 4, 1, 3)
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

    timer1_time += timer1.get_time()

    World.update()

    timer1.tick(60)
    clock.tick(60)

pg.quit()
