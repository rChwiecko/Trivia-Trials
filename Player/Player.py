import random

class Player:
    '''A class to represent a player.
    
    Attributes:
        playerID (int): Player ID, automatically and randomly generated. 
        playerName (str): Player name, input by user.
        score (int): Current game score of player.
        duckCount (int): Number of score boosters (ducks) a player has.
        streakCount (int): Number of consecutively correct answers a player has.
        correctCount (int): Total number of questions correctly answered by player.
    '''

    def __init__(self):
        self.__playerID = None      # player id, randomized
        self.__playerName = None    # player name, input by user
        self.__score = 0            # current game score
        self.__duckCount = 0        # number of ducks a player has
        self.__streakCount = 0      # number questions right in a row
        self.__correctCount = 0     # number questions correct

    def setName(self, name: str) -> None:        # make notAstringException
        '''Set name of player.

        Args:
            name (str): Input from user, user's name.
        '''

        self.__playerName = name    # get from user input, query would take from this method

    def setID(self) -> None:     # randomized
        '''Generate ID for this player.'''
        self.__playerID = random.randint(0,10000)   # generate random number

    def updateScore(self, score: float) -> None:   # setter, input from Ryan again, input how much it increases by
        '''Increments player score.
        
        Args:
            score (int): Amount of points earned for answering a question correctly.
        '''
        self.__score += score

    def updateDuckCount(self, count: int) -> None:   # setter, input from Ryan again, input how much it increases by
        '''Increments number of ducks in player's posession.
        
        Args:
            count (int): Amount of ducks earned for completing a level.
        '''
        self.__duckCount += count
    
    def updateStreakCount(self) -> None:
        '''Increments by 1 for each consecutively correct answer.'''
        self.__streakCount += 1     # if correct, Player.updateStreakCount()

    def updateCorrectCount(self, correct: int) -> None:
        ''''''
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