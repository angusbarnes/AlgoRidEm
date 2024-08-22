from dataclasses import dataclass
from enum import Enum
from common.game_entities import Territory

class ActionType(Enum):
    MOVE_TROOPS = 1
    ATTACK = 2
    RECRUIT_TROOPS = 3
    NEGOTIATE = 4

@dataclass
class ActionRequest:
    action_type: ActionType
    player_name: str
    source_territory: Territory
    target_territory: Territory
    troop_count: int