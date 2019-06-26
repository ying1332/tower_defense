import pygame
from tdmenu.menu import HorizontalMenu
import os
import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join('menu', 'menu.png')), (120, 50))
upgrade = pygame.transform.scale(pygame.image.load('upgrade.png'), (50, 50))

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [450, 700, 950]
        self.price = [500, 750, 1000]
        self.level = 1
        self.selected = False
        self.menu = HorizontalMenu(self.x, self.y, menu_bg, [4400, 5600], self.level)
        self.menu.add_btn(upgrade, 'Upgrade')
        self.tower_imgs = []
        self.gamage = 1
        self.place_color = (0, 0, 255, 128)

    def draw(self, win):
        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))
        if self.selected:
            self.menu.draw(win)

    def draw_radius(self, win):
        if self.selected:
            surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (0, 255, 0, 128), (self.range, self.range), self.range, 4)
            win.blit(surface, (self.x-self.range, self.y-self.range))

    def draw_placement(self, win):
        surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (45, 45), 45, 4)
        win.blit(surface, (self.x-45, self.y-45))

    def click(self, X, Y):
        img = self.tower_imgs[self.level-1]
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False

    def sell(self):
        return self.sell_price[self.level-1]

    def upgrade(self):
        if self.level  < len(self.tower_imgs):
            self.level += 1
            self.damage += 1

    def move(self, x, y):
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def get_upgrade_cost(self):
        return self.price[self.level-1]

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y
        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 120:
            return False
        else:
            return True
    
