

import pygame

#initialize the pygame
pygame.init

#create a screen
screen=pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("space game")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load('ufo.png')
playerX=370
playerY=480


#function
def player(x,y):
    screen.blit(playerImg, (x, y))
    


#game loop
running=True
while running:
    
    #red green blue
    screen.fill((192,192,192))
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    #if keystroke is pressed check weather right or left
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            print("Left arrow is pressed")
        if event.key==pygame.K_RIGHT:
            print("right arrow is pressed")
        if event.key==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                print("keystoke has been released")
                
                
                
    player(playerX,playerY)
    
    pygame.display.update()
    
    
    
    