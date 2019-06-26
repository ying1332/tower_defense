import pygame
from tower import Tower
import os
import math

range_imgs = [pygame.transform.scale(pygame.image.load(os.path.join('support', '4.png')), (90, 90)),
              pygame.transform.scale(pygame.image.load(os.path.join('support', '5.png')), (90, 90))]

class RangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs = range_imgs[:]
        self.effect = [0.2, 0.4]
        self.width = self.height = 90
        self.damage = 1
        self.name = 'range'

    def draw(self, win):
        super().draw(win)
        super().draw_radius(win)

    def support(self, towers):
        effected = []
        for tower in towers:
            x, y = tower.x, tower.y
            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis <= self.range + tower.width/2:
                effected.append(tower)
        for tower in effected:
            tower.range = tower.orig_range + round(tower.range * self.effect[self.level-1])
                

damage_imgs = [pygame.transform.scale(pygame.image.load(os.path.join('support', '8.png')), (90, 90)),
              pygame.transform.scale(pygame.image.load(os.path.join('support', '9.png')), (90, 90))]
class DamageTower(RangeTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs = damage_imgs[:]
        self.effect = [1, 2]
        self.width = self.height = 90
        self.damage = 1
        self.name = 'damage'

    def support(self, towers):
        effected = []
        for tower in towers:
            x, y = tower.x, tower.y
            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis <= self.range + tower.width/2:
                effected.append(tower)
        for tower in effected:
            tower.damage = tower.orig_damage + round(tower.orig_damage * self.effect[self.level-1])
        
