import random
import unittest
import Player

class TestPlayer(unittest.TestCase):
    '''Unit testing Player class methods.'''
    def test_setPermission(self):
        p = Player()
        p.setPermission(123456)
        self.assertEqual(p.getPermission(), 0)
        print("setPermission passed")
        
    def test_getPermission(self):
        p = Player()
        p.setPermission(2468)
        self.assertEqual(p.getPermission(), 0)
        print("getPermission passed")        

    def test_setName(self):     
        p = Player()
        p.setName("John")
        self.assertEqual(p.getName(), "John")
        self.assertIsInstance(p, Player)    # confirms if Player object initialized
        print("setName passed")

    def test_getName(self):
        p = Player()
        p.setName("Jane")
        self.assertEqual(p.getName(), "Jane")
        print("getName passed")

    def test_setID(self, player_id):     # randomized, check return value type
        p = Player()
        p.setID()
        self.assertIsInstance(p.getID(), int)
        print("setID passed")
        
    def test_getID(self):    
        p = Player()
        p.setID()
        self.assertIsInstance(p.getID(), int)
        print("getID passed")
        
    def test_updateScore(self, score):   
        player = Player()
        player.updateScore(1000)
        self.assertEqual(player.getScore(), 1000)
        player.updateScore(2000)
        self.assertEqual(player.getScore(), 3000)
        
    def test_getScore(self):
        player = Player()
        return self.__score
        
    def test_updateDuckCount(self, count):   
        player = Player()
        self.__duckCount += count

    def test_getDuckCount(self):
        player = Player()
        return self.__duckCount
        
    def test_updateStreakCount(self, streak):
        player = Player()
        self.__streakCount += streak

    def test_getStreakCount(self):  # streak counter, make set and get
        player = Player()
        return self.__streakCount

    def test_updateCorrectCount(self, correct):
        player = Player()
        self.__correctCount += correct

    def test_getCorrectCount(self):
        player = Player()
        return self.__correctCount    

    def test_updateDuckCount(self, count):   # input from Ryan again, input how much it increases by
        player = Player()
        self.__duckCount += count
        
    print("Player tests passed")

if __name__ == '__main__':
    unittest.main()