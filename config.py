from random import randrange
WIDTH = 700
HEIGHT = 800
WHITE = (255, 255, 255)
HERO_WIDTH, HERO_HEIGHT = 70,70
hp_hero = 20 + 3 * randrange(6)
dp_hero = 5 + randrange(6)
sp_hero = 2 * randrange(6)

hp_skeleton = 2 * randrange(6)
dp_skeleton = 0.5 * randrange(6)
sp_skeleton =  range(6)

hp_boss = 2 * randrange(6) + randrange(6)
dp_boss = 0.5 * randrange(6) + randrange(6)/2
sp_boss = randrange(6) + 1