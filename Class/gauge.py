import pygame
import random as r

pygame.init()

class Gauge():

    def __init__(self, x, y, image, other):
        self.x = x
        self.y = y
        self.image = image
        self.other = other
        self.rect = self.other.get_rect(center=(self.x, self.y))

        self.light1Pos = (self.rect.left + (self.rect.right-self.rect.left)/6, self.rect.top-50)
        self.light2Pos = (self.light1Pos[0] + (self.rect.right-self.rect.left)/6, self.rect.top-50)
        self.light3Pos = (self.light2Pos[0] + (self.rect.right-self.rect.left)/6, self.rect.top-50)
        self.light4Pos = (self.light3Pos[0] + (self.rect.right-self.rect.left)/6, self.rect.top-50)
        self.light5Pos = (self.light4Pos[0] + (self.rect.right-self.rect.left)/6, self.rect.top-50)
        self.lightImg = pygame.image.load("img/light.png")
        self.lightImg = pygame.transform.scale(self.lightImg, (30, 250))

        self.light1Rect = self.lightImg.get_rect(center=self.light1Pos)
        self.light2Rect = self.lightImg.get_rect(center=self.light2Pos)
        self.light3Rect = self.lightImg.get_rect(center=self.light3Pos)
        self.light4Rect = self.lightImg.get_rect(center=self.light4Pos)
        self.light5Rect = self.lightImg.get_rect(center=self.light5Pos)

        self.lightPos = [self.light1Rect, self.light2Rect, self.light3Rect, self.light4Rect, self.light5Rect]

        self.ligthen = 0

    def chooseLight(self):
        lightNb = r.randint(1,5)
        return lightNb    