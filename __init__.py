from Player import *
from Food import *

import random
import pyglet
from pyglet.window import Window, key
from pyglet import shapes

WIDTH = 800
HEIGHT = 600
FPS = 10
TITLE = 'Snake'

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)

LEFT = 65361
RIGHT = 65363
UP = 65362
DOWN = 65364

SCALE = 20

window = Window(WIDTH, HEIGHT, caption = TITLE, resizable = False)

player = Player(WHITE, SCALE)
food = Food(SCALE, GREEN)

score = 0

def main():
    reset()

    pyglet.clock.schedule_interval(update, 1/FPS)
    pyglet.app.run()

@window.event
def on_draw():
    window.clear()

    player.draw(shapes.Rectangle)
    food.draw(shapes.Rectangle)
    pyglet.text.Label(str(score),
                          font_name = 'helvetica',
                          font_size = 20,
                          x = WIDTH / 2, y = HEIGHT - 50,
                          anchor_x='center', anchor_y='center').draw()

def update(fps):
    player.update()

    # check if player collides with food
    if (player.blocks[0].x == food.x and
        player.blocks[0].y == food.y):
        global score
        score += 1
        foodPos = generateFoodGridPos()

        food.x = SCALE * foodPos[0]
        food.y = SCALE * foodPos[1]

        player.blocks.append( Block(player.blocks[-1].x - SCALE, player.blocks[-1].y, SCALE) )

    for i in range(len(player.blocks)):
        if (i != 0):
            if i < len(player.blocks):
                if (player.blocks[0].x == player.blocks[i].x and
                    player.blocks[0].y == player.blocks[i].y):
                        reset()

def generateFoodGridPos():
    MAX_NUM_GRID_X = WIDTH / SCALE
    MAX_NUM_GRID_Y = HEIGHT / SCALE

    posX = random.randint(1, MAX_NUM_GRID_X - 1)
    posY = random.randint(1, MAX_NUM_GRID_Y - 1)

    return ( posX, posY )

def reset():
    global score
    score = 0
    player.blocks = []
    player.blocks.append( Block(WIDTH / 2, HEIGHT / 2, SCALE) )

    foodPos = generateFoodGridPos()

    food.x = SCALE * foodPos[0]
    food.y = SCALE * foodPos[1]

@window.event
def on_key_press(symbol, modifiers):
    if (symbol == LEFT):
        player.velX = -SCALE
        player.velY = 0
    if (symbol == RIGHT):
        player.velX = SCALE
        player.velY = 0
    if (symbol == UP):
        player.velX = 0
        player.velY = SCALE
    if (symbol == DOWN):
        player.velX = 0
        player.velY = -SCALE

if __name__ == '__main__':
    main()