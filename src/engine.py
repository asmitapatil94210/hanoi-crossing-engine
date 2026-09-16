from constants import VISIBLE_POLES
from models import Action

def apply_move(game, player, move):
    if move.action == Action.LIFT:
        if game.hands[player] is not None or move.pole not in VISIBLE_POLES[player]:
            return
        game.hands[player] = game.poles[move.pole].pop()

    elif move.action == Action.PLACE:
        if game.hands[player] is None or move.pole not in VISIBLE_POLES[player]:
            return

        if game.poles[move.pole] and game.poles[move.pole][-1] < game.hands[player]:
            return
        game.poles[move.pole].append(game.hands[player])
        game.hands[player] = None
