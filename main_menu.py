import pygame
from game import Game
import os

start_btn = pygame.image.load(os.path.join('menu', 'button_play.png'))
logo = pygame.image.load('logo.png')

class MainMenu:
    def __init__(self):
        self.width = 1250
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join('game_assets', 'bg.png'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.btn = (self.width/2 - start_btn.get_width()/2, 350, start_btn.get_width(), start_btn.get_height())
    def __run__(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.win)
                            game.wave = 0
                            game.current_wave = [20, 0, 0][:]
                            game.__run__()
                self.draw(self.win)
        pygame.quit()

    def draw(self, win):
        self.win.blit(self.bg, (0,0))
        self.win.blit(logo, (self.width/2 - logo.get_width()/2, 0))
        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        pygame.display.update()


