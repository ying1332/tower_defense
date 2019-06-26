import pygame
from tdmenu.menu import PlayPauseButton

winbg = pygame.transform.scale(pygame.image.load('bg.png'), (1250, 700))

winimg = pygame.image.load('header_win.png')

wintab = pygame.transform.scale(pygame.image.load('table.png'), (400, 500))

play_button = pygame.transform.scale(pygame.image.load('button_start.png'), (75, 75))
pause_button = pygame.transform.scale(pygame.image.load('button_pause.png'), (75, 75))

class Screen:
    def __init__(self, wave, win):
        self.wave = wave
        self.faded = False
        self.win = win
        self.fade = pygame.Surface((1250, 700))

    def fadeoff(self):
        self.fade.fill((0, 0, 0))
        for alpha in range(0, 300):
            self.fade.set_alpha(alpha)
            self.win.blit(self.fade, (0, 0))
            self.fade.blit(winbg, (0, 0))
            self.fade.blit(wintab, (1250/2-150, 700/2-100))
            self.fade.blit(winimg, (1250/2-150, 700/2-150))
            pygame.display.update()
            pygame.time.delay(5)
##        self.event_check()
##
##    def event_check(self):
##        run = True
##        while run:
##            for event in pygame.event.get():
##                if event.type == pygame.MOUSEBUTTONUP:
##                    if self.playPauseButton.click(pos[0], pos[1]):
##                        self.pause = not self.pause
##                        self.playPauseButton.change_img()
##                        self.playPauseButton.draw(self.win)
##                        if not self.pause:
##                            game = Game(self.win)
##                            game.wave = 0
##                            game.current_wave = [20, 0, 0][:]
##                            game.__run__()

    def run(self):
        if not self.faded and self.wave == 16:
            self.fadeoff()

