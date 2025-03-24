import pygame
import os
from constants import *

bg_img = pygame.image.load('./assets/sky.png')
ground = pygame.image.load('./assets/ground.png')
pause_img = pygame.image.load('./assets/control.jpg')


left_melee = [None]*12
for picIndex in range(1,12):
    left_melee[picIndex] = pygame.transform.scale(pygame.image.load(os.path.join("assets/melee/left/", "run-" + str(picIndex-1) + ".png")), (CHAR_WIDTH, CHAR_HEIGHT))
    picIndex += 1

right_melee = [None]*12
for picIndex in range(1,12):
    right_melee[picIndex] = pygame.transform.scale(pygame.image.load(os.path.join("assets/melee/right/", "run-" + str(picIndex-1) + ".png")), (CHAR_WIDTH, CHAR_HEIGHT))
    picIndex += 1

left_melee[0] = pygame.transform.scale(pygame.image.load(os.path.join("assets/melee/left/", "ready.png")), (CHAR_WIDTH, CHAR_HEIGHT))
right_melee[0] = pygame.transform.scale(pygame.image.load(os.path.join("assets/melee/right/", "ready.png")), (CHAR_WIDTH, CHAR_HEIGHT))


left_worker_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets/worker", "ls.png")), (CHAR_WIDTH, CHAR_HEIGHT))
left_worker_2 = pygame.transform.flip(left_worker_1, True, False)
right_worker_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets/worker", "rs.png")), (CHAR_WIDTH, CHAR_HEIGHT))
right_worker_2 = pygame.transform.flip(right_worker_1, True, False)


left_ranged = [None]*12
for picIndex in range(12):
    left_ranged[picIndex] = pygame.transform.scale(pygame.image.load(os.path.join("assets/archer/left", "run-" + str(picIndex) + ".png")), (CHAR_WIDTH, CHAR_HEIGHT))
    picIndex += 1

right_ranged = [None]*12
for picIndex in range(12):
    right_ranged[picIndex] = pygame.transform.scale(pygame.image.load(os.path.join("assets/archer/right", "run-" + str(picIndex) + ".png")), (CHAR_WIDTH, CHAR_HEIGHT))
    picIndex += 1


left_barrack = pygame.transform.scale(pygame.image.load('./assets/building/left/barracks.png'), (BARRACK_WIDTH, BARRACK_HEIGHT))
left_mine = pygame.transform.scale(pygame.image.load('./assets/building/left/mine.png'), (MINE_WIDTH, MINE_HEIGHT))
left_wall = pygame.transform.scale(pygame.image.load('./assets/building/left/wall.png'), (WALL_WIDTH, WALL_HEIGHT))
left_tower = pygame.transform.scale(pygame.image.load('./assets/building/left/tower.png'), (TOWER_WIDTH, TOWER_HEIGHT))

right_barrack = pygame.transform.scale(pygame.image.load('./assets/building/right/barracks.png'), (BARRACK_WIDTH, BARRACK_HEIGHT))
right_mine = pygame.transform.scale(pygame.image.load('./assets/building/right/mine.png'), (MINE_WIDTH, MINE_HEIGHT))
right_wall = pygame.transform.scale(pygame.image.load('./assets/building/right/wall.png'), (WALL_WIDTH, WALL_HEIGHT))
right_tower = pygame.transform.scale(pygame.image.load('./assets/building/right/tower.png'), (TOWER_WIDTH, TOWER_HEIGHT))

fire_ball = pygame.transform.scale(pygame.image.load('./assets/fire.png'), (TOWER_ARROW_WIDTH, TOWER_ARROW_HEIGHT))
ranger_fire_ball = pygame.transform.scale(pygame.image.load('./assets/fire.png'), (10, 10))


winning_screen_p1 = pygame.transform.scale(pygame.image.load('./assets/winner_1.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
winning_screen_p2 = pygame.transform.scale(pygame.image.load('./assets/winner_2.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

coin = pygame.transform.scale(pygame.image.load('./assets/coin.png'), (50, 50))