import pygame
import os
from scorpion import Scorpion
from wizard import Wizard
from invader import Invader
from sword import Sword
from archer import ArcherLong
from archer import ArcherShort
from support import RangeTower
from support import DamageTower
import time
from tdmenu.menu import VerticalMenu, PlayPauseButton
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from screen import Screen
pygame.font.init()
pygame.mixer.init()

path = [(9, 212), (66, 211), (135, 211), (196, 234), (239, 260), (309, 267), (368, 270), (416, 270), (474, 266), (544, 259), (600, 249), (620, 206), (643, 156), (657, 115), (690, 74), (744, 74), (803, 73), (841, 113), (857, 147), (868, 183), (876, 210), (892, 237), (936, 273), (996, 284), (1062, 304), (1079, 364), (1064, 427), (1020, 470), (956, 481), (889, 483), (811, 501), (722, 529), (631, 548), (561, 544), (471, 546), (395, 542), (288, 538), (331, 540), (210, 529), (268, 534), (150, 514), (111, 477), (93, 442), (80, 397), (59, 355), (23, 334), (2, 328)]

lives_img = pygame.image.load('heart.png')
moneys_img = pygame.image.load('star.png')
side_img = pygame.transform.scale(pygame.image.load('side_menu.png'), (120, 500))

long_img = pygame.transform.scale(pygame.image.load(os.path.join('sidemenubtn', 'long.png')), (75, 75))

short_img = pygame.transform.scale(pygame.image.load(os.path.join('sidemenubtn', 'short.png')), (75, 75))

range_img = pygame.transform.scale(pygame.image.load(os.path.join('sidemenubtn', 'range.png')), (75, 75))

damage_img = pygame.transform.scale(pygame.image.load(os.path.join('sidemenubtn', 'damage.png')), (75, 75))

attack_tower_names = ['archer', 'archer_2']
support_tower_names = ['damage', 'range']

music = pygame.mixer.music.load('tower_defense.wav')

play_button = pygame.transform.scale(pygame.image.load('button_start.png'), (75, 75))
pause_button = pygame.transform.scale(pygame.image.load('button_pause.png'), (75, 75))
sound_btn = pygame.transform.scale(pygame.image.load('button_sound.png'), (75, 75))
sound_off_btn = pygame.transform.scale(pygame.image.load('button_sound_off.png'), (75, 75))
wave_bg = pygame.transform.scale(pygame.image.load('wave.png'), (205, 50))

#waves are in format
#(#scorpions, #wizards, #invaders, #swords)
waves = [
    [20, 0, 0],
    [50, 0, 0],
    [100, 0, 0],
    [0, 20, 0, 1],
    [10, 30, 0],
    [30, 10, 10],
    [20, 20, 10],
    [50, 40, 30, 1],
    [100, 50, 20],
    [100, 60, 25],
    [150, 80, 30],
    [100, 20, 50],
    [50, 120, 70],
    [100, 10, 100, 2],
    [200, 100, 120, 2],
    [300, 150, 150, 3]
]

