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
from Class.switch import Switch

#Create game screen
SCREEN = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("MENU")

#Import images
BG = pygame.image.load("img/back.png")
BG = pygame.transform.scale(BG, (1920, 1080))

TIMERI = pygame.image.load("img/timerbg.png")
TIMERI = pygame.transform.scale(TIMERI, (TIMERI.get_width()/3, TIMERI.get_height()/3))
TIMERRECT = TIMERI.get_rect(center=(960, 250))

GAUGE = pygame.image.load("img/gauge.png")
GAUGE = pygame.transform.scale(GAUGE, (1700, 100))

BALL = pygame.image.load("img/ball.png")
BALL = pygame.transform.scale(BALL, (30,30))

def test():
    pass

def get_font(size):
    return pygame.font.Font("asset/font.ttf", size)

def darken(image, percent = 50):
    newImg = image.copy()
    dark = pygame.Surface(newImg.get_size(), flags=pygame.SRCALPHA)
    dark.fill((50, 50, 50, 0))
    newImg.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    return newImg

def gameLoop():
    running = True

    timer = r.randint(60, 300)
    timerCircle = pygame.image.load("img/timerCircle.png")
    timerCircle = pygame.transform.scale(timerCircle, (60, 60))
    timerCircleRect = timerCircle.get_rect(center=(1140,140))
    timerGlass = pygame.image.load("img/timerglass.png")
    timerGlass = pygame.transform.scale(timerGlass, (50, 50))
    timerGlassRect = timerGlass.get_rect(center=(1140, 140))
    timerText = "18:04\n"
    timerTextSurface = []
    for line in timerText.split('\n'):
        timerTextSurface.append(get_font(100).render(line, True, "#ffffff"))

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
    rotateButtonRect = rotateButtonImg.get_rect(center=(960, 500))

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

    switchOn = pygame.image.load("img/switchOn.png")
    switchOn = pygame.transform.scale(switchOn, (40, 100))
    switchOff = pygame.image.load("img/switchOff.png")
    switchOff = pygame.transform.scale(switchOff, (40, 100))

    switch1 = Switch(735, 655, switchOn)
    switch2 = Switch(841, 655, switchOn)
    switch3 = Switch(957, 655, switchOn)
    switch4 = Switch(1063, 655, switchOn)
    switch5 = Switch(1200, 655, switchOn)
    switchList = [switch1, switch2, switch3, switch4, switch5]

    for switch in switchList:
        if switch.state == "Off":
            switch.image = switchOff

    chosenSwitch = 0

    while running and timer > 0:
        keys = pygame.key.get_pressed()
        SCREEN.blit(BG, (0,0))
        SCREEN.blit(TIMERI, TIMERRECT)
        SCREEN.blit(timerCircle, timerCircleRect)
        SCREEN.blit(timerGlass, timerGlassRect)
        SCREEN.blit(ballGauge.image, ballGauge.rect)
        SCREEN.blit(userBall.image, userBall.rect)
        SCREEN.blit(rotateButtonImg, rotateButtonRect)
        for text in timerTextSurface:
            SCREEN.blit(text, text.get_rect(center=(950,270)))

        for switch in switchList:
            SCREEN.blit(switch.image, switch.rect)

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
                print(MENU_MOUSE_POS)
        if keys[pygame.K_w]:
            if userBall.x < ballGauge.rect.right-130:
                userBall.move(1)
        if keys[pygame.K_m]:
            if userBall.x > ballGauge.rect.left+160:
                userBall.move(2)           
                
        if keys[pygame.K_a]:
            if chosenSwitch == 2:
                switch2.image = pygame.transform.scale(switch2.image, (40, 100))
            elif chosenSwitch == 3:
                switch3.image = pygame.transform.scale(switch3.image, (40, 100))
            elif chosenSwitch == 4:
                switch4.image = pygame.transform.scale(switch4.image, (40, 100))
            elif chosenSwitch == 5:
                switch5.image = pygame.transform.scale(switch5.image, (40, 100))
            chosenSwitch = 1
            switch1.image = pygame.transform.scale(switch1.image, (60, 120))
        if keys[pygame.K_z]:
            if chosenSwitch == 1:
                switch1.image = pygame.transform.scale(switch1.image, (40, 100))
            elif chosenSwitch == 3:
                switch3.image = pygame.transform.scale(switch3.image, (40, 100))
            elif chosenSwitch == 4:
                switch4.image = pygame.transform.scale(switch4.image, (40, 100))
            elif chosenSwitch == 5:
                switch5.image = pygame.transform.scale(switch5.image, (40, 100))
            chosenSwitch = 2
            switch2.image = pygame.transform.scale(switch2.image, (60, 120))
        if keys[pygame.K_e]:
            if chosenSwitch == 1:
                switch1.image = pygame.transform.scale(switch1.image, (40, 100))
            elif chosenSwitch == 2:
                switch2.image = pygame.transform.scale(switch2.image, (40, 100))
            elif chosenSwitch == 4:
                switch4.image = pygame.transform.scale(switch4.image, (40, 100))
            elif chosenSwitch == 5:
                switch5.image = pygame.transform.scale(switch5.image, (40, 100))
            chosenSwitch = 3
            switch3.image = pygame.transform.scale(switch3.image, (60, 120)) 
        if keys[pygame.K_r]:
            if chosenSwitch == 1:
                switch1.image = pygame.transform.scale(switch1.image, (40, 100))
            elif chosenSwitch == 2:
                switch2.image = pygame.transform.scale(switch2.image, (40, 100))
            elif chosenSwitch == 3:
                switch3.image = pygame.transform.scale(switch3.image, (40, 100))
            elif chosenSwitch == 5:
                switch5.image = pygame.transform.scale(switch5.image, (40, 100))
            chosenSwitch = 4
            switch4.image = pygame.transform.scale(switch4.image, (60, 120))
        if keys[pygame.K_t]:
            if chosenSwitch == 1:
                switch1.image = pygame.transform.scale(switch1.image, (40, 100))
            elif chosenSwitch == 2:
                switch2.image = pygame.transform.scale(switch2.image, (40, 100))
            elif chosenSwitch == 3:
                switch3.image = pygame.transform.scale(switch3.image, (40, 100))
            elif chosenSwitch == 4:
                switch4.image = pygame.transform.scale(switch4.image, (40, 100))
            chosenSwitch = 5
            switch5.image = pygame.transform.scale(switch5.image, (60, 120))

        if keys[pygame.K_TAB]:
            if chosenSwitch == 1:
                switch1.switch(switchOn, switchOff)
            elif chosenSwitch == 2:
                switch2.switch(switchOn, switchOff)
            elif chosenSwitch == 3:
                switch3.switch(switchOn, switchOff)
            elif chosenSwitch == 4:
                switch4.switch(switchOn, switchOff)
            elif chosenSwitch == 5:
                switch5.switch(switchOn, switchOff)

        #timer -= 1

        pygame.display.update()
        
    pygame.quit()
    sys.exit()

gameLoop()