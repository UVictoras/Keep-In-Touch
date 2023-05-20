import pygame

pygame.init()

class Button ():

    def __init__(self, x, y, image, function):
        self.x = x
        self.y = y
        self.image = image
        self.function = function
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False