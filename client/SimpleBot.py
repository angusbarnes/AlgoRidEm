from typing import List
from common.game_entities import GameState
from common.actions import *

class Bot:

    # IF you have never seen type hints before, "bot_id: int | str" simply means the variable 'bot_id'
    # will either be a int or string type
    def __init__(self, bot_id: int | str):
        # you can use this init function to set up any instance variables you want your bot to "remember".
        # If you want to support bot variations, you can also put parameters in the init function, but these
        # must have a default value

        # All bots are assigned a unique ID by the server. You should remember yours because it will be
        # needed later in order to get a list of owned territories
        self.ID = bot_id
        pass

    def play_turn(self, game_state: GameState, turn_number: int) -> ActionRequest | List[ActionRequest]:
        """
        THIS IS THE MOST IMPORTANT FUNCTION FOR YOUR BOT.

        Every turn, the server will call this function and provide the most recent state information.
        It is your job as the developer to interpret this information and construct a move or list of moves,
        based on it. These moves are known as actions in the API. You can make as many moves as you have,
        territories, however only one ActionType.MOVE_TROOPS can be made per territory, per turn.

        If you submit more actions than you are allowed, or any illegal actions, they will simply be ignored
        by the server. You will recieve no error message.

        Args:
            game_state: A GameState object representing the current game state, think of this like a representation
                        of the playing board
            turn_number: The current turn number of the game. You can use this to track game progress in order to
                         orchestrate complex, multi-turn strategies, or you can simply ignore it
        
        Returns:
            actions: A single ActionRequest object, or list of ActionRequest objects to describe your desired moves
        """

        # Implement your bot's decision-making logic here
        # Example: Concentrate troops on the weakest neighboring enemy territory and attack
        target_territory = self.find_weakest_neighbor(game_state)
        if target_territory:
            self.attack(target_territory)

    def defend_territory(self, game_state: GameState, territory_under_attack: Territory) -> ActionRequest:
        """
        In marginal cases, the game server may allow players to take a defensive action when attacked.
        The specifics of this will not be explained. If this function is called, the player may make ONE
        defensive action. THIS CANNOT INCLUDE MOVING TROOPS INTO AN ENEMY TERRITORY (however moving troops
        between player controlled territories is fine). This could be used to retreat (and protect troops),
        reinforce (add troops from neighbouring territory) or recruit new troops here (using territories).

        When necessary, the server will execute actions as follows:
            --> Server finds a conflict with marginal status (no clear winner)
            --> Server will call defend_territory on the attacked territory
            --> Server will execute coresponding action request
            --> Server will re-evaluate conflict to find winner

        Args:
            game_state: A GameState object representing the current game state, think of this like a representation
                        of the playing board
            territory_under_attack: This is a quick reference to the territory being attacked for convenience,
                                    you can use this to easily create an action which defends the attacked territory
        """

        return DEFAULT_PASS_ACTION

    def find_weakest_neighbor(self, game_state: GameState):
        weakest_neighbor = None
        weakest_troops = float('inf')
        for territory in self.territories:
            for neighbor in territory.neighbors:
                if neighbor.owner != self.name and neighbor.troops < weakest_troops:
                    weakest_neighbor = neighbor
                    weakest_troops = neighbor.troops
        return weakest_neighbor


    def observe_update(self, game_state: GameState):
        """
        Optional function to observe updates made by other players before it is your turn again.
        You can safely ignore this function if desired, you will always receive the most recent version
        of the game state in your turn function, this is simply incase you want to track the order of moves
        from other players (Advanced concept).

        Args:
            game_state: The current game state as a GameState object

        Returns:
            This function has no returns necessary
        """
        pass

    def attack(self, target_territory):
        # Implement battle logic here
        # Example: Commit all available troops to the attack
        target_territory.owner = self.name
        target_territory.troops = self.troops
        self.troops = 0