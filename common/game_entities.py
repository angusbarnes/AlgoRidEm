from dataclasses import dataclass, field
from typing import List
import random

@dataclass
class Territory:
    name: str
    ID: int
    x: int
    y: int
    resources: int
    owner_id: str | int = 0
    neighbors: List = field(default_factory=list)
    development_age: int = 0

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


class GameState:
    def __init__(self, board_size):
        self.territories: List[Territory] = self._create_board(board_size)
        self.turn = 0

    def _create_board(self, board_size):
        territories = []
        for x in range(board_size):
            for y in range(board_size):
                territory = Territory(f"T({x},{y})", x*y, x, y, random.randint(1, 100), random.randint(1, 10))
                territories.append(territory)
                # Connect neighboring territories
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor_x, neighbor_y = x + dx, y + dy
                    if 0 <= neighbor_x < board_size and 0 <= neighbor_y < board_size:
                        for t in territories:
                            if t.x == neighbor_x and t.y == neighbor_y:
                                territory.add_neighbor(t)
                                t.add_neighbor(territory)

        return territories
    
    def get_territories(self):
        return self.territories
    
    def get_territories_by_player(self, player_id):
        return [t for t in self.territories if t.owner_id == player_id]

    def check_victory(self):
        # Implement victory condition logic here
        # For example, the first player to control 50% of the territories wins
        pass