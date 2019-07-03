import json
import requests


def get_game_id(lichess_token): #Gets game id of the current playing game
    url = "https://lichess.org//api/account"
    headers = {"Authorization": f"Bearer {lichess_token}"}
    user_data = requests.get(url, headers=headers)
    print(f"Response: {user_data.status_code}")
    json_data = json.loads(json.dumps(user_data.json()))
    game_url = json_data["playing"]
    game_id = game_url.split("/")[-2]
    print(f"Game ID is: {game_id}")
    return game_id


def game_state(game_id, lichess_token):  # Streamer for the current game state
    url = f"https://lichess.org//api/bot/game/stream/{game_id}"
    headers = {"Authorization": f"Bearer {lichess_token}"}
    game_state = requests.get(url, headers=headers, stream=True)
    for line in game_state.iter_lines(decode_unicode=True):
        if line:
            if get_previous_move(line) != "none":
                return (get_previous_move(line))


def get_previous_move(line):  # Gets the move from the computer
    try:
        game_moves = json.loads(line)["state"]["moves"]
    except KeyError:  # After program is run, the API will return "gameState" which does not have key "state"
        game_moves = json.loads(line)["moves"]
    game_moves = game_moves.split(" ")
    if len(game_moves) % 2 == 0:
        return game_moves[-1]  # This is the last move in list of moves
    else:
        return "none"


def make_move(game_id, move, lichess_token):
    url = f"https://lichess.org//api/bot/game/{game_id}/move/{move}"
    headers = {"Authorization": f"Bearer {lichess_token}"}
    make_the_move = requests.post(url, headers=headers)
    print(f"Move response: {make_the_move.status_code}")
