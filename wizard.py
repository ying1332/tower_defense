import pygame
import os
from enemy import Enemy

imgs1 = [pygame.image.load(os.path.join('enemies/2', '2_enemies_1_walk_00' + str(x) + '.png'))for x in range(10)]
imgs2 = [pygame.image.load(os.path.join('enemies/2', '2_enemies_1_walk_0' + str(x) + '.png'))for x in range(10, 20)]
imgs23 = imgs1 + imgs2
imgs = []
for img in imgs23:
    imgs.append(pygame.transform.scale(img, (64, 64)))

class Wizard(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.health = 4
        self.name = 'wizard'
        self.max_health = 4
        self.money = 9
        self.imgs = imgs[:]
