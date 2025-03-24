import pygame
from loading_assets import *
from constants import *


CAPTION = "CASTLE_WAR"
 
MELEE_COST = 10
RANGED_COST = 20
WORKER_COST = 10

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
background = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
pause_img = pygame.transform.scale(pause_img, (800, 400))

font = pygame.font.Font('freesansbold.ttf', 32)


class Barrack:
    def __init__(self, isPlayerOne):
        self.isPlayerOne = isPlayerOne

        self.x = BARRACK_POS - BARRACK_WIDTH/2 if self.isPlayerOne else SCREEN_WIDTH - BARRACK_POS - BARRACK_WIDTH/2
        self.y = GROUND_HEIGHT - BARRACK_HEIGHT
        self.state = 0
        self.isHidden = False

        self.cool_down_count = 0
        self.health = BARRACK_HEALTH
        self.hitbox = (self.x, self.y, BARRACK_WIDTH, BARRACK_HEIGHT)


    def draw(self, win):
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)

        pygame.draw.rect(win, (255, 0, 0), (self.x , self.y - BARRACK_HEIGHT/2, BARRACK_WIDTH, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.x , self.y - BARRACK_HEIGHT/2, BARRACK_WIDTH*(self.health/BARRACK_HEALTH), 10))

        barrack = left_barrack if self.isPlayerOne else right_barrack
        win.blit(barrack, (self.x, self.y))

    def move(self, userInput):
        pass


class Mine:
    def __init__(self, isPlayerOne):
        self.isPlayerOne = isPlayerOne

        self.x = MINE_POS - MINE_WIDTH/2 if self.isPlayerOne else SCREEN_WIDTH - MINE_POS - MINE_WIDTH/2
        self.y = GROUND_HEIGHT - MINE_HEIGHT
        self.state = 0
        self.isHidden = False

        self.cool_down_count = 0
        self.health = MINE_HEALTH
        self.hitbox = (self.x, self.y, MINE_WIDTH, MINE_HEIGHT)


    def draw(self, win):
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)

        pygame.draw.rect(win, (255, 0, 0), (self.x , self.y - MINE_HEIGHT/2, MINE_WIDTH, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.x , self.y - MINE_HEIGHT/2, MINE_WIDTH*(self.health/MINE_HEALTH), 10))

        mine = left_mine if self.isPlayerOne else right_mine
        win.blit(mine, (self.x, self.y))

    def move(self, userInput):
        pass


class Wall:
    def __init__(self, isPlayerOne):
        self.isPlayerOne = isPlayerOne

        self.x = WALL_POS - WALL_WIDTH/2 if self.isPlayerOne else SCREEN_WIDTH - WALL_POS - WALL_WIDTH/2
        self.y = GROUND_HEIGHT - WALL_HEIGHT
        self.state = 0
        self.isHidden = False

        self.cool_down_count = 0
        self.health = WALL_HEALTH

        self.hitbox = (self.x, self.y, WALL_WIDTH, WALL_HEIGHT )


    def draw(self, win):
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)

        pygame.draw.rect(win, (255, 0, 0), (self.x , self.y - 1.25*WALL_HEIGHT, WALL_WIDTH, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.x , self.y - 1.25*WALL_HEIGHT, WALL_WIDTH*(self.health/WALL_HEALTH), 10))

        wall = left_wall if self.isPlayerOne else right_wall
        win.blit(wall, (self.x, self.y))

    def move(self, userInput):
        pass


