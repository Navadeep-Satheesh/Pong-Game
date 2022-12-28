import pygame
import random
import time

pygame.init()

global playing
global running
global screenNo
screenNo = 0
running = True
playing = False
screenWidth = 800
screenHeight  = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('')

clock  = pygame.time.Clock()


red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
grey = (158, 157, 155)

moveValue = 5
ballspeed = 4

padwidth = 25
padheight = 80
radius = 15
pad1x = 0
pad1y = screenHeight/2 - padheight/2
pad2x = screenWidth-padwidth
pad2y = screenHeight/2 - padheight/2

backx = 50
backy = 20

moveFlag1 = 0
moveFlag2 = 0


player1Point = 0
player2Point = 0

currentOption = 0

def resetBall():
    bally = int(screenHeight/2 - radius/2)
    ballx = int(screenWidth/2 - radius/2)
    ballxdir = random.choice([1,-1])
    ballydir = random.choice([1,-1])
    ballVelocityx = ballspeed*ballxdir
    ballVelocityy = ballspeed*ballydir
    return ballVelocityx,ballVelocityy,ballx,bally

def renderGameWindowWindow():
    
    
    pygame.draw.rect(screen,red,(pad1x,pad1y,padwidth,padheight))
    pygame.draw.rect(screen,red,(pad2x,pad2y,padwidth,padheight))
    pygame.draw.circle(screen,blue,(ballx,bally),radius)
    # pygame.draw.rect(screen,green,(0,0,backx,backy))
    renderText(player1Point,10,20,25,blue)
    renderText(player2Point,screenWidth-20,20,25,blue)
    # renderText("BACK",0,0,20,black)
    pygame.display.update()

def renderText(text,x,y,size,color):
    font = pygame.font.SysFont(None,size)
    screenText = font.render(str(text),True,color)
    screen.blit(screenText,(x,y))


def startGame():
    global screenNo
    screenNo = 1
def quitGame():
    global running
    running = False
def Help():
    global screenNo
    screenNo = 2
    print(screenNo)
def renderHelp():

    global screenNo
    global running
    size = 30
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if x >= 0 and x <= backx and y >= 0 and y <= backy :
                screenNo = 0
    text = [
          "UP ARROW - LEFT PAD UP",
        "DOWN ARROW - LEFT PAD DOWN",
           "W KEY   - RIGHT PAD UP",
           "S KEY   - RIGHT PAD DOWN"
    ]
    for line in text:
        y = screenHeight/2 - len(text)*size/4 + size*text.index(line)+1
        x = screenWidth/2 - max([len(x) for x in text])*size/4
        renderText(line,x,y,size,green)
    pygame.draw.rect(screen,green,(0,0,backx,backy))
    renderText("BACK",0,0,20,black)
    pygame.display.update()


def renderMenu():
    global running
    global currentOption
    
    size = 40
    options = ["NEW GAME","QUIT","HELP"]
    functions = [startGame,quitGame,Help]
    y = screenHeight/2 - size*2
    screen.fill(black)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if currentOption < len(options)-1:
                    currentOption+=1
                    print(currentOption)
            if event.key == pygame.K_UP:
                if currentOption > 0:
                    currentOption-=1 
                    print(currentOption)
            if event.key == pygame.K_RETURN:
                functions[currentOption]()
    boxx = max([len(x) for x in options])  
    pygame.draw.rect(screen,grey,(screenWidth/2 - boxx*size/2,y+(currentOption+1)*size,size*boxx,size))     
    for option in options:
        renderText(option,screenWidth/2 - len(option)*size/4,y+ (options.index(option)+1)*size,size,green)
         
    pygame.display.update()
ballVelocityx,ballVelocityy,ballx,bally = resetBall()

while running:
    
    
       
    screen.fill(black)
    if screenNo == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moveFlag1 = 1
                elif event.key == pygame.K_DOWN:
                    moveFlag1 = 2
                if event.key == pygame.K_w:
                    moveFlag2 = 1
                elif event.key == pygame.K_s:
                    moveFlag2 = 2
                if event.key == pygame.K_ESCAPE:
                    playing =False
                    screenNo = 0

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    moveFlag1 = 0
                elif event.key == pygame.K_DOWN:
                    moveFlag1 = 0

                if event.key == pygame.K_w:
                    moveFlag2 = 0
                elif event.key == pygame.K_s:
                    moveFlag2 = 0
            # elif event.type == pygame.MOUSEBUTTONDOWN:
                # x,y = pygame.mouse.get_pos()
                # if x >= 0 and x <= backx and y >= 0 and y <= backy :
# 
                    # screenNo = 0
    

        #=======pad direction controls
        if moveFlag1 == 1:
            pad2y-= moveValue
        elif moveFlag1 == 2:
            pad2y+= moveValue
        if moveFlag2 == 1:
            pad1y-= moveValue
        elif moveFlag2 == 2:
            pad1y+= moveValue


        #======= check pad go out
        if pad1y >= screenHeight - padheight:
            pad1y = screenHeight- padheight
        elif pad1y <= 0:
            pad1y = 0
        if pad2y >= screenHeight- padheight:
            pad2y = screenHeight- padheight
        elif pad2y <= 0:
            pad2y = 0


        #==ball direction controll
        if bally > pad1y-radius and bally < pad1y + padheight+ radius and ballx == padwidth + radius:
            ballVelocityx*= -1
            #ballVelocityy*= -1

        if bally > pad2y-radius and bally < pad2y + padheight+ radius and ballx == screenWidth - padwidth - radius:
            ballVelocityx*= -1
            #ballVelocityy*= -1

        if bally < 0:
        
            ballVelocityy*= -1  

        if bally > screenHeight - radius:

            ballVelocityy*= -1 


        #==== check for out
        if ballx < 0:
            player2Point+=1
            # ballVelocityx,ballVelocityy,ballx,bally = resetBall()
            ballx = screenWidth
            renderGameWindowWindow()
           
        elif ballx > screenWidth:
            player1Point+=1
            # ballVelocityx,ballVelocityy,ballx,bally = resetBall()
            ballx = 0
            renderGameWindowWindow()
            

        ballx+=ballVelocityx
        bally+=ballVelocityy
        renderGameWindowWindow()
        clock.tick(60)

    elif screenNo==0:
        renderMenu()
    elif screenNo == 2:
        renderHelp()


   
   
   