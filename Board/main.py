# import required module

# Author : Ryan and Sonia; Sonia contributed on the pause screen UI and button reactions 
import pygame, pygame_gui
from Board import * 
import json
from const import * 

""" The file provides the main game functionality for the Trivia Trials game """

#basic pygame properties
def game(new_game, game_data = None, player_list = None):
    """
    Run the main game loop.

    Args:
        new_game (bool): Indicates whether it's a new game or a saved game.
        game_data (dict): Dictionary containing saved game data.
        player_list (list): List of player data.

    Returns:
        None
    """

    pygame.init() # initialize Pygame

    # set up the Pygame screen
    screen = pygame.display.set_mode((1280, 800))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Trivia Trials")

    # initialize game variables
    running = True
    player_answering = False
    player_answer = ''
    player_answer_recorded = ''
    save_choosen = False
    game_save_choice = None
    #preliminaries for main loop
    # players = ['player1','ryan','sonia']
    # boardInstance = Board(players, screen, "1", 0)

    # Initialize game state and variables related to game state
    if not new_game:
        game_data_dict = game_data
        players = game_data_dict["players"]
        level_num = game_data_dict["level_number"]
        player_index = game_data_dict["player_index"]
        boardInstance = Board(players, screen, str(level_num), player_index)
    
    else:
        players = player_list
        boardInstance = Board(players, screen, '1', 0)

    gameState = "INITIAL"  # Corrected state name
    playersAsked = 0
    beginning = pygame.time.get_ticks()
    delay_start_time = None
    paused = False
    dataSaved = None
    pauseState = None
    question = ''

    # Main game loop
    while running:
        for event in pygame.event.get():   # Loop through all Pygame events
            if event.type == pygame.QUIT:  # Check if the user wants to quit the game
                running = False            # Set the running flag to False to exit the loop

            # Handle keyboard events
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:  # Check if the user pressed the ESC key
                    if gameState != "PAUSED":     # If the game is not paused
                        pauseState = gameState   # Store the current game state
                        gameState = "PAUSED"     # Change the game state to paused
                        paused = True            # Set the paused flag to True
                    else:
                        gameState = pauseState  # Restore the game state before pausing
                        pausedState = None      # Reset the paused state
                        paused = False          # Set the paused flag to False
                elif player_answering:           # If a player is answering a question
                    if event.key == pygame.K_BACKSPACE:  # Check if the backspace key is pressed
                        player_answer = player_answer[0:-1]  # Remove the last character from the answer
                    elif event.key == pygame.K_RETURN and player_answer != "":  # Check if the return key is pressed and an answer is given
                        boardInstance.answer_check(player_answer, question, players[playersAsked], False)  # Check the answer
                        player_answering = False   # Set the player_answering flag to False
                        player_answer_recorded = player_answer  # Record the player's answer
                        player_answer = ''          # Reset the player's answer
                    else:
                        player_answer += event.unicode  # Add the typed character to the answer

            # Handle mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check if a mouse button is pressed
                mouse_pos = pygame.mouse.get_pos()     # Get the mouse position
                if 1280/2-100 <= mouse_pos[0] <=1280/2+100 and 250 <= mouse_pos[1] <= 300 and gameState == "PAUSED":  # Check if mouse click is on "Resume" button
                    gameState = pauseState            # Resume the game
                    paused = False                    # Set the paused flag to False
                elif 350 <= mouse_pos[1] <= 400 and gameState == "PAUSED":  # Check if mouse click is on "Save and Quit" button
                    dataSaved = True                  # Set dataSaved flag to True
                    gameState = "CHOOSE_SAVE"        # Transition to choose save state
                elif 450 <= mouse_pos[1] <= 500 and gameState == "PAUSED":  # Check if mouse click is on "Don't Save and Quit" button
                    dataSaved = False                 # Set dataSaved flag to False
                    running = False                   # Terminate the game loop
                elif 10 <= mouse_pos[0] <= 50 and 10 <= mouse_pos[1] <= 50:  # Check if mouse click is on pause button
                    if (gameState != "PAUSED"):       # If the game is not paused
                        pauseState = gameState       # Store the current game state
                        gameState = "PAUSED"         # Change the game state to paused
                        paused = True                # Set the paused flag to True
                        rect_x = (WIDTH - 880) // 2   # Calculate the x-coordinate of the rectangle
                        rect_y = (HEIGHT - 600) // 2  # Calculate the y-coordinate of the

          # Handle mouse clicks for save choice
                elif gameState == "AWAIT_SAVE_CHOICE" and (WIDTH - 880) // 2 + 340 <= mouse_pos[0] <= (WIDTH - 880) // 2 + 580 and (HEIGHT - 600) // 2 + 200 <= mouse_pos[1] <= (HEIGHT - 600) // 2 + 260:  # Check if mouse click is on save slot 1
                    save_choosen = True                # Set save_choosen flag to True
                    game_save_choice = 1              # Set the chosen save slot
                elif gameState == "AWAIT_SAVE_CHOICE" and (WIDTH - 880) // 2 + 340 <= mouse_pos[0] <= (WIDTH - 880) // 2 + 580 and (HEIGHT - 600) // 2 + 300 <= mouse_pos[1] <= (HEIGHT - 600) // 2 + 360:  # Check if mouse click is on save slot 2
                    save_choosen = True                # Set save_choosen flag to True
                    game_save_choice = 2              # Set the chosen save slot
                elif gameState == "AWAIT_SAVE_CHOICE" and (WIDTH - 880) // 2 + 340 <= mouse_pos[0] <= (WIDTH - 880) // 2 + 580 and (HEIGHT - 600) // 2 + 400 <= mouse_pos[1] <= (HEIGHT - 600) // 2 + 460:  # Check if mouse click is on save slot 3
                    save_choosen = True                # Set save_choosen flag to True
                    game_save_choice = 3              # Set the chosen save slot
                elif gameState == "ANSWER_AWAIT" and players[playersAsked]["duck_count"] > 0 and (WIDTH - 880) // 2 * 2 + 550 <= mouse_pos[0] <= (WIDTH - 880) // 2 * 2 + 650 and (HEIGHT - 600) // 2 + 30 <= mouse_pos[1] <= (HEIGHT - 600) // 2 + 130:  # Check if mouse click is on use duck button
                        boardInstance.answer_check(player_answer, question, players[playersAsked], True)  # Check the answer using a duck
                        player_answering = False    # Set the player_answering flag to False
                        player_answer_recorded = player_answer  # Record the player's answer
                        player_answer = ''          # Reset the player's answer

        # Render the game board
        boardInstance.render()

        # Handle game state transitions and logic
        if gameState == "QUESTION_SHOW":
            # If it's time to show a question
            if playersAsked < boardInstance.playerCount:
                # If there are more players to ask
                question = boardInstance.drawQuestion(players[playersAsked], 1, 2, 0, True, player_answer)  # Draw the question
                lastAction = pygame.time.get_ticks()  # Record the time when the question was shown
                player_answering = True  # Set the player_answering flag to True
                gameState = "ANSWER_AWAIT"  # Transition to answer await state
            else:
                # If all players have been asked
                print("here")  # Print a message (should be replaced with appropriate action)
                gameState = "SHOW_RESULTS"  # Transition to show results state
        elif gameState == "INITIAL":
            # If it's the initial state
            boardInstance.render()  # Render the game board
            if beginning > 4000:
                # If more than 4 seconds have passed since the beginning
                gameState = "SHOW_PLAYER_TURN"  # Transition to show player turn state
            else:
                beginning = pygame.time.get_ticks()  # Record the time when the game started
        elif gameState == "SHOW_RESULTS":
            # If it's time to show results
            boardInstance.show_player_scores()  # Show player scores
            delay_start = pygame.time.get_ticks()  # Record the time when showing results started
            gameState = "SHOW_RESULTS_DELAY"  # Transition to show results delay state

        # Other game state transitions and logic are handled similarly...

        pygame.display.flip()  # Update the display
        clock.tick(60)         # Limit the frame rate to 60 FPS
