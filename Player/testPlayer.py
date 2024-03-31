import random
import unittest
import Player

class TestPlayer(unittest.TestCase):
    '''Unit testing Player class methods.'''
    def test_setPermission(self):
        player = Player()
        player.setPermission(123456)
        self.assertEqual(player.getPermission(), 0)
        print("setPermission passed")
        
    def test_getPermission(self):
        player = Player()
        player.setPermission(2468)
        self.assertEqual(player.getPermission(), 0)
        print("getPermission passed")        

    def test_setName(self):     
        player = Player()
        player.setName("John")
        self.assertEqual(player.getName(), "John")
        self.assertIsInstance(player, Player)    # confirms if Player object initialized
        print("setName passed")

    def test_getName(self):
        player = Player()
        player.setName("Jane")
        self.assertEqual(player.getName(), "Jane")
        print("getName passed")

    def test_setID(self, player_id):     # randomized, check return value type
        player = Player()
        player.setID()
        self.assertIsInstance(player.getID(), int)
        print("setID passed")
        
    def test_getID(self):   # checks if return value is integer
        player = Player()
        player.setID()
        self.assertIsInstance(player.getID(), int)
        print("getID passed")
        
    def test_updateScore(self, score):   # checks if counter increments appropriately
        player = Player()
        player.updateScore(1000)
        self.assertEqual(player.getScore(), 1000)
        player.updateScore(2000)
        self.assertEqual(player.getScore(), 3000)
        print("updateScore passed")
        
    def test_getScore(self):
        player = Player()
        player.updateScore(1000)
        self.assertEqual(player.getScore(), 1000)
        player.updateScore(2000)
        self.assertEqual(player.getScore(), 3000)
        print("getScore passed")
        
    def test_updateDuckCount(self, count):   
        player = Player()
        player.updateDuckCount(1)
        self.assertEqual(player.getDuckCount(), 1)
        player.updateDuckCount(2)
        self.assertEqual(player.getDuckCount(), 3)
        print("updateDuckCount passed")

    def test_getDuckCount(self):
        player = Player()
        player.updateDuckCount(1)
        self.assertEqual(player.getDuckCount(), 1)
        player.updateDuckCount(2)
        self.assertEqual(player.getDuckCount(), 3)
        print("getDuckCount passed")
        
    def test_updateStreakCount(self):
        player = Player()
        player.updateStreakCount()
        self.assertEqual(player.getStreakCount(), 1)
        player.updateStreakCount()
        self.assertEqual(player.getStreakCount(), 2)
        print("updateStreakCount passed")

    def test_getStreakCount(self):  # streak counter, make set and get
        player = Player()
        player.updateStreakCount()
        self.assertEqual(player.getStreakCount(), 1)
        player.updateStreakCount()
        self.assertEqual(player.getStreakCount(), 2)
        print("getStreakCount passed")

    def test_updateCorrectCount(self):
        player = Player()
        player.updateCorrectCount()
        self.assertEqual(player.getCorrectCount(), 1)
        player.updateCorrectCount()
        self.assertEqual(player.getCorrectCount(), 2)
        print("updateCorrectCount passed")

    def test_getCorrectCount(self):
        player = Player()
        player.updateCorrectCount()
        self.assertEqual(player.getCorrectCount(), 1)
        player.updateCorrectCount()
        self.assertEqual(player.getCorrectCount(), 2)
        print("getCorrectCount passed")   
        
    print("Player tests passed")

if __name__ == '__main__':
    unittest.main()