"""A class for a Player.
"""
import random
# testing testing
class Player:
    def __init__(self):
        self.__playerID = None      # player id, randomized
        self.__playerName = None    # player name, input by user
        self.__score = 0            # current game score
        self.__duckCount = 0        # number of ducks a player has
        self.__streakCount = 0      # number questions right in a row
        self.__correctCount = 0     # number variables correct

    """Function to allow user to input a name
    @params: name String
    """
    def setName(self, name: str) -> None:        # make notAstringException
        self.__playerName = name    # get from user input, query would take from this method

    # so Main Menu would create a new Player object upon every prompt, and then
    # it's Sahej's problem to read it in in a way that this object can set it
    def setID(self, player_id: int) -> None:     # randomize
        self.__playerID = random.randint(0,10000)

    def updateScore(self, score: float) -> None:   # setter, input from Ryan again, input how much it increases by
        self.__score += score

    def updateDuckCount(self, count: int) -> None:   # setter, input from Ryan again, input how much it increases by
        self.__duckCount += count
    
    def updateStreakCount(self, streak: int) -> None:
        self.__streakCount += streak

    def updateCorrectCount(self, correct: int) -> None:
        self.__correctCount += correct

    def getID(self) -> int:    
        return self.__playerID

    def getName(self) -> str:
        return self.__playerName

    def getScore(self) -> float:
        return self.__score

    def getDuckCount(self) -> int:
        return self.__duckCount

    def getStreakCount(self) -> int:  # streak counter, make set and get
        return self.__streakCount
    
    def getCorrectCount(self) -> int:
        return self.__correctCount