class Tower:
    def __init__(self, isPlayerOne):
        self.isPlayerOne = isPlayerOne

        self.x = (WALL_POS - TOWER_WIDTH/2) if self.isPlayerOne else (SCREEN_WIDTH - WALL_POS - TOWER_WIDTH/2)
        self.y = GROUND_HEIGHT - TOWER_HEIGHT
        self.state = 0
        self.isHidden = False
        self.bullets = []

        self.cool_down_count = 0
        self.health = 200
        self.hitbox = (self.x - TOWER_WIDTH if self.isPlayerOne else self.x + TOWER_WIDTH, self.y, TOWER_WIDTH, TOWER_HEIGHT)

    def draw(self, win):
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)
        
        if self.any_npcs_near():
            self.shoot()

        for bullet in self.bullets:
            bullet.draw()

        tower = left_tower if self.isPlayerOne else right_tower
        win.blit(tower, (self.x, self.y))

    def move(self, userInput):
        pass

    def any_npcs_near(self):
        npcs = right_player.team_list if self.isPlayerOne else left_player.team_list
        for npc in npcs:
            if abs(npc.x - self.x) < TOWER_RANGE:
                return True
        return False

    def cooldown(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.cooldown()
        self.fire()

        if self.cool_down_count == 0:
            bullet = TowerArrow(self.x, GROUND_HEIGHT - TOWER_ARROW_HEIGHT, 1 if self.isPlayerOne else -1)
            self.bullets.append(bullet)
            self.cool_down_count = 1

        for bullet in self.bullets:
            bullet.move()

    def fire(self):
        npcs = right_player.team_list if self.isPlayerOne else left_player.team_list

        for npc in npcs:
            for bullet in self.bullets:
                if not npc.isPlayerOne and npc.hitbox[0] < bullet.x:
                    npc.health -= bullet.damage
                    self.bullets.remove(bullet)
                if npc.isPlayerOne and npc.hitbox[0] + CHAR_WIDTH > bullet.x:
                    npc.health -= bullet.damage
                    self.bullets.remove(bullet)


class TowerArrow:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.damage = TOWER_DMG
        self.paddingX = 25
        self.paddingY = 25
    
    def draw(self):
        if self.direction == 1:
            win.blit(fire_ball, (self.x , self.y))
        else:
            win.blit(fire_ball, (self.x , self.y))

    def move(self):
        self.x = self.x + (self.direction*30)


class RangerArrow:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.paddingX = 0
        self.paddingY = 10
    
    def draw(self):
        win.blit(ranger_fire_ball, (self.x + self.paddingX, self.y + self.paddingY))

    def move(self):
        self.x = self.x + (self.direction * 30)


class Worker:
    def __init__(self, isPlayerOne):
        self.x = None
        self.y = None
        self.vel = 10
        self.isPlayerOne = isPlayerOne
        self.stepIndex = 0
        self.state = 0
        self.type = 'worker'

        self.health = WORKER_HEALTH
        self.cost = 10

        self.isHidden = False

        self.paddingX = 0
        self.paddingY = 0

        self.spawn()
        self.hitbox = (self.x, self.y, CHAR_HEIGHT, CHAR_WIDTH)

    def spawn(self):
        self.x = (BARRACK_POS - BARRACK_WIDTH/2 + CHAR_WIDTH/4 if self.isPlayerOne else SCREEN_WIDTH - BARRACK_POS - BARRACK_WIDTH/2 + CHAR_WIDTH/2) + self.paddingX
        self.y = GROUND_HEIGHT - CHAR_HEIGHT + self.paddingY

    def draw(self, win):
        # self.hitbox = (self.x, self.y, CHAR_WIDTH, CHAR_WIDTH)

        if self.state == 0 or self.state == 1 or self.state == 2:
            worker = left_worker_1 if self.isPlayerOne else right_worker_1
        if self.state == 3 or self.state == 4:
            worker = left_worker_2 if self.isPlayerOne else right_worker_2

        win.blit(worker, (self.x, self.y))
    
    def move(self, userInput):
        player = left_player if self.isPlayerOne else right_player
        player.numberOfHealer = 0
        player.numberOfMiners = 0

        self.mining(player)
        self.healing(player)

        if userInput[pygame.K_a] and self.isPlayerOne:
            self.state = 1
        elif userInput[pygame.K_l] and not self.isPlayerOne:
            self.state = 1
        elif userInput[pygame.K_s] and self.isPlayerOne:
            self.state = 3
        elif userInput[pygame.K_k] and not self.isPlayerOne:
            self.state = 3

        elif self.isPlayerOne and self.state == 1 and self.x < player.mine.x:
            self.isHidden = True
            self.state = 2
        elif not self.isPlayerOne and self.state == 1 and self.x > player.mine.x:
            self.isHidden = True
            self.state = 2
        elif self.isPlayerOne and self.state == 3 and self.x > player.wall.x:
            self.isHidden = True
            self.state = 4
        elif not self.isPlayerOne and self.state == 3 and self.x < player.wall.x:
            self.isHidden = True
            self.state = 4

        elif self.state == 1:
            self.isHidden = False
            self.x = (self.x - self.vel) if self.isPlayerOne else (self.x + self.vel)
        elif self.state == 3:
            self.isHidden = False
            self.x = (self.x + self.vel) if self.isPlayerOne else (self.x - self.vel)


    def mining(self, player):
        if self.isPlayerOne and self.x < player.mine.x:
            player.numberOfMiners += 1
        elif not self.isPlayerOne and self.x > player.mine.x:
            player.numberOfMiners += 1


    def healing(self, player):
        if self.isPlayerOne and self.x > player.wall.x:
            player.numberOfHealer += 1
        elif not self.isPlayerOne and self.x < player.wall.x:
            player.numberOfHealer += 1


class Melee:
    def __init__(self, isPlayerOne):
        self.x = None
        self.y = None
        self.vel = 10
        self.isPlayerOne = isPlayerOne
        self.stepIndex = 0
        self.state = 0
        self.type = 'melee'

        self.health = MELEE_HEALTH
        self.cost = MELEE_COST
        self.cool_down_count = 0
        self.damage = MELEE_DMG

        self.isHidden = False

        self.paddingX = 0
        self.paddingY = 0

        self.spawn()
        self.hitbox = (self.x, self.y, CHAR_HEIGHT, CHAR_WIDTH)

    def spawn(self):
        self.x = (BARRACK_POS - BARRACK_WIDTH/2 + CHAR_WIDTH/4 if self.isPlayerOne else SCREEN_WIDTH - BARRACK_POS - BARRACK_WIDTH/2 + CHAR_WIDTH/4) + self.paddingX
        self.y = GROUND_HEIGHT - CHAR_HEIGHT + self.paddingY

    def move(self, userInput):
        if self.state == 0 and (userInput[pygame.K_d] or userInput[pygame.K_z]) and self.isPlayerOne:
            self.state = 1
        elif self.state == 0 and (userInput[pygame.K_j] or userInput[pygame.K_m]) and not self.isPlayerOne:
            self.state = 1
        elif self.state == 1:
            self.x = (self.x + self.vel) if self.isPlayerOne else (self.x - self.vel)
        elif self.state == 2 and not self.any_npcs_near():
            self.state = 1

    def any_npcs_near(self):
        npcs = right_player.team_list if self.isPlayerOne else left_player.team_list
        for npc in npcs:
            if abs(npc.x - self.x) < 25:
                return True
        return False

    def cooldown(self):
        if self.cool_down_count >= MELEE_DELAY:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.cooldown()
        self.state = 2

        if self.cool_down_count == 0:
            self.cool_down_count = 1

        npcs = right_player.team_list if self.isPlayerOne else left_player.team_list 

        for npc in npcs:
            if abs(npc.x - self.x) < 25:
                npc.health -= self.damage

    def draw(self, win):
        self.hitbox = (self.x, self.y, CHAR_WIDTH, CHAR_WIDTH)
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)

        pygame.draw.rect(win, (255, 0, 0), (self.x , self.y - CHAR_HEIGHT/2, CHAR_WIDTH, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.x , self.y - CHAR_HEIGHT/2, CHAR_WIDTH*(self.health/MELEE_HEALTH), 10))

        if self.any_npcs_near():
            self.shoot()

        melee = left_melee if self.isPlayerOne else right_melee

        if self.stepIndex >= 12:
            self.stepIndex = 1
        if self.state == 0 or self.state == 2:
            win.blit(melee[self.stepIndex], (self.x, self.y))
        if self.state == 1:
            win.blit(melee[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1


class Ranged:
    def __init__(self, isPlayerOne):
        self.x = None
        self.y = None
        self.vel = 10
        self.isPlayerOne = isPlayerOne
        self.stepIndex = 0
        self.state = 0
        self.type = 'ranger'

        self.health = RANGED_HEALTH
        self.cost = RANGED_COST
        self.cool_down_count = 0
        self.damage = RANGED_DMG

        self.paddingX = 0
        self.paddingY = 0

        self.isHidden = False
        self.bullets = []

        self.spawn()
        self.hitbox = (self.x, self.y, CHAR_WIDTH, CHAR_WIDTH)


    def spawn(self):
        self.x = (BARRACK_POS - BARRACK_WIDTH/2 + CHAR_WIDTH/4 if self.isPlayerOne else SCREEN_WIDTH - BARRACK_POS - BARRACK_WIDTH/2 + CHAR_WIDTH/4) + self.paddingX
        self.y = GROUND_HEIGHT - CHAR_HEIGHT + self.paddingY


    def any_npcs_near(self):
        npcs = right_player.team_list if self.isPlayerOne else left_player.team_list
        for npc in npcs:
            if abs(npc.x - self.x) < 100:
                return True
        return False


    def draw(self, win):
        self.hitbox = (self.x, self.y, CHAR_WIDTH, CHAR_WIDTH)
        #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)

        if self.any_npcs_near():
            self.shoot()

        pygame.draw.rect(win, (255, 0, 0), (self.x , self.y - CHAR_HEIGHT/2, CHAR_WIDTH, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.x , self.y - CHAR_HEIGHT/2, CHAR_WIDTH*(self.health/RANGED_HEALTH), 10))

        for bullet in self.bullets:
            bullet.draw()
        
        ranged = left_ranged if self.isPlayerOne else right_ranged

        if self.stepIndex >= 11:
            self.stepIndex = 1
        if self.state == 0 or self.state == 2:
            win.blit(ranged[0], (self.x, self.y))
        if self.state == 1:
            win.blit(ranged[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1


    def move(self, userInput):
        if self.state == 0 and (userInput[pygame.K_f] or userInput[pygame.K_z]) and self.isPlayerOne:
            self.state = 1
        elif self.state == 0 and (userInput[pygame.K_h] or userInput[pygame.K_m]) and not self.isPlayerOne:
            self.state = 1
        elif self.state == 1:
            self.x = (self.x + self.vel) if self.isPlayerOne else (self.x - self.vel)
        elif self.state == 2 and not self.any_npcs_near():
            self.state = 1


    def cooldown(self):
        if self.cool_down_count >= RANGER_DELAY:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1


    def shoot(self):
        self.cooldown()
        self.fire()
        self.state = 2

        if self.cool_down_count == 0:
            bullet = RangerArrow(self.x, self.y, 1 if self.isPlayerOne else -1)
            self.bullets.append(bullet)
            self.cool_down_count = 1

        for bullet in self.bullets:
            bullet.move()


    def fire(self):
        npcs = right_player.team_list if self.isPlayerOne else left_player.team_list

        for npc in npcs:
            for bullet in self.bullets:
                if not npc.isPlayerOne and npc.hitbox[0] < bullet.x:
                    npc.health -= self.damage
                    self.bullets.remove(bullet)
                if npc.isPlayerOne and npc.hitbox[0] + CHAR_WIDTH/2 > bullet.x:
                    npc.health -= self.damage
                    self.bullets.remove(bullet)


class Player:
    def __init__(self, isPlayerOne):
        self.team_list = list()
        self.coin = INIT_RESOURCES
        self.isPlayerOne = isPlayerOne
        self.tower = Tower(self.isPlayerOne)
        self.mine = Mine(self.isPlayerOne)
        self.wall = Wall(self.isPlayerOne)
        self.numberOfMiners = 0
        self.numberOfHealer = 0
        self.cool_down_count = 0
        self.h_cool_down_count = 0
        self.workers = 0
        self.melee = 0
        self.ranger = 0

        self.spawn()

    def spawn(self):
        self.team_list.append(self.tower)
        self.team_list.append(self.wall)
        self.team_list.append(Barrack(self.isPlayerOne))
        self.team_list.append(self.mine)


    def add_worker(self):
        if self.coin >= WORKER_COST:
            self.team_list.append(Worker(self.isPlayerOne))
            self.workers += 1
            self.coin -= WORKER_COST

    def add_melee(self):
        if self.coin >= MELEE_COST:
            self.team_list.append(Melee(self.isPlayerOne))
            self.melee += 1
            self.coin -= MELEE_COST

    def add_ranged(self):
        if self.coin >= RANGED_COST:
            self.team_list.append(Ranged(self.isPlayerOne))
            self.ranger += 1
            self.coin -= RANGED_COST

    def team_size(self):
        return len(self.team_list) - 4

    def cooldown(self):
        if self.cool_down_count >= WORKER_DELAY:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def h_cooldown(self):
        if self.h_cool_down_count >= WORKER_DELAY:
            self.h_cool_down_count = 0
        elif self.h_cool_down_count > 0:
            self.h_cool_down_count += 1

    def generate_coin(self):
        self.cooldown()

        if self.cool_down_count == 0:
            self.coin += (WORKER_MINE*self.numberOfMiners)
            self.cool_down_count = 1

    def heal_wall(self):
        self.h_cooldown()

        if self.h_cool_down_count == 0 and self.wall.health<WALL_HEALTH:
            self.wall.health += WORKER_HEAL*self.numberOfHealer

    def display_stats(self):
        if self.isPlayerOne:
            print("PLAYER 1")
        else:
            print("PLAYER 2")
        print("Coins: ", self.coin)
        print("HEALTH: ", self.wall.health)
        print("HEALTH: ", self.tower.health)

def display_score():
    score_1 = font.render(" x " + str(left_player.coin), True, (255, 0, 0))
    score_2 = font.render(" x " + str(right_player.coin), True, (0, 0, 255))

    win.blit(score_1, (60, 20))
    win.blit(score_2, (SCREEN_WIDTH - 100, 20))

    win.blit(coin, (10, 10))
    win.blit(coin, (SCREEN_WIDTH - 150 , 10))

    # Player 1

    worker = font.render(" x " + str(left_player.workers), True, (255, 0, 0))
    win.blit(worker, (60, 70))
    win.blit(left_worker_1, (10, 70))

    melee = font.render(" x " + str(left_player.melee), True, (255, 0, 0))
    win.blit(melee, (60, 110))
    win.blit(left_melee[0], (10, 110))

    ranger = font.render(" x " + str(left_player.ranger), True, (255, 0, 0))
    win.blit(ranger, (60, 150))
    win.blit(left_ranged[0], (10, 150))

    # Player 2
    worker = font.render(" x " + str(right_player.workers), True, (0, 0, 255))
    win.blit(worker, (SCREEN_WIDTH - 100, 70))
    win.blit(right_worker_2, (SCREEN_WIDTH - 150, 70))

    melee = font.render(" x " + str(right_player.melee), True, (0, 0, 255))
    win.blit(melee, (SCREEN_WIDTH - 100, 110))
    win.blit(right_melee[0], (SCREEN_WIDTH - 150, 110))

    ranger = font.render(" x " + str(right_player.ranger), True, (0, 0, 255))
    win.blit(ranger, (SCREEN_WIDTH - 100, 150))
    win.blit(right_ranged[0], (SCREEN_WIDTH - 150, 150))

def pause_screen():
    win.blit(pause_img, (200, 100))

    pygame.time.delay(100)
    pygame.display.update()
    

def draw_game():
    win.fill((0, 0, 0))
    win.blit(background, (0,0))

    grd = pygame.transform.scale(ground, (SCREEN_WIDTH, SCREEN_HEIGHT))
    win.blit(grd, (0, GROUND_HEIGHT))

    display_score()

    left_player.generate_coin()
    left_player.heal_wall()
    right_player.generate_coin()
    right_player.heal_wall()


    for npc in left_player.team_list:
        if not npc.isHidden:
            npc.draw(win)
    
    for npc in right_player.team_list:
        if not npc.isHidden:
            npc.draw(win)

    pygame.time.delay(100)
    pygame.display.update()


run = True
pause = False
over = False


left_player = Player(True)
left_player.display_stats()
right_player = Player(False)
    

def data_processing(player):
    data = dict()

    data['wall'] = player.wall.health
    data['coins'] = player.coin
    data['melee'] = list()
    data['ranger'] = list()
    data['worker'] = list()

    for idx, npc in enumerate(player.team_list):
        if idx <= 3: 
            continue
        else:
            if npc.type == 'worker':
                data['worker'].append([npc.x, npc.state, npc.isHidden, npc.health])
            if npc.type == 'melee':
                data['melee'].append([npc.x, npc.state, npc.stepIndex, npc.cool_down_count, npc.health])
            if npc.type == 'ranger':
                data['ranger'].append([npc.x, npc.state, npc.stepIndex, npc.cool_down_count, npc.health])

    writable_content = ("START PLAYER1\n" if player.isPlayerOne else "START PLAYER2\n")
    writable_content += ("RESOURCES " + str(data['coins']) + "\n")
    writable_content += ("WALL " + str(data['wall']) + "\n")
    for x in data['melee']:
        writable_content += ("MELEE " + str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + " " + str(x[3]) + " " + str(x[4]) + "\n")
    for x in data['ranger']:
        writable_content += ("ARCHER " + str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + " " + str(x[3]) + " " + str(x[4]) + "\n")
    for x in data['worker']:
        writable_content += ("WORKER " + str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + " " + str(x[3]) + "\n")

    return writable_content


def save_game(player1, player2):
    try:
        writable_content = data_processing(player1)
        writable_content += data_processing(player2)
        
        file = open("save.txt", 'w')
        file.write(writable_content)
        file.close()
        print("GAME SAVED!!!")

    except :
        print("ERROR IN SAVING!!!")


def load_game():
    left_player = Player(True)
    right_player = Player(False)

    try:
        player = None

        file = open("save.txt")

        for line in file:
            commands = line.rstrip('\n').split(' ')
            if commands[0] == "START":
                player = left_player if commands[1] == "PLAYER1" else right_player
            elif commands[0] == "RESOURCES":
                player.coin = int(commands[1])
            elif commands[0] == "WALL":
                player.wall.health = int(commands[1])
            elif commands[0] == "ARCHER":
                ranger = Ranged(player.isPlayerOne)
                ranger.x = float(commands[1])
                ranger.state = int(commands[2])
                ranger.stepIndex = int(commands[3])
                ranger.cool_down_count = int(commands[4])
                ranger.health = int(commands[5])
                player.team_list.append(ranger)
            elif commands[0] == "MELEE":
                melee = Melee(player.isPlayerOne)
                melee.x = float(commands[1])
                melee.state = int(commands[2])
                melee.stepIndex = int(commands[3])
                melee.cool_down_count = int(commands[4])
                melee.health = int(commands[5])
                player.team_list.append(melee)
            elif commands[0] == "WORKER":
                worker = Worker(player.isPlayerOne)
                worker.x = float(commands[1])
                worker.state = int(commands[2])
                worker.isHidden = bool(commands[3])
                worker.health = int(commands[4])
                player.team_list.append(worker)

        print("LOADED SAVED FILE")

    except:
        print("UNABLE TO LOAD")
    
    return [left_player, right_player]

while run:
    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Input
    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_SPACE]:
        pause = not pause
        pygame.time.delay(100)
        continue

    if userInput[pygame.K_v] and userInput[pygame.K_LSHIFT]:
        save_game(left_player, right_player)

    if userInput[pygame.K_b] and userInput[pygame.K_LSHIFT]:
        [left_player, right_player] = load_game()
        draw_game()
        pause = True
        continue

    if pause:
        pause_screen()
        continue

    if userInput[pygame.K_q]:
        left_player.add_worker()
    if userInput[pygame.K_w]:
        left_player.add_melee()
    if userInput[pygame.K_e]:
        left_player.add_ranged()
    if userInput[pygame.K_p]:
        right_player.add_worker()
    if userInput[pygame.K_o]:
        right_player.add_melee()
    if userInput[pygame.K_i]:
        right_player.add_ranged()

    
    for npc in left_player.team_list:
        if npc.health <= 0:
            left_player.team_list.remove(npc)
        npc.move(userInput)

    for npc in right_player.team_list:
        if npc.health <= 0:
            right_player.team_list.remove(npc)
        npc.move(userInput)


    if left_player.wall.health <= 0:
        over = True
        win.fill((0, 0, 0))
        win.blit(winning_screen_p2, (0,0))
        pygame.display.update()

    elif right_player.wall.health <= 0:
        over = True
        win.fill((0, 0, 0))
        win.blit(winning_screen_p1, (0,0))
        pygame.display.update()
    
    
    
    # Draw Game in Window
    if not over:
        draw_game()