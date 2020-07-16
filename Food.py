class Food:
    def __init__(self, scale, color):
        self.x = None
        self.y = None
        self.w = scale
        self.h = scale
        self.color = color

    def draw(self, rect):
        rect(self.x, self.y, self.w, self.h, self.color).draw()