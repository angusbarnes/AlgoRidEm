from dataclasses import dataclass
from typing import List

@dataclass
class Territory:
    name: str
    ID: int
    resources: int
    owner: any = None
    neighbors: List['Territory'] = None
    development_age: int = 0

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)