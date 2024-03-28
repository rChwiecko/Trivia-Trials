import random
import unittest
import Player

class TestPlayer(unittest.TestCase):
    def test_settersGetters(self):
        def test_setName(self):     # checks if Player object was created
            player = Player()
            player.setName("name")
            self.assertEqual(player.getName(), "name")
            self.assertIsInstance(player, Player)
            print("setName passed")

        def test_getName(self):
            player = Player()
            player.setName("name")
            self.assertEqual(player.getName(), "name")
            print("getName passed")

        def test_setID(self, player_id):     # randomize
            player = Player()
            player.setID
            self.__playerID = random.randint(0,10000)
            print("setID passed")
        
        def test_getID(self):    
            player = Player()
            return self.__playerID

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

        print("setter/getter tests passed")

    def test_updaters(self):    # these are basically setters of sorts
        def test_updateScore(self, score):   # input from Ryan again, input how much it increases by
            player = Player()
            player.updateScore(1)
            self.assertEqual(player.getScore(), 1)
            player.updateScore(2)
            self.assertEqual(player.getScore(), 3)

        def test_updateDuckCount(self, count):   # input from Ryan again, input how much it increases by
            player = Player()
            self.__duckCount += count
        
        def test_updateStreakCount(self, streak):
            player = Player()
            self.__streakCount += streak

        def test_updateCorrectCount(self, correct):
            player = Player()
            self.__correctCount += correct
        
        print("update tests passed")

if __name__ == '__main__':
    unittest.main()