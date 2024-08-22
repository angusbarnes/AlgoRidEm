from client.SimpleBot import Bot
from common.game_entities import Territory
import random

class GameState:
    def __init__(self, num_players, board_size):
        self.territories = self._create_board(board_size)
        self.players = self._create_players(num_players)
        self.turn = 0

    def _create_board(self, board_size):
        territories = []
        for x in range(board_size):
            for y in range(board_size):
                territory = Territory(x, y, random.randint(1, 10))
                territories.append(territory)
                # Connect neighboring territories
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor_x, neighbor_y = x + dx, y + dy
                    if 0 <= neighbor_x < board_size and 0 <= neighbor_y < board_size:
                        neighbor = next(t for t in territories if t.x == neighbor_x and t.y == neighbor_y)
                        territory.add_neighbor(neighbor)
        return territories

    def _create_players(self, num_players):
        players = []
        for i in range(num_players):
            # Assign starting territories to each player
            start_territories = random.sample(self.territories, 2)
            for territory in start_territories:
                territory.owner = f"Player{i+1}"
                territory.troops = 10
            player = Bot(f"Player{i+1}", start_territories)
            players.append(player)
        return players

    def play_game(self):
        while True:
            for player in self.players:
                player.take_turn(self)
            self.turn += 1
            if self.check_victory():
                break

    def check_victory(self):
        # Implement victory condition logic here
        # For example, the first player to control 50% of the territories wins
        pass