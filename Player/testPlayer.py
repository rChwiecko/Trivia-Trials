import random
import unittest
import Player

class TestPlayer(unittest.TestCase):
    def test_setters(self):
        def test_setName(self):     # checks if Player object was created
            player = Player()
            player.setName("name")
            self.assertEquals(player, "name")
            self.assertIsInstance(player, Player)
            print("setter tests passed")
    
        def test_setID(self, player_id):     # randomize
            player = Player()
            self.__playerID = random.randint(0,10000)

    def test_updateScore(self, score):   # setter, input from Ryan again, input how much it increases by
        player = Player()
        self.__score += score

    def test_updateDuckCount(self, count):   # setter, input from Ryan again, input how much it increases by
        player = Player()
        self.__duckCount += count
    
    def test_updateStreakCount(self, streak):
        player = Player()
        self.__streakCount += streak

    def test_updateCorrectCount(self, correct):
        player = Player()
        self.__correctCount += correct

    def test_getID(self):    
        player = Player()
        return self.__playerID

    def test_getName(self):
        player = Player()
        return self.__playerName

    def test_getScore(self):
        player = Player()
        return self.__score

    def test_getDuckCount(self):
        player = Player()
        return self.__duckCount

    def test_getStreakCount(self):  # streak counter, make set and get
        player = Player()
        return self.__streakCount

    def test_getCorrectCount(self):
        player = Player()
        return self.__correctCount    

if __name__ == '__main__':
    unittest.main()