import pygame
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 800
FPS = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Trivia Trials')
main_menu = False
exit_menu = False
font_heading = pygame.font.Font('freesansbold.ttf', 36)
font = pygame.font.Font('freesansbold.ttf', 24)

# Load image
bg = pygame.transform.scale(pygame.image.load('assets/transparentduck.png'), (100, 100))
ball = pygame.transform.scale(pygame.image.load('assets/transparentduck.png'), (150, 150))
menu_command = 0

# Load logo image
logo = pygame.image.load('assets/transparentduck.png')  # Replace 'logo.png' with the path to your logo image
logo = pygame.transform.scale(logo, (100, 100))  # Scale the logo to an appropriate size