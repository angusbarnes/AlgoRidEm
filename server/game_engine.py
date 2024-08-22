from client.SimpleBot import Bot
from common.game_entities import GameState
import random

def _create_players(self, num_players):
    players = []
    for i in range(num_players):
        # Assign starting territories to each player
        start_territories = random.sample(self.territories, 2)
        for territory in start_territories:
            territory.owner = f"Player{i+1}"
            territory.troops = 10
        player = Bot(f"Player{i+1}")
        players.append(player)
    return players


def start_engine():
    state = GameState(10)

def engine_tick():
    pass
