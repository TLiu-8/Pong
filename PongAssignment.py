#########################################
# File Name: pongGameAssignment.py
# Description: Recreating Pong
# Author: Reymond Lee and Theo Liu
# Date: 04/24/2018
#########################################

import pygame
WIDTH = 810
HEIGHT = 600

from random import randint

TOP = 0
BOTTOM = HEIGHT
LEFT = 02
RIGHT = WIDTH

RED    = (221,  0, 72)
ORANGE = (253, 95,  0)
YELLOW = (255,255,  0)
GREEN  = (  0,255,  0)
BLUE   = ( 77, 77,255)
VIOLET = (104, 22,224)
PINK   = (255,105,180)
WHITE  = (255,255,255)
BLACK  = (  0,  0,  0)





outline = 0

inPlay = True
inMenu = True
inGame = True
gameEnd = True


scoreL = 0
scoreR = 0

ballX = 400
ballY = 300
ballR = 20

paddleLeftX = 20
paddleRightX = 780
paddleLeftY = 250
paddleRightY = 250

paddleLength = 100
paddleWidth = 10
shiftPaddle = 20

shiftX = 5
shiftY = 5





def leftColourChooser(leftCLR):
    if leftCLR == 1:
        CLR_L = RED
    elif leftCLR == 2:
        CLR_L = ORANGE
    elif leftCLR == 3:
        CLR_L = YELLOW
    elif leftCLR == 4:
        CLR_L = GREEN
    elif leftCLR == 5:
        CLR_L = BLUE
    elif leftCLR == 6:
        CLR_L = VIOLET
    elif leftCLR == 7:
        CLR_L = PINK
    elif leftCLR == 0:
        CLR_L = WHITE
    else:
        CLR_L = RED
    return CLR_L
    
def rightColourChooser(rightCLR):
    if rightCLR == 1:
        CLR_R = RED
    elif rightCLR == 2:
        CLR_R = ORANGE
    elif rightCLR == 3:
        CLR_R = YELLOW
    elif rightCLR == 4:
        CLR_R = GREEN
    elif rightCLR == 5:
        CLR_R = BLUE
    elif rightCLR == 6:
        CLR_R = VIOLET
    elif rightCLR == 7:
        CLR_R = PINK
    elif rightCLR == 0:
        CLR_R = WHITE
    else:
        CLR_R = BLUE
    return CLR_R
    
def pongMenu(leftColour,rightColour):
    gameWindow.fill(BLACK)
    gameWindow.blit(subtitles,(190,475))
    gameWindow.blit(titlePicture,(190,0))
    gameWindow.blit(player1Title,(10,270))
    gameWindow.blit(player2Title, (690,270))

    CLR_L = leftColourChooser(leftColour)
    CLR_R = rightColourChooser(rightColour)
    
    pygame.draw.rect(gameWindow,CLR_L,(paddleLeftX,330,paddleWidth,paddleLength),outline)
    pygame.draw.rect(gameWindow, CLR_R, (paddleRightX,330,paddleWidth,paddleLength),outline)
            
    pygame.display.update()
    pygame.time.delay(20)
        
def gameOver():
    gameWindow.blit(titlePicture,(190,0))
    gameWindow.blit(gameOverWord,(190,400))
    
    gameWindow.blit(player1Title,(10,270))
    gameWindow.blit(player2Title,(690,270))

    scoreBoardL = font.render(str(scoreL),1,WHITE)
    scoreBoardR = font.render(str(scoreR),1,WHITE)
    gameWindow.blit(scoreBoardL,(60,300))
    gameWindow.blit(scoreBoardR,(740,300))
    
    gameWindow.blit(copyRight,(190,520))
    pygame.display.update()
    pygame.time.delay(20)



def background(leftColour,rightColour):

    CLR_L = leftColourChooser(leftColour)
    CLR_R = rightColourChooser(rightColour)
    
    pygame.draw.line(gameWindow, WHITE,(400,0), (400,600),7)
    pygame.draw.rect(gameWindow, CLR_L, (paddleLeftX,paddleLeftY,paddleWidth,paddleLength),outline)
    pygame.draw.rect(gameWindow, CLR_R, (paddleRightX,paddleRightY,paddleWidth,paddleLength),outline)
    pygame.draw.circle(gameWindow, YELLOW, (ballX,ballY),ballR,outline)    


    
def redrawGameWindow(userMap,leftColour,rightColour):
    if userMap == 1:
        gameWindow.blit(earthMap,(0,0))
    elif userMap == 2:
        gameWindow.blit(lightSpeedMap,(0,0))
    else:
        gameWindow.blit(earthMap,(0,0))
    scoreBoard()
    background(leftColour,rightColour)
    pygame.display.update()
    pygame.time.delay(20)

def scoreBoard():
    scoreBoardL = font.render(str(scoreL),1,WHITE)
    scoreBoardR = font.render(str(scoreR),1,WHITE)
    gameWindow.blit(scoreBoardL,(250,50))
    gameWindow.blit(scoreBoardR,(550,50))

