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
        self.image = pg.Surface([2*margins+10, 75+10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = center_x-margins-5
        self.rect.y = screen_y-150-5
        self.wall = None

    def update(self):
        pass


class Text():
    def mkText(text, font, color, size, row):
        row = row*22
        text = [font.render(text, 1, color), center_x-margins+3, screen_y-170+row+3]
        all_text.append(text)

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
        x += -offset_x
        y += -offset_y

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

pg.init()

all_walls = pg.sprite.Group()
all_backgrounds = pg.sprite.Group()
all_actors = pg.sprite.Group()
all_sprites = pg.sprite.Group()
all_textBorder = pg.sprite.Group()
all_textBox = pg.sprite.Group()
all_text = []
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
textBoxState = False

center_x = int(screen_x/2)
center_y = int(screen_y/2)
margins = int((screen_x-200)/2)
player_center = int(player_size/2)
offset_x = initial_x-center_x
offset_y = initial_y-center_y
current_x = initial_x
current_y = initial_y

player = Actor(center_x-player_center, center_y-player_center)
all_actors.add(player)

textBorder = TextBorder(colors.BLUE_0)
all_textBorder.add(textBorder)

textBox = TextBox(colors.BLACK)
all_textBox.add(textBox)

screen = pg.display.set_mode([screen_x, screen_y], pg.DOUBLEBUF | pg.NOFRAME)
pg.display.set_caption('Project')

dx = 0
dy = 0
hitWall = False
hitPosWall = ''

clock = pg.time.Clock()
done = False

while not done:

    if pg.key.get_pressed()[pg.K_ESCAPE] is 1:
        done = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    if stage is 0 and history[0] is False:
        history[0] = True

        pg.event.set_allowed(None)
        pg.mixer.music.load('track_1.mp3')
        pg.mixer.music.play(-1, 0)
        screen.fill(colors.BLACK)

        all_actors.draw(screen)
        Text.mkText('This is the story of Red.', mainFont, colors.WHITE, 18, 1)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('Red is a simple shape, and he lives a simple life.', mainFont, colors.WHITE, 18, 2)
        Text.update()
        pg.time.delay(2500)

        Build.mkRoom(0, 0, 15, 160, 160, colors.BROWN_0, colors.BROWN, 'box')
        Text.mkText('Here is his office. It is his very own, and he is very glad to be in it.', mainFont, colors.WHITE, 18, 3)
        all_walls.update()
        all_backgrounds.update()
        Text.update()
        all_backgrounds.draw(screen)
        all_walls.draw(screen)
        all_actors.draw(screen)
        pg.display.flip()
        pg.time.delay(5000)

        all_text = []
        Text.mkText('Red is the ideal employee: he never misses work,', mainFont, colors.WHITE, 18, 1)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('he never causes trouble, and he never misses his assignments.', mainFont, colors.WHITE, 18, 2)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('He has many assignments.', mainFont, colors.WHITE, 18, 3)
        Text.update()
        pg.time.delay(5000)

        all_text = []
        Text.mkText('Too many assignments.', mainFont, colors.WHITE, 18, 1)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('But Red does not complain, because he is safe here in this office', mainFont, colors.WHITE, 18, 2)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('and everything he had ever wanted is in this office.', mainFont, colors.WHITE, 18, 3)
        Text.update()
        pg.time.delay(5000)

        all_text = []
        Text.mkText('He is happy.', mainFont, colors.WHITE, 18, 1)
        Text.update()
        pg.time.delay(5000)

        all_text = []
        Text.mkText('Inside his office he works all day', mainFont, colors.WHITE, 18, 1)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('and all night. But Red is happy to work in his office. And all is good.', mainFont, colors.WHITE, 18, 2)
        Text.update()
        pg.time.delay(5000)

        all_text = []
        Text.mkText('More importantly, Red does not break the rules.', mainFont, colors.WHITE, 18, 1)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('One rule here is that no one is allowed to leave their offices.', mainFont, colors.WHITE, 18, 2)
        Text.update()
        pg.time.delay(2500)

        Text.mkText('Not that the thought ever crossed his mind. Red is good.', mainFont, colors.WHITE, 18, 3)
        Text.update()
        pg.time.delay(5000)

        all_text = []
        Text.mkText('Red did not leave his office.', mainFont, colors.WHITE, 18, 1)
        Text.update()
        pg.time.delay(5000)

        pg.event.set_blocked(None)

        all_text = []
        stage = 'ready'
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
        Build.mkRoom(100, 145, 15, 800, 80, colors.BROWN_0, colors.BROWN, 'hall_2')
        Build.mkRoom(-50, 145, 15, 115, 80, colors.BROWN_0, colors.BROWN, 'hall_2')
        Build.mkRoom(0, 145, 15, 160, 80, colors.BROWN_0, colors.BROWN, 'wall_3')

        timer1_time = 0
        timer1 = pg.time.Clock()

    if stage is 1 and current_y > 158:
        stage = 2

    if stage is 1 and timer1_time > 60000:
        pg.mixer.music.fadeout(3000)
        all_text = []
        Text.mkText('And all was good.', mainFont, colors.WHITE, 18, 1)

        screen.fill(colors.BLACK)
        Text.update()

        pg.display.flip()
        pg.time.delay(5000)
        pg.quit()

    if stage is 2 and history[2] is False:
        history[2] = True
        Text.mkText('Red did not leave his office.', mainFont, colors.WHITE, 18, 1)
        Text.mkText('But this time his curiosity got the better of him.', mainFont, colors.WHITE, 18, 2)

    if stage is 2 and current_x > 250:
        stage = 3

    if stage is 3 and history[3] is False:
        history[3] = True
        all_text = []

    if stage is 3 and current_x > 400:
        stage = 4

    if stage is 4 and history[4] is False:
        history[4] = True
        Text.mkText('Red is breaking the rules.', mainFont, colors.WHITE, 18, 1)
        Text.mkText('But for what purpose? Red was happy in his office.', mainFont, colors.WHITE, 18, 2)
        Text.mkText('It is not too late to turn back.', mainFont, colors.WHITE, 18, 3)

    if history[4] == True and current_x in range(0, 160) and current_y in range(0, 160):
        stage = 1
        timer1_time = 60000

    if stage is 4 and current_x > 500:
        dx = +300
        all_walls.update()
        all_backgrounds.update()
        all_actors.update()
        stage = 5

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

    all_walls.update()
    all_backgrounds.update()
    all_actors.update()
    Text.update()

    screen.fill(colors.BLACK)
    all_backgrounds.draw(screen)
    all_walls.draw(screen)
    all_actors.draw(screen)
    Text.update()

    pg.display.flip()
    timer1.tick(60)
    clock.tick(60)
    print(current_x,current_y)

pg.quit()
