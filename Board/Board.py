import pygame
from questionGeneration import *
import random
from const import *
import endOfBoardException
pygame.init()
class Board:
    gameStatus = False
    time = None
    questionStatus = False
    font = pygame.font.Font(None, 36)
    playerCount = None
    playerIndex = None
    playerList = None
    screen = None
    curr_font = pygame.font.get_default_font()
    levelNum = None
    curr_question = None 
    answer_correct = False
    duck = pygame.image.load("./assets/transparentduck.png")
    scaled_duck_end = pygame.transform.scale(duck, (100, 100))
    scaled_duck_player = pygame.transform.scale(duck, (50, 50))
    pause = pygame.image.load("./assets/pauseButton.png")
    scaled_pause = pygame.transform.scale(pause,(40,40))
    checkMark = pygame.image.load("./assets/checkmark.png")
    scaled_checkMark = pygame.transform.scale(checkMark, (150, 150))
    RedX = pygame.image.load("./assets/redX.png")
    scaled_RedX = pygame.transform.scale(RedX, (150, 150))

    #constructor
    def __init__(self, playerList, screen, level, playerIndex, newGame = False) -> None:
        self.playerCount = len(playerList)
        self.newGame = newGame
        self.playerIndex = playerIndex
        self.playerList = playerList
        self.gameStatus = True
        self.screen = screen
        self.levelNum = level


    #draws board, win is the current window (screen)
    def drawBoard(self, win):
        win.fill("white")
        win.blit(self.scaled_pause, (10, 10))
        rect_x = (WIDTH - 880) // 2
        rect_y = (HEIGHT - 600) // 2
        pygame.draw.rect(win, BLACK, (rect_x, rect_y, 880, 600))
        level = "Level "+str(self.levelNum)
        self.drawText(level, self.curr_font, 30, BLACK, rect_x + 70, rect_y - 30)
        innerBoardWidth = 880-(BOARD_OUTLINE_OFFSET*2)
        innerBoardHeight = 600-(BOARD_OUTLINE_OFFSET*2)
        innerBoardStartX = rect_x+BOARD_OUTLINE_OFFSET
        innerBoardStartY = rect_y+BOARD_OUTLINE_OFFSET
        pygame.draw.rect(win, WHITE, (innerBoardStartX, innerBoardStartY, innerBoardWidth, innerBoardHeight))
        #draw inner squares
        currSquareColor = None
        for row in range(NUMROWS):
            for col in range(NUMCOLS):
                if row == 0:
                    currSquareColor = REDSQUARE
                elif row == 1:
                    currSquareColor = PURPLESQUARE
                else:
                    currSquareColor = BLUESQUARE
                player_row = self.playerIndex // NUMCOLS
                player_col = self.playerIndex % NUMCOLS    
                squareXCoord = innerBoardStartX+20+(col*(150+20.5))
                squareYCoord = innerBoardStartY+41+(row*(150+30))
                pygame.draw.rect(win, BLACK, (squareXCoord, squareYCoord, 150, 150))
                pygame.draw.rect(win, currSquareColor, (squareXCoord+BOARD_OUTLINE_OFFSET, squareYCoord+BOARD_OUTLINE_OFFSET, 150-(2*BOARD_OUTLINE_OFFSET), 150-(2*BOARD_OUTLINE_OFFSET)))
                if (row == player_row and col == player_col):
                    self.renderPlayers(squareXCoord,squareYCoord)
                if row == 0 and col == 0:
                    self.drawText("Start", self.curr_font, 25, BLACK, squareXCoord+40, squareYCoord+120)
                if row == 2 and col == 4:
                    self.drawText("End", self.curr_font, 25, BLACK, squareXCoord+40, squareYCoord+120)
                    self.screen.blit(self.scaled_duck_end, (squareXCoord+200, squareYCoord+20))

    #runs draw method
    def render(self):
        self.drawBoard(self.screen)

    #renders pause menu
    def pause(self, paused, dataSaved):
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
        if paused: 
            self.drawText("Resume Session", self.curr_font, 40, BLACK,  WIDTH // 4, HEIGHT // 4)  # Draw "Resume Session" text if paused
        else:
            if dataSaved:
                self.drawText("Data Saved", self.curr_font, 40, BLACK, WIDTH // 4, HEIGHT // 4)  # Draw "Data Saved" text if data saved   

    
    def drawText(self, text, fontname, fontsize, text_col, x, y):
        font = pygame.font.Font(fontname, fontsize)
        text_surface = font.render(text, True, text_col)
        self.screen.blit(text_surface, ((x, y)))
    #prints players on the screen
    def renderPlayers(self, firstSquareX, firstSquareY):
        for i in range(self.playerCount):
            if (i == 0):
                self.screen.blit(self.scaled_duck_player, (10 + firstSquareX, firstSquareY + 50))
            else:
                self.screen.blit(self.scaled_duck_player, (10+ firstSquareX + PLAYERDIST*i, firstSquareY + 50))
    #moves players
    def movePlayers(self):
        if self.playerIndex < 14:
            self.playerIndex += 1
        else:
            raise endOfBoardException.endOfBoardException("End of board")
        
    #renders question
    def drawQuestion(self, playersQuestion, level, square_col, time_elapsed, gen_new_question, player_answer): 
        pygame.draw.rect(self.screen, WHITE, (0, 0, 1280, 800))
        rect_x = (WIDTH - 880) // 2
        rect_y = (HEIGHT - 600) // 2
        pygame.draw.rect(self.screen, BLACK, (rect_x, rect_y, 880, 600))
        innerBoardWidth = 880-(BOARD_OUTLINE_OFFSET*2)
        innerBoardHeight = 600-(BOARD_OUTLINE_OFFSET*2)
        innerBoardStartX = rect_x+BOARD_OUTLINE_OFFSET
        innerBoardStartY = rect_y+BOARD_OUTLINE_OFFSET
        pygame.draw.rect(self.screen, WHITE, (innerBoardStartX, innerBoardStartY, innerBoardWidth, innerBoardHeight))
        self.drawText(str(playersQuestion["name"]+"'s Question"), self.curr_font, 50, BLACK, rect_x*2, rect_y+40)
        pygame.draw.rect(self.screen, BLACK, (rect_x+200, rect_y+400, 480, 90))
        pygame.draw.rect(self.screen, WHITE, (rect_x+200+BOARD_OUTLINE_OFFSET, rect_y+400+BOARD_OUTLINE_OFFSET, 480-(BOARD_OUTLINE_OFFSET*2), 90-(BOARD_OUTLINE_OFFSET*2)))
        pygame.draw.rect(self.screen, GREEN, (rect_x+200+BOARD_OUTLINE_OFFSET, rect_y+400+BOARD_OUTLINE_OFFSET, 16*time_elapsed, 90-(BOARD_OUTLINE_OFFSET*2)))
        #---------------------
        pygame.draw.rect(self.screen, BLACK, (innerBoardStartX+100, innerBoardStartY+285, 290, 50))
        pygame.draw.rect(self.screen, WHITE, (innerBoardStartX+100+BOARD_OUTLINE_OFFSET, innerBoardStartY+285+BOARD_OUTLINE_OFFSET, 290-(BOARD_OUTLINE_OFFSET*2), 50-(BOARD_OUTLINE_OFFSET*2)))
        self.drawText(player_answer, self.curr_font, 40, BLACK, innerBoardStartX+103, innerBoardStartY+289)
        
        if (gen_new_question): 
            player_row = self.playerIndex // NUMCOLS
            que_type = random.randint(1,2)
            if(player_row == 0):
                if que_type == 1:
                    self.curr_question = addition(self.levelNum).generateQuestion()
                else:
                    self.curr_question = subtraction(self.levelNum).generateQuestion()
            elif(player_row == 1):
                if que_type == 1:
                    self.curr_question = multiplication(self.levelNum).generateQuestion()
                else:
                    self.curr_question = division(self.levelNum).generateQuestion()
            else:
                if que_type == 2:
                    self.curr_question = quadratic(self.levelNum).generateQuestion()
                else:
                    self.curr_question = linear(self.levelNum).generateQuestion()
        self.drawText(self.curr_question[0], self.curr_font, 30, BLACK, innerBoardStartX+100, innerBoardStartY+175)
        self.drawText(self.curr_question[1], self.curr_font, 30, BLACK, innerBoardStartX+100, innerBoardStartY+205)
        self.drawText(self.curr_question[2], self.curr_font, 30, BLACK, innerBoardStartX+100, innerBoardStartY+235)
        return self.curr_question
    def showResults():
        pass
    #gives a countdown for which players turn it is
    def showPlayersTurn(self, name, time):
        rect_x = (WIDTH - 880) // 2
        rect_y = (HEIGHT - 600) // 2
        pygame.draw.rect(self.screen, WHITE, (rect_x+BOARD_OUTLINE_OFFSET, rect_y+BOARD_OUTLINE_OFFSET, 880-(BOARD_OUTLINE_OFFSET*2), 600-(BOARD_OUTLINE_OFFSET*2)))
        self.drawText(str(name["name"]+"'s turn"), self.curr_font, 50, BLACK, rect_x*2+50, rect_y+70)
        self.drawText(str(time), self.curr_font, 50, BLACK, rect_x+400, rect_y+250)
    #renders a button
    def draw_button(self, text, x, y):  # Define a function to draw a button on the screen
        pygame.draw.rect(self.screen, BLACK, (x, y, 200, 50))  # Draw the button rectangle
        if y == 250:  # Adjust text position based on button position
            self.drawText(text, self.curr_font, 25, WHITE, x + 60, y + 20)
        elif y == 350: 
            self.drawText(text, self.curr_font, 25, WHITE, x + 25, y + 20)
        else: 
            self.drawText(text, self.curr_font, 25, WHITE, x + 5, y + 22)
    def answer_check(self, answer, question, player):
        if isinstance(question[-1], int):
            try:
                answer = int(answer)
                if (answer == question[-1]):
                    player["score"] += 100
                    player["streak"] += 1
                    self.answer_correct = True
                else:
                    player["streak"] = 0
                    self.answer_correct = False
            except:
                player["streak"] = 0 
                self.answer_correct = False
        elif isinstance(question[-1], list):
            try:
                answer = answer.split(',')
                answer = answer.replace(' ', ' ')
                if (answer[0] in question[-1] and answer[1] in question[-1]):
                    player["score"] += 100
                    player["streak"] += 1
                    self.answer_correct = True
                else:
                    player["streak"] = 0
                    self.answer_correct = False
            except:
                player["streak"] = 0
                self.answer_correct = False
        else:
            try:
                answer = answer.replace(' ','')
                question_real = question[-1].replace(' ','')
                if (answer == question_real):
                    player["score"] += 100
                    player["streak"] += 1
                    print("score",player['score'])
                    self.answer_correct = True  
                else:
                    player['streak'] = 0
                    self.answer_correct = False
            except:
                player['streak'] = 0 
                self.answer_correct = False
    def show_answer_feedback(self, answer_recieved, question):
        rect_x = (WIDTH - 880) // 2
        rect_y = (HEIGHT - 600) // 2
        pygame.draw.rect(self.screen, WHITE, (0, 0, 1280, 800))
        self.drawText("Feedback On Answer", self.curr_font, 50, BLACK, rect_x*2, rect_y+70)
        self.drawText("Your Answer:    "+str(answer_recieved), self.curr_font, 40, BLACK, rect_x+100, rect_y+250)
        self.drawText("Correct Answer:    "+str(self.curr_question[-1]), self.curr_font, 40, BLACK, rect_x+100, rect_y+290)
        if self.answer_correct:
            self.screen.blit(self.scaled_checkMark, (rect_x+410, rect_y + 380))
        else:
            self.screen.blit(self.scaled_RedX, (rect_x+310, rect_y + 420))

