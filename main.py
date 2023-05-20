#Import librairies
import pygame, sys
import pygame.time

#Init the pygame library
pygame.init()

#Create game screen
SCREEN = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("MENU")

#Import images
BG = pygame.image.load("img/back.png")
BG = pygame.transform.scale(BG, (1920, 1080))

def gameLoop():
    running = True

    while running:
        SCREEN.blit(BG, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

gameLoop()