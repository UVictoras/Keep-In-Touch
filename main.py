#Import librairies
import pygame, sys
import pygame.time
import random as r

#Init the pygame library
pygame.init()

#Import Classes
from Class.button import Button

#Create game screen
SCREEN = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("MENU")

#Import images
BG = pygame.image.load("img/back.png")
BG = pygame.transform.scale(BG, (1920, 1080))

BUTTON = pygame.image.load("img/button.png")
BUTTON = pygame.transform.scale(BUTTON, (BUTTON.get_width()/1.3, BUTTON.get_height()/1.3))

def test():
    pass

def gameLoop():
    running = True

    timer = r.randint(60, 300)
    
    mainButton = Button(960, 250, BUTTON, test)
    while running and timer > 0:
        SCREEN.blit(BG, (0,0))
        SCREEN.blit(mainButton.image, mainButton.rect)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainButton.checkForInput(MENU_MOUSE_POS):
                    print("good")

        timer -= 1

        pygame.display.update()
        
    pygame.quit()
    sys.exit()

gameLoop()