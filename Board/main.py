import pygame
from Board import * 
#basic pygame properties
pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Trivia Trials")
running = True
#preliminaries for main loop
players = ['player1','ryan','sonia']
boardInstance = Board(players, screen, 1, 0)
gameState = "INITIAL"  # Corrected state name
playersAsked = 0
beginning = pygame.time.get_ticks()
delay_start_time = None
#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if gameState == "QUESTION_SHOW":
        if playersAsked < boardInstance.playerCount:
            boardInstance.drawQuestion("Ryan", 1, 2, 0)
            lastAction = pygame.time.get_ticks()  # Set last action time to now
            gameState = "ANSWER_AWAIT"
        else:
            delay_start_time = pygame.time.get_ticks()
            gameState = "MOVE_PLAYER_DELAY"  # Example of moving to the next state
    elif gameState == "INITIAL":
        boardInstance.render()
        if beginning > 2000:
            gameState = "SHOW_PLAYER_TURN"
        else:
            beginning = pygame.time.get_ticks()
    elif gameState == "ANSWER_AWAIT":
        time_taken = (pygame.time.get_ticks() - lastAction)  # Corrected time difference calculation
        if time_taken < 3000:
            boardInstance.drawQuestion(players[playersAsked], 1, 2, time_taken / 1000)
        else:
            playersAsked += 1  # Move to the next player
            gameState = "SHOW_PLAYER_TURN"  # Reset to show the next question
    elif gameState == "MOVE_PLAYERS":
        boardInstance.movePlayers()
        boardInstance.render()
        playersAsked = 0  # Resetting the playersAsked counter if needed
        delay_start_time = pygame.time.get_ticks()
        gameState = "SHOW_QUESTION_DELAY"

    elif gameState == "SHOW_PLAYER_TURN":
        if playersAsked < boardInstance.playerCount:
            boardInstance.showPlayersTurn(players[playersAsked], 0)
            lastAction = pygame.time.get_ticks()
            gameState = "3_SECOND_COUNTDOWN"
        else: 
            delay_start_time = pygame.time.get_ticks()
            gameState = "MOVE_PLAYER_DELAY"

    #All delay states
    elif gameState == "MOVE_PLAYER_DELAY":
        boardInstance.render()
        current_time = pygame.time.get_ticks()
        if (current_time - delay_start_time) >= 3000:
            # Delay period is over, switch to the next desired state
            gameState = "MOVE_PLAYERS"
    elif gameState == "SHOW_QUESTION_DELAY":
        current_time = pygame.time.get_ticks()
        if (current_time - delay_start_time) >= 1000:
            # Delay period is over, switch to the next desired state
            gameState = "SHOW_PLAYER_TURN"

    elif gameState == "3_SECOND_COUNTDOWN":
        current_time = pygame.time.get_ticks()
        if (current_time - lastAction) < 5000:
            boardInstance.showPlayersTurn(players[playersAsked], 5 - (current_time - lastAction)//1000)

        else:
            gameState = "QUESTION_SHOW"

    pygame.display.flip()
    clock.tick(60)  # Limits FPS to 60
pygame.quit()