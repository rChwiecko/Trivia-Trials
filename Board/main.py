import pygame
from Board import * 
pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Trivia Trials")
running = True
boardInstance = Board(['player1'],screen, 1, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # You could check for a keyboard event here and move the ducks when a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Let's say SPACE key will move the ducks
                boardInstance.movePlayers()  # This method could move the player based on the game logic

    # Render the board and the players in their current positions
    boardInstance.render()

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

