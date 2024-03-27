import random
import unittest
import Player

class TestPlayer(unittest.TestCase):
    def test_setName(self):     # checks if Player object was created
        player = Player()
        self.assertIsInstance(player, Player)

    # def setName(self, name):        # make notAstringException
    #     self.__playerName = name    # get from user input, query would take from this method
    
    def test_setID(self, player_id):     # randomize
        player = Player()
        self.__playerID = random.randint(0,10000)

    # def setID(self, player_id):     # randomize
    #     self.__playerID = random.randint(0,10000)

    def test_updateScore(self, score):   # setter, input from Ryan again, input how much it increases by
        player = Player()
        self.__score += score

    # def updateScore(self, score):   # setter, input from Ryan again, input how much it increases by
    #     self.__score += score

    def test_updateDuckCount(self, count):   # setter, input from Ryan again, input how much it increases by
        player = Player()
        self.__duckCount += count

    # def updateDuckCount(self, count):   # setter, input from Ryan again, input how much it increases by
    #     self.__duckCount += count
    
    def test_updateStreakCount(self, streak):
        player = Player()
        self.__streakCount += streak

    # def updateStreakCount(self, streak):
    #     self.__streakCount += streak

    def test_updateCorrectCount(self, correct):
        player = Player()
        self.__correctCount += correct

    # def updateCorrectCount(self, correct):
    #     self.__correctCount += correct

    def test_getID(self):    
        player = Player()
        return self.__playerID
    
    # def getID(self):    
    #     return self.__playerID

    def test_getName(self):
        player = Player()
        return self.__playerName
    
    # def getName(self):
    #     return self.__playerName

    def test_getScore(self):
        player = Player()
        return self.__score

    # def getScore(self):
    #     return self.__score

    def test_getDuckCount(self):
        player = Player()
        return self.__duckCount
    
    # def getDuckCount(self):
    #     return self.__duckCount

    def test_getStreakCount(self):  # streak counter, make set and get
        player = Player()
        return self.__streakCount
    
    # def getStreakCount(self):  # streak counter, make set and get
    #     return self.__streakCount

    def test_getCorrectCount(self):
        player = Player()
        return self.__correctCount    

    # def getCorrectCount(self):
    #     return self.__correctCount

if __name__ == '__main__':
    unittest.main()