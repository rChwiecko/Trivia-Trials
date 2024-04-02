'''
Description: This class is responsible for rendering the game board, providing methods that will ensure proper gameplay mechanics are delivered and also provides menus to save and exit games.  This class is branched into from the main.py file
Authors: Ryan, Sonia for pause and comments'''


import pygame # Import pygame modules
from questionGeneration import * # import question generation functions
import random
from const import * # Import constant values
import endOfBoardException # Import custom exception
from queryManager import * # Import query manager functions

pygame.init() # initialize the pygame module


class Board:
    """
    Represents the game board and handles rendering and game logic.

    Attributes:
        font (pygame.font.Font): Font for text rendering.
        playerCount (int): Number of players in the game.
        playerIndex (int): Index of the current player.
        playerList (list): List of player information.
        screen: Pygame window.
        curr_font (str): Current font used.
        levelNum (str): Current level number.
        curr_question (str): Current question being displayed.
        answer_correct (bool): Flag indicating if the answer is correct.
        duck_used (bool): Flag indicating if the duck item is used.
    """
    font = pygame.font.Font(None, 36) # font for text rendering
    playerCount = None # number of players in the game
    playerIndex = None # index of the current player
    playerList = None # list of player information
    screen = None # pygame window
    curr_font = pygame.font.get_default_font() # current font used
    levelNum = None # current level number
    curr_question = None # current question being displayed
    answer_correct = False # flag indicating if the answer is correct
    duck_used = False # flag indicating if the duck item is used

    # variables for graphics in the application
    duck = pygame.image.load("./assets/transparentduck.png")
    scaled_duck_end = pygame.transform.scale(duck, (100, 100))
    scaled_duck_player = pygame.transform.scale(duck, (50, 50))
    pause = pygame.image.load("./assets/pauseButton.png")
    scaled_pause = pygame.transform.scale(pause,(40,40))
    checkMark = pygame.image.load("./assets/checkmark.png")
    scaled_checkMark = pygame.transform.scale(checkMark, (150, 150))
    RedX = pygame.image.load("./assets/redX.png")
    scaled_RedX = pygame.transform.scale(RedX, (150, 150))
    streak = pygame.image.load("./assets/StreakIcon.png")
    scaled_streak = pygame.transform.scale(streak, (50, 50))

    #constructor
    def __init__(self, playerList, screen, level, playerIndex) -> None:
        """
        Initialize the Board object.

        Args:
            playerList (list): List of player information.
            screen: Pygame window.
            level (str): Current level number.
            playerIndex (int): Index of the current player.
        """
        self.playerCount = len(playerList) # Set the number of players in the game
        self.playerIndex = playerIndex # Set the index of the current player
        self.playerList = playerList # Set the list of player information
        self.screen = screen # Set the Pygame window
        self.levelNum = level # Set the current level number


    #draws board, win is the current window (screen)
    def drawBoard(self, win):
        """
        Draw the game board.

        Args:
            win: Pygame window.
        """
        win.fill("white")  # Fill the window with white color
        win.blit(self.scaled_pause, (10, 10))  # Draw the scaled pause button at (10, 10)
        rect_x = (WIDTH - 880) // 2  # Calculate the x-coordinate of the rectangle
        rect_y = (HEIGHT - 600) // 2  # Calculate the y-coordinate of the rectangle
        pygame.draw.rect(win, BLACK, (rect_x, rect_y, 880, 600))  # Draw the black rectangle for the board
        level = "Level " + str(self.levelNum)  # Format the level information
        self.drawText(level, self.curr_font, 30, BLACK, rect_x + 70, rect_y - 30)  # Draw the level information
        innerBoardWidth = 880 - (BOARD_OUTLINE_OFFSET * 2)  # Calculate the inner board width
        innerBoardHeight = 600 - (BOARD_OUTLINE_OFFSET * 2)  # Calculate the inner board height
        innerBoardStartX = rect_x + BOARD_OUTLINE_OFFSET  # Calculate the inner board starting x-coordinate
        innerBoardStartY = rect_y + BOARD_OUTLINE_OFFSET  # Calculate the inner board starting y-coordinate
        pygame.draw.rect(win, WHITE, (innerBoardStartX, innerBoardStartY, innerBoardWidth, innerBoardHeight))  # Draw the white inner board
        currSquareColor = None  # Initialize the current square color
        for row in range(NUMROWS):  # Iterate over the rows of the board
            for col in range(NUMCOLS):  # Iterate over the columns of the board
                if row == 0:  # Check if it's the first row
                    currSquareColor = REDSQUARE  # Set the current square color to red
                elif row == 1:  # Check if it's the second row
                    currSquareColor = PURPLESQUARE  # Set the current square color to purple
                else:  # For other rows
                    currSquareColor = BLUESQUARE  # Set the current square color to blue
                player_row = self.playerIndex // NUMCOLS  # Calculate the row of the current player
                player_col = self.playerIndex % NUMCOLS  # Calculate the column of the current player
                squareXCoord = innerBoardStartX + 20 + (col * (150 + 20.5))  # Calculate the x-coordinate of the current square
                squareYCoord = innerBoardStartY + 41 + (row * (150 + 30))  # Calculate the y-coordinate of the current square
                pygame.draw.rect(win, BLACK, (squareXCoord, squareYCoord, 150, 150))  # Draw the black square
                pygame.draw.rect(win, currSquareColor, (squareXCoord + BOARD_OUTLINE_OFFSET, squareYCoord + BOARD_OUTLINE_OFFSET, 150 - (2 * BOARD_OUTLINE_OFFSET), 150 - (2 * BOARD_OUTLINE_OFFSET)))  # Draw the colored square inside the black square
                if (row == player_row and col == player_col):  # Check if the current square is the player's position
                    self.renderPlayers(squareXCoord, squareYCoord)  # Render the players on the board
                if row == 0 and col == 0:  # Check if it's the start square
                    self.drawText("Start", self.curr_font, 25, BLACK, squareXCoord + 40, squareYCoord + 120)  # Draw "Start" text on the start square
                if row == 2 and col == 4:  # Check if it's the end square
                    self.drawText("End", self.curr_font, 25, BLACK, squareXCoord + 40, squareYCoord + 120)  # Draw "End" text on the end square
                    self.screen.blit(self.scaled_duck_end, (squareXCoord + 200, squareYCoord + 20))  # Display the scaled duck image at the end square

    #runs draw method
    def render(self):
        """Render the game board."""
        self.drawBoard(self.screen) # Draw the game board on the screen

    #renders pause menu
    def pause(self, paused, dataSaved):
        """
        Render the pause menu.

        Args:
            paused (bool): Flag indicating if the game is paused.
            dataSaved (bool): Flag indicating if the game data is saved.
        """
        pygame.draw.rect(self.screen, WHITE, (0,0, 1280, 800))
        duck_image = pygame.image.load("./assets/transparentduck.png")  # Load the image of the duck from file
        duck_image = pygame.transform.scale(duck_image, (100, 100))  # Scale the duck image to the desired size
        duck_rect = duck_image.get_rect()  # Get the rectangular area that bounds the duck image
        self.screen.blit(duck_image, (WIDTH // 2 - duck_rect.width // 2, 100))  # Draw the duck image on the screen
        title_font = pygame.font.SysFont(None, 40)  # Set the font and size for the title text
        self.drawText("Pause Game", self.curr_font, 40, BLACK, (1280/2)-120, 50)  # Draw the title text on the screen
        self.draw_button("Resume", 1280/2-100, 250)  # Draw the "Resume" button
        self.draw_button("Save and Quit", 1280/2-100, 350)  # Draw the "Save and Quit" button
        self.draw_button("          Quit", 1280/2-100, 450)  # Draw the "Don't Save and Quit" button
    
    def drawText(self, text, fontname, fontsize, text_col, x, y):
        """
        Draw text on the screen.

        Args:
            text (str): Text to be drawn.
            fontname: Font name.
            fontsize (int): Font size.
            text_col: Text color.
            x (int): X-coordinate of the text.
            y (int): Y-coordinate of the text.
        """

        font = pygame.font.Font(fontname, fontsize)  # Create a font object with the specified name and size
        text_surface = font.render(text, True, text_col)  # Create a surface with the specified text, antialiasing, and color
        self.screen.blit(text_surface, ((x, y)))  # Draw the text surface on the screen at the specified coordinates

    #prints players on the screen
    def renderPlayers(self, firstSquareX, firstSquareY):
        """
        Render players on the screen.

        Args:
            firstSquareX (int): X-coordinate of the first square.
            firstSquareY (int): Y-coordinate of the first square.
        """

        for i in range(self.playerCount):  # Iterate over the players
            if (i == 0):  # Check if it's the first player
                self.screen.blit(self.scaled_duck_player, (10 + firstSquareX, firstSquareY + 50))  # Draw the scaled duck image for the first player
            else:  # For other players
                self.screen.blit(self.scaled_duck_player, (10 + firstSquareX + PLAYERDIST * i, firstSquareY + 50))  # Draw the scaled duck image for other players at the appropriate position
    
    # Moves players       
    def movePlayers(self):
        """
        Move players on the board.
        """
        if self.playerIndex < 14:  # Check if the player index is within the board range
            self.playerIndex += 1  # Move the player forward
        else:  # If the player reaches the end of the board
            raise endOfBoardException.endOfBoardException("End of board")  # Raise an exception indicating the end of the board

        
    #renders question
    def drawQuestion(self, playersQuestion, level, square_col, time_elapsed, gen_new_question, player_answer):
        """
        Draw the question screen.

        Args:
            playersQuestion (dict): Dictionary containing player information.
            level (str): Current level number.
            square_col: Square color.
            time_elapsed: Time elapsed.
            gen_new_question (bool): Flag indicating whether to generate a new question.
            player_answer: Player's answer.

        Returns:
            str: Current question being displayed.
        """

        pygame.draw.rect(self.screen, WHITE, (0, 0, 1280, 800))  # Draw a white rectangle covering the entire screen
        rect_x = (WIDTH - 880) // 2  # Calculate the x-coordinate of the rectangle
        rect_y = (HEIGHT - 600) // 2  # Calculate the y-coordinate of the rectangle
        pygame.draw.rect(self.screen, BLACK, (rect_x, rect_y, 880, 600))  # Draw the black rectangle for the question screen
        innerBoardWidth = 880 - (BOARD_OUTLINE_OFFSET * 2)  # Calculate the inner board width
        innerBoardHeight = 600 - (BOARD_OUTLINE_OFFSET * 2)  # Calculate the inner board height
        innerBoardStartX = rect_x + BOARD_OUTLINE_OFFSET  # Calculate the inner board starting x-coordinate
        innerBoardStartY = rect_y + BOARD_OUTLINE_OFFSET  # Calculate the inner board starting y-coordinate
        pygame.draw.rect(self.screen, WHITE, (innerBoardStartX, innerBoardStartY, innerBoardWidth, innerBoardHeight))  # Draw the white inner board
        self.drawText(str(playersQuestion["name"] + "'s Question"), self.curr_font, 50, BLACK, rect_x * 2, rect_y + 40)  # Draw the player's name and "Question" text
        self.screen.blit(self.scaled_duck_end, (rect_x * 2 + 550, rect_y + 30))  # Display the scaled duck image
        pygame.draw.rect(self.screen, BLACK, (rect_x + 200, rect_y + 400, 480, 90))  # Draw the black rectangle for the progress bar
        pygame.draw.rect(self.screen, WHITE, (rect_x + 200 + BOARD_OUTLINE_OFFSET, rect_y + 400 + BOARD_OUTLINE_OFFSET, 480 - (BOARD_OUTLINE_OFFSET * 2), 90 - (BOARD_OUTLINE_OFFSET * 2)))  # Draw the white inner rectangle for the progress bar
        pygame.draw.rect(self.screen, GREEN, (rect_x + 200 + BOARD_OUTLINE_OFFSET, rect_y + 400 + BOARD_OUTLINE_OFFSET, 16 * time_elapsed, 90 - (BOARD_OUTLINE_OFFSET * 2)))  # Draw the green progress bar based on the time elapsed
        pygame.draw.rect(self.screen, BLACK, (innerBoardStartX + 100, innerBoardStartY + 285, 290, 50))  # Draw the black rectangle for the player's answer
        pygame.draw.rect(self.screen, WHITE, (innerBoardStartX + 100 + BOARD_OUTLINE_OFFSET, innerBoardStartY + 285 + BOARD_OUTLINE_OFFSET, 290 - (BOARD_OUTLINE_OFFSET * 2), 50 - (BOARD_OUTLINE_OFFSET * 2)))  # Draw the white inner rectangle for the player's answer
        self.drawText(player_answer, self.curr_font, 40, BLACK, innerBoardStartX + 103, innerBoardStartY + 289)  # Draw the player's answer
        if (gen_new_question):  # Check if a new question needs to be generated
            player_row = self.playerIndex // NUMCOLS  # Calculate the row of the current player
            que_type = random.randint(1, 2)  # Generate a random question type
            if(player_row == 0):  # Check if the player is in the first row
                if que_type == 1:  # Check if the question type is addition
                    self.curr_question = addition(self.levelNum).generateQuestion()  # Generate an addition question
                else:  # If the question type is not addition
                    self.curr_question = subtraction(self.levelNum).generateQuestion()  # Generate a subtraction question
            elif(player_row == 1):  # Check if the player is in the second row
                if que_type == 1:  # Check if the question type is multiplication
                    self.curr_question = multiplication(self.levelNum).generateQuestion()  # Generate a multiplication question
                else:  # If the question type is not multiplication
                    self.curr_question = division(self.levelNum).generateQuestion()  # Generate a division question
            else:  # For other rows
                if que_type == 2:  # Check if the question type is quadratic
                    self.curr_question = quadratic(self.levelNum).generateQuestion()  # Generate a quadratic question
                else:  # If the question type is not quadratic
                    self.curr_question = linear(self.levelNum).generateQuestion()  # Generate a linear question
        self.drawText(self.curr_question[0], self.curr_font, 30, BLACK, innerBoardStartX + 100, innerBoardStartY + 175)  # Draw the first part of the current question
        self.drawText(self.curr_question[1], self.curr_font, 30, BLACK, innerBoardStartX + 100, innerBoardStartY + 205)  # Draw the second part of the current question
        self.drawText(self.curr_question[2], self.curr_font, 30, BLACK, innerBoardStartX + 100, innerBoardStartY + 235)  # Draw the third part of the current question
        return self.curr_question  # Return the current question

    
    #gives a countdown for which players turn it is
    def showPlayersTurn(self, name, time):
        """
        Display the current player's turn.

        Args:
            name (str): Player's name.
            time: Time remaining for the turn.
        """
        rect_x = (WIDTH - 880) // 2  # Calculate the x-coordinate of the rectangle
        rect_y = (HEIGHT - 600) // 2  # Calculate the y-coordinate of the rectangle
        pygame.draw.rect(self.screen, WHITE, (rect_x + BOARD_OUTLINE_OFFSET, rect_y + BOARD_OUTLINE_OFFSET, 880 - (BOARD_OUTLINE_OFFSET * 2), 600 - (BOARD_OUTLINE_OFFSET * 2)))  # Draw the white inner board
        self.drawText(str(name["name"] + "'s turn"), self.curr_font, 50, BLACK, rect_x * 2 + 50, rect_y + 70)  # Draw the player's name and "turn" text
        self.drawText(str(time), self.curr_font, 50, BLACK, rect_x + 400, rect_y + 250)  # Draw the time remaining
    
    #renders a button
    def draw_button(self, text, x, y):  # Define a function to draw a button on the screen
        """
        Draw a button on the screen.

        Args:
            text (str): Text to be displayed on the button.
            x (int): X-coordinate of the button.
            y (int): Y-coordinate of the button.
        """

        pygame.draw.rect(self.screen, BLACK, (x, y, 200, 40))  # Draw the button rectangle
        if y == 250:  # Adjust text position based on button position
            self.drawText(text, self.curr_font, 25, WHITE, x + 60, y + 20)  # Draw the button text
        elif y == 350:
            self.drawText(text, self.curr_font, 25, WHITE, x + 25, y + 20)  # Draw the button text
        else: 
            self.drawText(text, self.curr_font, 25, WHITE, x + 5, y + 22)  # Draw the button text

    def answer_check(self, answer, question, player, duck_used):
        """
        Check the player's answer.

        Args:
            answer: Player's answer.
            question: Question asked.
            player: Player information.
            duck_used (bool): Flag indicating whether the duck item is used.
        """
        if duck_used:  # Check if the duck item is used
            player["score"] += self.update_points(player)  # Increase player's score
            player["streak"] += 1  # Increase player's streak
            self.duck_used = True  # Set duck_used flag to True
            player['duck_count'] = player['duck_count'] - 1  # Decrement duck count
        else:  # If duck item is not used
            self.duck_used = False  # Set duck_used flag to False
            if isinstance(question[-1], int):  # Check if the answer is an integer
                try:
                    answer = int(answer)  # Convert answer to integer
                    if (answer == question[-1]):  # Check if the answer is correct
                        player["score"] += self.update_points(player)  # Increase player's score
                        player["streak"] += 1  # Increase player's streak
                        self.answer_correct = True  # Set answer_correct flag to True
                    else:  # If the answer is incorrect
                        player["streak"] = 0  # Reset player's streak
                        self.answer_correct = False  # Set answer_correct flag to False
                except:  # If answer cannot be converted to integer
                    player["streak"] = 0  # Reset player's streak
                    self.answer_correct = False  # Set answer_correct flag to False
            elif isinstance(question[-1], float):  # Check if the answer is an integer
                try:
                    answer = float(answer)  # Convert answer to integer
                    if (answer == question[-1]):  # Check if the answer is correct
                        player["score"] += self.update_points(player)  # Increase player's score
                        player["streak"] += 1  # Increase player's streak
                        self.answer_correct = True  # Set answer_correct flag to True
                    else:  # If the answer is incorrect
                        player["streak"] = 0  # Reset player's streak
                        self.answer_correct = False  # Set answer_correct flag to False
                except:  # If answer cannot be converted to integer
                    player["streak"] = 0  # Reset player's streak
                    self.answer_correct = False  # Set answer_correct flag to False
            elif isinstance(question[-1], list):  # Check if the answer is a list
                try:
                    answer = answer.split(',')  # Split the answer by comma
                    answer = answer.replace(' ', ' ')  # Replace spaces in the answer
                    if (answer[0] in question[-1] and answer[1] in question[-1]):  # Check if both answers are correct
                        player["score"] += self.update_points(player)  # Increase player's score
                        player["streak"] += 1  # Increase player's streak
                        self.answer_correct = True  # Set answer_correct flag to True
                    else:  # If the answers are incorrect
                        player["streak"] = 0  # Reset player's streak
                        self.answer_correct = False  # Set answer_correct flag to False
                except:  # If an error occurs
                    player["streak"] = 0  # Reset player's streak
                    self.answer_correct = False  # Set answer_correct flag to False
            else:  # If the answer is not an integer or a list
                try:
                    answer = answer.replace(' ', '')  # Remove spaces from the answer
                    question_real = question[-1].replace(' ', '')  # Remove spaces from the real question
                    if (answer == question_real):  # Check if the answer is correct
                        player["score"] += self.update_points(player)  # Increase player's score
                        player["streak"] += 1  # Increase player's streak
                        self.answer_correct = True  # Set answer_correct flag to True
                    else:  # If the answer is incorrect
                        player['streak'] = 0  # Reset player's streak
                        self.answer_correct = False  # Set answer_correct flag to False
                except:  # If an error occurs
                    player['streak'] = 0  # Reset player's streak
                    self.answer_correct = False  # Set answer_correct flag to False


    def show_answer_feedback(self, answer_recieved, question):
        """
        Display feedback on the answer.

        Args:
            answer_recieved: Answer received from the player.
            question: Question asked.
        """
        rect_x = (WIDTH - 880) // 2  # Calculate the x-coordinate of the rectangle
        rect_y = (HEIGHT - 600) // 2  # Calculate the y-coordinate of the rectangle
        pygame.draw.rect(self.screen, WHITE, (0, 0, 1280, 800))  # Draw a white rectangle covering the entire screen
        if not self.duck_used:  # Check if the duck item is not used
            self.drawText("Feedback On Answer", self.curr_font, 50, BLACK, rect_x*2, rect_y+70)  # Draw feedback header
            self.drawText("Your Answer:    "+str(answer_recieved), self.curr_font, 40, BLACK, rect_x+100, rect_y+250)  # Draw player's answer
            self.drawText("Correct Answer:    "+str(self.curr_question[-1]), self.curr_font, 40, BLACK, rect_x+100, rect_y+290)  # Draw correct answer
            if self.answer_correct:  # Check if the answer is correct
                self.screen.blit(self.scaled_checkMark, (rect_x+410, rect_y + 380))  # Display checkmark
            else:  # If the answer is incorrect
                self.screen.blit(self.scaled_RedX, (rect_x+310, rect_y + 420))  # Display red cross
        else:  # If the duck item is used
            self.drawText("Duck Used!", self.curr_font, 50, BLACK, rect_x*2, rect_y+150)  # Display "Duck Used!" message
            self.screen.blit(self.scaled_checkMark, (rect_x*2+300, rect_y+150))  # Display checkmark


    def update_points(self, player):
        """
        Update player's points.

        Args:
            player: Player information.
        Returns:
            float: Updated score.
        """
        multiplier = 1.1  # Define multiplier for streak
        row_1_base = 50  # Base points for first row
        row_2_base = 75  # Base points for second row
        row_3_base = 100  # Base points for third row
        player_row = self.playerIndex // NUMCOLS  # Calculate the row of the player
        if player_row == 0:
            base_points = row_1_base  # Set base points for first row
        elif player_row == 1:
            base_points = row_2_base  # Set base points for second row
        else:
            base_points = row_3_base  # Set base points for third row
        
        base_points = base_points*(2**(int(self.levelNum)))  # Adjust base points based on level number
        score = base_points * (multiplier**player["streak"])  # Calculate score based on streak
        return score
    
    def show_player_scores(self):
        """Display player scores."""

        rect_x = (WIDTH - 880) // 2  # Calculate the x-coordinate of the rectangle
        rect_y = (HEIGHT - 600) // 2  # Calculate the y-coordinate of the rectangle
        pygame.draw.rect(self.screen, WHITE, (0, 0, 1280, 800))  # Draw a white rectangle covering the entire screen
        pygame.draw.rect(self.screen, BLACK, (rect_x, rect_y, 880, 600))  # Draw a black rectangle for the scoreboard
        pygame.draw.rect(self.screen, WHITE, (rect_x+BOARD_OUTLINE_OFFSET, rect_y+BOARD_OUTLINE_OFFSET, 880-(2*BOARD_OUTLINE_OFFSET), 600-(2*BOARD_OUTLINE_OFFSET)))  # Draw a white rectangle inside the black rectangle
        self.drawText("Scores", self.curr_font, 50, BLACK, rect_x*2+200, rect_y+70)  # Draw "Scores" header
        player_score_max = -1  # Initialize maximum player score
        winning_player_name = ''  # Initialize winning player name
        if self.playerIndex == 14:  # Check if all players have answered
            for i in range(self.playerCount):  # Iterate through players
                if player_score_max < self.playerList[i]['score']:  # Find the player with the highest score
                    player_score_max = self.playerList[i]['score']  # Update maximum player score
                    winning_player_name = self.playerList[i]['name']  # Update winning player name
        for i in range(self.playerCount):  # Iterate through players
            self.drawText(self.playerList[i]["name"]+":   "+str(round(self.playerList[i]["score"],2)), self.curr_font, 35, BLACK, rect_x+100, rect_y+250+(80*i))  # Display player name and score
            if (self.playerList[i]["streak"] > 0):  # Check if player has a streak
                self.screen.blit(self.scaled_streak, (rect_x + 400, rect_y+244+(80*i)))  # Display streak icon
                self.drawText(str(self.playerList[i]["streak"]), self.curr_font, 35, BLACK, rect_x + 445, rect_y+250+(80*i))  # Display streak count
                if self.playerIndex == 14 and self.playerList[i]["name"] == winning_player_name:  # Check if the player is the winner
                    self.screen.blit(self.scaled_duck_player, (rect_x + 500, rect_y+244+(80*i)))  # Display duck icon for the winner
                    self.drawText('+1', self.curr_font, 35, BLACK, rect_x + 510, rect_y+250+(80*i))  # Display duck count for the winner
                    self.playerList[i]["duck_count"] += 1  # Increment duck count for the winner


    def save_game(self, playerlist, id_override = None):
        """
        Save the game.

        Args:
            playerlist: List of players.
            id_override: ID for overriding the default save slot.
        """
        if id_override == None:  # Check if no override ID is provided
            rect_x = (WIDTH - 880) // 2  # Calculate the x-coordinate of the rectangle
            rect_y = (HEIGHT - 600) // 2  # Calculate the y-coordinate of the rectangle
            pygame.draw.rect(self.screen, WHITE, (0, 0, 1280, 800))  # Draw a white rectangle covering the entire screen
            pygame.draw.rect(self.screen, BLACK, (rect_x, rect_y, 880, 600))  # Draw a black rectangle for the save slot options
            pygame.draw.rect(self.screen, WHITE, (rect_x+BOARD_OUTLINE_OFFSET, rect_y+BOARD_OUTLINE_OFFSET, 880-(2*BOARD_OUTLINE_OFFSET), 600-(2*BOARD_OUTLINE_OFFSET)))  # Draw a white rectangle inside the black rectangle
            self.drawText("Choose save slot", self.curr_font, 50, BLACK, rect_x*2+60, rect_y+70)  # Draw "Choose save slot" header
            self.draw_button_new("Save1", (rect_x+340, rect_y + 200))  # Draw button for save slot 1
            self.draw_button_new("Save2", (rect_x+340, rect_y + 300))  # Draw button for save slot 2
            self.draw_button_new("Save3", (rect_x+340, rect_y + 400))  # Draw button for save slot 3
        else:  # If override ID is provided
            players = []  # Initialize list for player data
            for i in range(self.playerCount):  # Iterate through players
                players.append({  # Append player data to the list
                    "name":self.playerList[i]["name"],
                    "password":self.playerList[i]["password"],
                    "streak":self.playerList[i]["streak"],
                    "duck_count":self.playerList[i]["duck_count"],
                    "score":self.playerList[i]["score"]
                })
            data = {  # Create data object for saving the game
                "game_id":id_override,
                "level_number": self.levelNum,
                "player_index": self.playerIndex,
                "players":players
            }
            insert_game(data)  # Call function to insert the game data into storage

            
    def draw_button_new(self, text, pos, width=240, height = 60):
        """
        Draw a new style button on the screen.

        Args:
            text (str): Text to be displayed on the button.
            pos (tuple): Position (x, y) of the button.
            width (int): Width of the button.
            height (int): Height of the button.
        """
        font = pygame.font.Font(self.curr_font, 24)  # Set font for the button text
        button = pygame.Rect(pos, (width, height))  # Create rectangle for the button
        pygame.draw.rect(self.screen, 'light gray', button, 0, 5)  # Draw light gray rectangle for the button
        pygame.draw.rect(self.screen, 'dark gray', button, 5, 5)  # Draw dark gray border for the button
        text2 = font.render(text, True, 'black')  # Render the button text
        text_rect = text2.get_rect(center=button.center)  # Get the rectangle for the text
        self.screen.blit(text2, text_rect.topleft)  # Draw the text on the button

              
              
