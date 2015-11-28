import game


def mkRoom(x, y, t, w, h, wallColor, floorColor):
    wallTop = game.Wall(x, y, x+w, y+t, wallColor)
    wallLeft = game.Wall(x, y+t, x+t, y+h-t, wallColor)
    wallRight = game.Wall(x+w-t, y+t, x+w, y+h-t, wallColor)
    wallBottom = game.Wall(x, y+h-t, x+w, y+h, wallColor)

    floor = game.Background(x+t, y+t, x+w-t, y+h-t, floorColor)

    game.all_walls.add(wallTop)
    game.all_walls.add(wallLeft)
    game.all_walls.add(wallRight)
    game.all_walls.add(wallBottom)
    game.all_backgrounds.add(floor)
