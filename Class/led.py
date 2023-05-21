import pygame

class Led () :

    def __init__(self, x, y, image, imageOn):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.imageOn = imageOn

        self.turnedOn = False

    def turnOn(self):
        self.image = self.imageOn