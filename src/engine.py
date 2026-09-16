from constants import VISIBLE_POLES
from models import Action

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
        if not game.poles[move.pole]:
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

    if player.value == "A":
        if game.poles["1a"]:
            return False

        if game.poles["3a"] != list(range(2 * game.N - 1, 0, -2)):
            return False
        
    elif player.value == "B":
        if game.poles["1b"]:
            return False
        if game.poles["3b"] != list(range(2 * game.N, 0, -2)):
            return False

    return True
