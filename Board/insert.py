from queryManager import *
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
insert_game(game)
game = find_game_by_id(1)
print(game['players'][0])