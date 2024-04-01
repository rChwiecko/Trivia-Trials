from queryManager import *

""" This file inserts a game into the database and retrieves it by ID """

game = {
  "game_id": 1,
  "level_number": 2,
  "player_index": 14,
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

insert_game(game) # Insert the game into the database

game = find_game_by_id(1) # Retrieve the game by its ID

print(game['players'][0]) # Print the information of the first player in the retrieved game