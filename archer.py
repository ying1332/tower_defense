import pygame
from tower import Tower
import os
import math
from tdmenu.menu import HorizontalMenu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join('menu', 'menu.png')), (120, 50))
upgrade = pygame.transform.scale(pygame.image.load('upgrade.png'), (50, 50))

tower_imgs_1 = []
archer_imgs_1 = []

for i in range(7, 10):
    tower_imgs_1.append(pygame.transform.scale(pygame.image.load(os.path.join('archer/long', str(i) + '.png')),(64, 64)))
for i in range(37, 43):
    archer_imgs_1.append(pygame.image.load(os.path.join('archer/archer_top', str(i) + '.png')))

class ArcherLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs_1[:]
        self.archer_imgs = archer_imgs_1[:]
        self.archer_count = 0
        self.range = 200
        self.orig_range = self.range
        self.in_range = False
        self.left = False
        self.damage = 1
        self.orig_damage = self.damage
        self.width = 90
        self.height = 90
        self.menu = HorizontalMenu(self.x, self.y, menu_bg, [2000, 2500, 5000], self.level)
        self.menu.add_btn(upgrade, 'Upgrade')
        self.archer = self.archer_imgs[0]
        self.moving = False
        self.name = 'archer'


    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)
        if self.in_range and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs)*7:
                self.archer_count = 0
        self.archer = self.archer_imgs[self.archer_count // 7]
        if self.left == True:
            add = -self.archer.get_width() + 10
        else:
            add = (-self.archer.get_width() + 10)/5
        win.blit(self.archer, ((self.x+add), (self.y -self.archer.get_height() - 20)))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        money = 0
        self.in_range = False
        enemies_closest = []
        for enemy in enemies:
            x, y = enemy.x, enemy.y
            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis < self.range:
                self.in_range = True
                enemies_closest.append(enemy)
        enemies_closest.sort(key=lambda x: x.path_pos)
        if len(enemies_closest) > 0:
            first_enemy = enemies_closest[0]
            if self.archer_count == 28:
                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x  < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
        return money
tower_imgs = []
archer_imgs = []
for i in range(7, 10):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join('archer/short', str(i) + '.png')),(64, 64)))
for i in range(43, 49):
    archer_imgs.append(pygame.image.load(os.path.join('archer/short', str(i) + '.png')))

class ArcherShort(ArcherLong):
    def __init__(self, x, y):
        ArcherLong.__init__(self, x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 120
        self.in_range = False
        self.left = False
        self.damage = 2
        self.orig_damage = self.damage
        self.orig_range = self.range
        self.width = 90
        self.height = 90_2
        self.menu = HorizontalMenu(self.x, self.y, menu_bg, [2400, 2800, 5200], self.level)
        self.menu.add_btn(upgrade, 'Upgrade')
        self.name = 'archer'
