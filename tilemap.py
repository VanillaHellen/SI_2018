import pygame, sys
import random
import time
from pygame.locals import *
from astar import *
from dtree import *

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

ROADS = []
for w in range (0, 24):
    for h in range (0, 16):
        if (tilemap[h][w] == 1):
            ROADS.append((w, h))
print(ROADS)

#[[(house), [color, transparency, smell, elastic, other, dirt, size, weight, sound, reflectiveness]]]
DUMPSTERS = [[(20, 7), [[0.0, 0.0, 0.2, 0.0, 0.0, 0.2, 0.4, 0.5, 0.5, 0.6], [0.6, 0.1, 0.0, 0.0, 0.0, 0.7, 0.4, 0.5, 0.5, 0.3]]],
         [(17,3), [[0.5, 1, 0.3, 0.0, 0.1, 0.4, 0.3, 0.3, 0, 0.0], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [0.3, 1.0, 0.2, 0.0, 0.0, 0.2, 0.5, 0.5, 0.2, 0.0]]],
         [(8,3), [[0.4, 1.0, 0.2, 0.0, 0.1, 0.0, 0.5, 0.5, 0.2, 0.0],[0.7, 1.0, 0.0, 0.0, 0.0, 0.2, 0.1, 0.3, 0.2, 0.4], [0.4, 1.0, 0.2, 0.0, 0.1, 0.0, 0.9, 0.9, 0.2, 0.0]]],
         [(2,3), [[0.2, 1.0, 0.2, 0.0, 0.2, 0.1, 0.9, 0.9, 0.2, 0.0], [0.8, 0.4, 0.2, 0.0, 0.1, 0.3, 0.6, 0.7, 0.5, 0.2], [0.3, 1.0, 0.2, 0.0, 0.1, 0.7, 0.2, 0.2, 0.2, 0.0], [0.8, 1.0, 0.0, 0.1, 0.0, 0.4, 0.1, 0.1, 0.1, 0.1]]],
         [(2,12), [[0.0, 1.0, 0.2, 0.0, 0.0, 0.2, 0.9, 0.9, 0.2, 0.0], [0.3, 1.0, 0.2, 0.0, 0.7, 0.7, 1.0, 1.0, 0.2, 0.0]]],
         [(6,8), [[0.2, 0.1, 0.6, 0.2, 0.2, 0.3, 0.3, 0.3, 0.0, 0.0], [0.5, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.4, 0.4, 0.2], [0.2, 1.0, 0.2, 0.0, 0.3, 0.2, 0.9, 0.9, 0.2, 0.0], [0.0, 1.0, 0.0, 0.1, 0.0, 0.0, 0.1, 0.1, 0.1, 0.0]]]]


t = buildTree()
'''
dotfile = open("C:/Users/Agatha/Desktop/szi/dtree.dot", 'w')
tree.export_graphviz(t, out_file = dotfile, feature_names = ['color', 'transparency', 'smell', 'elastic', 'other', 'dirt', 'size', 'weight', 'sound', 'reflectiveness'])
dotfile.close()
'''

start_point = (18, 14)
final_point = (18, 15)
# road points for truck:
# main start poit: (18, 14)
# containers: green (18, 14) yellow (16, 14) blue (14, 14)
# houses: (2,3) (8,3) (17,3) (20,7) ?? (6, 8) (2, 12)

route = Plan_Route(start_point, final_point, ROADS)
actions = astar_search(route).reconstruct_path()
print(actions)

def move(pos, where):
    if (where == "up"):
        pos[1] -= 1
        return pos
    elif (where == "down"):
        pos[1] += 1
        return pos
    elif (where == "right"):
        pos[0] += 1
        return pos
    elif (where == "left"):
        pos[0] -= 1
        return pos

# garbage truck
TRUCK = pygame.image.load('truck.png')
TRUCKpos = list(start_point)

# set up the disp
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption('this truck empty! YEET!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if (event.key == K_RETURN):
                TRUCKpos = list(start_point)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_point = final_point
            mposX = int(pygame.mouse.get_pos()[1] / TILESIZE)
            mposY = int(pygame.mouse.get_pos()[0] / TILESIZE)
            if(tilemap[mposX][mposY]) == 1:
                final_point = (mposY, mposX)
                route = Plan_Route(start_point, final_point, ROADS)
                actions = astar_search(route).reconstruct_path()
                print(actions)

    for m in actions: # walk through listof moves generated by astar
        for row in range(MAPHEIGHT):
            # look through each column in a row
            for column in range(MAPWIDTH):
                pygame.draw.rect(DISPLAY, colours[tilemap[row][column]],
                                 (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))

        if(TRUCKpos != list(final_point)):
            TRUCKpos = move(TRUCKpos, m)
            DISPLAY.blit(TRUCK, (TRUCKpos[0]*TILESIZE, TRUCKpos[1]*TILESIZE))

            print(TRUCKpos[0], TRUCKpos[1])
########### trash recognition
            for i in range(0,6):
                if(DUMPSTERS[i][0] == (TRUCKpos[0], TRUCKpos[1])):
                    print(DUMPSTERS[i][1])  # prints data array
                    a = DUMPSTERS[i][1]
                    print(predictTypeOfTrash(t, a))  # prints recognised trash

###########
            pygame.display.update()
            time.sleep(0.1)
