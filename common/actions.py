from dataclasses import dataclass
from enum import Enum
from typing import Dict
from common.game_entities import Territory

class ActionType(Enum):
    NO_ACTION = 0
    MOVE_TROOPS = 1
    ATTACK = 2
    RECRUIT_TROOPS = 3
    NEGOTIATE = 4

@dataclass
class ActionRequest:
    action_type: ActionType
    source_territory: Territory
    target_territory: Territory = None
    request_data: Dict = None


DEFAULT_PASS_ACTION = ActionRequest(ActionType.NO_ACTION, None)
"""
A default action object which simply passes the players turn with no action.
Return this to do nothing.
"""