import pygame, time
from const import *
import endOfBoardException
pygame.init()
class Board:
    gameStatus = False
    font = pygame.font.Font(None, 36)
    playerCount = None
    playerIndex = None
    playerList = None
    board = None
    screen = None
    curr_font = pygame.font.get_default_font()
    levelNum = None
    duck = pygame.image.load("./assets/transparentduck.png")
    scaled_duck_end = pygame.transform.scale(duck, (100, 100))
    scaled_duck_player = pygame.transform.scale(duck, (50, 50))
    arrow = pygame.image.load("./assets/arrow.png")
    arrow_scaled = pygame.transform.scale(arrow, (50, 50))
    arrow_down = pygame.transform.rotate(arrow_scaled, 270)

    def __init__(self, playerList, screen, level, playerIndex, newGame = False) -> None:
        self.playerCount = len(playerList)
        self.newGame = newGame
        self.playerIndex = playerIndex
        self.playerList = playerList
        self.board = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        for i in range(NUMROWS):
            for j in range(NUMCOLS):
                if (i+j==self.playerIndex):
                    self.board[i][j] = 1
        self.gameStatus = True
        self.screen = screen
        self.level = level


    def drawBoard(self, win):
        win.fill("white")
        rect_x = (WIDTH - 880) // 2
        rect_y = (HEIGHT - 600) // 2
        pygame.draw.rect(win, BLACK, (rect_x, rect_y, 880, 600))
        level = "Level "+str(self.level)
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
                squareXCoord = innerBoardStartX+20+(col*(150+20.5))
                squareYCoord = innerBoardStartY+41+(row*(150+30))
                pygame.draw.rect(win, BLACK, (squareXCoord, squareYCoord, 150, 150))
                pygame.draw.rect(win, currSquareColor, (squareXCoord+BOARD_OUTLINE_OFFSET, squareYCoord+BOARD_OUTLINE_OFFSET, 150-(2*BOARD_OUTLINE_OFFSET), 150-(2*BOARD_OUTLINE_OFFSET)))
                if (NUMROWS*col + row == self.playerIndex):
                    self.renderPlayers(squareXCoord,squareYCoord)
                if row == 0 and col == 0:
                    self.drawText("Start", self.curr_font, 25, BLACK, squareXCoord+40, squareYCoord+120)
                if row == 2 and col == 4:
                    self.drawText("End", self.curr_font, 25, BLACK, squareXCoord+40, squareYCoord+120)
                    self.screen.blit(self.scaled_duck_end, (squareXCoord+200, squareYCoord+20))
                # if (row == 0 and col == 4) or (row == 1 and col == 0):
                #     self.screen.blit(arrow_down, (squareXCoord+48, squareYCoord+100))

    def render(self):
        self.drawBoard(self.screen)

    def pause(self):
        pass    
    def drawText(self, text, fontname, fontsize, text_col, x, y):
        font = pygame.font.Font(fontname, fontsize)
        text_surface = font.render(text, True, text_col)
        self.screen.blit(text_surface, ((x, y)))
    def renderPlayers(self, firstSquareX, firstSquareY):
        for i in range(self.playerCount):
            if (i == 0):
                self.screen.blit(self.scaled_duck_player, (10 + firstSquareX, firstSquareY + 50))
            else:
                self.screen.blit(self.scaled_duck_player, (10+ firstSquareX + PLAYERDIST*i, firstSquareY + 50))
    def movePlayers(self):
        if self.playerIndex < 15:
            self.playerIndex += 1
        else:
            raise endOfBoardException("End of board")