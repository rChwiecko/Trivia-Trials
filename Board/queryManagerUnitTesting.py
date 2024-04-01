import unittest # import the unittest module for writing and executing tests
from queryManager import * # import all functions and classes from the queryManager module

# generate and insert a sample game
game = {
    "game_id": 2,
    "level_number": 3,
    "player_index": 5,
    "players": [
        {
        "name": "Player4",
        "password": "password123",
        "streak": 2,
        "duck_count": 0,
        "score": 250
        }
    ]
    }

insert_game(game) # insert the sample game into the database

class TestQueryManager(unittest.TestCase):
    """A class to test the functionalities of the queryManager module """

    def test_dataTypes(self):
        """Test that the data types of the returned values are correct."""

        self.assertEqual(type(find_game_by_id(2)), dict) # assert that the return type of find_game_by_id is a dictionary
        self.assertEqual(type(get_player_scores()), dict) # assert that the return type of get_player_scores is a dictionary
        self.assertEqual(type(get_player_info()), dict) # assert that the return type of get_player_info is a dictionary

        print ("All data types are correct") # print message indicating that all data types are correct.

    def test_find_game_by_id(self):
        """Test that the correct game is returned by find_game_by_id method """

        game_from_db = find_game_by_id(2)# retrieve the game with game_id = 2 from the database
        # remove the '_id' key from the dictionary before comparing
        if '_id' in game_from_db: # check if '_id' key exists in the retrieved game document
            del game_from_db['_id']  # If '_id' key exists, remove it.
        self.assertEqual(game_from_db, game)# assert that the retrieved game matches the sample game

        print("Find_game_by_id is correct")# print message indicating that the test for find_game_by_id is correct

# run the tests
if __name__ == '__main__':
    unittest.main() # execute the unit tests defined in the TestQueryManager class
    print ("All tests passed!")# print message indicating that all tests passed


'''
Dont need to test for different data types because these functions are never directly accessed. In order for an incorrect data type to even attempt to be passed, it would have to go through the Board.py file which is impossible.
'''     