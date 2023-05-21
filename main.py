#Import librairies
import pygame, sys
import pygame.time
import random as r
from itertools import repeat

#Init the pygame library
pygame.init()

#Import Classes
from Class.ball import Ball
from Class.gauge import Gauge
from Class.led import Led
from Class.switch import Switch

#Create game screen
SCREEN = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("MENU")

#Import images
BG = pygame.image.load("img/back.png")
BG = pygame.transform.scale(BG, (1920, 1080))

TIMERI = pygame.image.load("img/timer/timerbg.png")
TIMERI = pygame.transform.scale(TIMERI, (1920, 1080))

GAUGE = pygame.image.load("img/gauge.png")
GAUGE = pygame.transform.scale(GAUGE, (1700, 100))

BALL = pygame.image.load("img/ball.png")
BALL = pygame.transform.scale(BALL, (30,30))

def shake():
    s = -1
    for _ in range(0,3):
        for x in range(0,20,5):
            yield (x*s, 0)
        for x in range(20, 0, 5):
            yield (x*s, 0)
        s *= -1
    while True: 
        yield (0,0)

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
    timerCircle = pygame.image.load("img/timer/timercircle.png")
    timerCircle = pygame.transform.scale(timerCircle, (1920, 1080))
    timerGlass = pygame.image.load("img/timer/timerglass.png")
    timerGlass = pygame.transform.scale(timerGlass, (1920, 1080))
    timerText = "18:04\n"
    timerTextSurface = []
    for line in timerText.split('\n'):
        timerTextSurface.append(get_font(100).render(line, True, "#ffffff"))

    reGauge = pygame.image.load("img/gauge/gauge.png")
    reGauge = pygame.transform.scale(reGauge, (1920, 1080))

    reBall = pygame.image.load("img/gauge/ball.png")
    reBall = pygame.transform.scale(reBall, (1920, 1080))

    ballGauge = Gauge(960, 960, reGauge, GAUGE)
    
    userBall = Ball(960, 540, reBall)

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

    switch1On = pygame.image.load("img/switch/blue/switch1.png")
    switch1On = pygame.transform.scale(switch1On, (1920, 1080))
    switch1Off = pygame.image.load("img/switch/yellow/switch1.png")
    switch1Off = pygame.transform.scale(switch1Off, (1920, 1080))

    switch2On = pygame.image.load("img/switch/blue/switch2.png")
    switch2On = pygame.transform.scale(switch2On, (1920, 1080))
    switch2Off = pygame.image.load("img/switch/yellow/switch2.png")
    switch2Off = pygame.transform.scale(switch2Off, (1920, 1080))

    switch3On = pygame.image.load("img/switch/blue/switch3.png")
    switch3On = pygame.transform.scale(switch3On, (1920, 1080))
    switch3Off = pygame.image.load("img/switch/yellow/switch3.png")
    switch3Off = pygame.transform.scale(switch3Off, (1920, 1080))

    switch4On = pygame.image.load("img/switch/blue/switch4.png")
    switch4On = pygame.transform.scale(switch4On, (1920, 1080))
    switch4Off = pygame.image.load("img/switch/yellow/switch4.png")
    switch4Off = pygame.transform.scale(switch4Off, (1920, 1080))
    
    switch5On = pygame.image.load("img/switch/blue/switch5.png")
    switch5On = pygame.transform.scale(switch5On, (1920, 1080))
    switch5Off = pygame.image.load("img/switch/yellow/switch5.png")
    switch5Off = pygame.transform.scale(switch5Off, (1920, 1080))

    switch1 = Switch(735, 655, switch1On)
    switch2 = Switch(851, 655, switch2On)
    switch3 = Switch(967, 655, switch3On)
    switch4 = Switch(1073, 655, switch4On)
    switch5 = Switch(1200, 655, switch5On)
    switchList = [switch1, switch2, switch3, switch4, switch5]
    switchOffList = [switch1Off, switch2Off, switch3Off, switch4Off, switch5Off]

    for i in range(len(switchList)):
        if switchList[i].state == "Off":
            switchList[i].image = switchOffList[i]

    switchListState = [switch1.state, switch2.state, switch3.state, switch4.state, switch5.state]
    solutionSwitch =["Off","On","Off","Off","On"]
    chosenSwitch = 1

    led1On = pygame.image.load("img/led/on/led1.png")
    led1On = pygame.transform.scale(led1On, (1920,1080))
    led1Off = pygame.image.load("img/led/off/led1.png")
    led1Off = pygame.transform.scale(led1Off, (1920,1080))

    led2On = pygame.image.load("img/led/on/led2.png")
    led2On = pygame.transform.scale(led2On, (1920,1080))
    led2Off = pygame.image.load("img/led/off/led2.png")
    led2Off = pygame.transform.scale(led2Off, (1920, 1080))

    led3On = pygame.image.load("img/led/on/led3.png")
    led3On = pygame.transform.scale(led3On, (1920,1080))
    led3Off = pygame.image.load("img/led/off/led3.png")
    led3Off = pygame.transform.scale(led3Off, (1920,1080))

    led4On = pygame.image.load("img/led/on/led4.png")
    led4On = pygame.transform.scale(led4On, (1920,1080))
    led4Off = pygame.image.load("img/led/off/led4.png")
    led4Off = pygame.transform.scale(led4Off, (1920,1080))

    led5On = pygame.image.load("img/led/on/led5.png")
    led5On = pygame.transform.scale(led5On, (1920,1080))
    led5Off = pygame.image.load("img/led/off/led5.png")
    led5Off = pygame.transform.scale(led5Off, (1920,1080))

    led1 = Led(755, 90, led1Off, led1On)
    led2 = Led(851, 90, led2Off, led2On)
    led3 = Led(967, 90, led3Off, led3On)
    led4 = Led(1073, 90, led4Off, led4On)
    led5 = Led(1200, 90, led5Off, led5On)

    ledList = [led1, led2, led3, led4, led5]

    ledId = 0
    ledTimer = 50

    startGame = [pygame.K_m, pygame.K_q]
    startGameInv = [pygame.K_q, pygame.K_m]

    turn = 0
    gameStarted = False

    offset = repeat((0,0))

    lose = False
    noHoldTimer = 3000
    outTimer = 3000

    menuMusic = pygame.mixer.Sound("sound/background-music.mp3")
    menuMusic.set_volume(0.2)

    switchSE = pygame.mixer.Sound("sound/effect/Button_Switch.wav")
    switchSE.set_volume(0.2)

    ledSE = pygame.mixer.Sound("sound/effect/LED_is_Activate.wav")
    ledSE.set_volume(0.2)

    lockedBoxImg = pygame.image.load("img/box/locked/lockedbox.png")
    lockedBoxImg = pygame.transform.scale(lockedBoxImg, (1920, 1080))
    lockedBoxText = pygame.image.load("img/box/locked/lockedtxt.png")
    lockedBoxText = pygame.transform.scale(lockedBoxText, (1920, 1080))

    mysteryOff = pygame.image.load("img/mystery/off.png")
    mysteryOff = pygame.transform.scale(mysteryOff, (1920, 1080))

    randomButton1 = pygame.image.load("img/randoms/blue.png")
    randomButton1 = pygame.transform.scale(randomButton1, (1920, 1080))
    randomButton2 = pygame.image.load("img/randoms/purple.png")
    randomButton2 = pygame.transform.scale(randomButton2, (1920, 1080))
    randomButton3 = pygame.image.load("img/randoms/pink.png")
    randomButton3 = pygame.transform.scale(randomButton3, (1920, 1080)) 

    trioGaugeBackGround = pygame.image.load("img/trio/gauge-background.png")
    trioGaugeBackGround = pygame.transform.scale(trioGaugeBackGround, (1920, 1080))

    gaugeBlue1Off = pygame.image.load("img/trio/blue/off/gauge1.png")
    gaugeBlue1Off = pygame.transform.scale(gaugeBlue1Off, (1920, 1080))
    gaugeBlue2Off = pygame.image.load("img/trio/blue/off/gauge2.png")
    gaugeBlue2Off = pygame.transform.scale(gaugeBlue2Off, (1920, 1080))
    gaugeBlue3Off = pygame.image.load("img/trio/blue/off/gauge3.png")
    gaugeBlue3Off = pygame.transform.scale(gaugeBlue3Off, (1920, 1080))
    gaugeBlue4Off = pygame.image.load("img/trio/blue/off/gauge4.png")
    gaugeBlue4Off = pygame.transform.scale(gaugeBlue4Off, (1920, 1080))
    gaugeBlue5Off = pygame.image.load("img/trio/blue/off/gauge5.png")
    gaugeBlue5Off = pygame.transform.scale(gaugeBlue5Off, (1920, 1080))
    gaugeBlueList = [gaugeBlue1Off, gaugeBlue2Off, gaugeBlue3Off, gaugeBlue4Off, gaugeBlue5Off]

    gaugeYellow1Off = pygame.image.load("img/trio/yellow/off/gauge1.png")
    gaugeYellow1Off = pygame.transform.scale(gaugeYellow1Off, (1920, 1080))
    gaugeYellow2Off = pygame.image.load("img/trio/yellow/off/gauge2.png")
    gaugeYellow2Off = pygame.transform.scale(gaugeYellow2Off, (1920, 1080))
    gaugeYellow3Off = pygame.image.load("img/trio/yellow/off/gauge3.png")
    gaugeYellow3Off = pygame.transform.scale(gaugeYellow3Off, (1920, 1080))
    gaugeYellow4Off = pygame.image.load("img/trio/yellow/off/gauge4.png")
    gaugeYellow4Off = pygame.transform.scale(gaugeYellow4Off, (1920, 1080))
    gaugeYellow5Off = pygame.image.load("img/trio/yellow/off/gauge5.png")
    gaugeYellow5Off = pygame.transform.scale(gaugeYellow5Off, (1920, 1080))
    gaugeYellowList = [gaugeYellow1Off, gaugeYellow2Off, gaugeYellow3Off, gaugeYellow4Off, gaugeYellow5Off]

    gaugePink1Off = pygame.image.load("img/trio/pink/off/gauge1.png")
    gaugePink1Off = pygame.transform.scale(gaugePink1Off, (1920, 1080))
    gaugePink2Off = pygame.image.load("img/trio/pink/off/gauge2.png")
    gaugePink2Off = pygame.transform.scale(gaugePink2Off, (1920, 1080))
    gaugePink3Off = pygame.image.load("img/trio/pink/off/gauge3.png")
    gaugePink3Off = pygame.transform.scale(gaugePink3Off, (1920, 1080))
    gaugePink4Off = pygame.image.load("img/trio/pink/off/gauge4.png")
    gaugePink4Off = pygame.transform.scale(gaugePink4Off, (1920, 1080))
    gaugePink5Off = pygame.image.load("img/trio/pink/off/gauge5.png")
    gaugePink5Off = pygame.transform.scale(gaugePink5Off, (1920, 1080))
    gaugePinkList = [gaugePink1Off, gaugePink2Off, gaugePink3Off, gaugePink4Off, gaugePink5Off]

    gaugeList = [gaugeBlueList, gaugeYellowList, gaugePinkList]

    blueRotate = pygame.image.load("img/rotating/blue-path.png")
    blueRotate = pygame.transform.scale(blueRotate, (1920, 1080))
    borderRotate = pygame.image.load("img/rotating/border.png")
    borderRotate = pygame.transform.scale(borderRotate, (1920, 1080))
    botDotRotate = pygame.image.load("img/rotating/bot-dot.png")
    botDotRotate = pygame.transform.scale(botDotRotate, (1920, 1080))
    duoPurpleRotate = pygame.image.load("img/rotating/duo-purple.png")
    duoPurpleRotate = pygame.transform.scale(duoPurpleRotate, (1920, 1080))
    tricolorRotate = pygame.image.load("img/rotating/tricolor-rotate.png")
    tricolorRotate = pygame.transform.scale(tricolorRotate, (1920, 1080))
    upDotRotate = pygame.image.load("img/rotating/up-dot.png")
    upDotRotate = pygame.transform.scale(upDotRotate, (1920, 1080))
    whiteRotate = pygame.image.load("img/rotating/white-circle.png")
    whiteRotate = pygame.transform.scale(whiteRotate, (1920, 1080))
    yellowCircleRotate = pygame.image.load("img/rotating/yellow-circle.png")
    yellowCircleRotate = pygame.transform.scale(yellowCircleRotate, (1920, 1080))
    yellowPathRotate = pygame.image.load("img/rotating/yellow-path.png")
    yellowPathRotate = pygame.transform.scale(yellowPathRotate, (1920, 1080))

    pressure1Arrow = pygame.image.load("img/pressure/pressure1/arrow.png")
    pressure1Arrow = pygame.transform.scale(pressure1Arrow, (1920, 1080))
    pressure1Circle = pygame.image.load("img/pressure/pressure1/circle.png")
    pressure1Circle = pygame.transform.scale(pressure1Circle, (1920, 1080))
    pressure1Press = pygame.image.load("img/pressure/pressure1/pressurizer.png")
    pressure1Press = pygame.transform.scale(pressure1Press, (1920, 1080))
    pressure1 = [pressure1Arrow, pressure1Circle, pressure1Press]

    pressure2Arrow = pygame.image.load("img/pressure/pressure2/arrow.png")
    pressure2Arrow = pygame.transform.scale(pressure2Arrow, (1920, 1080))
    pressure2Circle = pygame.image.load("img/pressure/pressure2/circle.png")
    pressure2Circle = pygame.transform.scale(pressure2Circle, (1920, 1080))
    pressure2Press = pygame.image.load("img/pressure/pressure2/pressurizer.png")
    pressure2Press = pygame.transform.scale(pressure2Press, (1920, 1080))
    pressure2 = [pressure2Arrow, pressure2Circle, pressure2Press]

    while running and timer > 0:
        keys = pygame.key.get_pressed()
        pressedKeys = []

        SCREEN.blit(BG, next(offset))
        SCREEN.blit(TIMERI, (0,0))
        SCREEN.blit(timerCircle, (0,0))
        SCREEN.blit(timerGlass, (0,0))
        SCREEN.blit(reGauge, (0,0))
        SCREEN.blit(reBall, userBall.rect)
        for text in timerTextSurface:
            SCREEN.blit(text, text.get_rect(center=(950,270)))

        for switch in switchList:
            SCREEN.blit(switch.image, (0,0))

        for led in ledList:
            SCREEN.blit(led.image, (0,0))

        SCREEN.blit(lockedBoxImg, (0,0))
        SCREEN.blit(lockedBoxText, (0,0))

        SCREEN.blit(mysteryOff, (0,0))

        SCREEN.blit(trioGaugeBackGround, (0,0))
        for list in gaugeList:
            for gaugeEl in list:
                SCREEN.blit(gaugeEl, (0,0))

        SCREEN.blit(randomButton1, (0,0))
        SCREEN.blit(randomButton2, (0,0))
        SCREEN.blit(randomButton3, (0,0))

        SCREEN.blit(blueRotate, (0,0))
        SCREEN.blit(borderRotate, (0,0))
        SCREEN.blit(botDotRotate, (0,0))
        SCREEN.blit(duoPurpleRotate, (0,0))
        SCREEN.blit(tricolorRotate, (0,0))
        SCREEN.blit(upDotRotate, (0,0))
        SCREEN.blit(whiteRotate, (0,0))
        SCREEN.blit(yellowCircleRotate, (0,0))
        SCREEN.blit(yellowPathRotate, (0,0))

        for item in pressure1:
            SCREEN.blit(item, (0,0))

        for item in pressure2:
            SCREEN.blit(item, (0,0))

        if chosenLight == 1:
            SCREEN.blit(light1Img, ballGauge.light1Rect)
        elif chosenLight == 2:
            SCREEN.blit(light2Img, ballGauge.light2Rect)
        elif chosenLight == 3:
            SCREEN.blit(light3Img, ballGauge.light3Rect)
        elif chosenLight == 4:
            SCREEN.blit(light4Img, ballGauge.light4Rect) 
        else:
            SCREEN.blit(light5Img, ballGauge.light5Rect)
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        if ledList[-1].turnedOn == True:
            winRect = pygame.Surface((1920,1080))
            winRect.set_alpha(128)
            winRect.fill((0,0,0))
            SCREEN.blit(winRect, (0,0))

            winText = get_font(100).render("YOU WIN", True, "#b68f40")
            winTextRect = winText.get_rect(center=(960,100))
            SCREEN.blit(winText, winTextRect)
            winTime = 60
            win = True
            while win:
                pygame.display.flip()
                winTime -= 1

                if winTime == 0:
                    menuMusic.stop()
                    win = False
                    running = False

        if lose:
            loseRect = pygame.Surface((1920, 1080))
            loseRect.set_alpha(128)
            loseRect.fill((0,0,0))
            SCREEN.blit(loseRect, (0,0))

            loseText = get_font(100).render("BETTER LUCK NEXT TIME...", True, "#b68f40")
            loseTextRect = loseText.get_rect(center=(960,100))
            SCREEN.blit(loseText, loseTextRect)
            loseTime = 100
            while lose:
                pygame.display.flip()
                loseTime -= 1

                if loseTime == 0:
                    menuMusic.stop()
                    lose = False
                    running = False

        clock = pygame.time.Clock()

        if solutionSwitch == switchListState:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    if chosenSwitch == 5:
                        chosenSwitch = 1
                    else:
                        chosenSwitch += 1
                if event.key == pygame.K_z:
                    if chosenSwitch == 1:
                        switchSE.play()
                        switch1.switch(switch1On, switch1Off)
                        switchListState[0] = switch1.state
                    elif chosenSwitch == 2:
                        switchSE.play()
                        switch2.switch(switch2On, switch2Off)
                        switchListState[1] = switch2.state
                    elif chosenSwitch == 3:
                        switchSE.play()
                        switch3.switch(switch3On, switch3Off)
                        switchListState[2] = switch3.state
                    elif chosenSwitch == 4:
                        switchSE.play()
                        switch4.switch(switch4On, switch4Off)
                        switchListState[3] = switch4.state
                    elif chosenSwitch == 5:
                        switchSE.play()
                        switch5.switch(switch5On, switch5Off)
                        switchListState[4] = switch5.state
                if event.key == pygame.K_ESCAPE:
                    menuMusic.stop()
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
                if event.key == pygame.K_m and turn == 0:
                    pressedKeys.append(pygame.K_m)
                if event.key == pygame.K_q and turn == 0:
                    pressedKeys.append(pygame.K_q)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(MENU_MOUSE_POS)      

        if turn == 0 and (pressedKeys == startGame or pressedKeys == startGameInv):
            gameStarted = True
            turn += 1

        if gameStarted:
            if menuMusic.get_num_channels() == 0:
                menuMusic.play(-1)

            if keys[pygame.K_q]:
                if userBall.x < ballGauge.rect.right-130:
                    userBall.move(1)
                if noHoldTimer != 3000:
                    noHoldTimer = 3000  
            if keys[pygame.K_m]:
                if userBall.x > ballGauge.rect.left+160:
                    userBall.move(2)  
                if noHoldTimer != 3000:
                    noHoldTimer = 3000  

            for lightPos in ballGauge.lightPos:
                if userBall.x in range(lightPos.left, lightPos.right) and ledId <= 4 and ledTimer <= 0 and turn >= 10:
                    if keys[pygame.K_m]:
                        if keys[pygame.K_q]:
                            ledSE.play()
                            ledList[ledId].turnedOn = True
                            ledList[ledId].turnOn()
                            ledId += 1
                            ledTimer = 100

                            if chosenLight == 1:
                                light1Img = darkenLight
                            elif chosenLight == 2:
                                light2Img = darkenLight
                            elif chosenLight == 3:
                                light3Img = darkenLight
                            elif chosenLight == 4:
                                light4Img = darkenLight
                            elif chosenLight == 5:
                                light5Img = darkenLight

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

                            #offset = shake()
                elif ballGauge.rect.left+160 in range(userBall.rect.left, userBall.rect.right) or ballGauge.rect.right-130 in range(userBall.rect.left, userBall.rect.right):
                    if outTimer == 0:
                        lose = True
                    outTimer -= 1
            
            if turn >= 10 and (pygame.K_m not in keys and pygame.K_q not in keys):
                if noHoldTimer == 0:
                    lose = True
                noHoldTimer -= 1


        #timer -= 1
        ledTimer -= 1

        if timer == 0:
            lose = True

        elif ballGauge.rect.left+160 not in range(userBall.rect.left, userBall.rect.right) and ballGauge.rect.right-130 not in range(userBall.rect.left, userBall.rect.right) and outTimer != 3000:
            outTimer = 3000

        if turn != 0 and turn < 10:
            turn += 1

        pygame.display.update()
        
    pygame.quit()
    sys.exit()

gameLoop()