from constants import VISIBLE_POLES
from models import Action, Move, Player

def apply_move(game, player, move):
    if move.action == Action.LIFT:
        if game.hands[player] is not None:
            return
        if move.pole is None or move.pole not in VISIBLE_POLES[player]:
            return
        if not game.poles[move.pole]:
            return
        game.hands[player] = game.poles[move.pole].pop()

    elif move.action == Action.PLACE:
        if game.hands[player] is None:
            return
        if move.pole is None or move.pole not in VISIBLE_POLES[player]:
            return
        if game.poles[move.pole] and game.poles[move.pole][-1] < game.hands[player]:
            return
        game.poles[move.pole].append(game.hands[player])
        game.hands[player] = None
    elif move.action == Action.SKIP:
        return

def check_win(game, player):
    if game.hands[player] is not None:
        return False

    if game.poles["2"]:
        return False

    if player == Player.A:
        if game.poles["1a"]:
            return False

        if game.poles["3a"] != list(range(2 * game.n - 1, 0, -2)):
            return False
        
    elif player == Player.B:
        if game.poles["1b"]:
            return False
        if game.poles["3b"] != list(range(2 * game.n, 0, -2)):
            return False

    return True

def get_valid_actions(game, player):
    valid_actions = []

    # Check if the player can lift a disk from any visible pole
    if game.hands[player] is None:
        for pole in VISIBLE_POLES[player]:
            if game.poles[pole]:
                valid_actions.append(Move(Action.LIFT, pole))

    # Check if the player can place a disk on any visible pole
    if game.hands[player] is not None:
        for pole in VISIBLE_POLES[player]:
            if not game.poles[pole] or game.poles[pole][-1] > game.hands[player]:
                valid_actions.append(Move(Action.PLACE, pole))

    # The player can always skip their turn
    valid_actions.append(Move(Action.SKIP, None))

    return valid_actions