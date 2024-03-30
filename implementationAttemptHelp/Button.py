import constants
import pygame
import sys
from queryManager import *

# pygame.init()


# WIDTH = 1280
# HEIGHT = 800
# FPS = 60

# screen = pygame.display.set_mode([WIDTH, HEIGHT])
# font = pygame.font.Font('freesansbold.ttf', 24)


class Button:
    def __init__(self, txt, pos, width=260, height=40):
        self.text = txt
        self.pos = pos
        self.width = width
        self.height = height
        self.button = pygame.Rect(self.pos, (self.width, self.height))

    def draw(self):
        pygame.draw.rect(constants.screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(constants.screen, 'dark gray', self.button, 5, 5)
        text2 = constants.font.render(self.text, True, 'black')
        text_rect = text2.get_rect(center=self.button.center)
        constants.screen.blit(text2, text_rect.topleft)

    def check_clicked(self):
        return self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]