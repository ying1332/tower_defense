import pygame
import os
from enemy import Enemy

imgs1 = [pygame.image.load(os.path.join('enemies/8', '8_enemies_1_walk_00' + str(x) + '.png'))for x in range(10)]
imgs2 = [pygame.image.load(os.path.join('enemies/8', '8_enemies_1_walk_0' + str(x) + '.png'))for x in range(10, 20)]
imgs23 = imgs1 + imgs2
imgs = []
for img in imgs23:
    imgs.append(pygame.transform.scale(img, (64, 64)))

class Sword(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.health = 20
        self.name = 'sword'
        self.max_health = 20
        self.money = 100
        self.imgs = imgs[:]