class Game:
    def __init__(self, win):
        self.width = 1250
        self.height = 700
        self.win = win
        self.enemies = []
        self.attack_towers = []
        self.support_towers = []
        self.lives = 15
        self.money = 2000
        self.bg = pygame.image.load(os.path.join('game_assets', 'bg.png'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.font = pygame.font.SysFont('comicsans', 60)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - side_img.get_width() +70, 250, side_img)
        self.menu.add_btn(long_img, 'buy_archer', 500)
        self.menu.add_btn(short_img, 'buy_archer_2', 750)
        self.menu.add_btn(damage_img, 'buy_damage', 1240)
        self.menu.add_btn(range_img, 'buy_range', 1200)
        self.moving_object = None
        self.wave = 0
        if self.wave <= 15:
            self.current_wave = waves[self.wave][:]
        self.pause = True
        self.music_on = True
        self.playPauseButton = PlayPauseButton(play_button, pause_button, 10, self.height-85)
        self.SoundButton = PlayPauseButton(sound_btn, sound_off_btn, 90, self.height-85)
        
    def draw(self):
        self.win.blit(self.bg, (0, 0))
        to_del = []
        if self.moving_object:
            self.moving_object.draw_placement(self.win)
            for tower in self.attack_towers + self.support_towers:
                tower.draw_placement(self.win)
        for en in self.enemies:
            if en.x < -5:
                to_del.append(en)
            else:
                en.draw(self.win)
        for d in to_del:
            self.lives -= 1
            self.enemies.remove(d)
        for tw in self.attack_towers:
            self.money += tw.attack(self.enemies)
        for tw in self.support_towers:
            tw.support(self.attack_towers)
        if self.selected_tower:
            self.selected_tower.draw(self.win)
        if self.moving_object:
            self.moving_object.draw(self.win)
        for tw in self.attack_towers:
            tw.draw(self.win)
        for tw in self.support_towers:
            tw.draw(self.win)
        self.playPauseButton.draw(self.win)
        self.SoundButton.draw(self.win)
        text = self.font.render(str(self.lives), 1, (255, 255, 255))
        live_img = pygame.transform.scale(lives_img, (50, 50))
        start_x = self.width - live_img.get_width()-5
        self.win.blit(text, (start_x - text.get_width()-10, 13))
        self.win.blit(live_img, (start_x, 10))

        text = self.font.render(str(self.money), 1, (255, 255, 255))
        money_img = pygame.transform.scale(moneys_img, (50, 50))
        start_x = self.width - money_img.get_width()-5
        self.win.blit(text, (start_x - text.get_width()-10, 75))
        self.win.blit(money_img, (start_x, 65))

        self.win.blit(wave_bg, (10, 10))
        text = self.font.render('Wave #' + str(self.wave), 1, (255, 255, 255))
        self.win.blit(text, (10 + wave_bg.get_width()/2 - text.get_width()/2, 20))
        self.menu.draw(self.win)
        pygame.display.update()

    def point_to_line(self, tower):
##        old version
##        x, y = tower.x, tower.y
##        for n, point in enumerate(path):
##            point_x, point_y = point[0], point[1]
##            dis_x = abs(point_x - x)
##            dis_y = abs(point_y - y)
##            dis = math.sqrt((dis_x - x)**2 + (dis_y - y)**2)
##            print(dis)
##            if dis < 130:
##                return False
        return True
            

    def gen_enemies(self):
        if sum(self.current_wave) <= 0 and len(self.enemies) == 0:
            self.wave += 1
            self.current_wave = waves[self.wave]
            self.pause = True
            self.playPauseButton.change_img()
        else:
            wave_enemies = [Scorpion(), Wizard(), Invader(), Sword()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] -= 1
                    break

    def __run__(self):
        pygame.mixer.music.play(loops=-1)
        run = True
        clock = pygame.time.Clock()
        tower_list = self.attack_towers[:] + self.support_towers[:]
        while run:
            clock.tick(60)
            pos = pygame.mouse.get_pos()
            if self.pause == False:
                if time.time() - self.timer > 1.5:
                    if self.wave == 16:
                        self.wave16()
                        run = False
                    else:
                        self.timer = time.time()
                        self.gen_enemies()
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.moving_object:
                        not_allowed = False
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True
                            self.moving_object.draw_placement(self.win)
                            tower.draw_placement(self.win)
                        if not not_allowed and self.point_to_line(self.moving_object):
                            self.moving_object.move(pos[0], pos[1])
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)
                            self.moving_object.moving = False
                            self.moving_object = None
                    else:
                        if self.playPauseButton.click(pos[0], pos[1]):
                            self.pause = not self.pause
                            self.playPauseButton.change_img()
                        if self.SoundButton.click(pos[0], pos[1]):
                            self.music_on = not self.music_on
                            self.SoundButton.change_img()
                            if self.music_on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()
                        side_menu_clicked = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_clicked:
                            cost = self.menu.get_item_cost(side_menu_clicked)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_clicked)
                    #===========================
                    btn_clicked = None
                    if self.selected_tower:
                        btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                        if btn_clicked == 'Upgrade':
                            cost = self.selected_tower.menu.get_upgrade_cost()
                            if self.money >= cost:
                                self.money -= cost
                                self.selected_tower.upgrade()
                    if not btn_clicked:    
                        for tw in self.support_towers + self.attack_towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False
            self.draw()
            if self.lives <= 0:
                print('You Lose')
                self.wave16()
                run = False

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ['buy_archer', 'buy_archer_2', 'buy_damage', 'buy_range']
        object_list = [ArcherLong(x, y), ArcherShort(x, y), DamageTower(x, y), RangeTower(x, y)]
        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            
        except Exception as e:
            print(str(e), 'NOT VALID NAME')

    def wave16(self):
        screen = Screen(16, self.win)
        screen.run()
