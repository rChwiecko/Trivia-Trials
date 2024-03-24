import pygame
from Board import * #this import wont work for you Sahej, so you can comment it out for now
pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Trivia Trials")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    BoardInstance = Board(['test','player2','player3'], screen, 1, 0) #you can comment this out aswell
    if BoardInstance.gameStatus:
        Board.render(BoardInstance) #comment this out aswell
    
    #Add your render method and anything necessary to show your main menu here, 
    #try to limit it to just making a main menu instance and calling your render method
    #so youll probably have to add 2 lines below this comment

    #*** here ***#



    screen


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()