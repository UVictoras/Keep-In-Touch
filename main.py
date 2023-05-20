#Import librairies
import pygame, sys
import pygame.time
import random as r

#Init the pygame library
pygame.init()

#Import Classes
from Class.button import Button
from Class.ball import Ball
from Class.gauge import Gauge

#Create game screen
SCREEN = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("MENU")

#Import images
BG = pygame.image.load("img/back.png")
BG = pygame.transform.scale(BG, (1920, 1080))

BUTTON = pygame.image.load("img/button.png")
BUTTON = pygame.transform.scale(BUTTON, (BUTTON.get_width()/1.3, BUTTON.get_height()/1.3))

GAUGE = pygame.image.load("img/gauge.png")
GAUGE = pygame.transform.scale(GAUGE, (1700, 100))

BALL = pygame.image.load("img/ball.png")
BALL = pygame.transform.scale(BALL, (30,30))

def test():
    pass


def darken(image, percent = 50):
    newImg = image.copy()
    dark = pygame.Surface(newImg.get_size(), flags=pygame.SRCALPHA)
    dark.fill((50, 50, 50, 0))
    newImg.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    return newImg

def gameLoop():
    running = True

    timer = r.randint(60, 300)

    ballGauge = Gauge(960, 960, GAUGE)
    
    userBall = Ball(960, 967, BALL)

    darkenLight = darken(ballGauge.lightImg)
    light1Img = darkenLight
    light2Img = darkenLight
    light3Img = darkenLight
    light4Img = darkenLight 
    light5Img = darkenLight

    rotateButtonUp = pygame.image.load("img/rotateButton1.jpg")
    rotateButtonUp = pygame.transform.scale(rotateButtonUp, (100, 100))
    rotateButtonRight = pygame.image.load("img/rotateButton2.png")
    rotateButtonRight = pygame.transform.scale(rotateButtonRight, (100, 100))
    rotateButtonDown = pygame.image.load("img/rotateButton3.png")
    rotateButtonDown = pygame.transform.scale(rotateButtonDown, (100, 100))

    rotateButtonImg = rotateButtonUp
    rotateButtonRect = rotateButtonImg.get_rect(center=(960, 400))

    chosenLight = ballGauge.chooseLight()

    if chosenLight == 1:
        light1Img = ballGauge.lightImg
    elif chosenLight == 2:
        light2Img = ballGauge.lightImg
    elif chosenLight == 3:
        light3Img = ballGauge.lightImg
    elif chosenLight == 4:
        light4Img = ballGauge.lightImg
    elif chosenLight == 5:
        light5Img = ballGauge.lightImg
       
    mainButton = Button(960, 250, BUTTON, test)
    while running and timer > 0:
        keys = pygame.key.get_pressed()
        SCREEN.blit(BG, (0,0))
        SCREEN.blit(mainButton.image, mainButton.rect)
        SCREEN.blit(ballGauge.image, ballGauge.rect)
        SCREEN.blit(userBall.image, userBall.rect)
        SCREEN.blit(rotateButtonImg, rotateButtonRect)

        SCREEN.blit(light1Img, ballGauge.light1Rect)
        SCREEN.blit(light2Img, ballGauge.light2Rect)
        SCREEN.blit(light3Img, ballGauge.light3Rect)
        SCREEN.blit(light4Img, ballGauge.light4Rect)
        SCREEN.blit(light5Img, ballGauge.light5Rect)
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_p:
                    if rotateButtonImg == rotateButtonUp:
                        rotateButtonImg = rotateButtonRight
                if event.key == pygame.K_o:
                    if rotateButtonImg == rotateButtonRight:
                        rotateButtonImg = rotateButtonDown
                if event.key == pygame.K_i:
                    if rotateButtonImg == rotateButtonDown:
                        rotateButtonImg = rotateButtonUp
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainButton.checkForInput(MENU_MOUSE_POS):
                    print("good")
        if keys[pygame.K_w]:
            if userBall.x < ballGauge.rect.right-130:
                userBall.move(1)
        if keys[pygame.K_m]:
            if userBall.x > ballGauge.rect.left+160:
                userBall.move(2)               

        #timer -= 1

        pygame.display.update()
        
    pygame.quit()
    sys.exit()

gameLoop()