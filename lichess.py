import json
import requests


def get_game_id(lichess_token):
    url = "https://lichess.org//api/account"
    headers = {"Authorization": f"Bearer {lichess_token}"}
    user_data = requests.get(url, headers=headers)
    print(f"Response: {user_data.status_code}")
    json_data = json.loads(json.dumps(user_data.json()))
    game_url = json_data["playing"]
    game_id = game_url.split("/")[-2]
    print(f"Game ID is: {game_id}")
    return game_id


def make_move(game_id, move, lichess_token):
    url = f"https://lichess.org//api/bot/game/{game_id}/move/{move}"
    print(url)
    headers = {"Authorization": f"Bearer {lichess_token}"}
    print(headers)
    make_the_move = requests.post(url, headers=headers)
    moveJson = json.loads(json.dumps(make_the_move.json()))
    print(moveJson)
    print(make_the_move)
    print(f"Move response: {make_the_move.status_code}")
