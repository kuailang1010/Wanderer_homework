import pygame
from config import *
import os
import random
from random import randrange
pygame.init()

myfont=pygame.font.SysFont("monospace",15)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FLOOR_IMAGE = pygame.image.load(os.path.join('pictures', 'floor.png'))
WALL_IMAGE = pygame.image.load(os.path.join('pictures', 'wall.png'))
# Generate random wall coordination
possible_coordinates1 = [(x*70, y*70) for x in range(1, 4) for y in range(4)]
wall_coordinates = random.sample(possible_coordinates1, 4)

possible_coordinates2 = [(x*70, y*70) for x in range(1, 4) for y in range(5, 7 )]
wall_coordinates.extend(random.sample(possible_coordinates2, 5))

possible_coordinates3 = [(x*70, y*70) for x in range(1, 4) for y in range(8, 10)]
wall_coordinates.extend(random.sample(possible_coordinates3, 3))

possible_coordinates4 = [(x*70, y*70) for x in range(5, 9) for y in range(1, 3)]
wall_coordinates.extend(random.sample(possible_coordinates4, 6))

possible_coordinates5 = [(x*70, y*70) for x in range(5, 9) for y in range(4, 6)]
wall_coordinates.extend(random.sample(possible_coordinates5, 6))

possible_coordinates6 = [(x*70, y*70) for x in range(5, 9) for y in range(7, 9)]
wall_coordinates.extend(random.sample(possible_coordinates6, 5))

#Random skeleton location
skelon_coordinates = []
skelon_generation = random.sample([(x*70, y*70) for x in range(1,9) for y in range(1,9)] , 40)

#Random boss location
boss_coordinates = []
boss_generation = random.sample([(x*70, y*70) for x in range(1,9) for y in range(1,9)] , 40)


for loc in skelon_generation:
   if len(skelon_coordinates) == 3:
        break
   elif loc not in wall_coordinates:
        skelon_coordinates.append(loc)

for loc in boss_generation:
   if len(boss_coordinates) == 1:
        break
   elif loc not in wall_coordinates and loc not in skelon_coordinates:
        boss_coordinates.append(loc)





HERO_IMAGE_DOWN = pygame.image.load(os.path.join('pictures','hero-down.png'))
HERO_IMAGE_UP = pygame.image.load(os.path.join('pictures','hero-up.png'))
HERO_IMAGE_LEFT = pygame.image.load(os.path.join('pictures','hero-left.png'))
HERO_IMAGE_RIGHT = pygame.image.load(os.path.join('pictures','hero-right.png'))
SKELETON_IMAGE = pygame.image.load(os.path.join('pictures','skeleton.png'))
BOSS_IMAGE = pygame.image.load(os.path.join('pictures','boss.png'))

wall_x = []
wall_y = []
for a in wall_coordinates:
    n = 0
    for b in a:
        if n == 0:
            wall_x.append(b)
            n += 1
        else:
            wall_y.append(b)


def draw_map(P,skeleton1,skeleton2,skeleton3,boss):

    WIN.fill(WHITE)
    # floor
    for m in range(10):
        for n in range(10):

            WIN.blit(FLOOR_IMAGE, (m*70, n*70))

    # random walls

    for wall in wall_coordinates:
        WIN.blit(WALL_IMAGE, wall)

        # Hero

    Hero_text = myfont.render(f"{P}",1,(0,0,0))
    WIN.blit(Hero_text,(0,705))


    skeleton1.draw(WIN)
    skeleton2.draw(WIN)
    skeleton3.draw(WIN)
    boss.draw(WIN)
    P.draw(WIN)


    pygame.display.update()



def main():

    P = Player(0,0,HERO_IMAGE_DOWN,hp_hero,dp_hero,sp_hero)

    skeleton1 = Skeleton(skelon_coordinates[0][0],skelon_coordinates[0][1],SKELETON_IMAGE,hp_skeleton,dp_skeleton,sp_skeleton, True)
    skeleton2 = Skeleton(skelon_coordinates[1][0], skelon_coordinates[1][1], SKELETON_IMAGE,hp_skeleton,dp_skeleton,sp_skeleton, False)
    skeleton3 = Skeleton(skelon_coordinates[2][0], skelon_coordinates[2][1], SKELETON_IMAGE,hp_skeleton,dp_skeleton,sp_skeleton, False)
    boss = Boss(boss_coordinates[0][0], boss_coordinates[0][1], BOSS_IMAGE,hp_boss,dp_boss,sp_boss)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(6)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        P.move()
        draw_map(P,skeleton1,skeleton2,skeleton3,boss)





class Player():

    def __init__(self, x, y,  image, HP, DP, SP):
        self.x = x
        self.y = y
        self.vel = 70
        self.image = image
        self.HP = HP
        self.DP = DP
        self.SP = SP

    def __str__(self):
        return f"Hero (Level 1) HP: {self.HP}/{hp_hero} | DP: {self.DP} | SP: {self.SP}"

    def draw(self,WIN):

        WIN.blit(self.image, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.x > 0 and (self.x - self.vel, self.y) not in wall_coordinates:
                self.x -= self.vel
            self.image = HERO_IMAGE_LEFT
        if keys[pygame.K_d]:
            if self.x < 630 and (self.x + self.vel, self.y) not in wall_coordinates:
                self.x += self.vel
            self.image = HERO_IMAGE_RIGHT
        if keys[pygame.K_w]:
            if self.y > 0 and (self.x , self.y - self.vel) not in wall_coordinates:
                self.y -= self.vel
            self.image = HERO_IMAGE_UP
        if keys[pygame.K_s]:
            if self.y < 630 and (self.x , self.y + self.vel) not in wall_coordinates:
                self.y += self.vel
            self.image = HERO_IMAGE_DOWN


class Skeleton():
    def __init__(self, x, y, image,HP, DP, SP, Key):
        self.x = x
        self.y = y
        self.image = image
        self.HP = HP
        self.DP = DP
        self.SP = SP
        self.key = Key
    def draw(self,WIN):

        WIN.blit(self.image, (self.x, self.y))

class Boss():
    def __init__(self, x, y, image,HP, DP, SP):
        self.x = x
        self.y = y
        self.image = image
        self.HP = HP
        self.DP = DP
        self.SP = SP
    def draw(self,WIN):

        WIN.blit(self.image, (self.x, self.y))




if __name__ == "__main__":
    main()
