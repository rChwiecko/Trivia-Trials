# import pygame
# from Board import * 
# pygame.init()
# screen = pygame.display.set_mode((1280, 800))
# clock = pygame.time.Clock()
# pygame.display.set_caption("Trivia Trials")
# running = True
# boardInstance = Board(['player1','ryan','sonia'],screen, 1, 0)
# gameState = "QUESTION_SHOWN"
# playersAsked = 0
# lastAction = pygame.time.get_ticks()
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     boardInstance.render()
#     if gameState == "QUESTION_SHOWN":
#         boardInstance.drawQuestion("Ryan",1,2,0)
#         time_started = pygame.time.get_ticks()
#         gameState = "ANSWER_AWAIT"
#     elif gameState == "ANSWER_AWAIT":
#         time_taken = pygame.time.get_ticks()
#         if time_taken/1000 < 10:
#             boardInstance.drawQuestion("Ryan",1,2,time_taken/1000)
#         else:
#             playersAsked += 1
#             if playersAsked < boardInstance.playerCount:
#                 gameState = "QUESTION_SHOWN"
#             else:
#                 gameState = "MOVE_PLAYERS"
#                 playersAsked = 0
#     pygame.display.flip()
#     clock.tick(60)  # limits FPS to 60
# pygame.quit()     
#imports   
import pygame
from Board import * 
#basic pygame properties
pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Trivia Trials")
running = True
#preliminaries for main loop
boardInstance = Board(['player1','ryan','sonia'], screen, 1, 0)
gameState = "QUESTION_SHOW"  # Corrected state name
playersAsked = 0
lastAction = pygame.time.get_ticks()
delay_start_time = None
#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    boardInstance.render()

    if gameState == "QUESTION_SHOW":
        if playersAsked < boardInstance.playerCount:
            boardInstance.drawQuestion("Ryan", 1, 2, 0)
            lastAction = pygame.time.get_ticks()  # Set last action time to now
            gameState = "ANSWER_AWAIT"
        else:
            delay_start_time = pygame.time.get_ticks()
            gameState = "MOVE_PLAYER_DELAY"  # Example of moving to the next state

    elif gameState == "ANSWER_AWAIT":
        time_taken = (pygame.time.get_ticks() - lastAction)  # Corrected time difference calculation
        if time_taken < 3000:  # 30 seconds in milliseconds
            boardInstance.drawQuestion("Ryan", 1, 2, time_taken / 1000)
        else:
            playersAsked += 1  # Move to the next player
            gameState = "QUESTION_SHOW"  # Reset to show the next question

    elif gameState == "MOVE_PLAYERS":
        boardInstance.movePlayers()
        # Ensure the gameState is set to the correct value to restart the question cycle
        gameState = "QUESTION_SHOW"  # Reset to this state to start questions again
        playersAsked = 0  # Resetting the playersAsked counter if needed
    if gameState == "MOVE_PLAYER_DELAY":
        current_time = pygame.time.get_ticks()
        if (current_time - delay_start_time) >= 3000:
            # Delay period is over, switch to the next desired state
            gameState = "MOVE_PLAYERS"
    pygame.display.flip()
    clock.tick(60)  # Limits FPS to 60
pygame.quit()
