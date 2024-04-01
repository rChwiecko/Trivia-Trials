import unittest
from Board import *
from queryManager import *
player_list = [] #make empty, wont affect testing
screen = None #doesnt need to be initialized
level = 1 #first level
index = 0 #first index on board
id_override = 2 #this is an example id that is valid and the game will use to locate where in the database the game be stored

example_player_list = [{
        "name": "Player4",
        "password": "password123",
        "streak": 2,
        "duck_count": 0,
        "score": 0
        }
    ]
#the expected output when data is pulled from database
expected_output = {
  "game_id": 2,
  "level_number": 1,
  "player_index": 0,
  "players": [
    {
      "name": "Player4",
      "password": "password123",
      "streak": 0,
      "duck_count": 0,
      "score": 0
    }
  ]
}
#creating board instance
instance = Board(example_player_list, screen, level, index)
class TestBoard(unittest.TestCase):

    def test_save_game(self):
        instance.save_game(example_player_list, id_override)
        game_pulled = find_game_by_id(id_override)
        print(game_pulled)
        player_pulled = game_pulled["players"][0]
        self.assertIsInstance(find_game_by_id(id_override), dict) #testing if game pulled is of correct type
        #testing all attributes of game pulled
        self.assertEqual(expected_output["game_id"], game_pulled["game_id"]) 
        self.assertEqual(expected_output["level_number"], game_pulled["level_number"])
        self.assertEqual(expected_output["player_index"], game_pulled["player_index"])
        self.assertEqual(player_pulled["name"], example_player_list[0]["name"])
        self.assertEqual(player_pulled["password"], example_player_list[0]["password"])
        self.assertEqual(player_pulled["streak"], example_player_list[0]["streak"])
        self.assertEqual(player_pulled["duck_count"], example_player_list[0]["duck_count"])
        self.assertEqual(player_pulled["score"], example_player_list[0]["score"])

        
if __name__ == "__main__":
    unittest.main()                                                               
         