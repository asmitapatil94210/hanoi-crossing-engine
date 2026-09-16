from enum import Enum

class Action(Enum):
    LIFT = "Lift"
    PLACE = "Place"
    SKIP = "Skip"

class Move:
    def __init__(self, action, pole):
        self.action = action
        self.pole = pole

class Player(Enum):
    A = "A"
    B = "B"

class GameState:
    def __init__(self, n, poles, hands):
        self.n = n
        self.poles = poles
        self.hands = hands