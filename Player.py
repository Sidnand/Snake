class Player:
    def __init__(self, color, scale):
        self.blocks = [] # store a list of blocks
        self.velX = scale
        self.velY = 0
        self.color = color

    def draw(self, rect):
        for block in self.blocks:
            rect(block.x, block.y, block.w, block.h, self.color).draw()

    def update(self):
        lastPosX = None
        lastPosY = None

        for i in range(len(self.blocks)):
            if i == 0:
                lastPosX = self.blocks[i].x
                lastPosY = self.blocks[i].y

                self.blocks[i].x += self.velX
                self.blocks[i].y += self.velY
            elif i > 0:
                tempPosX = self.blocks[i].x
                tempPosY = self.blocks[i].y

                self.blocks[i].x = lastPosX
                self.blocks[i].y = lastPosY

                lastPosX = tempPosX
                lastPosY = tempPosY

class Block:
    def __init__(self, x, y, scale):
        self.w = scale
        self.h = scale
        self.x = x
        self.y = y