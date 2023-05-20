import pygame
import random as r

class Switch ():

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.possibleColors = ["Blue","Purple"]
        self.color = r.choice(self.possibleColors)
        
        self.possibleState = ["On","Off"]
        self.state = r.choice(self.possibleState)

    def switch(self, onImg, offImg):
        if self.state == "On":
            self.state = "Off"
            self.image = offImg
        elif self.state == "Off":
            self.state = "On"
            self.image = onImg