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

instance = Board(player_list, screen, level, index)
class TestBoard(unittest.TestCase):
    def test_save_game(self):
        instance.save_game(player_list, id_override)
        game_pulled = find_game_by_id(id_override)
        self.assertIsInstance(find_game_by_id(id_override), dict)
        self.assertEqual(expected_output["game_id"], game_pulled["game_id"]) #pull the game out of the database and see if the same as the expected output
        self.assertEqual(expected_output["level_number"], game_pulled["level_number"])
        self.assertEqual(expected_output["player_index"], game_pulled["player_index"])
if __name__ == "__main__":
    unittest.main()                                                               
         