print "Welcome to our Pong game!"
print "Controls for Player 1 are:\nW key to move up\nS key to move down"
print "Controls for Player 2 are:\nUp key to move up\nDown key to move down"
print "Here are your possible colours:"
print "Input 9 for default"
print "1 for Red\n2 for Orange\n3 for Yellow\n4 for Green\n5 for Blue\n6 for Purple\n7 for Pink\n8 for White"
userLeftColour = input("Player 1, what colour do you want your paddle to be?: ")
userRightColour = input("Player 2, what colour do you want your paddle to be?: ")
difficulty = input("Do you want the speed to be easy (1), medium (2), or hard (3): ")
userMap = input("Do you want the Earth Background (1)\nLight Speed Background (2): ")




pygame.init()
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))

font = pygame.font.SysFont("Impact",50)
titleFont = pygame.font.SysFont("Impact",100)
smallerFont = pygame.font.SysFont("Impact",30)
subtitles = font.render("Press Space to begin.",1,YELLOW)
player1Title = smallerFont.render("Player 1",1,YELLOW)
player2Title = smallerFont.render("Player 2",1,YELLOW)
gameOverWord = titleFont.render("GAME OVER",1,YELLOW)
copyRight = smallerFont.render("By: Reymond Lee and Theodore Liu" , 1, WHITE)


titlePicture = pygame.image.load("title.png")
earthMap = pygame.image.load("Map1.png")
lightSpeedMap = pygame.image.load("Map2.png")

pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

hit = pygame.mixer.Sound('Hit.wav')
hit.set_volume(0.8)

while inPlay:
    while inMenu:

        pygame.event.get()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            inMenu = False
            inGame = True
            scoreL = 0
            scoreR = 0
        elif keys[pygame.K_ESCAPE]:
            inMenu = False
            gameEnd = False
            inPlay = False
        else:
            pongMenu(userLeftColour,userRightColour)
    BEGIN = pygame.time.get_ticks()        
    while inGame:

        redrawGameWindow(userMap,userLeftColour,userRightColour)

        pygame.event.get()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            if paddleRightY <= 0:
                paddleRightY=0
            else:
                paddleRightY = paddleRightY - shiftPaddle
            
            
        elif keys[pygame.K_DOWN]:
            if paddleRightY >= 500:
                paddleRightY = 500
            else:
                paddleRightY = paddleRightY + shiftPaddle
        if keys[pygame.K_w]:
            if paddleLeftY <= 0:
                paddleLeftY = 0
            else:
                paddleLeftY = paddleLeftY - shiftPaddle
        elif keys[pygame.K_s]:
            if paddleLeftY >= 500:
                paddleLeftY = 500
            else:
                paddleLeftY = paddleLeftY +shiftPaddle
        if keys[pygame.K_ESCAPE]:
            inGame = False
            inPlay = False

        if ballX - ballR == paddleLeftX and ballY>=paddleLeftY and ballY<= paddleLeftY + paddleLength:
            hit.play()
            if difficulty == 1:
                shiftX = 10
            elif difficulty == 2:
                shiftX = 15
            elif difficulty == 3:
                shiftX = 20
            shiftX = shiftX
            
        if ballX + ballR == paddleRightX and ballY>=paddleRightY and ballY<= paddleRightY+paddleLength:
            hit.play()
            if difficulty == 1:
                shiftX = 10
            elif difficulty == 2:
                shiftX = 15
            elif difficulty == 3:
                shiftX = 20
            shiftX = -shiftX
                        
        if ballY+ballR > BOTTOM or ballY-ballR < TOP:
            hit.play()
            shiftY = -shiftY
            
        if ballX-ballR < LEFT:
            scoreR = scoreR+1
            ballX = 400
            ballY = 300
            shiftX = 8
            direction = randint(1,4)
            if direction == 2:
                shiftX = -shiftX
                shiftY = -shiftY
            elif direction == 3:
                shiftX = shiftX
                shiftY = -shiftY
            elif direction == 4:
                shiftX = -shiftX
                shiftY = shiftY

        if ballX+ballR > 790:
            scoreL = scoreL+1
            ballX = 400
            ballY = 300
            shiftX = 8
            direction = randint(1,2)
            if direction == 2:
                shiftX = -shiftX
                shiftY = -shiftY
            elif direction == 3:
                shiftX = shiftX
                shiftY = -shiftY
            elif direction == 4:
                shiftX = -shiftX
                shiftY = shiftY

          
    

        
        ballX = ballX + shiftX
        ballY = ballY + shiftY   

            
        if scoreL == 7:
            elapsed = pygame.time.get_ticks() - BEGIN
            print "Player 1 Wins!"
            inGame = False
            print "Click ESC if you want to exit the game over"
            print float(elapsed)/1000, "seconds have passed since the beginning of tbe main loop"
        elif scoreR == 7:
            elapsed = pygame.time.get_ticks() - BEGIN
            print "Player 2 Wins!"
            inGame = False
            print "Click ESC if you want to exit the game over"
            print float(elapsed)/1000, "seconds have passed since the beginning of tbe main loop"


    while gameEnd:
        gameWindow.fill(BLACK)
        gameOver()

        pygame.event.get()
        keys = pygame.key.get_pressed()
               
        if keys[pygame.K_ESCAPE]:
            gameEnd = False
            inMenu = True

pygame.mixer.music.stop()
pygame.quit()
    
    
   
    
    
    
    
