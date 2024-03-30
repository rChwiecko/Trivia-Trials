import pygame, pygame_gui
from Board import * 
#basic pygame properties
def game(new_game, game_data = None, player_list = None):
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Trivia Trials")
    running = True
    #preliminaries for main loop
    players = ['player1','ryan','sonia']
    boardInstance = Board(players, screen, "1", 0)
    gameState = "INITIAL"  # Corrected state name
    playersAsked = 0
    beginning = pygame.time.get_ticks()
    delay_start_time = None
    paused = None
    dataSaved = None
    pauseState = None
    #main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Use "P" key to toggle pause
                    if gameState != "PAUSED":
                        pauseState = gameState  # Save the current state
                        gameState = "PAUSED"  # Change to paused state
                    else:
                        gameState = pauseState  # Restore the previous state
                        pauseState = None  # Clear the saved state
                elif event.key == pygame.K_ESCAPE and gameState != "PAUSED":
                    pauseState = gameState
                    gameState = "PAUSE"
                    paused = True
                elif event.key == pygame.K_ESCAPE and gameState == "PAUSED":
                    gameState = pauseState
                    pausedState = None
                    paused = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 1280/2-100 <= mouse_pos[0] <=1280/2+100 and 250 <= mouse_pos[1] <= 300:  # Check if mouse click is on "Resume" button
                    gameState = pauseState
                    paused = False
                elif 350 <= mouse_pos[1] <= 400:  # Check if mouse click is on "Save and Quit" button
                    dataSaved = True
                elif 450 <= mouse_pos[1] <= 500:  # Check if mouse click is on "Don't Save and Quit" button
                    running = False
                elif 10 <= mouse_pos[0] <= 50 and 10 <= mouse_pos[1] <= 50:
                    gameState = "PAUSED"
                    paused = True
        boardInstance.render()
        if gameState == "QUESTION_SHOW":
            if playersAsked < boardInstance.playerCount:
                boardInstance.drawQuestion(players[playersAsked], 1, 2, 0, True)
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
            if time_taken <= 30000:
                boardInstance.drawQuestion(players[playersAsked], 1, 2, time_taken / 1000, False)
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
        elif gameState == "PAUSED":
            boardInstance.pause(paused, dataSaved)

        #All delay states
        elif gameState == "MOVE_PLAYER_DELAY":
            boardInstance.render()
            current_time = pygame.time.get_ticks()
            if (current_time - delay_start_time) >= 3000:
                # Delay period is over, switch to the next desired state
                gameState = "MOVE_PLAYERS"
        elif gameState == "SHOW_QUESTION_DELAY":
            current_time = pygame.time.get_ticks()
            if (current_time - delay_start_time) >= 2000:
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


