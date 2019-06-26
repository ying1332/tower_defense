import pygame
import math

class Enemy:
    def __init__(self):
        self.x = 35
        self.y = 222
        self.animation_count = 0
        self.health = 5
        self.width = 64
        self.height = 64
        #path not hardcoded
        self.path = [(8, 218), (175, 222), (253, 267), (573, 267), (634, 218), (647, 143), (674, 99), (725, 78), (810, 81), (844, 123), (861, 180), (876, 216), (910, 256), (965, 269), (1014, 301), (1066, 333), (1072, 393), (1066, 441), (1022, 485), (947, 486), (734, 522), (216, 564), (147, 540), (106, 488), (88, 420), (67, 371), (27, 346), (0, 339)]
        self.vel = 3
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.imgs = []
        self.flipped = False
        self.max_health = 5

    def draw(self, win):
        self.img = self.imgs[self.animation_count]
        win.blit(self.img, (self.x-self.img.get_width(), self.y-self.img.get_height()))
        self.health_bar(win)
        self.move()

    def health_bar(self, win):
        length = 50
        move_by = length/self.max_health
        health_bar = move_by*self.health
        pygame.draw.rect(win, (255, 0, 0), (self.x-50, self.y-70, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x-50, self.y-70, health_bar, 10), 0)

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = -10, 335
        else:
            x2, y2 = self.path[self.path_pos+1]
        x1 += 20
        x2 += 20
        dirn = ((x2 - x1)*3, (y2 - y1)*3)
        length = math.sqrt(dirn[0]**2 + dirn[1]**2)
        dirn = (dirn[0]/length*1.2, dirn[1]/length*1.2)
        if dirn[0] < 0 and not self.flipped:
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)
                self.flipped = True
        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))
        self.x = move_x
        self.y = move_y
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.move_dis += length
        if dirn[0] >= 0:
            if dirn[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:
            if dirn[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y <= y2:
                    self.path_pos += 1

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
