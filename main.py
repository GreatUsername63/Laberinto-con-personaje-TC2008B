import pygame, sys
from pygame.locals import *
pygame.init()
WIDTH, HEIGHT = 600, 600
disp = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Laberinto de Santy")

colorFondo = (0,0,10)
colorLaberinto = (150,150,255)
playerRec = [10,10,4,4] #x,y,width,height
playerColor = (150,255,150)
speed = 1/10
lineas = [
    (20,20),(580,20),
    (20,60),(20,580),
    (20,580),(530,580),
    (580,20),(580,580),
    (20,60),(330,60),
    (370,60),(580,60),
    (330,60),(330,140),
    (370,60),(370,100),
    (60,100),(290,100),
    (370,100),(540,100),
    (290,100),(290,140),
    (100,140),(290,140),
    (370,140),(540,140),
    (100,140),(100,180),
    (140,180),(370,180),
    (410,180),(580,180),
    (60,100),(60,220),
    (60,220),(330,220),
    (410,220),(540,220),
    (410,180),(410,260),
    (410,220),(540,220),
    (20,260),(150,260),
    (230,260),(290,260),
    (450,260),(580,260),
    (290,220),(290,260),
    (330,180),(330,300),
    (370,140),(370,300),
    (60,300),(150,300),
    (270,300),(330,300),
    (370,300),(540,300),
    (190,220),(190,510),
    (60,340),(100,340),
    (310,340),(500,340),
    (100,380),(150,380),
    (310,380),(540,380),
    (540,300),(540,380),
    (310,340),(310,380),
    (270,420),(580,420),
    (270,300),(270,420),
    (230,460),(540,460),
    (230,260),(230,510),
    (60,340),(60,470),
    (150,300),(150,470),
    (20,470),(60,470),
    (100,380),(100,510),
    (60,510),(190,510),
    (270,500),(430,500),
    (470,500),(580,500),
    (270,500),(270,550),
    (430,500),(430,530),
    (350,530),(530,530),
    (20,550),(230,550),
    (310,530),(310,580),
    (530,530),(530,580)
]

def recToLineCollision(rec,line):
    recLines = (
        ((rec[0],rec[1]),(rec[0]+rec[2],rec[1])),
        ((rec[0],rec[1]),(rec[0],rec[1]+rec[3])),
        ((rec[0]+rec[2],rec[1]),(rec[0]+rec[2],rec[1]+rec[3])),
        ((rec[0],rec[1]+rec[3]),(rec[0]+rec[2],rec[1]+rec[3]))
    )
    #line points
    x3 = line[0][0]
    x4 = line[1][0]
    y3 = line[0][1]
    y4 = line[1][1]
    for rl in recLines:
        #pygame.draw.line(disp,(255,0,0),rl[0],rl[1])
        #rec's lines points
        x1 = rl[0][0]
        x2 = rl[1][0]
        y1 = rl[0][1]
        y2 = rl[1][1]

        #Avoid division by 0 error
        divisor = ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        if divisor == 0:
            continue

        #Calculate the distance to intersection point
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / divisor
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / divisor

        if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
            return True
    return False
        
        

while True:
    #Dibujar fondo
    disp.fill(colorFondo)
    for i in range(0,len(lineas),2):
        pygame.draw.line(disp,colorLaberinto,lineas[i],lineas[i+1],3)
    pygame.draw.rect(disp,playerColor,playerRec)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerRec[0] >= 0:
        playerRec[0] -= speed
    if keys[pygame.K_UP] and playerRec[1] >= 0:
        playerRec[1] -= speed
    if keys[pygame.K_RIGHT] and playerRec[0] + playerRec[2] <= WIDTH:
        playerRec[0] += speed
    if keys[pygame.K_DOWN] and playerRec[1] + playerRec[3] <= HEIGHT:
        playerRec[1] += speed

    #Por cada linea detectar si hay colision
    for i in range(0,len(lineas),2):
        if (recToLineCollision(playerRec,(lineas[i],lineas[i+1]))):
            if keys[pygame.K_LEFT] and playerRec[0] >= 0:
                playerRec[0] += speed
            if keys[pygame.K_UP] and playerRec[1] >= 0:
                playerRec[1] += speed
            if keys[pygame.K_RIGHT] and playerRec[0] + playerRec[2] <= WIDTH:
                playerRec[0] -= speed
            if keys[pygame.K_DOWN] and playerRec[1] + playerRec[3] <= HEIGHT:
                playerRec[1] -= speed

    
    pygame.display.update()
    
