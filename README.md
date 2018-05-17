# SI_2018
Sztuczna Inteligencja 2018 WMI UAM

Developed on Python 3.6 with pygame library

## tilemap.py and astar.py ( + truck.png)

A map with a few types of tiles:
 - grass
 - road
 - houses
 - garbage cans
 - garbage dump
 
 + a garbage truck
 
tilemap uses astar algorithm to find the shortest way from start_point to final_point,
the way might be defined only on road tiles

the truck movement is animated and it stops after reaching the destination,
pressing ENTER will yeet the truck anew (replaying the last route)
you can set the new destination for the truck by clicking the mouse button (if the non-road tile is clicked, nothing happens)

## game.py (old map)

Steering
- Arrow keys
- 1, 2, 3 for truck color change
