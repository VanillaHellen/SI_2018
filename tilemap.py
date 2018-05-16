import pygame, sys
import random
import time
from pygame.locals import *

# constants
G = 0 # GRASS
R = 1 # ROAD
C = 2 # GARBAGECAN
H = 3 # HOUSE
D = 4 # GARBAGE DUMP
P = 5 # PLASTIC
PP = 6 # PAPER
GL = 7 #GLASS

# colours
colours = {
    G: (58, 163, 42),
    R: (192, 192, 192),
    C: (255, 0, 10),
    H: (240, 230, 140),
    D: (99, 85, 37),
    P: (135,206,250),
    PP: (255,255,51),
    GL: (127,255,0)
}

tilemap = [
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],
    [G, H, H, H, G, G, G, H, H, H, G, G, G, G, G, G, H, H, H, G, G, G, G, G, G],
    [G, H, C, H, G, G, G, H, C, H, G, G, G, G, G, G, H, C, H, G, G, G, G, G, G],
    [G, G, R, G, G, G, G, G, R, G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G],
    [G, G, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, G, G, G, G, G],
    [G, G, R, G, G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, R, G, G, G, G, G],
    [G, G, R, G, G, H, H, H, G, G, G, G, R, G, G, G, G, G, G, R, G, H, H, G, G],
    [G, G, R, G, G, H, C, H, G, G, G, G, R, G, G, G, G, G, G, R, R, C, H, G, G],
    [G, G, R, G, G, G, R, G, G, G, G, G, R, G, G, G, G, G, G, R, G, H, H, G, G],
    [G, G, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, G, G, G, G, G],
    [G, G, R, G, G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, G, G, G, G, G],
    [G, G, R, G, G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, G, G, G, G, G],
    [G, G, R, G, G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, G, G, G, G, G],
    [G, H, C, H, G, G, G, G, G, G, G, G, R, G, D, D, D, D, D, G, G, G, G, G, G],
    [G, H, H, H, G, G, G, G, G, G, G, G, R, G, P, D, PP, D, GL, G, G, G, G, G, G],
    [G, G, G, G, G, G, G, G, G, G, G, G, R, R, R, R, R, R, R, G, G, G, G, G, G],
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],

]

# map dimensions
TILESIZE = 40
MAPWIDTH = 25
MAPHEIGHT = 17

# garbage truck
TRUCK = pygame.image.load('truck.png')
TRUCKpos = [18,15]

def move(pos):

    #tryLeft
    if (tilemap[pos[1]][pos[0] - 1] == 1):
        pos[0] -= 1
        return pos

    #tryUp
    elif (tilemap[pos[1] - 1][pos[0]] == 1):
        pos[1] -= 1
        return pos

    # tryRight
    elif (tilemap[pos[1]][pos[0] + 1] == 1):
        pos[0] += 1
        return pos

    #tryDown
    if (tilemap[pos[1] + 1][pos[0]] == 1):
        pos[1] += 1
        return pos




# set up the disp
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption('Inteligentna Śmieciara')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if (event.key == K_RETURN):
                TRUCKpos = [18,15]
        '''elif event.type == KEYDOWN:
            if (event.key == K_RETURN):
                TRUCKpos = move(TRUCKpos)
                if TRUCKpos[0] > MAPWIDTH - 1:
                    TRUCKpos[0] -= 1
                if TRUCKpos[0] < 0:
                    TRUCKpos[0] += 1
                if TRUCKpos[1] > MAPHEIGHT - 1:
                    TRUCKpos[1] -= 1
                if TRUCKpos[1] < 0:
                    TRUCKpos[1] += 1'''

    for row in range(MAPHEIGHT):
        # look through each column in a row
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAY, colours[tilemap[row][column]],
                             (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))

    TRUCKpos = move(TRUCKpos)
    if TRUCKpos[0] > MAPWIDTH - 1:
        TRUCKpos[0] -= 1
    if TRUCKpos[0] < 0:
        TRUCKpos[0] += 1
    if TRUCKpos[1] > MAPHEIGHT - 1:
        TRUCKpos[1] -= 1
    if TRUCKpos[1] < 0:
        TRUCKpos[1] += 1
    DISPLAY.blit(TRUCK, (TRUCKpos[0]*TILESIZE, TRUCKpos[1]*TILESIZE))

    pygame.display.update()
    time.sleep(0.1)
