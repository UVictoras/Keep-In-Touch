import pygame

class Ball ():

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self, id):
        if id == 1:
            self.x += 10
        else:
            self.x -= 10
        self.rect = self.image.get_rect(center=(self.x, self.y))